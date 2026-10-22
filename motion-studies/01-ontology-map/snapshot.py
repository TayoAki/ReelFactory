from playwright.sync_api import sync_playwright
from pathlib import Path
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1920,'height':1080});page.goto('http://127.0.0.1:8765/motion-studies/01-ontology-map/index.html');page.evaluate('document.fonts.ready');page.wait_for_function('!!window.__timelines?.main');s=Image.new('RGB',(1280,404),'#111820');d=ImageDraw.Draw(s)
 for j,t in enumerate([.4,1,3,3.6,4,5.2,6,7]):
  page.evaluate('(t)=>{window.__timelines.main.seek(t);return true}',t);f=root/f'state-{j}.png';page.screenshot(path=str(f));x=j%4*320;y=j//4*202;s.paste(Image.open(f).resize((320,180)),(x,y));d.text((x+4,y+182),str(t),fill='white')
 s.save(root/'reconstruction-states.jpg');b.close()
