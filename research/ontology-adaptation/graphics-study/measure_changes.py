from pathlib import Path
import subprocess,json
import numpy as np
root=Path(__file__).resolve().parent;parts=json.loads((root.parent/'uploaded-parts.json').read_text());offsets=[];off=0
for p in parts:offsets.append(off);off+=p['duration']
ranges=[('opening',8,15),('stack',55,81),('overview-focus',209.5,249),('modeled',249,333),('connectors',602,675),('governance',1423,1462),('agents',1473,1521),('rollout',1800,1956),('best-practices',1958,2043)]
results=[]
for name,a,z in ranges:
 k=max(i for i,v in enumerate(offsets) if v<=a);proc=subprocess.Popen(['ffmpeg','-v','error','-ss',str(a-offsets[k]),'-i',parts[k]['path'],'-t',str(z-a),'-vf','fps=4,crop=458:262:12:50,scale=229:131','-pix_fmt','rgb24','-f','rawvideo','-'],stdout=subprocess.PIPE);n=229*131*3;prev=None;rows=[];j=0
 while True:
  data=proc.stdout.read(n)
  if len(data)!=n:break
  cur=np.frombuffer(data,np.uint8).reshape(131,229,3).astype(np.int16)
  if prev is not None:
   d=np.abs(cur-prev);rows.append({'time':round(a+(j+.5)/4,3),'mean_rgb_change':round(float(d.mean()),4),'changed_fraction_over_15':round(float((d.max(axis=2)>15).mean()),4)})
  prev=cur;j+=1
 proc.wait();active=[r for r in rows if r['mean_rgb_change']>.45 and r['changed_fraction_over_15']>.012];groups=[]
 for r in active:
  if not groups or r['time']-groups[-1][-1]['time']>.5:groups.append([r])
  else:groups[-1].append(r)
 intervals=[dict(start=g[0]['time']-.25,end=g[-1]['time'],peak_mean=max(r['mean_rgb_change'] for r in g)) for g in groups]
 results.append(dict(id=name,start=a,end=z,sample_rate=4,intervals=intervals,measurements=rows));print(name,intervals,flush=True)
(root/'motion-measurements.json').write_text(json.dumps(results,indent=2))
