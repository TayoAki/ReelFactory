from pathlib import Path
import sys,json,hashlib,subprocess,html,base64,shutil
from collections import Counter
from curation import FAMILIES,INSTANCES
R=Path(__file__).resolve().parent;ROOT=R.parent;SRC=ROOT/'full-video/original.mp4';FPS=30
T=json.loads((ROOT/'research/fabric-youtube/HtR5m5VjaDQ/transcript.json').read_text())['transcript'];EVENTS=json.loads((ROOT/'full-video/event-map.json').read_text())['events'];PLAN=json.loads((ROOT/'full-video/plan.json').read_text());OLD=json.loads((ROOT/'research/ontology-adaptation/template-library/catalog.json').read_text())['sequences']
for folder in ['frames/full','frames/graphic','entries','templates','packets']:(R/folder).mkdir(parents=True,exist_ok=True)
def clock(t):return f'{int(t)//60:02}:{t%60:05.2f}'
def frame(t):return max(0,min(round(t*FPS),round(PLAN['source_duration']*FPS)-2))
def paths(t):
 f=frame(t);return {'full_frame':f'frames/full/{f:07d}.jpg','graphic_region':f'frames/graphic/{f:07d}.jpg','requested_seconds':t,'sample_frame':f,'normalized_source_seconds':f/FPS,'temporal_precision':'Normalized 30fps screenshot within approximately one frame; the chosen teaching anchors remain estimated.'}
def captions(a,b):return [{'text':r['text'],'start':float(r['startMs'])/1000,'end':float(r['endMs'])/1000} for r in T if float(r['startMs'])/1000<b and float(r['endMs'])/1000>a]
def excerpt(a,b):return ' '.join(r['text'] for r in T if float(r['startMs'])/1000<b and float(r['endMs'])/1000>a)
def nearby(t):return captions(max(0,t-2),t+2)
entries=[];allframes=set();unassigned=[]
for idx,(id,a,b,family,label,times,why) in enumerate(INSTANCES):
 fam=FAMILIES[family];states=[]
 for j,t in enumerate(times):
  p=paths(t);allframes.add(p['sample_frame']);states.append({'id':f'state-{j+1:02}','sequence_role':'earlier observed state' if j==0 else 'later observed state' if j==len(times)-1 else 'intermediate observed state','time':t,'timecode':clock(t),'images':p,'nearby_original_transcript':nearby(t),'state_observation_status':'Source screenshot, with sequence-level observations below; exact object-change annotations require visual review of the frame.'})
 anchors=[]
 for e in EVENTS:
  t=e['source_time']
  if not a<=t<b:continue
  same=[x['source_time'] for x in EVENTS if t<x['source_time']<b];limit=min(same) if same else b
  sampletimes=[max(a,t-.25),min(t+.25,limit-1/FPS),min(t+1,limit-1/FPS)]
  images=[]
  for phase,tm in zip(['before','near-transition','after'],sampletimes):
   p=paths(max(a,tm));allframes.add(p['sample_frame']);images.append({'phase':phase,**p})
  anchors.append({'estimated_anchor':t,'nearby_original_transcript':nearby(t),'source_images':images,'interpretation':'A sampled source change window, not the original keyframe timing or word-aligned speech trigger.'})
 overlap=[s for s in OLD if max(a,s['start'])<min(b,s['end'])]
 entry={'id':id,'index':idx+1,'source_video':'https://www.youtube.com/watch?v=HtR5m5VjaDQ','source_start':a,'source_end':b,'source_timecode':clock(a)+'–'+clock(b),'template_id':family,'label':label,'category':'authentic-ui-evidence' if family=='ui-evidence' else 'chapter-navigation' if family=='chapter' else 'explanatory-graphic-or-overlay','teaching_intent':why,'relationship':fam[0],'original_transcript':excerpt(a,b),'original_transcript_segments':captions(a,b),'transcript_status':'Verbatim supplied rolling transcript text; timing overlaps and transcription errors remain. This is not a rewritten quotation.','rhetorical_move':fam[1],'parameterized_transcript_patterns':fam[2],'semantic_slots':fam[3],'selection_rule':fam[4],'better_alternative_or_misuse':fam[5],'motion_recipe':fam[6],'state_images':states,'change_windows':anchors,'prior_source_observations':[{'id':s['id'],'observed_state_pattern':s['observed_state_pattern'],'persistent_context':s['persistent_context'],'evidence_status':s['evidence_status']} for s in overlap],'image_reference_use':{'recommended_reference_images':[s['images']['graphic_region'] for s in ([states[0],states[len(states)//2],states[-1]] if len(states)>3 else states)],'purpose':'Original visual evidence for generated storyboard art direction; diagram-region crops exclude presenter/caption distractions.','keep':'Visual hierarchy, shape/texture, icon mass, typography, color roles, whitespace and persistent-object relationships when appropriate.','replace':'Source product labels, business claims, values and entities according to the new verified script.','never_use':'Rejected reconstruction screenshots as style references.'},'confidence':{'source_images':'Directly extracted from original uploaded footage; not generated or taken from the failed recreation.','coverage':'All 58 curated instances plus the previous 206 estimated visual anchors are indexed; micro-transition exhaustiveness is not certified.','pedagogy_and_templates':'Editorial interpretations grounded in the paired transcript and images.','timing':'Estimated teaching/cut anchors, not word alignment.'}}
 entries.append(entry);(R/'entries'/(id+'.json')).write_text(json.dumps(entry,indent=2))
for e in EVENTS:
 if not any(a<=e['source_time']<b for _,a,b,*_ in INSTANCES):unassigned.append(e['source_time'])
# Retain any source anchor outside the curated entry intervals as explicit audit evidence.
extra=[]
for t in unassigned:
 item={'time':t,'reason':'Prior source anchor lies outside a curated graphic interval; retained for coverage review.','nearby_original_transcript':nearby(t),'images':[]}
 for phase,tm in [('before',max(0,t-.25)),('during',t+.25),('after',t+1)]:
  p=paths(tm);allframes.add(p['sample_frame']);item['images'].append({'phase':phase,**p})
 extra.append(item)
# One decode pass, selecting the requested normalized source frames. Two outputs preserve full evidence and a graphic-only reference crop.
missing=[n for n in sorted(allframes) if not (R/f'frames/full/{n:07d}.jpg').exists() or not (R/f'frames/graphic/{n:07d}.jpg').exists()]
if missing:
 def select_expression(values):
  if len(values)==1:return f'eq(n,{values[0]})'
  mid=len(values)//2
  return f'if(lt(n,{values[mid]}),{select_expression(values[:mid])},{select_expression(values[mid:])})'
 expression=select_expression(missing)
 filt=f"[0:v]fps=30,select='{expression}',split=2[full][crop];[crop]crop=458:282:12:30[graphic]"
 args=['ffmpeg','-v','error','-y','-i',str(SRC),'-filter_complex',filt,'-map','[full]','-fps_mode','vfr','-q:v','2','-frame_pts','1',str(R/'frames/full/%07d.jpg'),'-map','[graphic]','-fps_mode','vfr','-q:v','2','-frame_pts','1',str(R/'frames/graphic/%07d.jpg')]
 subprocess.run(args,check=True)
for n in allframes:
 assert (R/f'frames/full/{n:07d}.jpg').exists(),n
 assert (R/f'frames/graphic/{n:07d}.jpg').exists(),n
families=[]
for id,fam in FAMILIES.items():
 instances=[e['id'] for e in entries if e['template_id']==id];record={'id':id,'relationship':fam[0],'teaching_job':fam[1],'transcript_patterns':fam[2],'semantic_slots':fam[3],'choose_when':fam[4],'choose_something_else_when':fam[5],'motion_grammar':fam[6],'instances':instances,'classification':'Curated editorial teaching template; not a trained classifier or a product fact.'};families.append(record);(R/'templates'/(id+'.json')).write_text(json.dumps(record,indent=2))
manifest={'source_video':'https://www.youtube.com/watch?v=HtR5m5VjaDQ','source_file':'../full-video/original.mp4','source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'source_duration_seconds':PLAN['source_duration'],'instances':entries,'templates':families,'unassigned_anchor_audit':extra,'counts':{'graphic_instances':len(entries),'template_families':len(families),'meaningful_state_samples':sum(len(e['state_images']) for e in entries),'change_windows':sum(len(e['change_windows']) for e in entries),'prior_anchors':len(EVENTS),'unassigned_prior_anchors':len(unassigned),'unique_source_frames':len(allframes),'image_files':len(allframes)*2},'crop_provenance':'Deterministic screenshot extraction: full source 640x360 plus crop x12 y30 w458 h282. No generative alteration, no upscaling. Full image retained for checking crop context.','observation_vs_interpretation':'Screenshots and raw transcript are source evidence. Teaching roles, parameterized sentences, choices and transfer rules are editorial interpretation. Estimated anchors are not exact spoken triggers.','coverage':'Complete uploaded 34:28 source reviewed through prior scan; curated instances and all prior estimated anchors retained. Not a claim to annotate every animation keyframe.'}
(R/'library.json').write_text(json.dumps(manifest,indent=2));(R/'counts.json').write_text(json.dumps(manifest['counts'],indent=2));print(json.dumps(manifest['counts']),flush=True)
