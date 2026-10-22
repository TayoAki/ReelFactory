from pathlib import Path
import subprocess,sys
R=Path(__file__).resolve().parent
for script in ['build.py','enrich.py','build_review.py','validate.py']:
 subprocess.run([sys.executable,str(R/script)],check=True)
