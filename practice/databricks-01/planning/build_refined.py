"""Reproducible current-reference refinement. Does not bypass the storyboard review for new content."""
from pathlib import Path
import argparse,subprocess,sys,os
P=Path(__file__).resolve().parent;p=argparse.ArgumentParser();p.add_argument('--render',action='store_true');a=p.parse_args()
for name in ['generate_graphics.py','refine_graphics.py','readability-study/refine_captions.py']:subprocess.run([sys.executable,str(P/name)],check=True)
if a.render:
 env=dict(os.environ,HYPERFRAMES_BROWSER_PATH='/usr/bin/chromium');subprocess.run(['npx','-y','hyperframes@0.8.181','render',str(P/'generated'),'-q','high','-f','30','--workers','4','-o',str(P/'generated/render.mp4')],env=env,check=True)
 for name in ['package_graphics.py','readability-study/build_findings.py','build_review.py','verify_outputs.py']:subprocess.run([sys.executable,str(P/name)],check=True)
