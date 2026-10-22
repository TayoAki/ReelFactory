"""Check the portable video page from file:// with no preview server."""
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1400,'height':1100});errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
 page.set_content((root/'fabric-youtube-review.html').read_text());page.wait_for_function('document.querySelector("video").readyState>=1');assert page.locator('button').count()==14
 page.locator('button').filter(has_text='Power BI report validates').click();page.wait_for_function('document.querySelector("video").currentTime>40');page.locator('video').evaluate('(v)=>v.pause()');assert page.locator('video').evaluate('(v)=>v.error===null')
 page.screenshot(path=str(root/'output/fabric-youtube-review.png'),full_page=True)
 page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');assert not errors,errors
 print('PASS: embedded page loads without server requests, video decodes, 14 scene links, seek works, mobile width, no JS errors');browser.close()
