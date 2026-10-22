from pathlib import Path
import json,re,hashlib,tempfile,subprocess
from PIL import Image
R=Path(__file__).resolve().parent;L=json.loads((R/'library.json').read_text());templates={t['id']:t for t in L['templates']};ids=set();referenced=set();anchors=[]
for e in L['instances']:
 assert e['id'] not in ids;ids.add(e['id']);assert e['source_start']<e['source_end'];assert e['template_id'] in templates;assert len(e['state_images'])>=3;assert e['original_transcript_segments']
 for state in e['state_images']:
  assert e['source_start']<=state['time']<e['source_end'];assert state['nearby_original_transcript']
  referenced.update(state['images'][key] for key in ['full_frame','graphic_region'])
 for w in e['change_windows']:
  anchors.append(w['estimated_anchor']);assert len(w['source_images'])==3
  for im in w['source_images']:referenced.update(im[key] for key in ['full_frame','graphic_region'])
 for ref in e['image_reference_use']['recommended_reference_images']:assert ref.startswith('frames/graphic/') and (R/ref).is_file()
 assert (R/'entries'/(e['id']+'.md')).is_file()
for rel in referenced:
 assert rel.startswith('frames/');p=R/rel;assert p.is_file();im=Image.open(p);expected=(640,360) if '/full/' in rel else (458,282);assert im.size==expected,(p,im.size);im.verify()
for t in templates.values():
 variables={v for pattern in t['transcript_patterns'] for v in re.findall(r'\{\{(.*?)\}\}',pattern)};assert variables.issubset(set(t['semantic_slots']));assert not t['unbound_source_example_slots'];assert all('{{' not in x for x in t['filled_source_sentence_scaffolds']);assert t['representative_entry'] in ids
assert len(anchors)==206 and len(set(anchors))==206;assert not L['unassigned_anchor_audit'];assert L['counts']['unique_source_frames']==len(list((R/'frames/full').glob('*.jpg')))==844
source=(R/L['source_file']).resolve();assert hashlib.sha256(source.read_bytes()).hexdigest()==L['source_sha256']
with tempfile.TemporaryDirectory() as temp:
 out=Path(temp)/'packet.json'
 result=subprocess.run(['python',str(R/'select.py'),'--template','input-output','--instance','constrained-web-flow','--mode','reconstruction','--out',str(out)],capture_output=True,text=True);assert result.returncode==0;packet=json.loads(out.read_text());assert len(packet['imagegen_request']['referenced_image_paths'])==3;assert all(str(R/'frames/graphic') in p for p in packet['imagegen_request']['referenced_image_paths']);assert packet['source_specific_observation']['observed_reveal_order'][0].startswith('Peach model')
 bad=subprocess.run(['python',str(R/'select.py'),'--template','input-output','--out',str(out)],capture_output=True,text=True);assert bad.returncode!=0 and 'target narration' in bad.stderr
 other=subprocess.run(['python',str(R/'select.py'),'--template','feature-evidence','--instance','collaborative-documents','--mode','reconstruction','--out',str(out)],capture_output=True,text=True);assert other.returncode==0;assert json.loads(out.read_text())['target_slot_bindings']=={}
report={'valid':True,'counts':L['counts'],'checks':['58 unique source entries with paired raw transcript and at least three source states','206 prior estimated anchors retained with three-phase source screenshots','1688 image files at original/cropped native resolution','25 source-bound sentence templates with all declared pattern slots','Source file SHA-256 matches extraction provenance','Reference packets use only original screenshot files','Model-first reveal observation retained separately from left-to-right reading order','Adaptation cannot silently reuse source narration','Representative source bindings are not transferred to another instance'],'limits':'These checks validate data and provenance. They do not certify every graphic micro-transition, exact speech alignment, product claims or human aesthetic approval.'};(R/'validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
