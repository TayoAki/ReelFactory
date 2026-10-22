from pathlib import Path
import re,json,csv,html,ast
R=Path(__file__).resolve().parent;repo=R.parent
script=repo/'motion-pilot-fabric/input-transcript.txt';lines=script.read_text().splitlines()
configs=[
('What Microsoft Fabric brings together',8,9,'tutorial','Workflow overview','Shared platform with labelled workload roles; avoid implying one execution engine.'),
('What OneLake actually shares',9,9,'tip_hack','Shared foundation','OneLake foundation plus distinct access paths; supported shortcuts labelled.'),
('Where Fabric IQ fits',10,11,'comparison','Business context layer','Data below, definitions/context above, consuming experiences separate.'),
('Why tables alone miss business meaning',17,18,'myth_bust','Context gap','Question card with temperature/sales/shipment sources; reveal the missing relationships.'),
('Define inventory risk before asking AI',19,20,'do_dont','Definition repair','Keep same question; compare below-threshold versus projected shortage before replenishment.'),
('A fluent answer still needs checking',21,22,'tip_hack','Evidence inspection','Answer → interpretation → calculation → evidence; no unverified success check.'),
('The building blocks of an ontology',26,29,'tutorial','Entity definition','Use our interview image-first build: type, instance, properties, relationship, binding, rules/metrics.'),
('Inheritance has limits',30,32,'do_dont','Hierarchy with caveats','Location/Store and Product/Frozen Product hierarchy; separate source binding and relationship caveats.'),
('Reuse the Power BI model you already built',36,38,'tutorial','Semantic reuse','Semantic model → generated definition; show review step, not automatic correctness.'),
('Who owns the DAX calculation',39,41,'comparison','Ownership','Source-owned DAX measure linked to ontology metric; keep Read/Build/write caveats.'),
('Add metadata that changes the answer',45,48,'tip_hack','Ambiguity repair','Temperature units, product identifiers and approved definitions; metadata is not an access policy.'),
('Writing a rule does not run automation',49,51,'myth_bust','Definition versus execution','Natural-language rule card and separately configured execution path; no completed action.'),
('Where ontology bindings can point',55,57,'tutorial','Source mapping','Lakehouse/Eventhouse/semantic model source routes; no invented universal database.'),
('The query path determines freshness',58,60,'comparison','Execution routes','SQL/KQL/DAX/optional graph routes with different refresh indicators, not a live-data guarantee.'),
('Plan mode before Act mode',64,68,'do_dont','Review gate','Draft → inspect/validate → deliberate Act; real UI required for actual demo claim.'),
('Save a version before changing definitions',69,70,'tip_hack','Version boundary','Named version before change; restore replaces whole definition.'),
('One retail question crosses several sources',74,79,'tutorial','Worked operational question','Store, inventory, products, refrigeration, deliveries; no fabricated matching stores or values.'),
('How to judge an agent answer',80,81,'tip_hack','Verification checklist','Definitions → intended source → checkable output; graphic supports a practical review.'),
('Check calculations against the source report',85,88,'tutorial','Provenance inspection','Query/filter/source measure → same-filter Power BI report; returned table is bounded.'),
('Whose identity does the interactive agent use',89,91,'do_dont','Access boundary','Signed-in user → allowed sources; ontology sharing and source permissions separate.'),
('A temperature exception is not proof of cause',95,98,'myth_bust','Correlation versus causation','Co-occurring observations → investigation lead → additional records needed.'),
('Forecasting needs its own analytical workflow',99,101,'tutorial','Forecast boundary','Target/horizon/inputs/method/validation; prepared evaluated model rather than prediction magic.'),
('When a materialized graph helps',105,108,'comparison','Relationship traversal','Supplier → products → shipments → stores; eligibility boundary and refresh scope.'),
('A concept diagram is not an instance graph',109,110,'myth_bust','Schema versus execution','Definitions and materialized instance data side by side; retain execution-path caveat.'),
('Choose the right agent experience',114,116,'comparison','Role comparison','Ontology agent/data agent/operations agent roles; include semantic-model-binding known issue.'),
('Check MCP authentication limits first',117,118,'do_dont','Integration constraint','Compatible client → endpoint → auth → supported interaction; flag documented service-principal issue.'),
('Start monitoring with one test condition',122,124,'tutorial','Monitoring boundary','Separate operational ontology, temperature condition, cycle and aggregation limits.'),
('Approving an action does not change its identity',125,127,'myth_bust','Execution identity','Recommendation → review → action; creator delegated identity remains the execution identity.'),
('Where Activator belongs',128,129,'comparison','Separate execution path','Ontology rule description versus separately configured/tested Activator workflow.'),
('Cowork uses the report route',133,136,'do_dont','Grounding boundary','Power BI report/model → Cowork draft; not direct ontology grounding; verify values/citations limitation.'),
('A chat session is not your knowledge repository',140,142,'tip_hack','Durable knowledge','Session lifecycle versus durable definitions/version ownership; exact current limits retained.'),
('Ontology import is not lossless OWL support',143,144,'do_dont','Interoperability constraint','Supported input formats → import summary → preserved/adjusted/skipped elements.'),
('Plan the old-experience migration',145,145,'tip_hack','Migration','Old item → separate new item → reconnect consumers; date-sensitive claim requires current check.'),
('Evaluate the complete question-to-answer workflow',149,151,'tutorial','Evaluation loop','Known-good answers, interpretation/calculation/access and human correction time.'),
('Measure the complete cost',152,152,'tip_hack','Cost scope','Capacity, storage and consuming operations; billing categories/status date-sensitive, no invented prices.'),
('Use your own baseline',153,154,'do_dont','Evidence over borrowed benchmarks','Team baseline → actual evaluation → expand/improve/pause; no borrowed percentage.'),
('Start with one team and one decision',158,160,'tutorial','Focused rollout','Decision owner + analyst + operator; required workspace/capacity/admin settings.'),
('Test ambiguity and missing data before expanding',161,162,'do_dont','Pilot acceptance','Normal/ambiguous/missing-data/access test cases before scale.'),
('The business question should guide the model',163,164,'tip_hack','Takeaway','Recurring decision → explicit meaning and sources → evaluated response.')]
section='';sections={}
for i,l in enumerate(lines,1):
 if re.match(r'^\d+ [A-Za-z]',l):section=l
 sections[i]=section
records=[]
for i,(title,a,b,angle,pattern,graphic) in enumerate(configs,1):
 block=[];demo=[];current=None
 for number in range(a,b+1):
  line=lines[number-1]
  if line.startswith(('On screen:','Sources:','Source:')):continue
  if line.startswith('Demo prompt:'):demo.append({'line':number,'text':line});continue
  if not line.strip():continue
  if line.startswith('Josh:'):current='host'
  elif line.startswith('Guest:'):current='guest'
  else:
   # Infer the continuing speaker from preceding dialogue in the same source section.
   for prev in reversed(lines[:number-1]):
    if prev.startswith('Josh:'):current='host';break
    if prev.startswith('Guest:'):current='guest';break
  block.append({'source_line':number,'role':current,'verbatim':line,'spoken_text':re.sub(r'^(Josh|Guest): ','',line)})
 text=' '.join(x['spoken_text'] for x in block);wc=len(text.split());cid=f'V{i:02}'
 record={'id':cid,'title':title,'source_kind':'earlier supplied interview script, NOT newly uploaded recording','source_section':sections[a],'source_lines':[a,b],'recording_start':None,'recording_end':None,'status':'script_draft_awaiting_recording','bucket':'experiment','angle':angle,'delivery':'educational','content_type':'educational','format':'qa','cta_type':'none','graphic_pattern':pattern,'graphic_reason':graphic,'verbatim_passages':block,'production_prompts_not_assumed_spoken':demo,'word_count':wc,'estimated_duration_seconds':[round(wc/160*60),round(wc/130*60)],'estimate_basis':'130–160 spoken words per minute; NOT measured audio timing','written_hook':' '.join(title.split()[:7]),'verbal_hook':block[0]['spoken_text'] if block else None,'visual_hook':graphic,'outlier_validation':'not researched; do not label proven or invent views/followers','technical_review':'source-script claims; verify current official docs before final production','publish_status':'draft only'}
 if i==2:record['variant_of']='V01';record['variant_reason']='Focused OneLake cut of the platform overview; overlapping source passage, not a new unique moment.'
 if wc>160:record['length_note']='May exceed a minute; retain coherent meaning rather than speeding up or cutting caveats.'
 records.append(record)
 out=f'# {cid}: {title}\n\n**SCRIPT DRAFT — not extracted from the new recording. Audio and timestamps pending.**\n\n'
 out+=f'Source: [{sections[a]}, lines {a}–{b}](../../motion-pilot-fabric/input-transcript.txt#L{a}). Estimated {record["estimated_duration_seconds"][0]}–{record["estimated_duration_seconds"][1]} seconds; actual duration unknown.\n\n'
 out+=f'## Hook stack\n\n- Verbal: use the exact recorded opening if it matches the script below; verify against audio.\n- Written (editorial title, not added speech): {record["written_hook"]}\n- Visual: {graphic}\n\n## Verbatim source passages\n\n'
 out+='\n\n'.join('> '+x['verbatim'] for x in block)
 out+=f'\n\n## Graphic plan\n\n{pattern}. {graphic}\n\nUse Fabric mint/teal; generate master and coherent build-state images, reconstruct editable layers, then align events to verified recorded words. For 9:16, use a speaker zone above a full-width diagram; never crop the whole 16:9 composition. Burn captions in a dedicated safe band.\n\n## Checks before rendering\n\nMatch this draft to the recording, review word-level transcript, retain context/caveats, select authentic source assets, inspect storyboard images and bounds. No invented audio timings, executed results, creator performance or CTA.\n'
 if demo:out+='\nProduction prompt in this span (not assumed spoken):\n\n'+'\n\n'.join('> '+x['text'] for x in demo)+'\n'
 (R/'drafts'/f'{cid}.md').write_text(out)
(R/'planning/clip_candidates.json').write_text(json.dumps(records,indent=2))
with open(R/'planning/clip_candidates.csv','w') as f:
 w=csv.writer(f);w.writerow(['id','title','source_section','start_line','end_line','words','estimated_seconds_min','estimated_seconds_max','status','variant_of'])
 for r in records:w.writerow([r['id'],r['title'],r['source_section'],*r['source_lines'],r['word_count'],*r['estimated_duration_seconds'],r['status'],r.get('variant_of','')])
# Comprehensive script example/production-prompt bank, with every matched passage kept separate from claims/results.
examples=[]
for i,line in enumerate(lines,1):
 if i>167:break
 if i<5 or line.startswith(('Sources:','Source:')):continue
 if re.search(r'\b(example|imagine|scenario|such as|for instance|our demo|for this demo|for the demo|suppose|Demo prompt:|inventory at risk|Celsius|TemperatureC|revenue|frozen|Lakeshore|supplier|Teams|forecast|Read and Build)\b',line,re.I) or line.startswith('Demo prompt:'):
  examples.append({'id':f'E{len(examples)+1:03}','source_section':sections[i],'line':i,'verbatim':line,'kind':'production_prompt_not_assumed_spoken' if line.startswith('Demo prompt:') else 'production_screen_direction_not_spoken' if line.startswith('On screen:') else 'script_example_or_scenario','recording_confirmed':False})
(R/'planning/script_examples.json').write_text(json.dumps(examples,indent=2))
# Browsable draft gallery: explicitly no video players until actual clips exist.
cards=''.join(f'<article data-search="{html.escape(r["title"].lower())}"><small>{r["id"]} · {r["word_count"]} words · estimated {r["estimated_duration_seconds"][0]}–{r["estimated_duration_seconds"][1]}s</small><h2>{html.escape(r["title"])}</h2><p>{html.escape(r["graphic_reason"])}</p><a href="drafts/{r["id"]}.md">Read verbatim draft</a></article>' for r in records)
(R/'index.html').write_text('''<!doctype html><html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Fabric short-form draft bank</title><style>body{max-width:1200px;margin:36px auto;padding:0 20px;background:#f4faf7;color:#183b31;font:17px/1.5 system-ui}h1{font:42px Georgia}.notice{padding:20px;border:1px solid #99c6b5;background:#e2f2e9;border-radius:14px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}article{background:white;padding:22px;border:1px solid #d4e7dd;border-radius:16px}h2{font:25px Georgia}a{color:#117865}input{width:100%;padding:14px;margin:24px 0;font:inherit}</style><h1>Fabric short-form draft bank</h1><div class="notice"><strong>Audio ingest blocked:</strong> the new recording exceeds the 32 MiB transfer limit. These are script-based drafts from the earlier interview, not extracted recording moments or finished video clips. All recording timestamps are intentionally empty.</div><p>'''+str(len(records))+''' candidates, including one overlapping variant. Full-word citations, graphic choices and scope caveats are saved in each draft.</p><input placeholder="Filter by topic" oninput="document.querySelectorAll('article').forEach(e=>e.hidden=!e.dataset.search.includes(this.value.toLowerCase()))"><div class="grid">'''+cards+'</div></html>')
print(len(records),'draft candidates;',len(examples),'source-script example/production passages')
