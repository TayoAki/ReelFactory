from pathlib import Path
import subprocess,concurrent.futures,json,csv,io
from PIL import Image
import numpy as np
R=Path(__file__).resolve().parent;SRC=R.parents[1]/'source.mp4';A=1120/30
subprocess.run(['ffmpeg','-v','error','-y','-i',str(SRC),'-vf','fps=6,crop=555:30:5:327,scale=1665:90','-vsync','0',str(R/'caption-samples/%04d.png')],check=True)
def inspect(f):
 out=subprocess.check_output(['tesseract',str(f),'stdout','--psm','7','tsv'],stderr=subprocess.DEVNULL,text=True);rows=list(csv.DictReader(io.StringIO(out),delimiter='\t'));words=[q for q in rows if q.get('text','').strip() and float(q.get('conf',-1))>0];im=np.asarray(Image.open(f).convert('RGB'));r,g,b=im[:,:,0],im[:,:,1],im[:,:,2];mask=(r>135)&(g>55)&(g<185)&(b<80)&(r.astype(float)>g.astype(float)*1.25);yy,xx=np.where(mask);bounds=None
 if len(xx)>20:bounds=[int(np.percentile(xx,2)),int(np.percentile(yy,2)),int(np.percentile(xx,98)),int(np.percentile(yy,98))]
 highlight=None
 if bounds:
  overlaps=[max(0,min(int(w['left'])+int(w['width']),bounds[2])-max(int(w['left']),bounds[0])) for w in words]
  if overlaps and max(overlaps)>0:highlight=int(np.argmax(overlaps))
 i=int(f.stem)-1;return {'relative_time':round((i+.5)/6,4),'source_time':round(A+(i+.5)/6,4),'text':' '.join(w['text'] for w in words),'highlight_word':highlight,'orange_bounds':bounds,'words':[{'text':w['text'],'x':int(w['left'])/3+5,'y':int(w['top'])/3+327,'w':int(w['width'])/3,'h':int(w['height'])/3,'confidence':float(w['conf'])} for w in words]}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(inspect,sorted((R/'caption-samples').glob('*.png'))))
(R/'source-caption-measurements.json').write_text(json.dumps(rows,indent=2));last=None
for q in rows:
 if q['text']!=last:print(q['source_time'],q['text'],q['highlight_word']);last=q['text']
