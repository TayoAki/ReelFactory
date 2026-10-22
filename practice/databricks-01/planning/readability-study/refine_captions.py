from pathlib import Path
import json,html,shutil
from PIL import ImageFont
R=Path(__file__).resolve().parent;G=R.parent/'generated';p=G/'index.html';s=p.read_text();A=1120/30
shutil.copy('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',G/'assets/caption-bold.ttf')
phrases=[(37.333333,'SO I COME FROM'),(38.333333,'THE GENIE ONE WORLD'),(39.666667,'GENIE ONE IS OUR'),(41.,'AI CO-WORKER FOR BUSINESS USERS'),(43.2,'IT CONNECTS TO'),(44.2,'YOUR DATA AND TOOLS'),(45.6,'IT ANSWERS QUESTIONS ABOUT'),(47.2,'YOUR BUSINESS'),(48.05,'IT ACTS ON THE'),(49.05,'ANSWERS THAT IT GIVES YOU'),(50.2,'ALL WITHIN THE GOVERNANCE'),(51.5,'FRAMEWORK THAT YOU ALREADY HAVE'),(53.35,'BUT GENIE ONE SITS'),(54.65,'IN A LARGER STACK OF'),(57.,'AI CO-WORKERS AND'),(58.35,'OTHER AI TOOLS ON DATABRICKS'),(60.6,'SO FOR EXAMPLE IF'),(61.7,'GENIE ONE IS OUR'),(62.85,'AGENT FOR BUSINESS USERS'),(64.6,'GENIE CODE IS OUR'),(66.,'AGENT FOR TECHNICAL USERS'),(67.65,'IT HELPS THEM WRITE'),(68.7,'CODE AND DO'),(69.85,'OTHER WORK WITHIN THE LAKEHOUSE'),(71.7,'WE ALSO HAVE GENIE AGENTS'),(73.5,'WHICH CAN BE ACCESSED'),(74.7,'BY BOTH TYPES OF USERS'),(76.2,"AND THEY'RE REALLY FOCUSED"),(77.35,'ON DOMAIN-SPECIFIC WORK'),(79.3,"THEY'RE ESSENTIALLY DOMAIN EXPERTS"),(81.05,'AND I CAN ACTUALLY'),(81.7,'COVER THAT IN MORE'),(82.55,'DEPTH IF WE WANT TO')]
measure=json.loads((R/'source-caption-measurements.json').read_text());font=ImageFont.truetype(str(G/'assets/caption-bold.ttf'),14);blocks=[];events=[];report=[]
# Remove old accumulating/ASR-based caption spans and their timeline sets.
s='\n'.join(line for line in s.splitlines() if not (line.lstrip().startswith('<div id="c') and '<div class="ev1-cap"' in line) and 'tl.set("#cap-' not in line)
for i,(a,text) in enumerate(phrases):
 b=phrases[i+1][0] if i+1<len(phrases) else 83.7;words=text.split();wid=[font.getlength(w) for w in words];gap=font.getlength(' ');left=320-(sum(wid)+gap*(len(words)-1))/2;centers=[]
 for w in wid:centers.append(left+w/2);left+=w+gap
 spans=''.join(f'<span id="readable-{i}-{j}" class="w">{html.escape(w)}</span>' for j,w in enumerate(words));blocks.append(f'<div class="clip readable-caption" data-start="{max(0,a-A):.6f}" data-duration="{b-a:.6f}" style="position:absolute;inset:0;width:1920px;height:1080px;z-index:60"><div class="ev1-cap">{spans}</div></div>')
 samples=[q for q in measure if a<=q['source_time']<b and q['orange_bounds']];last=-1;anchors=[]
 if a<39.4 or a>=81.53:samples=[]
 if samples:
  for q in samples:
   box=q['orange_bounds'];cx=(box[0]+box[2])/6+5;j=min(range(len(words)),key=lambda j:abs(centers[j]-cx));j=max(last,j)
   if j!=last:anchors.append((q['source_time'],j));last=j
 else:anchors=[(a+(b-a)*j/len(words),j) for j in range(len(words))]
 # Start with the first word; move emphasis using orange rectangle locations where available.
 if not anchors or anchors[0][0]>a+.05:anchors.insert(0,(a,0))
 prev=None
 for t,j in anchors:
  if prev is not None:events.append(f'tl.set("#readable-{i}-{prev}",{{backgroundColor:"transparent"}},{max(0,t-A):.6f});')
  events.append(f'tl.set("#readable-{i}-{j}",{{backgroundColor:"#b96500"}},{max(0,t-A):.6f});');prev=j
 report.append({'source_start':a,'source_end':b,'text':text,'highlight_source':'Source orange-background positions sampled at 6fps; monotonic word mapping' if samples else 'Even word stepping within source phrase; source color obscured by presenter background','highlight_events':anchors})
needle='\n<script>\n';assert needle in s;s=s.replace(needle,'\n'+''.join(blocks)+'\n<script>\n',1)
css='''@font-face{font-family:CaptionBold;src:url(assets/caption-bold.ttf);font-weight:700}:root{--ev1-cap-size:42px}.ev1-cap{top:1002px;font-family:CaptionBold,Arial,sans-serif;font-size:45px;font-weight:700;line-height:1.1;gap:5px;letter-spacing:-.8px}.ev1-cap .w{font-family:CaptionBold,Arial,sans-serif;font-weight:700;-webkit-text-stroke:.8px white;paint-order:normal;text-shadow:-3px -3px 0 #514b45,3px -3px 0 #514b45,-3px 3px 0 #514b45,3px 3px 0 #514b45,-4px 0 0 #514b45,4px 0 0 #514b45,0 -4px 0 #514b45,0 4px 0 #514b45,0 2px 5px #0008;padding:0 2px}.readable-caption .w{opacity:1!important}'''
s=s.replace('</style>',css+'\n</style>');s=s.replace('window.__timelines=window.__timelines||{};','\n'.join(events)+'\nwindow.__timelines=window.__timelines||{};');p.write_text(s)
(R/'caption-plan.json').write_text(json.dumps({'method':'Source phrase boundaries interpreted from 6fps OCR and frames; wording normalized to transcript; emphasis approximated from measured orange-background positions, not certified word alignment','phrases':report},indent=2));print('Rebuilt',len(report),'source-derived caption phrases with a real bold font')
