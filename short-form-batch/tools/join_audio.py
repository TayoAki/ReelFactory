from pathlib import Path
import json,subprocess,shutil
R=Path(__file__).resolve().parents[1];m=json.loads((R/'source-audio/manifest.json').read_text());original=R/'source-audio/original-parts';original.mkdir(exist_ok=True)
args=['ffmpeg','-y','-loglevel','error']
for p in m['parts']:
 dst=original/p['name']
 if not dst.exists():shutil.copyfile(p['path'],dst)
 args+=['-i',str(dst)]
f=''.join(f'[{i}:a]' for i in range(5))+'concat=n=5:v=0:a=1[a]'
subprocess.run(args+['-filter_complex',f,'-map','[a]','-c:a','aac','-b:a','192k','-movflags','+faststart',str(R/'source-audio/combined-working.m4a')],check=True)
print('Combined original discussion audio',flush=True)
