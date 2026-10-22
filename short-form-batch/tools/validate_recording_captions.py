"""Inspect the final subtitle artifacts for overflow, conflicting cues and invalid clocks."""
import pathlib,json,re
from PIL import ImageFont
P=pathlib.Path(__file__).resolve().parents[1]/'recording-clips';font=ImageFont.truetype(str(P/'assets/CaptionSans.ttf'),55);bold=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',55);bad=[];timing=[];maxw=0;count=0

def seconds(s):
 a,b,c=s.replace(',','.').split(':');return int(a)*3600+int(b)*60+float(c)
for p in sorted((P/'captions').glob('*.ass')):
 prev=0
 for line in p.read_text().splitlines():
  if not line.startswith('Dialogue:'):continue
  a=line.split(',',9);start,end=seconds(a[1]),seconds(a[2]);count+=1
  if end<=start or start<prev-.015:timing.append({'clip':p.stem,'start':start,'end':end,'previous_end':prev})
  prev=end
  text=re.sub(r'\{[^}]*\}','',a[-1])
  for row in text.split('\\N'):
   w=font.getlength(row)+max([bold.getlength(x)-font.getlength(x) for x in row.split()] or [0]);maxw=max(maxw,w)
   if w>870:bad.append({'clip':p.stem,'text':row,'width':w})
for p in sorted((P/'captions').glob('*.vtt')):
 prev=0
 for line in p.read_text().splitlines():
  if ' --> ' not in line:continue
  a,b=map(seconds,line.split(' --> '))
  if a<0 or b<=a or a<prev-.015:timing.append({'clip':p.stem,'format':'VTT','start':a,'end':b,'previous_end':prev})
  prev=b
(P/'caption-fit-review.json').write_text(json.dumps({'max_line_width_with_one_bold_word':maxw,'available_width':870,'overflow':bad,'scope':'Every 55px caption line plus maximum highlighted-bold-word width increase'},indent=2));(P/'caption-timing-review.json').write_text(json.dumps({'word_highlight_events':count,'conflicts':timing,'status':'pass' if not timing else 'needs review'},indent=2));print('Caption validation:',len(bad),'overflow,',len(timing),'timing conflicts,',count,'word events')
if bad or timing:raise SystemExit(1)
