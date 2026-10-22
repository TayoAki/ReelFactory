from pathlib import Path
import subprocess
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent
pairs=[42.5,44.8,47.3,51.7,56.3,62.4,69.86,77.29,81.8]
for group in range(3):
 sheet=Image.new('RGB',(1280,3*390),'#172129');d=ImageDraw.Draw(sheet)
 for row,t in enumerate(pairs[group*3:group*3+3]):
  for col,file in enumerate(['source.mp4','previous-version/practice-v1.mp4']):
   out=r/f'compare-{group}-{row}-{col}.jpg';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t-1120/30),'-i',str(r/file),'-frames:v','1','-vf','scale=640:360',str(out)],check=True)
   sheet.paste(Image.open(out),(col*640,row*390+30));d.text((col*640+12,row*390+8),f'{"REFERENCE" if col==0 else "PREVIOUS PRACTICE"} | source {t:.2f}s',fill='white')
 sheet.save(r/f'comparison-sheet-{group}.jpg')
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'source.mp4'),'-i',str(r/'previous-version/practice-v1.mp4'),'-filter_complex',"[0:v]scale=640:360,pad=640:392:0:32:color=0x172129,drawtext=text='REFERENCE':x=12:y=8:fontsize=18:fontcolor=white[a];[1:v]scale=640:360,pad=640:392:0:32:color=0x172129,drawtext=text='PREVIOUS PRACTICE':x=12:y=8:fontsize=18:fontcolor=white[b];[a][b]hstack[v]",'-map','[v]','-map','1:a','-c:v','libx264','-crf','20','-preset','fast','-c:a','aac','-shortest','-movflags','+faststart',str(r/'comparison-before.mp4')],check=True)
