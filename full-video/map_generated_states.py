from pathlib import Path
import json,sys,inspect
import graphics as g
R=Path(__file__).resolve().parent;P=json.loads((R/'plan.json').read_text());E=json.loads((R/'event-map.json').read_text())['events'];SC={s['id']:s for s in P['scenes']};orig=g.C.text;signature=inspect.signature(orig);objects=[]
def capture(*args,**kw):
 b=signature.bind(*args,**kw);b.apply_defaults();o=b.arguments
 if o['a']>=.5:objects.append({'text':o['text'],'x':o['x'],'y':o['y'],'size':o['size'],'alpha':o['a'],'bold':o['bold'],'color':o['color']})
 return orig(*args,**kw)
g.C.text=capture;rows=[];previous={};previous_objects={}
for e in E:
 s=SC[e['scene']]
 if s['kind'] not in ['native','hybrid','demo-overlay','chapter']:continue
 future=[v for v in s['event_anchors'] if v>e['source_time']];t=min(e['source_time']+1,(future[0] if future else s['source_end'])-1/30);objects.clear();g.native(s,t);now={o['text'] for o in objects};past=previous.get(s['id'],set());old=previous_objects.get(s['id'],{});changes=[{'text':o['text'],'old_alpha':old[o['text']]['alpha'],'new_alpha':o['alpha']} for o in objects if o['text'] in old and abs(o['alpha']-old[o['text']]['alpha'])>.1];rows.append({'scene':s['id'],'anchor_time':e['source_time'],'sample_time':t,'added_text':sorted(now-past),'removed_text':sorted(past-now),'persistent_text':sorted(now&past),'emphasis_changes':changes,'text_objects':objects.copy(),'classification':'Captured from the reconstruction display-list, not OCR or annotation of the original source. Compare with the original in the event atlas.'});previous[s['id']]=now;previous_objects[s['id']]={o['text']:o for o in objects}
(R/'reconstruction-state-map.json').write_text(json.dumps(rows,indent=2));print(len(rows),'reconstructed states with added, removed and persistent text')
