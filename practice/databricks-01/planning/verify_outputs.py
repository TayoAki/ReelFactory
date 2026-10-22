from pathlib import Path
import json,subprocess,concurrent.futures
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parent;G=P/'generated';manifest=json.loads((G/'manifest.json').read_text());assert len(manifest['scenes'])==12
files=[G/'graphics.mp4',G/'comparison.mp4']
for s in manifest['scenes']:
 folder=G/s['folder'];assert (folder/'graphic.png').exists()
 for phase in ['start','middle','end']:
  assert (folder/f'comparison-{phase}.jpg').exists();assert (folder/f'generated-{phase}.png').exists();assert (folder/f'original-{phase}.png').exists()
 files.extend([folder/'motion.mp4',folder/'comparison.mp4'])
def verify(f):
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(f)]));v=next(s for s in info['streams'] if s['codec_type']=='video');assert v['r_frame_rate']=='30/1';assert any(s['codec_type']=='audio' for s in info['streams']);subprocess.run(['ffmpeg','-v','error','-i',str(f),'-f','null','-'],check=True);return {'file':str(f.relative_to(P)),'duration':float(info['format']['duration']),'resolution':[v['width'],v['height']],'decode':'passed'}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:media=list(pool.map(verify,files))
assert abs(media[0]['duration']-manifest['duration'])<.08
for i,s in enumerate(manifest['scenes']):
 for clip in media[2+i*2:4+i*2]:assert abs(clip['duration']-s['duration'])<.10
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1440,'height':1100});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto('http://127.0.0.1:8765/practice/databricks-01/planning/template-review.html');page.wait_for_function('document.querySelector("#full").readyState>=1');assert page.locator('[data-scene]').count()==12;assert page.locator('.source-recipe').count()==27
 for i in range(12):
  page.locator(f'[data-scene="{i}"]').click();assert 'Scene '+str(i+1).zfill(2) in page.locator('#title').inner_text()
  for phase in ['start','middle','end']:
   page.locator(f'[data-phase="{phase}"]').click();page.locator('#frame').evaluate('(e)=>e.decode()');assert page.locator('#frame').evaluate('(e)=>e.naturalWidth')==1280
 page.wait_for_function('document.querySelector("#scene-video").readyState>=1');page.locator('#speed').select_option('.5');assert page.locator('#scene-video').evaluate('(v)=>v.playbackRate')==.5;page.locator('#plus').click();page.wait_for_function('document.querySelector("#scene-video").currentTime>0')
 page.locator('.source-recipe').nth(26).locator('summary').first.click();assert page.locator('.source-recipe').nth(26).evaluate('(e)=>e.open');assert not errors
 page.locator('[data-scene="6"]').click();page.locator('#frame').evaluate('(e)=>e.decode()');page.screenshot(path=str(G/'review-screen.png'),full_page=False)
 # Inspect visible leaf text and graphic bounds at regular intermediate frames in the editable composition.
 page.goto('http://127.0.0.1:8765/practice/databricks-01/planning/generated/index.html');page.set_viewport_size({'width':1920,'height':1080});page.wait_for_function('!!window.__timelines?.main')
 violations=page.evaluate('''()=>{let out=[];for(let t=0;t<46.36;t+=.25){window.__timelines.main.seek(t);document.querySelectorAll('.clip').forEach(e=>e.style.display=t>=+e.dataset.start&&t<+e.dataset.start+(+e.dataset.duration)?'':'none');for(const e of document.querySelectorAll('.product,.label,.node,.ev1-cap .w')){if(!e.getClientRects().length)continue;let opacity=1;for(let n=e;n;n=n.parentElement)opacity*=+getComputedStyle(n).opacity;if(opacity<.03)continue;const r=e.getBoundingClientRect();if(r.left<9||r.top<9||r.right>1911||r.bottom>1071)out.push({t,id:e.id,issue:'outside frame'});if(!e.children.length&&(e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2))out.push({t,id:e.id,issue:'leaf text overflow'})}}return out}''');assert not violations,violations[:5];b.close()
report={'scene_count':12,'matched_keyframe_pairs':36,'source_sequences_catalogued':27,'media':media,'review_controls':'12 scene buttons, 3 phases each, frame step, speed and source-library disclosure passed','layout_sample_interval_seconds':.25,'layout_violations':violations,'page_errors':errors,'limits':'Bounds/decode checks do not certify overlap semantics, factual correctness, exact easing or caption alignment.'};(G/'verification.json').write_text(json.dumps(report,indent=2));print('Verified 26 videos, 12 graphic exports, 36 matched pairs, 27 source recipes and review controls')
