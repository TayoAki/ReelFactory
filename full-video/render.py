from pathlib import Path
import json,math,subprocess,concurrent.futures,sys
from PIL import Image,ImageDraw
import graphics as g
R=Path(__file__).resolve().parent;P=json.loads((R/'plan.json').read_text());O=R/'renders';O.mkdir(exist_ok=True);V=R/'previews';V.mkdir(exist_ok=True)
def run(args):subprocess.run(args,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
def render(s):
 out=O/(s['id']+'.mp4')
 if out.exists():return s['id']+' cached'
 n=round(s['source_end']*30)-round(s['source_start']*30);dur=n/30
 if s['kind']=='existing':
  run(['ffmpeg','-y','-i',str(R.parent/'practice/databricks-01/planning/generated/graphics-refined-v2.mp4'),'-an','-t',str(dur),'-r','30','-c:v','libx264','-preset','veryfast','-crf','19','-threads','2','-pix_fmt','yuv420p',str(out)]);return s['id']
 temp=O/(s['id']+'-base.mp4');p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','30','-i','pipe:0','-an','-c:v','libx264','-preset','veryfast','-crf','19','-threads','2','-pix_fmt','yuv420p',str(temp)],stdin=subprocess.PIPE)
 last=None;data=None
 for i in range(n):
  t=s['source_start']+i/30;ct=g.cache_time(s,t)
  if ct!=last:data=g.native(s,ct).tobytes();last=ct
  p.stdin.write(data)
 p.stdin.close()
 if p.wait():raise RuntimeError(s['id'])
 if s['kind'] in ['hybrid','demo','demo-overlay']:
  x,y,w,h=g.ui_box(s['id']);dx=(x-12)*3+36;dy=(y-50)*3+150
  if s['kind'].startswith('demo'):
   x,y,w,h=12,30,458,282;dx,dy=36,150;sw,sh=1374,786
   if s['kind']=='demo-overlay':y=188;h=124;dy=150+round(158*786/282);sh=786-round(158*786/282)
  else:sw,sh=w*3,h*3
  enable=":enable='lt(t,8)+gte(t,25)'" if s['id']=='skills' else ''
  filt=f'[1:v]crop={w}:{h}:{x}:{y},scale={sw}:{sh}:flags=lanczos,setpts=PTS-STARTPTS[ui];[0:v][ui]overlay={dx}:{dy}:shortest=1{enable}[v]'
  run(['ffmpeg','-y','-i',str(temp),'-ss',str(s['source_start']),'-i',str(R/'original.mp4'),'-filter_complex',filt,'-map','[v]','-an','-t',str(dur),'-r','30','-c:v','libx264','-preset','veryfast','-crf','19','-threads','2','-pix_fmt','yuv420p',str(out)]);temp.unlink()
 else:temp.rename(out)
 return s['id']
def previews():
 sheets=[]
 for s in P['scenes']:
  if s['kind']=='existing':continue
  t=min(s['source_end']-.1,s['source_start']+max(1,s['duration']*.6));im=g.native(s,t);im.save(V/(s['id']+'.jpg'),quality=90)
  thumb=im.resize((384,216));card=Image.new('RGB',(384,245),'#111b22');card.paste(thumb,(0,25));ImageDraw.Draw(card).text((6,5),f"{s['number']:02} {s['id']}  {t:.1f}s",fill='white');sheets.append(card)
 for j in range(0,len(sheets),12):
  sheet=Image.new('RGB',(1536,735),'#111b22')
  for i,im in enumerate(sheets[j:j+12]):sheet.paste(im,(i%4*384,i//4*245))
  sheet.save(V/f'sheet-{j//12}.jpg')
if __name__=='__main__':
 if '--preview' in sys.argv:previews()
 else:
  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
   for f in concurrent.futures.as_completed([ex.submit(render,s) for s in P['scenes']]):print(f.result(),flush=True)
  (R/'render-concat.txt').write_text('\n'.join("file '"+str(O/(s['id']+'.mp4'))+"'" for s in P['scenes']))
  run(['ffmpeg','-y','-f','concat','-safe','0','-i',str(R/'render-concat.txt'),'-i',str(R/'original.mp4'),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','128k','-t',str(P['source_duration']),'-movflags','+faststart',str(R/'full-reconstruction.mp4')])
