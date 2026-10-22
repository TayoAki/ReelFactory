from pathlib import Path
import json,math,subprocess
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parent;n=json.loads((R/'narration.json').read_text());frames=math.ceil(n['duration']*30)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:8765/interview-segment-fabric/scene.html');page.evaluate('document.fonts.ready');page.wait_for_function('Array.from(document.images).every(i=>i.complete)')
 for name,t in [('00-host',2),('01-shared-model',9),('02-entity',13),('03-instance',16),('04-properties',19),('05-relationship',23),('06-binding',28),('07-rules-metrics',32.5)]:
  page.evaluate('(t)=>renderAt(t)',t);page.screenshot(path=str(R/f'storyboard/{name}.png'))
 page.evaluate('renderAt(34)');page.screenshot(path=str(R/'rebuilt-master.png'))
 checks=[]
 for cue in json.loads((R/'captions.json').read_text()):
  t=(cue['start']+cue['end'])/2;state=page.evaluate('(t)=>renderAt(t)',t)
  c=page.evaluate("""()=>{const a=document.getElementById('captions').getBoundingClientRect(),b=document.getElementById('caption-band').getBoundingClientRect();return {text:document.getElementById('captions').textContent,fit:a.left>=b.left&&a.right<=b.right&&a.top>=b.top&&a.bottom<=b.bottom}}""")
  assert c['fit'] and c['text']==cue['text'],c
  assert state['role']==cue['role'],state
  checks.append(c)
 for t in [12.3,13,15.1,18.1,21.8,23,26,28,32,38]:
  page.evaluate('(t)=>renderAt(t)',t)
  fit=page.evaluate("""()=>Array.from(document.querySelectorAll('#store-label,#unit-label,.chip,.source-title,.source-subtitle,.instance-title,.instance-type')).map(e=>{const a=e.getBoundingClientRect(),p=e.closest('.entity,#source,#instance').getBoundingClientRect();return {id:e.id||e.textContent,fit:a.left>=p.left-1&&a.right<=p.right+1&&a.top>=p.top-1&&a.bottom<=p.bottom+1}})""")
  assert all(v['fit'] for v in fit),fit
 page.evaluate('renderAt(38)')
 assert page.evaluate("""()=>['store','unit','instance','source','speaker'].every(id=>document.getElementById(id).getBoundingClientRect().bottom<document.getElementById('caption-band').getBoundingClientRect().top)""")
 assert not errors,errors
 (R/'layout-check.json').write_text(json.dumps({'captions':checks,'speaker_roles':'all caption midpoints match dialogue role','caption_separation':'passed','label_bounds':'10 intermediate/settled samples passed','browser_errors':errors},indent=2))
 enc=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-vcodec','mjpeg','-r','30','-i','pipe:0','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(R/'silent.mp4')],stdin=subprocess.PIPE)
 for i in range(frames):
  page.evaluate('(t)=>renderAt(t)',i/30);enc.stdin.write(page.screenshot(type='jpeg',quality=98))
  if i%200==0:print(f'{i}/{frames}',flush=True)
 enc.stdin.close();assert enc.wait()==0;b.close()
