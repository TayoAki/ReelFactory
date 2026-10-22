import json,subprocess
from pathlib import Path
import cv2,numpy as np
root=Path(__file__).resolve().parent;parts=json.loads((root.parents[1]/'research/ontology-adaptation/uploaded-parts.json').read_text());src=parts[0]['path'];rows=[]
for t in [8.1,8.2,8.3,8.4,8.6,8.8,9,10,10.4,10.8,11,11.2,11.6,12,12.4,12.8,13,13.2,13.4,13.6,13.8,14,14.2,14.6,15,15.2]:
 raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(t),'-i',src,'-frames:v','1','-pix_fmt','rgb24','-f','rawvideo','-']);im=np.frombuffer(raw,np.uint8).reshape(360,640,3);r,g,b=im[:,:,0],im[:,:,1],im[:,:,2];mask=((r>100)&(r<210)&(g>40)&(g<140)&(b>35)&(b<110)&(r.astype(float)>g*1.25)).astype(np.uint8)*255;mask[320:]=0;cs,_=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE);boxes=[]
 for c in cs:
  x,y,w,h=cv2.boundingRect(c)
  if 195<x<440 and 70<y<180 and 85<w<190 and .8<w/h<1.2:boxes.append((x,y,w,h))
 best=max(boxes,key=lambda b:b[2]*b[3]) if boxes else None;rows.append(dict(time=t,bbox=best));print(t,best)
(root/'source-card-track.json').write_text(json.dumps(rows,indent=2))
subprocess.run(['ffmpeg','-v','error','-y','-ss','8','-i',src,'-t',str(218/30),'-c:v','libx264','-preset','fast','-crf','18','-an','-movflags','+faststart',str(root/'source.mp4')],check=True)
