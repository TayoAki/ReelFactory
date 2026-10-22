from pathlib import Path
import json,subprocess,base64,html,concurrent.futures
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parent;P=json.loads((R/'plan.json').read_text());S=P['scenes'];EVENTS=json.loads((R/'event-map.json').read_text())['events'];REC={r['scene']:r for r in json.loads((R/'recipes.json').read_text())};D=R/'comparison';D.mkdir(exist_ok=True)
def run(a):subprocess.run(a,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
def clock(t):return f'{int(t)//60:02}:{int(t)%60:02}'
def data(p):return 'data:'+('video/mp4' if p.suffix=='.mp4' else 'image/jpeg')+';base64,'+base64.b64encode(p.read_bytes()).decode()
# The transcript contains overlapping rolling captions: truncate at the next segment's start.
T=json.loads((R.parent/'research/fabric-youtube/HtR5m5VjaDQ/transcript.json').read_text())['transcript']
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
subs=[]
for i,row in enumerate(T):
 a=float(row['startMs'])/1000;b=min(float(row['endMs'])/1000,float(T[i+1]['startMs'])/1000 if i+1<len(T) else P['source_duration'])
 if b>a:subs.append(f'{len(subs)+1}\n{stamp(a)} --> {stamp(b)}\n{row["text"]}\n')
(R/'transcript-captions.srt').write_text('\n'.join(subs))
# Optional captions and chapter markers preserve clean diagram frames by default.
meta=[';FFMETADATA1']
for section in S:
 meta += ['[CHAPTER]','TIMEBASE=1/1000','START='+str(round(section['source_start']*1000)),'END='+str(round(section['source_end']*1000)),'title='+section['id'].replace('-',' ').title()]
(R/'chapters.ffmetadata').write_text('\n'.join(meta))
run(['ffmpeg','-v','error','-y','-i',str(R/'full-reconstruction.mp4'),'-i',str(R/'chapters.ffmetadata'),'-i',str(R/'transcript-captions.srt'),'-map','0:v','-map','0:a','-map','2:s','-map_metadata','1','-map_chapters','1','-c:v','copy','-c:a','copy','-c:s','mov_text','-disposition:s:0','0','-metadata:s:s:0','language=eng','-movflags','+faststart',str(R/'chaptered-reconstruction.mp4')])
(R/'chaptered-reconstruction.mp4').replace(R/'full-reconstruction.mp4')

# Full comparison uses exactly the same source clock and one narration track.
run(['ffmpeg','-y','-i',str(R/'original.mp4'),'-i',str(R/'full-reconstruction.mp4'),'-i',str(R/'chapters.ffmetadata'),'-filter_complex',"[0:v]scale=640:360,pad=640:392:0:32:black,drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='ORIGINAL':x=12:y=8:fontsize=18:fontcolor=white[l];[1:v]scale=640:360,pad=640:392:0:32:black,drawtext=fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf:text='RECONSTRUCTION':x=12:y=8:fontsize=18:fontcolor=white[r];[l][r]hstack=shortest=1[v]",'-map','[v]','-map','0:a','-map_metadata','2','-map_chapters','2','-c:v','libx264','-preset','veryfast','-crf','22','-threads','3','-c:a','aac','-b:a','96k','-t',str(P['source_duration']),'-movflags','+faststart',str(R/'full-comparison.mp4')])
def section(s):
 a=s['source_start'];b=s['source_end'];anchors=s['event_anchors'];start=max(a,min((anchors[1] if len(anchors)>1 else a),b-4));duration=min(8,b-start);clip=D/(s['id']+'.mp4')
 if not clip.exists():run(['ffmpeg','-v','error','-y','-ss',str(start),'-i',str(R/'full-comparison.mp4'),'-t',str(duration),'-an','-c:v','libx264','-preset','veryfast','-crf','24','-threads','1','-movflags','+faststart',str(clip)])
 imgs=[]
 for j,f in enumerate([.1,.5,.9]):
  t=a+(b-a)*f;out=D/(s['id']+f'-{j}.jpg');run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(R/'full-comparison.mp4'),'-frames:v','1','-q:v','3',str(out)]);imgs.append(out)
 excerpt=' '.join(r['text'] for r in T if float(r['startMs'])/1000>=a and float(r['startMs'])/1000<b)
 s['transcript_excerpt']=excerpt;s['status']='rendered';s['comparison_clip_start']=start;s['comparison_clip_duration']=duration;s['evidence']='Three matched source-clock samples and an eight-second motion excerpt; full section remains available in full comparison.';s['remaining_differences']='Vector geometry, icon silhouettes, motion curves and some estimated event times differ. Static presenter placeholders are intentional. UI regions reuse source footage.'
 return s,clip,imgs
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:results=list(ex.map(section,S))
P['reuse_disclosure']='Original narration and live product UI are retained. Diagrams are reconstructed. Static fictional presenters. Approximate transcript captions supplied separately; refined product-family passage retains its existing captions.'
P['verification']={'timeline':'44 continuous sections cover 0–2068.479674 seconds','motion_precision':'Source-derived estimates; not original keyframes','human_fidelity_approval':False,'render_fps':30,'render_size':[1920,1080]}
(R/'coverage.json').write_text(json.dumps(P,indent=2));(R/'plan.json').write_text(json.dumps(P,indent=2))
intro='''<!doctype html><meta charset="utf-8"><title>Full reference study</title><style>body{font:16px system-ui;background:#111b22;color:#eef3f5;max-width:1320px;margin:32px auto;padding:0 20px}h1{font-size:30px}p{line-height:1.5;color:#c9d5dc}details{border:1px solid #3d535f;border-radius:12px;margin:14px 0;padding:18px}summary{cursor:pointer;font-size:19px;font-weight:650}video{width:100%;margin-top:20px}img{width:100%;margin:10px 0}small{color:#8ec8c9}button{background:#294e59;color:white;padding:10px;border:0;border-radius:6px;margin:5px}blockquote{line-height:1.5;max-height:220px;overflow:auto}a{color:#8ed8e1}</style><h1>Full 34:28 reference study</h1><p><a href="https://www.youtube.com/watch?v=HtR5m5VjaDQ">Original YouTube reference</a></p><p>44 continuous sections. Original on the left; reconstruction on the right. Expand any section to inspect motion and three matched source-clock samples.</p><p>Rebuilt explanatory diagrams, approximate source-derived timing, static fictional presenters. Live product UI and narration reuse the source. This is a reconstruction study, with fidelity still open for review; it is not a claim of exact reproduction or new product behavior.</p><p><a href="full-reconstruction.mp4">Full reconstruction</a> · <a href="full-comparison.mp4">Full comparison</a> · <a href="transcript-captions.srt">Approximate transcript captions</a> · <a href="coverage.json">Machine-readable coverage</a> · <a href="event-atlas.html">206-anchor image atlas</a></p><button onclick="document.querySelectorAll('details').forEach(x=>x.open=true)">Expand all</button><button onclick="document.querySelectorAll('details').forEach(x=>x.open=false)">Collapse all</button>'''
parts=[intro];md=['# Full-video reconstruction and comparison','',P['reuse_disclosure'],'','The 1fps whole-source scan and prior dense samples support broad coverage. They do not prove that every micro-transition is matched. Each section has three matched frames and a short motion comparison. Full comparison preserves the complete source clock.','']
for s,clip,imgs in results:
 title=f"{s['number']+1:02}. {clock(s['source_start'])}–{clock(s['source_end'])} · {s['id']}";kind=s['kind'];eventrows=''.join('<li><b>'+clock(e['source_time'])+'</b> — '+html.escape(' / '.join(x['text'] for x in e['nearby_captions'][:2]))+'</li>' for e in EVENTS if e['scene']==s['id']);parts.append(f'<details><summary>{html.escape(title)}</summary><p><small>{kind}</small> · {html.escape(s["teaching_purpose"])}</p><p><b>Why this graphic:</b> {html.escape(REC[s["id"]]["why"]+" Motion: "+REC[s["id"]]["motion"]+" Keep stable: "+REC[s["id"]]["persist"]+" Alternative: "+REC[s["id"]]["alternative"]+". "+REC[s["id"]]["reject"])}</p><video controls preload="none" src="{data(clip)}"></video><p>Motion excerpt starts at {clock(s["comparison_clip_start"])}. Samples below: 10%, 50% and 90% through the section.</p>'+''.join(f'<img loading="lazy" src="{data(p)}">' for p in imgs)+f'<p>{html.escape(s["remaining_differences"])}</p><details><summary>Visual anchors and nearby narration (approximate)</summary><ol>{eventrows}</ol></details><details><summary>Corresponding transcript</summary><blockquote>{html.escape(s["transcript_excerpt"])}</blockquote></details></details>')
 md.extend([f'## {title}',f'- Kind: {kind}',f'- Purpose: {s["teaching_purpose"]}',f'- Events: {", ".join(clock(e) for e in s["event_anchors"])}',f'- Comparison: [motion](comparison/{s["id"]}.mp4)',f'- Limit: {s["remaining_differences"]}',''])
(R/'review.html').write_text(''.join(parts));(R/'REVIEW.md').write_text('\n'.join(md))
print('Review exported',flush=True)
