from pathlib import Path
import json
R=Path(__file__).parent
source=(R.parent/'motion-pilot-fabric/input-transcript.txt').read_text().splitlines()
rs=json.loads((R/'planning/clip_candidates.json').read_text());assert len(rs)==39
for r in rs:
 assert r['recording_start'] is None and r['recording_end'] is None
 assert r['status']=='script_draft_awaiting_recording' and r['bucket']=='experiment'
 assert (R/'drafts'/f'{r["id"]}.md').is_file()
 for p in r['verbatim_passages']:
  assert p['verbatim']==source[p['source_line']-1]
  assert not p['verbatim'].startswith(('Demo prompt:','On screen:','Sources:','Source:'))
for p in R.rglob('*.json'):json.loads(p.read_text())
report={'script_drafts':len(rs),'unique_provisional_script_takeaways':len(rs)-sum(bool(r.get('variant_of')) for r in rs),'verbatim_script_passages':'match cited lines','script_draft_recording_timestamps':'all null; these remain separate from actual recording clips','json_files':'parse successfully'}
manifest=R/'recording-clips/manifest.json'
if manifest.exists():
 actual=json.loads(manifest.read_text());checks=json.loads((R/'recording-clips/export-validation.json').read_text())
 assert len(actual['clips'])==len(checks)==57
 assert all(c['source_start']>=0 and c['source_end']>c['source_start'] and (R/'recording-clips'/c['export']).is_file() for c in actual['clips'])
 report['current_recording']={'source_seconds':actual['duration'],'selected_clips':len(actual['clips']),'rendered_clips':sum(c['status']=='rendered draft' for c in actual['clips']),'full_decode_checks':len(checks),'access_blocker_resolved':True,'review_status':'ASR transcript and technical claims remain review drafts'}
(R/'validation.json').write_text(json.dumps(report,indent=2));print(report)
