"""Validate the planning contract and reference IDs. Does not certify facts or visual quality."""
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('storyboard',type=Path);args=p.parse_args()
root=Path(__file__).resolve().parents[1];plan=json.loads(args.storyboard.read_text());contract=json.loads((root/'references/storyboard-contract.json').read_text());catalog=json.loads((root/'references/catalog.json').read_text());ids={s['id'] for s in catalog['sequences']};templates={s['template_id'] for s in catalog['sequences']};errors=[]
for key in contract['required']:
 if key not in plan:errors.append('Missing '+key)
if plan.get('mode') not in contract['properties']['mode']['enum']:errors.append('Invalid mode')
seen=set()
for s in plan.get('scenes',[]):
 label='Scene '+str(s.get('id','?'))
 for key in contract['properties']['scenes']['items']['required']:
  if not s.get(key):errors.append(label+': missing/empty '+key)
 if plan.get('visual_workflow')=='image-first':
  if not s.get('master_image'):errors.append(label+': missing generated master image')
  states=s.get('state_images',[])
  if len(states)<3 and not s.get('state_count_exception_reason'):errors.append(label+': image-first explanation requires at least three meaningful state images')
  for state in states:
   for field in ['id','image','narration_role','new_understanding','persistent','next_transition']:
    if not state.get(field):errors.append(label+': state '+str(state.get('id','?'))+' missing '+field)
   if state.get('image') and not (args.storyboard.parent/state['image']).is_file():errors.append(label+': missing image file '+state['image'])
  if s.get('master_image') and not (args.storyboard.parent/s['master_image']).is_file():errors.append(label+': master image file does not exist')
  if s.get('status') in ['motion_ready','animation_rendered'] and not s.get('layer_reconstruction'):errors.append(label+': motion requires editable layer reconstruction')
 if s.get('id') in seen:errors.append(label+': duplicate ID')
 seen.add(s.get('id'))
 if s.get('reference_sequence') not in ids:errors.append(label+': unknown reference sequence')
 if s.get('template_id') not in templates:errors.append(label+': unknown template family')
 if s.get('source_end',1)<=s.get('source_start',0):errors.append(label+': non-positive source interval')
 if s.get('render_end',1)<=s.get('render_start',0):errors.append(label+': non-positive render interval')
 if any(not u.startswith(('https://','http://')) for u in s.get('sources',[])):errors.append(label+': invalid source URL')
 if s.get('status') in ['generation_requested','rendered_for_review','assets_ready','motion_ready'] and not (s.get('approved_by_user') or s.get('generation_authorized_by_user') or plan.get('generation_authorization')):errors.append(label+': generated without recorded approval or authorization')
 if s.get('approved_by_user') and not s.get('approval_record'):errors.append(label+': human approval asserted without a record')
if plan.get('mode')=='technical-adaptation' and not plan.get('technical_rewrite'):errors.append('Adaptation requires original/proposed rewrite and reasons')
report={'valid':not errors,'scene_count':len(plan.get('scenes',[])),'reference_sequences':len(ids),'checks':'Required fields, known reference/template IDs, intervals, URLs, recorded authorization, and image-first state counts/image-file existence when selected. Does not assess visual quality.','errors':errors};print(json.dumps(report,indent=2));raise SystemExit(bool(errors))
