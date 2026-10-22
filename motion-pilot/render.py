from playwright.sync_api import sync_playwright
import subprocess
from pathlib import Path
root=Path(__file__).resolve().parent
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1)
 page.goto('http://127.0.0.1:8765/motion-pilot/scene.html');page.evaluate('document.fonts.ready');page.wait_for_function('Array.from(document.images).every(i=>i.complete)')
 enc=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-vcodec','png','-r','30','-i','pipe:0','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(root/'silent.mp4')],stdin=subprocess.PIPE)
 for i in range(279):
  page.evaluate('(t)=>renderAt(t)',i/30)
  data=page.screenshot()
  enc.stdin.write(data)
  if i in [21,84,144,204]: (root/f'state-{i:03}.png').write_bytes(data)
 enc.stdin.close();assert enc.wait()==0
 b.close()
