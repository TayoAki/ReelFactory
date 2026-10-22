from pathlib import Path
from PIL import Image
import cairosvg
A=Path(__file__).resolve().parent/'assets'
for p in A.glob('*.svg'):
 if p.stem=='genie':continue
 svg=p.read_text()
 for color,label in [('#eaf3f4','light'),('#70c3c3','teal'),('#eb795f','red'),('#35585f','dark')]:
  svg2=svg.replace('<path ',f'<path fill="{color}" ').replace('currentColor',color)
  (A/(p.stem+'-'+label+'.png')).write_bytes(cairosvg.svg2png(bytestring=svg2.encode(),output_width=144,output_height=144))
p=A/'guest-full.png';im=Image.open(p);im.crop((0,0,1920,995)).resize((1920,1080),Image.Resampling.LANCZOS).save(p)
