from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];D=json.loads((R/'source-audio/transcript-base.json').read_text());words=[w for s in D['segments'] for w in s['words']]
# Approximate locations come from reading the full first pass; actual edit points snap to second-pass sentence/word boundaries.
rows=[
('Your data stack still needs business meaning',95,139,'contrast','Tables and dashboards','A dependable business answer','Context links the facts','raw-data gap'),
('The same temperature can mean different things',184,240,'contrast','Outside air','Refrigeration unit','45°F','illustrative temperature context'),
('Which shipment date means arrival',248,296,'contrast','Order date','Expected arrival','Several dates, different meanings','shipment-date example'),
('Inventory at risk has two definitions',326,378,'contrast','Below threshold now','Shortage before delivery','Inventory at risk','warehouse versus planning example'),
('Data without meaning is ingredients without a recipe',375,406,'contrast','Ingredients','Recipe','Data needs business context','speaker analogy'),
('When the analyst is the only recipe',407,444,'ownership','Business question','Human translation','Institutional knowledge','analyst knowledge example'),
('Fabric brings the workflow together',483,534,'workflow','Ingest and prepare','Analyze and report','Shared platform, different workloads','platform overview'),
('OneLake shared data different engines',548,583,'ownership','Shared governed data','Different compute engines','OneLake','shared data foundation'),
('Shortcuts reference data elsewhere',583,624,'ownership','Source data','Supported shortcut','Reference rather than duplicate','supported shortcut example'),
('Ontology supplies meaning over data',629,684,'ownership','Source records','Business concepts','Ontology definitions','context layer, not transactional storage'),
('Entity type versus instance',739,779,'entities','Store','Example store 402','Type → instance','illustrative Seattle store'),
('Properties describe relationships connect',779,813,'entities','Store','Refrigeration Unit','operates','properties and relationship example'),
('Bindings connect concepts to source fields',814,841,'ownership','Business property','Source field','Data binding','illustrative column mapping'),
('Namespaces prevent semantic collisions',842,878,'contrast','HR contract','Sales contract','Same word, different scopes','contract namespace example'),
('Inheritance reuses a base structure',881,929,'hierarchy','Location','Store','inherits structure','Location/Store and Product/Frozen Product examples'),
('A derived type needs its own binding',931,957,'boundary','Inherited structure','Own source binding','Preview constraint','derived-type binding limit'),
('Relationships are not automatically inherited',959,987,'hierarchy','Product → Supplier','Frozen Product','Define ordinary relationships explicitly','preview inheritance caveat'),
('Query the derived type explicitly',989,1047,'hierarchy','Product','Frozen Product','Name relevant types','hypothetical omitted frozen-products analysis'),
('Reuse the Power BI model you already built',1074,1138,'ownership','Power BI semantic model','Ontology definitions','Reuse and review','semantic-model generation'),
('Customer definitions still need a human decision',1144,1218,'contrast','Marketing customer','Finance customer','Governance resolves meaning','hypothetical customer-definition collision'),
('The source model owns the DAX',1283,1312,'ownership','Power BI semantic model','Ontology metric','references source DAX','DAX ownership example'),
('Source permissions still matter',1314,1342,'boundary','Ontology access','Source Read + Build','Both are required','semantic-model access'),
('The schema cannot explain priority',1359,1435,'contrast','Priority = 1','Approved business definition','Meaning is not just a data type','illustrative priority classification'),
('Temperature units change the interpretation',1434,1481,'contrast','10°C','10°F','10°C = 50°F','illustrative unit mismatch'),
('Synonyms connect business vocabulary',1488,1510,'entities','Retail location','Shops','Entity synonyms','retail-location/shop naming example'),
('AI proposes a model humans review it',1509,1534,'workflow','Inspect supported sources','Review the proposal','Draft is not approval','ontology-agent drafting'),
('Business rules need explicit links',1539,1589,'boundary','Inventory-risk definition','Store + Inventory','Rule context','descriptive rule links'),
('Describing the rule is not executing it',1610,1634,'boundary','Definition and context','Consuming query engine','Separate responsibilities','rule versus execution boundary'),
('Different sources serve different workloads',1648,1707,'workflow','Lakehouse records','Eventhouse telemetry','Semantic-model measures','documented source routes'),
('Definitions route the question to sources',1708,1754,'ownership','Definitions + mappings','Native source engine','Query the appropriate source','source execution explanation'),
('Freshness depends on the execution path',1813,1887,'evidence','Streaming observations','Imported report refresh','Check source timestamps','illustrative mixed-freshness example'),
('Review before switching to Act',1932,2009,'workflow','Plan and inspect','Act deliberately','Review gate','proposal-first authoring'),
('A restore replaces the whole definition',2036,2094,'workflow','Save named version','Restore definition','Preserve current version first','hypothetical version rollback'),
('One retail prompt crosses several concepts',2141,2179,'entities','Priority stores','Inventory and deliveries','Example operations question','recorded prompt excerpt, not executed demo'),
('Check the answer and expose missing data',2308,2368,'evidence','Approved definition','Source evidence','Make gaps visible','hypothetical offline freezer sensor'),
('Ask for the query and compare filters',2369,2420,'evidence','Source measure + query','Same report filters','Check the calculation','source-report verification'),
('A chat table is not a complete export',2420,2441,'evidence','Displayed rows','All matching records','Bounded results','returned-table boundary'),
('The agent uses the signed-in identity',2448,2478,'boundary','Signed-in user','Allowed source data','Existing permissions apply','interactive-agent identity'),
('Test with the real end-user role',2478,2540,'boundary','Author account','Regional manager','Source access determines results','hypothetical configured West-region RLS'),
('Forecasting needs a separate modeling workflow',2548,2598,'workflow','Target and horizon','Inputs and method','Evaluate a dedicated model','forecast workflow; omit later Dataverse claim'),
('A forecast is not a deterministic fact',2618,2657,'evidence','Historical evaluation','Uncertainty','Show the basis for trust','forecast-evaluation example'),
('When the relationship path is the question',2690,2737,'graph','Supplier → Products','Shipments → Stores','Illustrative recall path','hypothetical supplier exposure; no SQL-failure claim'),
('Graph projection has eligibility limits',2775,2835,'graph','Eligible operational data','Defined entity keys','Preview projection scope','source eligibility and semantic-model exclusion'),
('The concept map is not the instance graph',2849,2895,'graph','Business definitions','Optional materialized graph','Different jobs and refresh needs','schema versus execution layer'),
('Data agent versus operations agent',2923,2952,'contrast','Conversational analytics','Monitor and recommend','Different agent roles','omit unsupported combined-condition example'),
('MCP integration needs supported authentication',3038,3098,'boundary','Compatible client','Ontology endpoint','Check current authentication limits','preview service-principal known issue'),
('Keep monitoring conditions simple',3105,3154,'boundary','One configured condition','Monitoring cycle','Preview limitations','no guaranteed notification latency'),
('A written rule does not create an Activator flow',3158,3201,'boundary','Natural-language rule','Configured Activator workflow','Separate configuration','rule versus automation'),
('Cowork grounds on the Power BI report',3209,3255,'ownership','Power BI report','Cowork draft','Report route, not ontology item','current documented grounding boundary'),
('Verify report numbers before sharing the draft',3255,3304,'evidence','Draft statement','Source report values','Verify before sharing','illustrative revenue percentage, not measured outcome'),
('Chat history is not durable business knowledge',3305,3353,'boundary','Browser conversation','Saved ontology definitions','Persist the durable meaning','session-lifetime limits'),
('Import support does not promise lossless OWL',3357,3407,'workflow','Supported definitions','Review import summary','Preserved · adjusted · skipped','interoperability limits'),
('Plan the old-experience migration',3410,3441,'workflow','Old experience','Separate new item','Reconnect and review consumers','date-sensitive retirement guidance'),
('Measure the whole reviewed workflow',3464,3523,'evidence','Known-good answer','Human review + correction','Use your own baseline','evaluation design, no borrowed percentage'),
('Nonbillable reasoning is not a free workflow',3524,3603,'boundary','Reasoning status','Compute and storage','Measure total consumption','preview billing and hypothetical large query'),
('Start with one team and one decision',3610,3654,'workflow','One recurring decision','Test then expand','Start small','pilot rollout advice'),
('A merger is also a collision of definitions',3683,3739,'contrast','Company A meaning','Company B meaning','Thought experiment','speculative merger discussion, not product capability')
]
# Sentence starts/ends retain actual source continuity; never create words or a new voice.
starts=[i for i in range(len(words)) if i==0 or re.search(r'[.!?][\"”\']?$',words[i-1]['word'])]
ends=[i for i,w in enumerate(words) if re.search(r'[.!?][\"”\']?$',w['word'])]
def nearest(candidates,t,key,window=6):
 near=[i for i in candidates if abs(words[i][key]-t)<=window]
 return min(near or candidates,key=lambda i:abs(words[i][key]-t))
clips=[]
for num,(title,a,b,fam,left,right,focus,kind) in enumerate(rows,1):
 ia=nearest(starts,a,'start');ib=nearest(ends,b,'end');ws=words[ia:ib+1]
 if not ws:raise ValueError(title)
 start=max(0,ws[0]['start']-.1);end=ws[-1]['end']+.12
 if ib+1<len(words):end=min(end,max(ws[-1]['end']+.015,words[ib+1]['start']-.025))
 text=' '.join(w['word'] for w in ws)
 clip={'id':f'C{num:02}','title':title,'source_start':start,'source_end':end,'duration':end-start,'part_ranges':[],'family':fam,'left_label':left,'right_label':right,'focus_label':focus,'example_kind':kind,'words':[{**w,'start':w['start']-start,'end':w['end']-start} for w in ws],'transcript_asr':text,'source_kind':'actual uploaded recording; continuous audio excerpt','transcript_status':'second-pass ASR; orthography and technical terms reviewed during clip QA','status':'planned','publish_status':'draft for review','narration_replaced':False,'actual_timestamps':True,'context_label':'Preview context · Oct 2026' if any(k in kind for k in ['preview','current documented','date-sensitive','session-lifetime','billing']) else 'Illustrative scenario' if any(k in kind for k in ['hypothetical','illustrative','example','analogy']) else 'Original discussion excerpt','review_flags':[]}
 if 'speculative' in kind:clip['context_label']='Thought experiment';clip['review_flags'].append('Speculative discussion, not verified product behavior.')
 if title.startswith('Graph projection'):clip['review_flags'].append('Retain eligibility, keys and semantic-model exclusions; do not suggest universal Graph support.')
 if title.startswith('The same temperature') or title.startswith('Temperature units'):clip['review_flags'].append('Illustrative context/units example, not a food or pharmaceutical safety threshold.')
 if '80%' in text or '20%' in text:clip['review_flags'].append('Unsubstantiated percentage in source; hold before export.')
 if any(s in text.lower() for s in ['time out and crash','terrible at deep','dataverse']):clip['review_flags'].append('Potential unsupported architectural claim; hold before export.')
 if any('hold before export' in x for x in clip['review_flags']):clip['status']='hold_for_boundary_revision'
 for part in json.loads((R/'source-audio/manifest.json').read_text())['parts']:
  p0=part['offset'];p1=p0+part['duration']
  if end>p0 and start<p1:clip['part_ranges'].append({'part':part['name'],'start':max(start,p0)-p0,'end':min(end,p1)-p0})
 clips.append(clip)
P=R/'recording-clips';P.mkdir(exist_ok=True);(P/'manifest.json').write_text(json.dumps({'source':'five actual audio parts; full first and second ASR passes completed','duration':D['duration'],'clips':clips},indent=2))
(P/'selection-review.txt').write_text('\n\n'.join(f'{c["id"]} {c["source_start"]:.2f}–{c["source_end"]:.2f} ({c["duration"]:.1f}s) {c["title"]}\n{c["status"]}: {c["review_flags"]}\n{c["transcript_asr"]}' for c in clips))
print('Selected',len(clips),'continuous excerpts; holds',[(c['id'],c['title']) for c in clips if c['status'].startswith('hold')])
