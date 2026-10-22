from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
import json
r=Path(__file__).resolve().parent;plan=json.loads((r/'storyboard.json').read_text())['beats'];sheet=Image.new('RGB',(1280,808),'#17212a');d=ImageDraw.Draw(sheet)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1920,'height':1080});page.goto('http://127.0.0.1:8765/practice/databricks-01/index.html');page.evaluate('document.fonts.ready');page.wait_for_function('!!window.__timelines?.main')
 for i,beat in enumerate(plan):
  t=beat['start']+(beat['end']-beat['start'])*.8;page.evaluate('''t=>{window.__timelines.main.seek(t);for(const e of document.querySelectorAll('.clip')){let a=+e.dataset.start,z=a+(+e.dataset.duration);e.style.display=t>=a&&t<z?'':'none'}}''',t);f=r/f'frame-{i}.png';page.screenshot(path=str(f));x=i%2*640;y=i//2*202;sheet.paste(Image.open(f).resize((320,180)),(x,y));d.text((x+328,y+30),beat['id'],fill='white');d.text((x+328,y+55),f'{t:.2f}s',fill='white')
 page.evaluate('''()=>{window.__timelines.main.seek(43);for(const e of document.querySelectorAll('.clip')){let a=+e.dataset.start,z=a+(+e.dataset.duration);e.style.display=43>=a&&43<z?'':'none'}}''');print(page.evaluate('''()=>Object.fromEntries(['one','code','agents'].map(id=>{const r=document.getElementById(id).getBoundingClientRect();return[id,{x:r.x/3,y:r.y/3,w:r.width/3,h:r.height/3}]}))'''));b.close()
sheet.save(r/'storyboard-frames.jpg')
