from pathlib import Path
import subprocess,json
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent;parts=json.loads((ROOT.parent/'uploaded-parts.json').read_text());offsets=[];total=0
for p in parts:offsets.append(total);total+=p['duration']
sequences=[
('01-icon-map',8,15),('02-white-system',38,54),('03-layered-cards',55,81),('04-context-problem',110,137),('05-query-ambiguity',139,159),('06-source-context',174,208),('07-system-to-focus',209.5,249),('08-modeled-build',249,333),('09-learned-context',334,397),('10-overview-rank',399,450),('11-chart-focus',455,510),('12-connectors',551,675),('13-memory-ui',680,711),('14-demo-context',777,866),('15-demo-inspection',866,990),('16-citations',990,1094),('17-followups',1094,1219),('18-chapter-docs',1248.5,1305),('19-governed-actions',1305,1388),('20-governance-cards',1423,1462),('21-agent-hierarchy',1465,1521),('22-scheduling-surfaces',1523,1611),('23-demo-actions',1614,1682),('24-agent-inspection',1682,1786),('25-getting-started',1795,1850),('26-rollout-build',1850,1956),('27-best-practices',1958,2043)]
# Endpoints plus six intermediate states: exact timestamps are retained, not guessed transitions.
manifest=[]
for name,a,z in sequences:
 times=[round(a+(z-a)*j/7,3) for j in range(8)];folder=ROOT/name;folder.mkdir(exist_ok=True);sheet=Image.new('RGB',(1280,404),'#111820');d=ImageDraw.Draw(sheet)
 for j,t in enumerate(times):
  k=max(i for i,v in enumerate(offsets) if v<=t);local=t-offsets[k];path=folder/f'{j:02}.png'
  if not path.exists():subprocess.run(['ffmpeg','-v','error','-y','-ss',str(local),'-i',parts[k]['path'],'-frames:v','1',str(path)],check=True)
  x=j%4*320;y=j//4*202;sheet.paste(Image.open(path).resize((320,180)),(x,y));d.text((x+4,y+182),f'{int(t)//60:02}:{t%60:06.3f}  ({t:.3f}s)',fill='white')
 sheet.save(ROOT/(name+'.jpg'),quality=94);manifest.append(dict(id=name,start=a,end=z,samples=times,sheet=name+'.jpg'))
(ROOT/'sequences.json').write_text(json.dumps(manifest,indent=2));print('27 sequences / 216 source frames created')
