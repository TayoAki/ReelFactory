from pathlib import Path
from PIL import Image,ImageDraw
import subprocess,json
root=Path('/workspace/ReelFactory/videos/14-fabric-ontology-explained');out=root/'out/final-scenes';out.mkdir(exist_ok=True);shots=json.loads((root/'work/shots.json').read_text());sheet=Image.new('RGB',(1920,((len(shots)+2)//3)*400),'#172127');d=ImageDraw.Draw(sheet)
for i,s in enumerate(shots):
 t=round(s['start']+(s['end']-s['start'])*.7,3);f=out/f'{i:02}.jpg';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(root/'out/final.mp4'),'-frames:v','1','-vf','scale=640:360',str(f)],check=True);x=i%3*640;y=i//3*400;sheet.paste(Image.open(f),(x,y));d.text((x+10,y+365),f'{i+1:02} / {t:.2f}s / '+s['scene'][:55],fill='white')
sheet.save(out/'all-scenes.jpg',quality=92);print(len(shots),'final scene samples extracted')
