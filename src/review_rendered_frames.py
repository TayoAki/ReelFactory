"""Produce review sheets from the actual final MP4, one sample per semantic beat."""
import json,math,subprocess
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont

ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
    for folder in sorted((ROOT/'videos').iterdir()):
        final=folder/'out/final.mp4';verification=folder/'out/verification.json';target=folder/'out/snaps/final-samples.json'
        if not final.exists() or not verification.exists() or target.exists():continue
        beats=json.loads((folder/'work/timeline.json').read_text())['beats'];out=target.parent;out.mkdir(exist_ok=True)
        info=json.loads(verification.read_text());fw,fh=(640,360) if info['width']>info['height'] else (360,640);cellh=fh+40
        sheet=Image.new('RGB',(fw*3,cellh*math.ceil(len(beats)/3)),'#141b23');draw=ImageDraw.Draw(sheet);entries=[]
        for i,beat in enumerate(beats):
            t=round((beat['start']+beat['voice_end'])/2,3);frame=out/f'final-{i+1:02}.jpg'
            subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(final),'-frames:v','1','-vf',f'scale={fw}:{fh},format=yuvj420p',str(frame)],check=True)
            x=i%3*fw;y=i//3*cellh;sheet.paste(Image.open(frame),(x,y));draw.text((x+12,y+fh+8),f'{i+1:02} / {t:.3f}s',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16),fill='white');entries.append({'time':t,'file':frame.name,'beat_text':beat['text']})
        sheet.save(out/'contact-sheet.jpg',quality=93);target.write_text(json.dumps({'source':'../final.mp4','review_scope':'one actual rendered frame per semantic beat; not exhaustive frame review','samples':entries},indent=2));print('Final-frame sheet',folder.name,flush=True)
