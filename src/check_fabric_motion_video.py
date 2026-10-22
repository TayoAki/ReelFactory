"""Check for visible motion in genuine demo regions of the final encoded video."""
from pathlib import Path
import json,subprocess,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[1];folder=ROOT/'videos'/(sys.argv[1] if len(sys.argv)>1 else '12-fabric-motion-refined');items=[]
if (folder/'work/source-excerpts.json').exists():
 original=json.loads((folder/'work/source-excerpts.json').read_text());manifest={'motion':[{'start':v['output_start'],'end':v['output_end'],'asset':v['asset'],'bounds':v.get('bounds',[280,140,1360,765])} for v in original['clips']]}
else:manifest=json.loads((folder/'work/motion-and-framing.json').read_text())
for clip in manifest['motion']:
 a,z=clip['start'],clip['end'];x,y,w,h=clip['bounds'];times=[a+(z-a)*.2,a+(z-a)*.8];frames=[]
 for t in times:
  raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(t),'-i',str(folder/'out/final.mp4'),'-frames:v','1','-vf',f'crop={w}:{h}:{x}:{y},scale=360:240','-pix_fmt','rgb24','-f','rawvideo','-']);frames.append(np.frombuffer(raw,dtype=np.uint8).reshape(240,360,3).astype(np.int16))
 delta=np.max(np.abs(frames[0]-frames[1]),axis=2);fraction=float(np.mean(delta>10));items.append({'asset':clip['asset'],'times':times,'fraction_of_region_pixels_changed_over_10':round(fraction,6),'visible_change':fraction>.0001})
report={'method':'Two decoded final-video frames per genuine demo segment; compare RGB pixel differences inside the video region, excluding captions and title','checks':items};(folder/'out/motion-check.json').write_text(json.dumps(report,indent=2));print(json.dumps(report));assert any(v['visible_change'] for v in items),'No moving demo segment detected; investigate the render'
