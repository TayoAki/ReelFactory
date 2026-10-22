from pathlib import Path
import re,json,ast,hashlib
R=Path(__file__).resolve().parent
playbook=Path('/workspace/attachments/1c7f31b8-1045-44ba-a96d-c33e3c13994f/Pasted text.txt')
kit=Path('/workspace/archive-review/current-editor-v1/NextPhase-EditorV1/skill/editor-v1')
text=playbook.read_text();lines=text.splitlines();examples=[];heading=''
for i,line in enumerate(lines,1):
 if line.startswith('#'):heading=line.strip('# ')
 if line.startswith('#'):continue
 if re.search(r'\b(example|e\.g\.|for instance|such as|invented|fictional)\b',line,re.I) or '→' in line or '{{' in line:
  if not line.strip():continue
  examples.append({'id':f'PB{len(examples)+1:03}','section':heading,'line':i,'excerpt':line,'classification':'instructional example/template; not verified creator/client performance','provenance':'uploaded playbook'})
blocks=[]
for m in re.finditer(r'^```([^\n]*)\n(.*?)^```',text,re.M|re.S):
 start=text[:m.start()].count('\n')+1
 blocks.append({'id':f'CB{len(blocks)+1:03}','language':m.group(1),'line':start,'content':m.group(2),'classification':'sample schema/template/illustration, not a live source result'})
(R/'templates/playbook_examples.json').write_text(json.dumps({'extraction_scope':'Every explicit example/template/arrow-pattern line and every fenced sample block in the supplied playbook; not claimed to be independently verified real-world evidence.','source_sha256':hashlib.sha256(playbook.read_bytes()).hexdigest(),'example_template_lines':examples,'sample_blocks':blocks},indent=2))
# Extract every routable device row in the supplied skill's central table.
skill=(kit/'SKILL.md').read_text();part=skill[skill.index('| device |'):skill.index('**Layer order:')];devices=[]
for line in part.splitlines()[2:]:
 if not line.startswith('|'):continue
 cells=[c.strip() for c in line.strip('|').split('|')]
 if len(cells)<3:continue
 devices.append({'id':f'D{len(devices)+1:02}','device':cells[0],'use_when':cells[1],'reported_recipe':cells[2],'source':'Editor V1 SKILL.md §2','evidence_status':'reported by supplied package; not independently remeasured in this task','fabric_adaptation':'Use only if it explains the spoken relationship; Fabric theme and legibility override red/amber defaults and arbitrary rapid cuts.'})
(R/'templates/editor_devices.json').write_text(json.dumps(devices,indent=2))
# All callable definitions in both supplied device components, for implementation lookup without running setup.
functions=[]
for rel in ['components/ev1_devices.py','components/ev1_more.py']:
 t=ast.parse((kit/rel).read_text())
 for node in t.body:
  if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and not node.name.startswith('_'):
   functions.append({'name':node.name,'source':rel,'line':node.lineno,'args':[a.arg for a in node.args.args],'doc':(ast.get_docstring(node) or '')[:400]})
(R/'templates/editor_implementation_index.json').write_text(json.dumps(functions,indent=2))
# Extract all worked-example line→device→source mappings, without importing the example's content into Fabric scripts.
plan=(kit/'template/example/PLAN.md').read_text();part=plan[plan.index('| t |'):plan.index('## As built')];beats=[]
for l in part.splitlines()[2:]:
 if not l.startswith('|'):continue
 cells=[c.strip() for c in l.strip('|').split('|')]
 if len(cells)>=4:beats.append({'reported_time':cells[0],'example_words':cells[1],'device':cells[2],'source_material':cells[3],'reuse':'Structure/device purpose only; do not borrow claims, footage, voice or text for Fabric.'})
(R/'templates/editor_worked_example_beats.json').write_text(json.dumps(beats,indent=2))
summary={'playbook_example_template_lines':len(examples),'playbook_fenced_samples':len(blocks),'editor_device_routing_rows':len(devices),'editor_public_helpers':len(functions),'editor_worked_example_beats':len(beats),'source_archive':'NextPhase — Editor V1 Skill-20261021T163545Z-1-001.zip','recording_reviewed':False}
(R/'templates/extraction_summary.json').write_text(json.dumps(summary,indent=2));print(summary)
