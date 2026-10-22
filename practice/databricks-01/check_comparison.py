from pathlib import Path
from playwright.sync_api import sync_playwright
import json
r=Path(__file__).resolve().parent
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1920,'height':1080});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto('http://127.0.0.1:8765/practice/databricks-01/index.html');page.wait_for_function('!!window.__timelines?.main');states=[]
 for t in [38.,42.5,49.4,51.7,57.,70.,78.,82.]:
  q=page.evaluate('''t=>{window.__timelines.main.seek(t-1120/30);return Object.fromEntries(['family','chat','chat-boundary','code','agents','full-speaker','intro-speaker'].map(id=>[id,Number(getComputedStyle(document.getElementById(id)).opacity)]))}''',t);states.append({'source_time':t,**q})
 assert states[0]['intro-speaker']==1
 assert states[1]['family']==1 and states[1]['chat']==0
 assert states[2]['chat']==1 and states[2]['family']==0
 assert states[3]['chat-boundary']==1
 assert states[4]['family']==1 and states[4]['chat']==0
 assert states[5]['code']==1 and states[5]['agents']==0
 assert states[6]['code']==1 and states[6]['agents']==1
 assert states[7]['full-speaker']==1
 page.goto('http://127.0.0.1:8765/practice/databricks-01/comparison-review.html');page.wait_for_function('document.querySelector("video").readyState>=1');v=page.locator('video');assert abs(v.evaluate('(v)=>v.duration')-46.3667)<.1
 page.locator('[data-time]').nth(5).click();page.wait_for_function('document.querySelector("video").currentTime>27');a=v.evaluate('(v)=>v.currentTime');page.locator('#forward').click();page.wait_for_function('t=>Math.abs(document.querySelector("video").currentTime-t)<.01',arg=a+1/30)
 page.locator('#speed').select_option('.5');assert v.evaluate('(v)=>v.playbackRate')==.5
 page.locator('#toggle').click();page.wait_for_function('document.querySelector("video").readyState>=1 && document.querySelector("#toggle").textContent==="Show revised attempt"');page.wait_for_function('t=>Math.abs(document.querySelector("video").currentTime-t)<.1',arg=a+1/30)
 assert not errors;b.close()
report={'graphic_states':states,'comparison_duration':46.3667,'frame_step':'passed','speed_control':'passed','before_after_switch_retains_time':'passed','page_errors':errors};(r/'comparison-check.json').write_text(json.dumps(report,indent=2));print('Graphic states, portable comparison, frame step, speed, before/after switch: passed')
