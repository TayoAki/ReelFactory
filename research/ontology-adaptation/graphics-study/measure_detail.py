from pathlib import Path
from PIL import Image
import subprocess,json
import numpy as np
root=Path(__file__).resolve().parent;parts=json.loads((root.parent/'uploaded-parts.json').read_text());offsets=[];off=0
for p in parts:offsets.append(off);off+=p['duration']
# Dense regional changes. Thresholding detects visible changes; it cannot reveal original keyframes/easing.
ranges=[('card-stack',54.8,57,(150,90,200,180)),('architecture-camera',233.8,236.5,(12,50,458,262)),('governance-flip',1429,1432,(50,124,160,136)),('list-focus',1989.3,1990.1,(170,64,290,100))];reports=[]
for name,a,z,(x,y,w,h) in ranges:
 k=max(i for i,o in enumerate(offsets) if o<=a);raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(a-offsets[k]),'-i',parts[k]['path'],'-t',str(z-a),'-vf',f'crop={w}:{h}:{x}:{y},fps=30','-pix_fmt','rgb24','-f','rawvideo','-']);arr=np.frombuffer(raw,np.uint8).reshape(-1,h,w,3).astype(np.int16);delta=np.abs(np.diff(arr,axis=0));means=delta.mean(axis=(1,2,3));frac=(delta.max(axis=3)>15).mean(axis=(1,2));active=np.flatnonzero((means>.45)&(frac>.01));runs=[]
 for j in active:
  if not runs or j-runs[-1][-1]>2:runs.append([int(j)])
  else:runs[-1].append(int(j))
 intervals=[{'start':round(a+(r[0]+1)/30,3),'end':round(a+(r[-1]+2)/30,3),'duration':round((r[-1]-r[0]+1)/30,3)} for r in runs if len(r)>1];reports.append({'id':name,'roi':[x,y,w,h],'search_window':[a,z],'visible_change_intervals':intervals});print(name,intervals)
# Approximate point correspondence from OCR; glyph heights are not font sizes.
ocr={}
for name in ['D2-architecture-camera/00.png','D2-architecture-camera/11.png']:
 im=Image.open(root/name);up=root/'ocr-temp.png';im.resize((1920,1080)).save(up);result=subprocess.run(['tesseract',str(up),'stdout','--psm','11','tsv'],capture_output=True,text=True);rows=[]
 for line in result.stdout.splitlines()[1:]:
  f=line.split('\t')
  if len(f)>=12 and any(w in f[11].lower() for w in ['modeled','ontology']):rows.append(dict(text=f[11],x=round(int(f[6])/3,2),y=round(int(f[7])/3,2),width=round(int(f[8])/3,2),height=round(int(f[9])/3,2)))
 ocr[name]=rows;print(name,rows)
(root/'detail-measurements.json').write_text(json.dumps({'intervals':reports,'ocr_anchor_boxes':ocr,'limits':'30fps regional changes from compressed 360p input. Starts/ends threshold-dependent, approximately +/-2 frames; camera scale from OCR is approximate, not recovered source transforms.'},indent=2))
