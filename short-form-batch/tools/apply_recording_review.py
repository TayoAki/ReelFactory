"""Documented boundary and orthography fixes after contextual ASR; never alter recorded words."""
import pathlib,json
P=pathlib.Path(__file__).resolve().parents[1];Q=P/'recording-clips';d=json.loads((Q/'manifest.json').read_text());parts=json.loads((P/'source-audio/manifest.json').read_text())['parts'];review=[]
# Absolute values make repeated application idempotent.
starts={'C09':602.600975,'C10':634.58,'C12':780.180975,'C14':841.100975,'C27':1550.12195,'C31':1819.22195,'C33':2045.06195}
# C09's precise existing range is retained unless an additional 60ms context is required.
starts.pop('C09')
for c in d['clips']:
 old=c['source_start'];new=starts.get(c['id'],old);delta=new-old
 if abs(delta)>.001:
  c['source_start']=new;c['duration']=c['source_end']-new;c['words']=[{**w,'start':w['start']-delta,'end':w['end']-delta} for w in c['words'] if (w['start']+w['end'])/2>=delta]
  c['boundary_note']='Post-context ASR review: remove preceding sentence tail, or retain the full opening syllable.'
  review.append({'id':c['id'],'previous_start':old,'new_start':new,'change':'source boundary only; continuous original audio'})
 for w in c['words']:
  if c['id']=='C31' and w['word'].lower().strip('.,')=='nipples':
   prev=w['word'];w['word']=prev.replace('nipples','apples');c.setdefault('caption_corrections',[]).append({'from':prev,'to':w['word'],'reason':'apples-versus-oranges phrase confirmed by independent tiny.en full-recording pass at 1824.38s; contextual base.en misrecognition'});review.append({'id':'C31','caption_from':prev,'caption_to':w['word'],'evidence':'source-audio/transcript-first-pass.txt at 1824.38s'})
 c['transcript_asr']=' '.join(w['word'] for w in c['words']);c['part_ranges']=[]
 for p in parts:
  start=p['offset'];end=start+p['duration']
  if c['source_end']>start and c['source_start']<end:c['part_ranges'].append({'part':p['name'],'start':max(c['source_start'],start)-start,'end':min(c['source_end'],end)-start})
 if c['id'] in ['C16','C47']:c['context_label']='Preview context · Oct 2026'
 if c['id']=='C34':c['context_label']='Recorded question · illustrative retail scenario'
 (Q/'captions'/f'{c["id"]}-words.json').write_text(json.dumps(c,indent=2))
 (Q/'storyboards'/c['id']/'storyboard.json').parent.mkdir(exist_ok=True)
 sp=Q/'storyboards'/c['id']/'storyboard.json'
 if sp.exists():
  s=json.loads(sp.read_text());s['source_quote']=c['transcript_asr'];s['source_start']=c['source_start'];s['source_end']=c['source_end'];s['exact_quote_status']=c['transcript_status'];s['source_observation_vs_adaptation']='Original screenshot used for style. These relationship diagrams are editorial adaptations, not measured reconstructions of the source motion.';sp.write_text(json.dumps(s,indent=2))
(Q/'manifest.json').write_text(json.dumps(d,indent=2));(Q/'manual-caption-boundary-review.json').write_text(json.dumps(review,indent=2))
(Q/'selection-review.txt').write_text('\n\n'.join(f'{c["id"]} {c["source_start"]:.2f}–{c["source_end"]:.2f} ({c["duration"]:.1f}s) {c["title"]}\n{c["transcript_asr"]}\nReview: {c["review_flags"]}' for c in d['clips']))
print('Applied',len(review),'documented review adjustments')
