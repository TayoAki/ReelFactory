import subprocess,time
from pathlib import Path
R=Path(__file__).resolve().parent
while not (R/'full-reconstruction.mp4').exists():time.sleep(5)
# Wait until the render driver exits: the MP4 may exist before its index is written.
while subprocess.run(['pgrep','-f','^/workspace/scratch/ev1-venv/bin/python full-video/render.py$'],capture_output=True).returncode==0:time.sleep(5)
subprocess.run(['/workspace/scratch/ev1-venv/bin/python',str(R/'refine_layout.py')],check=True)
subprocess.run(['/workspace/scratch/ev1-venv/bin/python',str(R/'build_review.py')],check=True)
