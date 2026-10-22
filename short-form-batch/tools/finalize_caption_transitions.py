"""Replace the caption area from its clean scene layer, then burn corrected nonoverlapping cues.
This preserves the already-rendered independent diagram motion and copies the actual audio stream.
"""
import pathlib,json,subprocess,concurrent.futures,time
from PIL import Image
R=pathlib.Path(__file__).resolve().parents[2];P=R/'short-form-batch/recording-clips';D=json.loads((P/'manifest.json').read_text());done=[]
def work(c):
 target=P/'exports'/f'{c["id"]}.mp4';cache=P/'render-cache'/c['id'];patch=cache/'clean-caption-band.png';tmp=cache/'caption-transition-final.mp4'
 im=Image.open(cache/'base.png');im.crop((60,1380,1020,1650)).save(patch)
 filt=f"[0:v][1:v]overlay=x=60:y=1380,ass={P/'captions'/str(c['id']+'.ass')}:fontsdir={P/'assets'},format=yuv420p[v]"
 cmd=['ffmpeg','-y','-v','error','-threads','1','-i',str(target),'-loop','1','-framerate','1','-i',str(patch),'-filter_complex_threads','1','-filter_complex',filt,'-map','[v]','-map','0:a','-t',str(c['duration']),'-c:v','libx264','-threads','1','-preset','veryfast','-crf','18','-c:a','copy','-movflags','+faststart',str(tmp)]
 subprocess.run(cmd,check=True);tmp.replace(target)
 return {'id':c['id'],'correction':'Nonoverlapping cue transitions; original caption area restored from clean base layer before replacement','audio':'AAC stream copied unchanged','video':'One additional H.264 encode at CRF 18; original diagram motion preserved'}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for row in pool.map(work,[c for c in D['clips'] if int(c['id'][1:])<=36]):done.append(row);print('CAPTION FINAL',row['id'],flush=True)
(P/'caption-transition-finalization.json').write_text(json.dumps(done,indent=2))
