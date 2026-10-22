from pathlib import Path
from playwright.sync_api import sync_playwright
import json,subprocess,numpy as np
r=Path(__file__).resolve().parent
arrays=[]
for p in [r/'assets/narration.wav',r/'practice.mp4']:
 raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ar','16000','-ac','1','-f','f32le','-']);arrays.append(np.frombuffer(raw,np.float32))
n=min(map(len,arrays));a,b=arrays[0][:n].astype(float),arrays[1][:n].astype(float);cor=float(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)));assert cor>.97
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=browser.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto('http://127.0.0.1:8765/practice/databricks-01/review.html');page.wait_for_function('document.querySelector("video").readyState>=1');assert page.locator('[data-beat]').count()==8;page.locator('[data-beat="4"]').click();page.wait_for_function('document.querySelector("#job").textContent==="Expand the category"');job=page.locator('#job').inner_text();assert job=='Expand the category';assert 'family' in page.locator('#why').inner_text();assert page.locator('video').evaluate('(v)=>v.currentTime')>16;assert not errors;browser.close()
report={'normalized_audio_waveform_correlation':round(cor,5),'original_source_narration_preserved':True,'player_scene_buttons':8,'teaching_job_and_rationale_navigation':'passed','page_errors':errors};(r/'delivery-check.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))
