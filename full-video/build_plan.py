from pathlib import Path
import json
R=Path(__file__).resolve().parent;ROOT=R.parent;duration=json.loads((R/'source-scan.json').read_text())['duration']
# Times are source-clock estimates checked against the complete 1fps scan, existing dense samples and transcript.
segments=[
('opening',0,8,'speaker','Host introduction',[]),
('intro-map',8,17,'native','Sources converge into Genie Ontology',[8,9.2,10.5,12,13.5,15]),
('host-topic',17,37.333333,'speaker','Host frames the ontology explanation',[27,30]),
('product-family',37.333333,83.7,'existing','Product definition, worked example, governance and product-family comparison',[39.8,43.35,46,47.65,48.85,50.6,53.8,55.167,55.833,61,63.52,64.65,68.56,72.45,77.35,81.53]),
('guest-context',83.7,109.5,'speaker','Guest introduces the context problem',[]),
('wrong-source',109.5,138,'native','A generic model picks the wrong revenue source',[110.5,115,118,125,128,132]),
('ambiguity',138,159.3,'native','Undefined churn rules and stale campaign data cause wrong answers',[138.5,143,147,151,154,157]),
('context-in-heads',159.3,174.2,'speaker','Context lives in documents and people',[]),
('context-repair',174.2,209.5,'native','Existing assets drift; context repairs the question-to-answer route',[174.5,177,180,184,189,196,202,206]),
('architecture',209.5,249,'native','A shared system has modeled and learned context; focus the modeled side',[209.5,215,221,228,234.367,236.1,239]),
('modeled',249,333.5,'native','Build the governed semantics hierarchy',[249,256,263,281,292,307,315,322]),
('learned',333.5,402,'native','Infer context from sources and repeated work',[334,340,347,353,359,365,371,379,386,394]),
('ranking',402,454,'native','Rank context and expose it to consumers',[403,409,413,419,430,438,446]),
('benchmark',454,512,'native','Compare the source-reported accuracy and runtime',[454.5,461,469,479,490,500]),
('host-benchmark',512,525,'speaker','Host asks about the benchmark',[]),
('benchmark-return',525,546,'native','Return to the same chart during the follow-up',[525,531,539]),
('connectors',546,679,'native','Different access paths: SQL, live tools and indexed search',[546,557,567,577,587,600,604,610,615,624,636,644,652,660,670]),
('memory',679,714.5,'hybrid','Personal memory: a stable heading plus authentic interface evidence',[679,686,695,704,710]),
('host-memory',714.5,773,'speaker','Host discusses personal and organizational context',[]),
('demo-one-title',773,776.5,'chapter','Demo chapter card',[773]),
('demo-one-start',776.5,822,'demo','Orient in the actual Genie interface',[789,808,817]),
('demo-context-overlay',822,855,'demo-overlay','Explain context sources above the real prompt',[822,828,835,843,850]),
('demo-one',855,1223,'demo','Query analysis, results, citations, definitions and follow-ups',[879,908,941,990,1018,1046,1072,1105,1148,1180,1203]),
('host-outcomes',1223,1248,'speaker','Host asks about visibility and business context',[1229,1238]),
('outcomes-title',1248,1266,'chapter','From answers to outcomes',[1248]),
('documents',1266,1308,'hybrid','Co-author documents; inspect the authentic evidence',[1266,1275,1284,1294,1302]),
('external-tools',1308,1316,'native','Work also lives in third-party tools',[1308,1311]),
('actions',1316,1355,'native','Permissions constrain tool use and write routes',[1316,1321,1326,1332,1338,1346]),
('skills',1355,1391,'hybrid','Save repeatable tasks as skills and govern distribution',[1355,1363,1371,1378,1385]),
('host-governance',1391,1423,'speaker','Host asks why skill governance matters',[]),
('governance',1423,1464,'native','Three peer governance needs',[1423,1429.23,1430.53,1431.43,1444,1452]),
('agent-intro',1464,1475,'hybrid','A custom agent bundles sources, instructions, skills and memory',[1464,1470]),
('agents',1475,1523,'native','Build agent inputs, examples and parent/child hierarchy',[1475,1479,1484,1490,1496,1503,1510,1517]),
('orchestration',1523,1553,'hybrid','Schedule and trigger recurring work',[1523,1533,1543]),
('surfaces',1553,1608,'hybrid','Access through mobile, desktop, chat and MCP',[1553,1567,1576,1584,1594,1601]),
('demo-two-title',1608,1614,'chapter','Second demo chapter card',[1608]),
('demo-two',1614,1788,'demo','Real actions, scheduled work and custom-agent configuration',[1623,1642,1668,1697,1727,1747,1760,1774]),
('host-start',1788,1794.7,'speaker','Host asks how to get started',[]),
('getting-started-title',1794.7,1796.5,'chapter','Getting started',[1794.7]),
('starting-summary',1796.5,1805,'native','Pick a workflow, ground the data, then expand',[1796.5,1799,1801.5]),
('rollout-one',1805,1850,'native','Pick one team and define benchmark questions',[1805,1814,1825,1834,1842]),
('rollout-two',1850,1957,'native','Record baseline, involve experts, connect sources, iterate',[1850,1860,1871,1880,1890,1901,1911,1920,1932,1944,1952]),
('best-practices',1957,2044,'native','Advance through five fixed recommendations',[1957,1963,1989.733,2006,2019,2029]),
('closing',2044,duration,'speaker','Closing conversation',[])]
scenes=[]
for i,(id,a,b,kind,purpose,events) in enumerate(segments):
 assert i==0 or abs(a-segments[i-1][2])<.001
 scenes.append({'number':i,'id':id,'source_start':a,'source_end':b,'duration':b-a,'kind':kind,'teaching_purpose':purpose,'event_anchors':events,'status':'planned','generation_authorized':'User requested the entire video and each motion-graphics explanation','precision':'Boundaries/events are estimates from 1fps full scan, existing dense samples and transcript; not original keyframes','reuse_rule':'Retain known objects; animate only the new relationship or active focus. Preserve actual UI as evidence rather than inventing execution.','fidelity_review':'pending'})
plan={'source':'https://www.youtube.com/watch?v=HtR5m5VjaDQ','source_duration':duration,'fps':30,'width':1920,'height':1080,'scope':'Whole uploaded 34:28 source, including motion-graphics sections, chapter cards, authentic UI evidence and static fictional presenter intervals','renderer':'Native editable vector/display-list reconstruction with frame-based animation; the existing refined passage is reused','reuse_disclosure':'Source narration and live product UI are retained. Native diagrams and layout are reconstructed; presenters are static fictional placeholders. Optional captions derive from approximate transcript segments; the reused refined passage retains its existing captions.','scenes':scenes}
(R/'plan.json').write_text(json.dumps(plan,indent=2));print(len(scenes),'continuous sections;',round(sum(s['duration'] for s in scenes),3),'seconds')
