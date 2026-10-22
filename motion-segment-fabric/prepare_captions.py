from pathlib import Path
import json,re
R=Path(__file__).parent
n=json.loads((R/'narration.json').read_text())
phrases=[
['Which refrigeration units','does a store operate?'],
['Model Store and Refrigeration Unit','as entity types:','reusable definitions of business concepts.'],
['Region and priority are properties','that describe a store.'],
['Name the relationship operates.',"In Microsoft’s example,","the store’s Location ID","matches the unit’s Store ID."],
['Data bindings map the definitions','to their source tables','in a lakehouse.'],
['A consuming application uses these mappings','to query the sources.','The ontology defines the connection;','source records stay','in their owning systems.']]
def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
cues=[]
for s,ps in zip(n['segments'],phrases):
 pos=0
 for p in ps:
  tokens=p.split();ws=s['words'][pos:pos+len(tokens)]
  assert [norm(w['text']) for w in ws]==[norm(w) for w in tokens],(p,ws)
  events=[dict(text=token,start=s['start']+w['offset']/1e7,end=s['start']+(w['offset']+w['duration'])/1e7) for token,w in zip(tokens,ws)]
  cues.append(dict(start=events[0]['start'],end=events[-1]['end']+.22,text=p,words=events));pos+=len(tokens)
 assert pos==len(s['words'])
for i in range(len(cues)-1):cues[i]['end']=min(cues[i]['end'],cues[i+1]['start'])
(R/'captions.json').write_text(json.dumps(cues,indent=2))
def tc(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02}.{ms%1000:03}'
(R/'captions.vtt').write_text('WEBVTT\n\n'+'\n\n'.join(f'{tc(c["start"])} --> {tc(c["end"])}\n{c["text"]}' for c in cues)+'\n')
print(len(cues),'caption phrases;',sum(len(c['words']) for c in cues),'aligned words')
