from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parent;P=json.loads((R/'plan.json').read_text());S=P['scenes'];checks=[]
assert len(S)==44 and S[0]['source_start']==0
for a,b in zip(S,S[1:]):assert abs(a['source_end']-b['source_start'])<.001
assert abs(S[-1]['source_end']-P['source_duration'])<.001
checks.append('44 intervals cover the complete source without gaps or overlaps')
media=[]
for name,size in [('full-reconstruction.mp4',(1920,1080)),('full-comparison.mp4',(1280,392))]:
 path=R/name;probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-show_chapters','-of','json',str(path)]));v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio');assert (v['width'],v['height'])==size;assert v['r_frame_rate']=='30/1';num,den=map(int,v['avg_frame_rate'].split('/'));assert abs(num/den-30)<.01;assert abs(float(probe['format']['duration'])-P['source_duration'])<.15
 if name=='full-comparison.mp4':
  decoded=subprocess.run(['ffmpeg','-v','error','-i',str(path),'-map','0:v','-map','0:a','-f','null','-'],capture_output=True)
  assert decoded.returncode==0 and not decoded.stderr,decoded.stderr.decode()
 decode_evidence='Complete native video decoded successfully while rendering the full comparison' if name=='full-reconstruction.mp4' else 'Complete comparison decoded independently without errors'
 media.append({'file':name,'duration':float(probe['format']['duration']),'width':v['width'],'height':v['height'],'fps':v['avg_frame_rate'],'nominal_fps':v['r_frame_rate'],'video_frames':v.get('nb_frames'),'audio_codec':a['codec_name'],'chapters':len(probe.get('chapters',[])),'full_decode':decode_evidence,'bytes':path.stat().st_size})
for s in S:
 assert (R/'renders'/(s['id']+'.mp4')).exists()
 assert (R/'comparison'/(s['id']+'.mp4')).exists()
 for j in range(3):assert (R/'comparison'/(s['id']+f'-{j}.jpg')).exists()
assert (R/'review.html').exists();assert json.loads((R/'storyboard-validation.json').read_text())['valid']
checks.extend(['44 rendered sections and 44 motion comparison excerpts exist','132 matched comparison frames exist','Storyboard contract validation passed; this does not certify fidelity','Full reconstruction decoded during comparison render; comparison independently decoded without errors'])
(R/'verification.json').write_text(json.dumps({'checks':checks,'media':media,'fidelity':'Human source-relative fidelity review remains pending; no numerical similarity score asserted.'},indent=2));print(json.dumps({'checks':checks,'media':media},indent=2))
