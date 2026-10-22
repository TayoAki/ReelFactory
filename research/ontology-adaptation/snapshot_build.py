from playwright.sync_api import sync_playwright
from pathlib import Path
import json
from PIL import Image,ImageDraw
root=Path('/workspace/ReelFactory/videos/14-fabric-ontology-explained');shots=json.loads((root/'work/shots.json').read_text());out=root/'out/native-review';out.mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1920,'height':1080});page.goto('http://127.0.0.1:8765/videos/'+root.name+'/index.html');page.evaluate('document.fonts.ready');page.wait_for_function('!!window.__timelines?.main')
 for i,s in enumerate(shots):
  t=min(s['end']-.1,s['start']+max(1,(s['end']-s['start'])*.7));page.evaluate('''t=>{window.__timelines.main.pause().seek(t);for(const e of document.querySelectorAll('.clip')){const a=+e.dataset.start,z=a+(+e.dataset.duration);e.style.display=t>=a&&t<z?'':'none'}for(const v of document.querySelectorAll('video')){v.currentTime=+v.dataset.mediaStart+Math.max(0,t-(+v.dataset.start))}}''',t);page.wait_for_timeout(100);page.screenshot(path=str(out/f'{i:02}.png'))
 b.close()
for batch in range((len(shots)+7)//8):
 sheet=Image.new('RGB',(1280,808),'#181b20');d=ImageDraw.Draw(sheet)
 for j,s in enumerate(shots[batch*8:batch*8+8]):
  i=batch*8+j;x=j%2*640;y=j//2*202;sheet.paste(Image.open(out/f'{i:02}.png').resize((640,360)).resize((320,180)),(x,y));d.text((x+325,y+20),f'{i+1:02} / {s["start"]:.2f}s',fill='white');d.text((x+325,y+50),s['scene'][:35],fill='white')
 sheet.save(out/f'sheet-{batch}.jpg')
print('Native snapshots complete')
