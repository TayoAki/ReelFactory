from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parents[2]
subprocess.run([sys.executable,str(root/"src/build_recreations.py"),"--only",Path(__file__).resolve().parent.name],check=True)
