"""Portable silent vertical edit. Pillow frames -> FFmpeg H.264; no paid APIs."""
import json, math, subprocess, argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from lab import run
ROOT=Path(__file__).resolve().parents[1]
W,H=540,960
BG='#0b111a'; PANEL='#141f2c'; FG='#edf4f7'; MUTED='#92a6b6'; MINT='#73f1c4'; RED='#ff858b'; PURPLE='#b8a0ff'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
def font(n,b=False,mono=False):return ImageFont.truetype(MONO if mono else BOLD if b else FONT,n)
def txt(d,xy,s,n=20,fill=FG,b=False,mono=False):d.text(xy,s,font=font(n,b,mono),fill=fill)
def box(d,xy,fill=PANEL,outline=None):d.rounded_rectangle(xy,14,fill=fill,outline=outline,width=2)
def wrap(d,s,width,n):
 out=[];line=''
 for w in s.split():
  test=(line+' '+w).strip()
  if d.textlength(test,font=font(n))>width and line:out.append(line);line=w
  else:line=test
 if line:out.append(line)
 return out

def frame(sc,p,idx,elapsed,total,evidence):
 im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
 # Quiet technical grid, behind a consistent editorial frame.
 for x in range(0,W,36):d.line((x,120,x,790),fill='#101a26')
 for y in range(120,790,36):d.line((0,y,W,y),fill='#101a26')
 txt(d,(36,47),'REEL / FACTORY',13,MINT,True);txt(d,(375,47),'FIELD NOTES',12,MUTED)
 d.line((36,85,504,85),fill='#2b3b4a')
 txt(d,(36,112),sc['eyebrow'],12,MINT,True)
 # Small entrance, then settle for reading.
 dy=int(15*(1-min(1,p*8))**2)
 for j,line in enumerate(sc['title']):txt(d,(34,155+j*49+dy),line,32,FG if j==0 else MINT,True)
 kind=sc['kind'];top=310
 box(d,(34,top,506,716))
 txt(d,(55,331),'MICROSOFT / DOCUMENTATION IMAGE' if kind=='docs' else 'LOCAL LAB / SYNTHETIC DATA',11,MUTED,True)
 if kind=='docs':
  raw=Image.open(ROOT/'content/fabric-watermark/assets'/sc['asset']).convert('RGB')
  fit=raw.copy();fit.thumbnail((440,150))
  im.paste(fit,(50+(440-fit.width)//2,380))
  # A closer view preserves the actual documentation pixels.
  if sc['asset']=='connect-lookup-copy.png':
   crop=raw.crop((480,105,760,245));label='DETAIL / COPY ACTIVITY'
  else:
   crop=raw.crop((850,85,1220,245));label='DETAIL / SAVE WATERMARK'
  crop.thumbnail((420,100));im.paste(crop,(60+(420-crop.width)//2,568))
  txt(d,(57,540),label,11,MUTED,True)
  txt(d,(55,686),'Microsoft Learn / CC BY 4.0 / crop',11,MUTED)
 elif kind in ['table','checkpoint','miss']:
  txt(d,(58,380),'ID',15,MUTED,True);txt(d,(202,380),'MODIFIED',15,MUTED,True)
  for j,r in enumerate(evidence['source']):
   y=423+j*64
   highlight=(kind=='table' and j<2) or (kind=='checkpoint' and j==0) or (kind=='miss' and j==1)
   if highlight:box(d,(49,y-8,490,y+42),'#35242d' if kind=='miss' else '#17392f')
   txt(d,(62,y),str(r['id']),24,RED if kind=='miss' and j==1 else FG,mono=True)
   txt(d,(202,y),r['modified'],23,MINT if highlight else FG,mono=True)
   if kind=='miss' and j==1:d.line((58,y+17,466,y+17),fill=RED,width=3)
  if kind=='checkpoint':txt(d,(57,643),'saved cursor: 10:00:00',18,MINT,mono=True)
  elif kind=='miss':txt(d,(57,638),'WHERE modified > 10:00:00',16,RED,mono=True)
  else:txt(d,(57,643),'101 and 102 share a timestamp.',17,MINT)
 elif kind=='hook':
  box(d,(57,384,483,451),'#17392f');txt(d,(79,404),'RUN COMPLETED',24,MINT,True)
  txt(d,(58,490),'EXPECTED',13,MUTED,True);txt(d,(306,490),'LOADED',13,MUTED,True)
  txt(d,(78,516),'3',98,FG,True);txt(d,(321,516),'2',98,RED,True)
  txt(d,(60,654),'Status and correctness can disagree.',17,MUTED)
 elif kind=='code':
  for j,line in enumerate(['ORDER BY modified, id','','WHERE modified > :time','   OR (modified = :time','       AND id > :id)']):txt(d,(56,389+j*37),line,17,MINT if j>=2 else FG,mono=True)
  box(d,(56,612,484,684),'#263047');txt(d,(74,627),'cursor = (10:00:00, 101)',17,PURPLE,mono=True);txt(d,(74,651),'next key: 102',15,FG,mono=True)
 elif kind=='proof':
  for j,key in enumerate(evidence['fixed_ids']):
   x=60+j*145;box(d,(x,401,x+128,503),'#17392f');txt(d,(x+21,430),str(key),29,MINT,True)
  for j,line in enumerate(['PASS  all source keys loaded','PASS  second upsert: 3 rows','PASS  no duplicate keys']):txt(d,(59,552+j*40),line,17,MINT,mono=True)
 elif kind=='boundary':
  for j,(a,b) in enumerate([('PROVEN HERE','Timestamp ties in a fixed snapshot'),('TEST SEPARATELY','Late arrivals / updates / deletes'),('ALSO REQUIRED','Checkpoint + write recovery')]):
   y=383+j*103;txt(d,(57,y),a,12,PURPLE if j else MINT,True)
   for k,line in enumerate(wrap(d,b,400,18)):txt(d,(57,y+28+k*25),line,18)
 else:
  for j,line in enumerate(['01  Compare expected keys','02  Repeat the same load','03  Inject a partial failure']):txt(d,(57,401+j*77),line,19,MINT if p>j*.2 else MUTED,True)
  txt(d,(57,656),'Make correctness observable.',18,PURPLE)
 for j,line in enumerate(wrap(d,sc['caption'],460,22)):txt(d,(36,754+j*32),line,22,FG)
 txt(d,(36,873),'MICROSOFT DOCS / REFERENCE IMAGE' if kind=='docs' else 'LOCAL DEMO  /  NOT A FABRIC RUN',11,MUTED,True)
 d.rectangle((36,914,504,917),fill='#263544');d.rectangle((36,914,36+468*elapsed/total,917),fill=MINT)
 txt(d,(36,932),f'{idx+1:02d} / {N_SCENES:02d}',10,MUTED);txt(d,(418,932),f'{int(elapsed):02d}:{int(total):02d}',10,MUTED)
 # Per-shot subtle camera movement in the lab panel is expressed by animated emphasis;
 # an onset line adds motion without moving the text during reading.
 d.line((35,top+1,35+int(469*min(1,p*2)),top+1),fill=MINT,width=2)
 return im

def main():
 global N_SCENES
 ap=argparse.ArgumentParser();ap.add_argument('--version',choices=['v1','v2'],default='v1');ap.add_argument('--fps',type=int,default=24);ap.add_argument('--stills-only',action='store_true');args=ap.parse_args()
 e=run();scenes=json.loads((ROOT/'content/fabric-watermark'/('scenes-v2.json' if args.version=='v2' else 'scenes.json')).read_text());N_SCENES=len(scenes);total=sum(s['duration'] for s in scenes)
 out=ROOT/'output'/('v2' if args.version=='v2' else '.');out.mkdir(parents=True,exist_ok=True);stills=[];elapsed=0
 for i,s in enumerate(scenes):
  im=frame(s,.5,i,elapsed+s['duration']/2,total,e);im.save(out/f'shot-{i+1:02}.png');stills.append(im);elapsed+=s['duration']
 sheet=Image.new('RGB',(W*4,H*math.ceil(len(scenes)/4)),BG)
 for i,im in enumerate(stills):sheet.paste(im,((i%4)*W,(i//4)*H))
 sheet.thumbnail((1440,1280));sheet.save(out/'contact-sheet.jpg',quality=92)
 if args.stills_only:return
 cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(args.fps),'-i','-','-an','-vf','scale=1080:1920:flags=lanczos','-c:v','libx264','-preset','fast','-crf','19','-threads','4','-pix_fmt','yuv420p','-movflags','+faststart',str(out/'fabric-watermark-silent.mp4')]
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE);elapsed=0
 try:
  for i,s in enumerate(scenes):
   for k in range(round(s['duration']*args.fps)):
    p=k/(s['duration']*args.fps);im=frame(s,p,i,elapsed+k/args.fps,total,e);proc.stdin.write(im.tobytes())
   elapsed+=s['duration'];print('Rendered',s['id'],flush=True)
 finally:proc.stdin.close()
 if proc.wait()!=0:raise RuntimeError('FFmpeg failed')
 print(out/'fabric-watermark-silent.mp4')
if __name__=='__main__':main()
