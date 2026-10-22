from pathlib import Path
import json,html,base64,subprocess,concurrent.futures
R=Path(__file__).resolve().parent;E=json.loads((R/'event-map.json').read_text())['events'];P=json.loads((R/'plan.json').read_text());S={s['id']:s for s in P['scenes']};STATES={(r['scene'],r['anchor_time']):r for r in json.loads((R/'reconstruction-state-map.json').read_text())};D=R/'event-frames';D.mkdir(exist_ok=True)
def one(pair):
 i,e=pair;s=S[e['scene']];future=[x for x in s['event_anchors'] if x>e['source_time']];t=min(e['source_time']+1,(future[0] if future else s['source_end'])-1/30);f=D/f'{i:03}-{e["scene"]}.jpg'
 if not f.exists():subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(R/'full-comparison.mp4'),'-frames:v','1','-vf','scale=960:294','-q:v','3',str(f)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 e['sample_time']=t;e['comparison_frame']=str(f.relative_to(R));return e,f
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rows=list(ex.map(one,enumerate(E)))
body=['<!doctype html><meta charset="utf-8"><title>206 visual anchors</title><style>body{background:#101b22;color:#eaf3f4;font:16px system-ui;max-width:1100px;margin:30px auto;padding:0 20px}p{line-height:1.5;color:#c5d3d8}details{border:1px solid #34525b;padding:15px;border-radius:12px;margin:14px 0}summary{font-size:20px;cursor:pointer}img{width:100%;margin:18px 0 8px}article{border-top:1px solid #34525b;margin-top:16px}a{color:#88d7d7}</style><h1>206 visual anchors across the full source</h1><p>Original left; reconstruction right. Each image samples approximately one second after an estimated visual anchor, capped before the next anchor. These are source-clock checks, not exact spoken triggers or a claim that every animation keyframe is matched.</p><p>Nearby rolling transcript segments provide context. Read the section review for selection reasoning, alternatives and motion excerpts.</p>']
for scene,s in S.items():
 rr=[(e,f) for e,f in rows if e['scene']==scene]
 if not rr:continue
 body.append('<details><summary>'+html.escape(scene.replace('-',' ').title())+f' — {len(rr)} anchors</summary>')
 for e,f in rr:
  t=e['source_time'];stamp=f'{int(t)//60:02}:{t%60:06.3f}';quotes=' / '.join(x['text'] for x in e['nearby_captions'][:2]);url='data:image/jpeg;base64,'+base64.b64encode(f.read_bytes()).decode()
  state=STATES.get((scene,e['source_time']),{});delta='Reconstruction text added: '+(', '.join(state.get('added_text',[])) or 'none')+'. Removed: '+(', '.join(state.get('removed_text',[])) or 'none')+'. Emphasis changes: '+(', '.join(c['text'] for c in state.get('emphasis_changes',[])) or 'none')+'. These changes describe our reconstruction; compare against the original above.';delta=delta if state else 'This interval uses a reused refined passage, a presenter callout, or authentic UI. Native text-state changes are not extracted for this interval; inspect the matched comparison.';body.append('<article><h3>'+stamp+' · '+html.escape(e['graphic_type'])+'</h3><p>'+html.escape(quotes)+'</p><img loading="lazy" src="'+url+'"><p>'+html.escape(e['relationship_to_teach'])+'</p><p>'+html.escape(delta)+'</p></article>')
 body.append('</details>')
(R/'event-atlas.html').write_text(''.join(body));(R/'event-map.json').write_text(json.dumps({'source':P['source'],'duration':P['source_duration'],'events':[e for e,f in rows],'precision':'Estimated anchors with nearby transcript; each matched image is sampled after the anchor, not word aligned.'},indent=2));print('206 matched event samples exported',flush=True)
