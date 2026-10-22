from pathlib import Path
import subprocess,json,concurrent.futures
import numpy as np
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;ROOT=R.parent;parts=json.loads((ROOT/'research/ontology-adaptation/uploaded-parts.json').read_text())
def scan(item):
 i,p=item;folder=R/'source-scan'/f'part{i:02}';folder.mkdir(exist_ok=True);subprocess.run(['ffmpeg','-v','error','-y','-i',p['path'],'-vf','fps=1,scale=320:180','-vsync','0',str(folder/'%04d.jpg')],check=True);return folder
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:folders=list(pool.map(scan,enumerate(parts)))
rows=[];offset=0
for i,(p,folder) in enumerate(zip(parts,folders)):
 for j,f in enumerate(sorted(folder.glob('*.jpg'))):
  t=offset+j+.5;im=np.asarray(Image.open(f));pane=im[28:153,8:233];light=(pane.min(2)>205).mean();dark=((pane[:,:,0]<65)&(pane[:,:,1]<95)&(pane[:,:,2]<105)).mean();outside=im[8:22,8:225].mean((0,1));brown=outside[0]>outside[1]*1.5 and outside[1]<55;white=(im[8:22,8:225].min(2)>220).mean()>.75
  kind='brown-graphic' if brown and dark>.30 else 'ui-evidence' if brown and light>.35 else 'white-graphic' if white and light>.55 else 'chapter' if brown and (pane[:,:,0]>170).mean()>.55 else 'speaker-or-transition'
  rows.append({'time':round(t,3),'part':i,'frame':str(f.relative_to(R)),'kind':kind,'light':round(float(light),3),'dark':round(float(dark),3)})
 offset+=p['duration']
(R/'source-scan.json').write_text(json.dumps({'duration':offset,'sample_fps':1,'classification':'color/region candidates for manual inspection, not verified cut detection','frames':rows},indent=2))
# Full-timeline strips at 10s intervals; all samples retained for finer review.
chosen=[q for n,q in enumerate(rows) if n%10==0]
for g in range((len(chosen)+39)//40):
 group=chosen[g*40:g*40+40];sheet=Image.new('RGB',(1600,202*((len(group)+4)//5)),'#172129');d=ImageDraw.Draw(sheet)
 for k,q in enumerate(group):x=k%5*320;y=k//5*202;sheet.paste(Image.open(R/q['frame']),(x,y));d.text((x+5,y+182),f'{q["time"]:.1f}s {q["kind"]}',fill='white')
 sheet.save(R/'source-scan'/f'overview-{g+1}.jpg',quality=92)
last=None
for q in rows:
 if q['kind']!=last:
  print(q['time'],q['kind']);last=q['kind']
