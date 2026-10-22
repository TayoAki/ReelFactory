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
report={'drafts':len(rs),'unique_provisional_takeaways':len(rs)-sum(bool(r.get('variant_of')) for r in rs),'verbatim_script_passages':'match cited lines','actual_recording_timestamps':'all null as required','actual_recording_reviewed':False,'actual_recording_videos_rendered':0,'json_files':'parse successfully','missing_source':'M4A exceeds 32 MiB download limit'}
(R/'validation.json').write_text(json.dumps(report,indent=2));print(report)
