from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path('/workspace/ReelFactory/research/ontology-adaptation/graphics-study')
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto('http://127.0.0.1:8765/research/ontology-adaptation/graphics-study/reference-graphics-inspector.html',wait_until='load');assert page.locator('.sequence').count()==27;assert page.locator('video').count()==7;assert page.locator('[data-seq]').count()==216
 page.locator('#hierMode').click();assert page.locator('#hierView').is_visible();page.locator('#cardMode').click();assert page.locator('#cardView').is_visible();page.locator('#showBoxes').uncheck();assert page.locator('#cardView .overlay').first.is_hidden();page.locator('#showBoxes').check();page.locator('#layoutMode').click();page.screenshot(path=str(root/'inspector-layout-check.png'))
 counts={}
 for k in range(5):page.locator('#partFilter').select_option(str(k));counts[k]=page.locator('.sequence:not(.hidden)').count();assert counts[k]>0
 page.locator('#partFilter').select_option('all');page.locator('[data-seq="7"][data-frame="3"]').click();assert page.locator('#modal').is_visible();old=page.locator('#frameTime').inner_text();page.locator('#next').click();assert page.locator('#frameTime').inner_text()!=old;page.keyboard.press('Escape');assert page.locator('#modal').is_hidden()
 for i in range(7):
  video=page.locator('video').nth(i);video.evaluate('(v)=>v.load()');page.wait_for_function('(i)=>document.querySelectorAll("video")[i].readyState>=1',arg=i);assert video.evaluate('(v)=>v.duration')>2;page.locator('.speed').nth(i).select_option('0.25');assert video.evaluate('(v)=>v.playbackRate')==.25
 assert not errors;report={'sequences':27,'frame_controls':216,'reference_loops':7,'all_loop_metadata_loaded':True,'part_filter_counts':counts,'layout_modes':'passed','frame_scrubber':'passed','playback_speed_controls':'passed','page_errors':errors};(root/'inspector-verification.json').write_text(json.dumps(report,indent=2));print(json.dumps(report));b.close()
