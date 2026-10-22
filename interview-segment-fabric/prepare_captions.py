from pathlib import Path
import json,re
R=Path(__file__).parent;n=json.loads((R/'narration.json').read_text());cues=[]
def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
for s in n['segments']:
 tokens=s['text'].split();ws=s['words'];assert [norm(t) for t in tokens]==[norm(w['text']) for w in ws],(tokens,ws)
 group=[]
 for i,(token,w) in enumerate(zip(tokens,ws)):
  group.append(dict(text=token,start=s['start']+w['offset']/1e7,end=s['start']+(w['offset']+w['duration'])/1e7))
  if len(group)>=6 or token.endswith(('.',',','?','!')) or i==len(tokens)-1:
   cues.append(dict(start=group[0]['start'],end=group[-1]['end']+.2,text=' '.join(w['text'] for w in group),words=group,role=s['role']));group=[]
for i in range(len(cues)-1):cues[i]['end']=min(cues[i]['end'],cues[i+1]['start'])
(R/'captions.json').write_text(json.dumps(cues,indent=2))
def tc(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02}.{ms%1000:03}'
(R/'captions.vtt').write_text('WEBVTT\n\n'+'\n\n'.join(f'{tc(c["start"])} --> {tc(c["end"])}\n{c["text"]}' for c in cues)+'\n')
print(len(cues),'phrases')
