"""Index all matched example cues in the full recording, including material excluded from shorts."""
import json,re,pathlib
P=pathlib.Path(__file__).resolve().parents[1];src=json.loads((P/'source-audio/transcript-base.json').read_text());clips=json.loads((P/'recording-clips/manifest.json').read_text())['clips']
patterns={
 'medical-diagnosis analogy':r'\bx.ray\b|broken arm|break your arm',
 'raw temperature and unit context':r'\b45\b|forty.five|pharmaceutical|frozen food|Celsius|Fahrenheit|temperature scale',
 'shipment date ambiguity':r'order date|shipment date|shipping date|arrival date|expected arrival|six different',
 'inventory-risk competing definitions':r'inventory at risk|safety buffer|supply planner|warehouse manager',
 'ingredients versus recipe':r'ingredients|recipe|pantry',
 'institutional-knowledge dependency':r'analyst.*knows|walks.*door|retires|institutional knowledge',
 'store type and physical instance':r'\b402\b|downtown Seattle|store number|entity instance',
 'contracts across namespaces':r'HR.*contract|sales.*contract|contract.*HR|contract.*sales',
 'inheritance and derived types':r'frozen product|derived type|parent type|refrigerated location',
 'conflicting customer definitions':r'90.days|ninety.days|marketing customer|finance customer|outstanding invoice',
 'DAX source-measure change':r'CFO|net revenue|revenue calculation|profit margin|source math',
 'priority-store definitions':r'priority.*store|priority.*one|priority.*1|square footage',
 'entity synonyms':r'\bshops\b|\bshop\b|retail location|synonym',
 'natural language retail operations prompt':r'late deliver|next 24 hours|offline.*sensor|sensor.*offline|six hours',
 'source freshness and filtering':r'stale|refresh.*hour|yesterday.*data|same.*filter|reporting period',
 'version and rollback illustration':r'rollback|roll back|named version|version history',
 'regional identity/RLS':r'West region|western region|regional manager|god.mode|row.level security',
 'forecast decision and uncertainty':r'100,000|hundred.thousand|forecast|prediction|probabilistic',
 'supplier recall path':r'contaminat|recall|agricultural supplier|raw ingredients',
 'trigger/monitoring example':r'five.minute|five minutes|twenty.four hours|alert.*minute|Activator',
 'report-grounded draft verification':r'15.percent|15%|fifteen.percent|board.ready|PowerPoint|quarterly.*summary',
 'large-query billing illustration':r'ten.*billion|billions|massive.*query|compute consumption|free.*reasoning',
 'corporate-merger thought experiment':r'merger|M\s*&\s*A|two massive global|company A|company B',
 'explicit illustrative cue':r'for example|let.s say|imagine|hypothetical|suppose|think of it|analogy|concrete example|what if',
}
rows=[]
for i,s in enumerate(src['segments']):
 tags=[name for name,rx in patterns.items() if re.search(rx,s['text'],re.I)]
 if not tags:continue
 # Exact ASR segment, not a rewritten quote. Adjacent context retained separately.
 rows.append({'id':f'E{len(rows)+1:03}','source_start':s['start'],'source_end':s['end'],'tags':tags,'transcript_asr':s['text'],'context_before':src['segments'][i-1]['text'] if i else '', 'context_after':src['segments'][i+1]['text'] if i+1<len(src['segments']) else '', 'associated_clips':[c['id'] for c in clips if c['source_start']<s['end'] and c['source_end']>s['start']], 'evidence_kind':'speaker illustration/claim; not independently demonstrated product behavior','status':'automatic example-cue index; human classification pending'})
(P/'recording-clips/full-recording-example-cues.json').write_text(json.dumps({'scope':'Every segment matching the documented cue patterns across all five audio parts, including rejected or unselected material. Not a claim of semantic exhaustiveness.','patterns':patterns,'count':len(rows),'examples':rows},indent=2));print('Indexed',len(rows),'example-bearing source segments')
