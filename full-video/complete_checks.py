from pathlib import Path
import time,subprocess,concurrent.futures
R=Path(__file__).resolve().parent
while not (R/'review.html').exists():
 active=subprocess.run(['pgrep','-f','^/workspace/scratch/ev1-venv/bin/python /workspace/ReelFactory/full-video/build_review.py$'],capture_output=True).returncode==0
 if not active:raise RuntimeError('Review builder ended without review.html; inspect final-pass.log')
 time.sleep(5)
def check(name):
 result=subprocess.run(['/workspace/scratch/ev1-venv/bin/python',str(R/name)],capture_output=True,text=True);(R/(name+'.log')).write_text(result.stdout+result.stderr);result.check_returncode();print(name+' completed',flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(check,['verify.py','build_atlas.py']))
