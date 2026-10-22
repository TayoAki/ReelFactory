from pathlib import Path
import subprocess,json
import numpy as np
root=Path('/workspace/ReelFactory/videos/14-fabric-ontology-explained');checks=[]
for label,a,z in [('entity morph',25.8,26.5),('relationship draw',34.3,35.2),('source detail zoom',54.3,56.8),('shipment route highlight',76,77.4)]:
 raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(a),'-i',str(root/'out/final.mp4'),'-t',str(z-a),'-vf','crop=1300:750:72:140,scale=320:185','-pix_fmt','rgb24','-f','rawvideo','-']);frames=np.frombuffer(raw,np.uint8).reshape(-1,185,320,3).astype(np.int16);diff=np.abs(np.diff(frames,axis=0));means=diff.mean(axis=(1,2,3));fraction=float(np.mean(means>.005));checks.append({'segment':label,'start':a,'end':z,'decoded_frames':len(frames),'fraction_of_frame_pairs_with_visible_change':round(fraction,4),'mean_RGB_delta_per_frame':round(float(means.mean()),4)})
(root/'out/animation-check.json').write_text(json.dumps({'method':'Successive decoded final-video frames at 30 fps in active animation windows; motion continuity check, not an aesthetic equivalence score','checks':checks},indent=2));print(json.dumps(checks));assert all(c['fraction_of_frame_pairs_with_visible_change']>.8 for c in checks)
