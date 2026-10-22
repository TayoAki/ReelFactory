from pathlib import Path
import json
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parent
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=browser.new_page(viewport={'width':1360,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:8765/full-video/review.html',wait_until='domcontentloaded',timeout=60000)
 count=page.locator('body > details').count();assert count==44,count
 page.locator('body > details > summary').first.click();v=page.locator('video').first;v.evaluate('(v)=>v.load()');page.wait_for_function('document.querySelector("video").readyState>=2',timeout=30000);v.evaluate('(v)=>v.play()');page.wait_for_timeout(700);state=v.evaluate('(v)=>({time:v.currentTime,duration:v.duration,width:v.videoWidth,height:v.videoHeight})');assert state['time']>0;v.evaluate('(v)=>v.pause()');page.screenshot(path=str(R/'review-ui.png'))
 assert not errors,errors
 browser.close()
(R/'ui-verification.json').write_text(json.dumps({'top_level_sections':count,'embedded_motion_clip_playback':state,'page_errors':errors,'screenshot':'review-ui.png'},indent=2));print('Review UI: 44 sections, embedded clip plays, no page errors')
