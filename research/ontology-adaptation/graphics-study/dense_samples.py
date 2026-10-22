from pathlib import Path
import subprocess,json
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent;parts=json.loads((root.parent/'uploaded-parts.json').read_text());offsets=[];off=0
for p in parts:offsets.append(off);off+=p['duration']
seq=[('D1-stack-morph',54.8,57.0),('D2-architecture-camera',233.8,236.5),('D3-connector-build',603,612),('D4-governance-card',1428,1434),('D5-agent-camera',1484,1491),('D6-best-practice-focus',1988.8,1990.8)]
for name,a,z in seq:
 if name!='D6-best-practice-focus':continue
 folder=root/name;folder.mkdir(exist_ok=True);s=Image.new('RGB',(1280,606),'#101820');d=ImageDraw.Draw(s)
 for j in range(12):
  t=a+(z-a)*j/11;k=max(i for i,v in enumerate(offsets) if v<=t);f=folder/f'{j:02}.png';subprocess.run(['ffmpeg','-v','error','-ss',str(t-offsets[k]),'-i',parts[k]['path'],'-frames:v','1','-y',str(f)],check=True);x=j%4*320;y=j//4*202;s.paste(Image.open(f).resize((320,180)),(x,y));d.text((x+3,y+182),f'{t:.3f}s',fill='white')
 s.save(root/(name+'.jpg'),quality=95)
(root/'dense-sequences.json').write_text(json.dumps([dict(id=n,start=a,end=z) for n,a,z in seq],indent=2));print('6 dense motion sequences created')
