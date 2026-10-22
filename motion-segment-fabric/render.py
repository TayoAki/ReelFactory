from playwright.sync_api import sync_playwright
import subprocess,json,math
from pathlib import Path
R=Path(__file__).resolve().parent
N=json.loads((R/'narration.json').read_text());D=N['duration'];frames=math.ceil(D*30)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1)
 page.goto('http://127.0.0.1:8765/motion-segment-fabric/scene.html');page.evaluate('document.fonts.ready')
 for name,t in [('00-question',1.7),('01-entities',8),('02-properties',14),('03-relationship',22),('04-bindings',28),('05-boundary',38)]:
  page.evaluate('(t)=>renderAt(t)',t);page.screenshot(path=str(R/f'rebuilt-{name}.png'))
 checks=[]
 for t in [4.5,5.6,8,11.9,12.4,16.8,17.5,21.5,25.6,27,28,38]:
  page.evaluate('(t)=>renderAt(t)',t)
  fit=page.evaluate('''()=>Array.from(document.querySelectorAll('#store-label,#unit-label,.chip,.source .name,.source .key')).map(e=>{const a=e.getBoundingClientRect(),p=e.closest('.entity,.source').getBoundingClientRect();return {id:e.id||e.textContent,fit:a.left>=p.left-1&&a.right<=p.right+1&&a.top>=p.top-1&&a.bottom<=p.bottom+1}})''')
  assert all(v['fit'] for v in fit),(t,fit)
  checks.append({'time':t,'bounds':fit})
 # Check each subtitle phrase near its spoken midpoint, and keep diagram out of caption band.
 caption_checks=[]
 for cue in json.loads((R/'captions.json').read_text()):
  t=(cue['start']+cue['end'])/2;page.evaluate('(t)=>renderAt(t)',t)
  c=page.evaluate("""()=>{const a=document.getElementById('captions').getBoundingClientRect(),b=document.getElementById('caption-band').getBoundingClientRect();return {text:document.getElementById('captions').textContent,fit:a.left>=b.left&&a.right<=b.right&&a.top>=b.top&&a.bottom<=b.bottom}}""")
  assert c['fit'] and c['text']==cue['text'],c
  caption_checks.append(c)
 checks.append({'caption_phrases':caption_checks})
 page.evaluate('renderAt(28)')
 overlap=page.evaluate("""()=>{const top=document.getElementById('caption-band').getBoundingClientRect().top;return ['store','unit','store-source','unit-source','join-key'].every(id=>document.getElementById(id).getBoundingClientRect().bottom<top)}""")
 assert overlap
 (R/'layout-check.json').write_text(json.dumps(checks,indent=2))
 enc=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-vcodec','mjpeg','-r','30','-i','pipe:0','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(R/'silent.mp4')],stdin=subprocess.PIPE)
 for i in range(frames):
  page.evaluate('(t)=>renderAt(t)',i/30);enc.stdin.write(page.screenshot(type='jpeg',quality=98))
  if i%150==0:print(f'{i}/{frames}',flush=True)
 enc.stdin.close();assert enc.wait()==0;b.close()
