import os,json,subprocess
from PIL import Image,ImageDraw
root=os.path.dirname(__file__);rows=json.load(open(root+'/uploaded-parts.json'));cuts=json.load(open(root+'/visual-change-candidates.json'));os.makedirs(root+'/changes',exist_ok=True)
for batch in range((len(cuts)+7)//8):
 sheet=Image.new('RGB',(1280,808),'#222');d=ImageDraw.Draw(sheet)
 for n,c in enumerate(cuts[batch*8:batch*8+8]):
  for side,dt in enumerate([-.25,.35]):
   t=min(rows[c['part']]['duration']-.15,max(0,c['local']+dt));p=f'{root}/changes/{batch*8+n:02}-{side}.jpg';subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',rows[c['part']]['path'],'-frames:v','1','-y',p],check=True)
   j=n*2+side;x=j%4*320;y=j//4*202;sheet.paste(Image.open(p).resize((320,180)),(x,y));g=c['global_time'];d.text((x+3,y+182),f'{int(g)//60:02}:{g%60:05.2f} '+('before' if side==0 else 'after'),fill='white')
 sheet.save(f'{root}/changes-{batch}.jpg')
print('done')
