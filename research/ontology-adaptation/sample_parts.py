import json,os,subprocess
from PIL import Image,ImageDraw
root=os.path.dirname(__file__); rows=json.load(open(root+'/uploaded-parts.json'));offset=0
for i,r in enumerate(rows):
 folder=f'{root}/frames/part{i:02}';os.makedirs(folder,exist_ok=True)
 subprocess.run(['ffmpeg','-v','error','-i',r['path'],'-vf','fps=1/20','-q:v','3',folder+'/%03d.jpg'],check=True)
 import glob
 files=sorted(glob.glob(folder+'/*.jpg'));sheet=Image.new('RGB',(1280,((len(files)+3)//4)*202),'#222222');d=ImageDraw.Draw(sheet)
 for j,p in enumerate(files):
  im=Image.open(p).resize((320,180));x=j%4*320;y=j//4*202;sheet.paste(im,(x,y));t=offset+10+j*20;d.text((x+4,y+182),f'{int(t)//60:02}:{int(t)%60:02} global | part {i} ~{10+j*20}s',fill='white')
 sheet.save(f'{root}/part{i:02}-contact.jpg');offset+=r['duration']
print('Total',offset,'seconds; five contact sheets created')
