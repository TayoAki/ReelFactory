"""Original commentary on a concrete creator demo; local rights-flagged review cut."""
import json,html,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];KIT=ROOT/'vendor/editor-v1';ID='13-fabric-youtube-case-study';OUT=ROOT/'videos'/ID;SOURCE=ROOT/'research/fabric-youtube/mFoSVcj6tLw';VIDEO=SOURCE/'reference.mp4'
sys.path.insert(0,str(KIT/'components'))
from ev1_more import Comp,captions,fr,sfx

def main():
 t=json.loads((OUT/'work/timeline.json').read_text());duration=fr(t['duration']+.4);c=Comp(duration);media=OUT/'assets/media';shutil.copytree(KIT/'assets',OUT/'assets/ev1',dirs_exist_ok=True);(OUT/'out').mkdir(exist_ok=True)
 c.css.append('''*{box-sizing:border-box}html,body{width:1920px;height:1080px;font-family:var(--ev1-sans)}:root{--ev1-cap-size:37px}.scene{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,#4a2873,#24103e 55%,#130b21);color:white}.brand{position:absolute;left:72px;top:27px;font-size:20px;letter-spacing:.12em;color:#d6c6f5}.tag{position:absolute;right:72px;top:27px;font-size:18px;color:#d6c6f5}.title{position:absolute;left:72px;top:73px;width:1776px;height:62px;font-size:43px;line-height:1.3;font-weight:700;letter-spacing:-.025em}.credit{position:absolute;left:72px;top:1033px;font-size:16px;color:#d6c6f5}.provenance{position:absolute;left:96px;top:912px;font-size:18px;color:#d6c6f5}.card{position:absolute;left:150px;top:275px;width:1620px;height:500px;border:2px solid #9e7cd0;border-radius:30px;padding:65px;background:linear-gradient(145deg,#65448e,#2d1849)}.big{font-size:76px;line-height:1.22;letter-spacing:-.035em;font-weight:700}.small{font-size:32px;line-height:1.55;color:#e1d4f4}.label{font-size:24px;color:#d7c1ff;letter-spacing:.06em}.step{position:absolute;top:300px;width:490px;height:340px;border:2px solid #9e7cd0;border-radius:28px;padding:40px;background:linear-gradient(145deg,#65448e,#2d1849)}.verb{font-size:58px;font-weight:700;margin-top:45px}.detail{font-size:28px;line-height:1.4;color:#e1d4f4;margin-top:25px}.ev1-cap{gap:.22em}''')
 shots=[];clips=[]
 def base(title,source=False):return '<div class="scene"><div data-safe="header" class="brand">REELFACTORY / FABRIC LAB</div><div data-safe="header" class="tag">DEMO ANALYSIS</div><div data-safe="title" class="title">'+html.escape(title)+'</div><div data-safe="footer" class="credit">Source: Guy in a Cube · Marthe Moengen · “Build a Microsoft Fabric Data Agent” · May 15, 2025</div>'
 def add(a,z,title,body,label,source='Original explanation of the cited demo'):
  if z<=a:return
  c.clip(a,z,base(title)+body+'</div>',z=1);shots.append({'start':fr(a),'end':fr(z),'scene':label,'evidence':source});sfx(c,a,'click_soft',.26)
  pid=c.uid('progress');c.clip(a,z,f'<div style="position:absolute;left:72px;top:1018px;width:1776px;height:3px;background:#ffffff22"><div id="{pid}" style="height:3px;background:#b9a0ff;transform-origin:0 50%"></div></div>',z=55);c.at(f'tl.fromTo("#{pid}",{{scaleX:{a/duration:.6f}}},{{scaleX:{z/duration:.6f},duration:{z-a:.4f},ease:"none",immediateRender:false}},{a:.4f});')
 def reveal(i,a):c.at(f'tl.fromTo("#{i}",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.3,ease:"power2.out",immediateRender:false}},{a:.4f});')
 def card(a,heading,sub):
  i=c.uid('card');reveal(i,a);return f'<div id="{i}" data-safe="content" class="card"><div class="big">{heading}</div><div class="small" style="margin-top:45px">{sub}</div></div>'
 def film(a,z,source_start,title,label):
  name=f'demo-{len(clips)+1:02}.mp4';target=media/name
  if not target.exists():subprocess.run(['ffmpeg','-v','error','-y','-ss',str(source_start),'-i',str(VIDEO),'-t',str(z-a),'-vf','fps=30','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-an',str(target)],check=True)
  add(a,z,title,'<div data-safe="provenance" class="provenance">Creator’s demonstration · original screen footage · our explanatory narration</div>',label,f'https://www.youtube.com/watch?v=mFoSVcj6tLw&t={int(source_start)}s')
  vid=c.video(a,z,'assets/media/'+name,0,3,style='left:280px;top:140px;width:1360px;height:765px;object-fit:contain;border-radius:12px;background:#f8f8f8;transform-origin:50% 50%');c.at(f'tl.fromTo("#{vid}",{{scale:.985}},{{scale:1,duration:.25,ease:"power2.out",immediateRender:false}},{a:.4f});')
  clips.append({'asset':name,'output_start':a,'output_end':z,'source_in':source_start,'source_out':round(source_start+z-a,4),'source_url':'https://www.youtube.com/watch?v=mFoSVcj6tLw','uploader':'Guy in a Cube','presenter':'Marthe Moengen','source_date':'2025-05-15','source_audio':'removed; original local review narration','frame':'whole 16:9 source frame, contain fit; no source crop','rights':'FLAG: video-specific reuse license and permission not confirmed; local commentary review only'})
 def steps(a,labels):
  body=''
  for k,(name,detail) in enumerate(labels):
   i=c.uid('step');reveal(i,a+.1+k*.35);body+=f'<div id="{i}" data-safe="content" class="step" style="left:{150+555*k}px"><div class="label">0{k+1}</div><div class="verb">{name}</div><div class="detail">{detail}</div></div>'
  return body
 for b in t['beats']:
  a,z=fr(b['start']),fr(b['end']);scene=b['scene']
  if scene=='hook':
   cut=min(z,fr(a+4.5));film(a,cut,331.2,'The answer came back. Then came the check.','Cold open: agent and report compared')
   add(cut,z,'A convincing answer still needs a check.',card(cut,'Watch the validation.','A concrete lesson from a real Microsoft Fabric demonstration.'),'Original lesson framing')
  elif scene=='case':
   cut=min(z,fr(a+4.5));film(a,cut,135,'A real use case: YouTube analytics','Connected sources and selected tables')
   add(cut,z,'Two sources. Two different questions.',steps(cut,[('Videos','Video statistics in a<br>Power BI semantic model'),('Comments','Comment sentiment<br>in a lakehouse'),('Context','Tell the agent which<br>source to use')]),'Source-routing mental model')
  elif scene=='definitions':
   cut=min(z,fr(a+4.8));film(a,cut,224.3,'Define what the fields actually mean.','Actual business-definition instructions')
   add(cut,z,'Same word. Different business meaning.',card(cut,'Comment likes ≠ video likes','The demo explains the field meanings and routes comment questions to the comment source.'),'Concrete semantic trap explained')
  elif scene=='question':film(a,z,290,'Test a question with a checkable answer.','Question: total views on January 10, 2025')
  elif scene=='query':
   cut=min(z,fr(a+3.7));film(a,cut,299,'Open the query behind the answer.','Generated DAX expanded')
   film(cut,z,320,'Compare with the same Power BI model.','Build the independent report table')
  elif scene=='precision':
   cut=min(z,fr(a+4.9));film(a,cut,331.2,'The presenter notices rounding.','Actual chat-to-report precision comparison')
   add(cut,z,'A precision issue to evaluate.',card(cut,'Rounded summary ≠ exact count','Decide which level of precision the question requires.<br>This observation alone does not prove an invented answer.'),'Interpret the evidence carefully')
  elif scene=='second':
   cut=fr(a+(z-a)*.5);film(a,cut,345,'Second test: a title containing “Fabric”.','Filtered top-video question and answer')
   film(cut,z,359,'Check the filter, ranking and report result.','Power BI report validates the filtered ranking')
  else:add(a,z,'Use this method for your first Fabric agent.',steps(a,[('Define','Business terms<br>and source meanings'),('Inspect','Generated query<br>and filters'),('Compare','A trusted result<br>before sharing')]),'Reusable method drawn from the case')
  words=[w for w in t['words'] if b['start']-.001<=w['s']<b['voice_end']+.001]
  for n in range(0,len(words),5):
   group=words[n:n+5];end=fr(words[n+5]['s']) if n+5<len(words) else z
   if group and end>fr(group[0]['s']):captions(c,[([(w['w'],w['s']) for w in group],end)],y='91%',z=60)
 c.clip(fr(t['duration']),duration,'<div class="scene"></div>',z=1);c.write(str(OUT/'index.html'),'assets/ev1/tokens.css',title='Microsoft Fabric / what a real demo teaches');p=OUT/'index.html';p.write_text(p.read_text().replace('window.__timelines["main"] = tl;','window.__timelines=window.__timelines||{};window.__timelines["main"] = tl;'))
 c.write_cues(str(OUT/'sfx-cues.txt'));(OUT/'work/shots.json').write_text(json.dumps(shots,indent=2));(OUT/'work/render-info.json').write_text(json.dumps({'duration':duration,'width':1920,'height':1080,'fps':30,'shots':len(shots)},indent=2));(OUT/'work/source-excerpts.json').write_text(json.dumps({'clips':clips,'total_excerpt_seconds':round(sum(v['output_end']-v['output_start'] for v in clips),2),'rights_status':'unconfirmed; local commentary review, not a cleared public release'},indent=2))
 (OUT/'PLAN.md').write_text((ROOT/'research/fabric-youtube/CONTENT-BRIEF.md').read_text()+'''\n\n## Local cut\nOriginal script, local synthetic Kokoro review voice, actual source screen excerpts muted, original explanatory cards and V1 captions/cues. This is analysis of Guy in a Cube's demo, not a claimed Fabric execution by us. The creator's observed rounding is described without inventing exact values or claiming hallucination. No guarantee about current product availability is inferred from this May 2025 UI. Exact source and output in/out points are in work/source-excerpts.json. Whole source frames are retained. No publishing or permission outreach.\n''')
 print('Built',duration,'seconds;',len(shots),'shots;',round(sum(v['output_end']-v['output_start'] for v in clips),1),'seconds source footage',flush=True)
if __name__=='__main__':main()
