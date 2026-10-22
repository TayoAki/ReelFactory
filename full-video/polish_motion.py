from render import *
import time
while subprocess.run(['pgrep','-f','^/workspace/scratch/ev1-venv/bin/python /workspace/ReelFactory/full-video/refine_layout.py$'],capture_output=True).returncode==0:time.sleep(5)
ids={'intro-map','wrong-source','ambiguity','context-repair','architecture','learned','connectors','actions','skills','agents','rollout-one','rollout-two','demo-context-overlay','documents'}
scenes=[s for s in P['scenes'] if s['id'] in ids]
for s in scenes:(O/(s['id']+'.mp4')).unlink(missing_ok=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for f in concurrent.futures.as_completed([ex.submit(render,s) for s in scenes]):print('Motion pass:',f.result(),flush=True)
run(['ffmpeg','-y','-f','concat','-safe','0','-i',str(R/'render-concat.txt'),'-i',str(R/'original.mp4'),'-map','0:v','-map','1:a','-c:v','copy','-c:a','copy','-t',str(P['source_duration']),'-movflags','+faststart',str(R/'full-reconstruction.mp4')])
subprocess.run(['/workspace/scratch/ev1-venv/bin/python',str(R/'build_review.py')],check=True)
