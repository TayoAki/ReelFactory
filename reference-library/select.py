"""Create a source-backed image-generation packet after choosing the teaching relationship.
This retrieves curated references; it does not infer factual truth or automatically choose a diagram from keywords.
"""
from pathlib import Path
import argparse,json,re
R=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--template',required=True);p.add_argument('--instance');p.add_argument('--narration');p.add_argument('--slots',default='{}');p.add_argument('--mode',choices=['adaptation','reconstruction'],default='adaptation');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
L=json.loads((R/'library.json').read_text());templates={t['id']:t for t in L['templates']};entries={e['id']:e for e in L['instances']}
if a.template not in templates:p.error('Unknown teaching relationship. Choose from: '+', '.join(templates))
if a.mode=='adaptation' and not a.narration:p.error('Adaptation requires the target narration; source wording must not silently become the new script')
t=templates[a.template];e=entries[a.instance or t['representative_entry']]
if e['template_id']!=a.template:p.error('Instance belongs to a different teaching relationship')
slots=json.loads(a.slots);slots={**t['example_source_bindings'],**slots} if a.mode=='reconstruction' and e['id']==t['representative_entry'] else slots;patterns=t['transcript_patterns'];bound=[re.sub(r'\{\{(.*?)\}\}',lambda m:str(slots.get(m[1],m[0])),x) for x in patterns];refs=[str((R/x).resolve()) for x in e['image_reference_use']['recommended_reference_images']]
assert all(Path(x).is_file() for x in refs)
text=a.narration or e['original_transcript'];prompt=f'''Create a single settled storyboard master image for this technical teaching beat.
Teaching relationship: {t['relationship']}. Teaching job: {t['teaching_job']}.
Target narration: {text}
Target semantic slots: {json.dumps(slots,ensure_ascii=False)}
Reference image 1 is the selected original-source style anchor. Further original-source images show earlier/build states. Use their visual hierarchy, icon mass, typography, color roles, surfaces, spacing and persistent relationships when appropriate. Do not use the rejected reconstruction as a reference.
Source-specific observation: {json.dumps(e['source_specific_observation'],ensure_ascii=False)}
The finished diagram's reading order is separate from its reveal order. For adaptation, align the planned state sequence with the new narration; for reconstruction, follow the observed source sequence.
Mode: {a.mode}. {'Preserve the reference content and label source claims accurately.' if a.mode=='reconstruction' else 'Replace reference product labels, values, examples and claims with the supplied verified target content. Do not transfer source benchmarks, availability or access guarantees.'}
Deliver a polished readable still with exact requested labels and useful whitespace. It is a candidate for human image review before editable reconstruction and motion. Produce only this master still; later states should be derived from it to preserve continuity.'''
packet={'template_id':t['id'],'instance_id':e['id'],'selection_reason':t['choose_when'],'alternative_or_misuse':t['choose_something_else_when'],'target_narration':text,'target_slot_bindings':slots,'binding_origin':'Representative source example' if a.mode=='reconstruction' and e['id']==t['representative_entry'] else 'Explicit target bindings only; representative-source bindings are not silently transferred to another instance','sentence_scaffolds':bound,'source_quote':e['original_transcript'],'source_range':[e['source_start'],e['source_end']],'source_specific_observation':e['source_specific_observation'],'reading_order_and_reveal_order_are_separate':True,'original_reference_assets_relative_to_library':e['image_reference_use']['recommended_reference_images'],'imagegen_request':{'prompt':prompt,'referenced_image_paths':refs,'transparent_background':False},'storyboard_requirement':'Generate a master still, derive at least three coherent state images, compare to original references, review, reconstruct editable layers, then animate.','confidence':'Curated references and editorial sentence scaffolds; not a trained selector, word-alignment model or claim verifier.'}
a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(packet,indent=2));a.out.with_suffix('.prompt.txt').write_text(prompt);print('Wrote',a.out,'with',len(refs),'original source-image references')
