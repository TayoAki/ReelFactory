from pathlib import Path
import cv2,numpy as np,json
r=Path(__file__).resolve().parent;paths=sorted((r/'D2-architecture-camera').glob('[0-9][0-9].png'));base=cv2.imread(str(paths[0]),0);template=base[164:186,347:387];rows=[]
for j,p in enumerate(paths):
 img=cv2.imread(str(p),0)[50:312,12:470];best=(-1,None,None)
 for scale in np.linspace(.98,1.85,60):
  tmp=cv2.resize(template,None,fx=scale,fy=scale,interpolation=cv2.INTER_CUBIC);res=cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF_NORMED);_,v,_,xy=cv2.minMaxLoc(res)
  if v>best[0]:best=(v,scale,xy)
 val,s,(x,y)=best;rows.append(dict(time=round(233.8+j*(236.5-233.8)/11,3),match_confidence=round(float(val),3),scale=round(float(s),3),label_left=x+12,label_top=y+50))
(r/'camera-track.json').write_text(json.dumps({'method':'Multi-scale grayscale template match on the highlighted Modeled Ontology heading; estimates only, not original keyframes','samples':rows},indent=2));print(json.dumps(rows))
