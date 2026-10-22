from pathlib import Path
import json
R=Path(__file__).resolve().parent;P=json.loads((R/'plan.json').read_text());T=json.loads((R.parent/'research/fabric-youtube/HtR5m5VjaDQ/transcript.json').read_text())['transcript'];recipes={r['scene']:r for r in json.loads((R/'recipes.json').read_text())};old=json.loads((R.parent/'research/ontology-adaptation/template-library/catalog.json').read_text())['sequences'];events=[]
for s in P['scenes']:
 rec=recipes[s['id']];overlap=[o for o in old if max(o['start'],s['source_start'])<min(o['end'],s['source_end'])]
 for i,t in enumerate(s['event_anchors']):
  captions=[{'text':r['text'],'start':float(r['startMs'])/1000,'end':float(r['endMs'])/1000} for r in T if abs(float(r['startMs'])/1000-t)<4]
  events.append({'scene':s['id'],'source_time':t,'event_index':i,'nearby_captions':captions,'timing_status':'Estimated visual anchor with nearby rolling captions; this is not an exact spoken trigger or word alignment.','graphic_type':rec['template'],'relationship_to_teach':rec['relationship'],'motion_recipe':rec['motion'],'persistent_context':rec['persist'],'selection_reason':rec['why'],'alternative':rec['alternative'],'alternative_rejection':rec['reject'],'misuse_risk':rec['risk'],'observed_sequence_patterns':[{'source_id':o['id'],'pattern':o['observed_state_pattern'],'evidence_frames':o['evidence_frames']} for o in overlap],'review_state':'Rendered reference study; exact event matching requires source-clock review.'})
(R/'event-map.json').write_text(json.dumps({'source':P['source'],'duration':P['source_duration'],'events':events,'precision':'Approximate source-derived anchors, not exhaustive keyframes. These are candidates for learning a reusable teaching grammar, not a trained compiler.'},indent=2))
print(len(events),'visual anchors linked to nearby transcript and teaching recipes')
