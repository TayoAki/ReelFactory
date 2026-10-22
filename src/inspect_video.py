"""Extract review frames with exact timestamps; does not infer content from transcripts.
python src/inspect_video.py video.mp4 --start 0 --duration 8 --fps 2 --out output/reference
Use --fps 24 or 30 for an exhaustive short transition review at source frame rate.
"""
import argparse,json,subprocess,math
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
p=argparse.ArgumentParser();p.add_argument('video');p.add_argument('--start',type=float,default=0);p.add_argument('--duration',type=float,default=8);p.add_argument('--fps',type=float,default=2);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
if a.start<0 or not 0<a.duration<=60 or not 0<a.fps<=60:p.error('Use start>=0, duration 0–60 seconds, fps 0–60')
a.out.mkdir(parents=True,exist_ok=True)
if any(a.out.glob('frame-*.png')):p.error('Output already contains frames; choose a fresh folder')
subprocess.run(['ffmpeg','-v','error','-ss',str(a.start),'-i',a.video,'-t',str(a.duration),'-vf',f'fps={a.fps},scale=360:640:force_original_aspect_ratio=decrease,pad=360:640:(ow-iw)/2:(oh-ih)/2','-frames:v',str(math.ceil(a.duration*a.fps)),str(a.out/'frame-%05d.png')],check=True)
frames=sorted(a.out.glob('frame-*.png'))
if not frames:raise SystemExit('No frames extracted')
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15)
entries=[]
for offset in range(0,len(frames),20):
 batch=frames[offset:offset+20];sheet=Image.new('RGB',(360*5,670*math.ceil(len(batch)/5)),'#0b111a');d=ImageDraw.Draw(sheet)
 for j,f in enumerate(batch):
  n=offset+j;time=a.start+n/a.fps;x=j%5*360;y=j//5*670
  sheet.paste(Image.open(f),(x,y));d.text((x+8,y+645),f'{time:.3f}s / sample {n}',font=font,fill='white')
  entries.append({'file':f.name,'sample_time_seconds':round(time,6),'review_status':'not reviewed'})
 sheet.save(a.out/f'sheet-{offset//20+1:03}.jpg',quality=90)
(a.out/'frames.json').write_text(json.dumps({'input':Path(a.video).name,'sampling_fps':a.fps,'exhaustive':False,'note':'Sampling timestamps approximate FFmpeg fps filter output; use source frame timestamps for frame-exact EDL. No visual review is implied by extraction.','frames':entries},indent=2))
print(f'Extracted {len(frames)} frames; review sheets and annotate before making style claims.')
