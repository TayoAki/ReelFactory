import json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
n=json.loads((R/'narration.json').read_text());D=n['duration']
args=['ffmpeg','-y','-loglevel','error']
for i in range(len(n['segments'])):args+=['-i',str(R/'assets'/f'voice-{i}.mp3')]
f=[]
for i,s in enumerate(n['segments']):f.append(f'[{i}:a]adelay={round(s["start"]*1000)}:all=1[a{i}]')
f.append(''.join(f'[a{i}]' for i in range(len(n['segments'])))+'amix=inputs='+str(len(n['segments']))+':duration=longest:normalize=0,apad,atrim=duration='+str(D)+'[out]')
subprocess.run(args+['-filter_complex',';'.join(f),'-map','[out]','-c:a','aac','-b:a','160k',str(R/'ontology-narration.m4a')],check=True)
if (R/'silent.mp4').exists():
 subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(R/'silent.mp4'),'-i',str(R/'ontology-narration.m4a'),'-map','0:v:0','-map','1:a:0','-c','copy','-t',str(D),'-movflags','+faststart',str(R/'fabric-ontology-captioned.mp4')],check=True)
