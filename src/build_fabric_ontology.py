"""Native V1 / HyperFrames adaptation of the complete interview's visual grammar."""
import json,html,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];KIT=ROOT/'vendor/editor-v1';ID='14-fabric-ontology-explained';OUT=ROOT/'videos'/ID
sys.path.insert(0,str(KIT/'components'))
from ev1_more import Comp,fr,captions,sfx
from ontology_motion import OntologyMotion

def main():
 t=json.loads((OUT/'work/timeline.json').read_text());dur=fr(t['duration']+.5);c=Comp(dur);m=OUT/'assets/media';m.mkdir(parents=True,exist_ok=True);(OUT/'out').mkdir(exist_ok=True);shutil.copytree(KIT/'assets',OUT/'assets/ev1',dirs_exist_ok=True)
 for n in ['presenters.png','binding-doc.png','entity-doc.png']:shutil.copy(ROOT/'content/fabric-ontology'/n,m/n)
 shutil.copy('/workspace/generated_images/exec-04e77403-f08a-40cd-91be-91becabbe271.png',m/'retail.png')
 c.css.append('''*{box-sizing:border-box}html,body{width:1920px;height:1080px}:root{--ev1-cap-size:38px}.world{position:absolute;inset:0;color:#fff2dc;font-family:var(--ev1-sans);background-color:#21130c;background-image:linear-gradient(#db7d2510 1px,transparent 1px),linear-gradient(90deg,#db7d2510 1px,transparent 1px),radial-gradient(ellipse at 60% 0%,#4b2414,transparent 70%);background-size:60px 60px,60px 60px,100% 100%;border:5px solid #e58a20}.brand{position:absolute;left:65px;top:28px;font-size:19px;letter-spacing:.14em;color:#e5b785}.status{position:absolute;right:65px;top:28px;font-size:18px;color:#e5b785}.panel{position:absolute;left:72px;top:140px;width:1300px;height:750px;border-radius:28px;background:#18333b;box-shadow:0 24px 55px #0004;overflow:hidden}.light{background:#f7f7f2;color:#203c42}.panel h1{margin:38px 45px 12px;font-size:46px;line-height:1.15;letter-spacing:-.035em}.subtitle{margin:0 45px;font-size:24px;color:#b7cfd0;line-height:1.5}.light .subtitle{color:#507075}.portrait{position:absolute;left:1430px;top:267px;width:410px;height:546px;border:2px solid #cda56b77;border-radius:25px;overflow:hidden;background:radial-gradient(ellipse at 50% 35%,#52665d,#172a28 80%)}.portrait:before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,#ffffff0a 1px,transparent 1px);background-size:50px 100%}.portrait img{position:absolute;bottom:0;width:200%;height:auto;max-width:none}.maya img{left:-100%}.noah img{left:0}.portrait:not(.speaker-full):not(.split-left):not(.split-right) img{width:280%}.portrait.maya:not(.speaker-full):not(.split-left):not(.split-right) img{left:-160%}.portrait.noah:not(.speaker-full):not(.split-left):not(.split-right) img{left:-20%}.who{position:absolute;bottom:16px;left:22px;font-size:22px;line-height:1.5;text-shadow:0 2px 8px #000}.who small{display:block;font-size:14px;color:#e6c394}.footer{position:absolute;left:72px;bottom:34px;font-size:17px;color:#dbb88b}.folio{position:absolute;right:72px;bottom:34px;font-size:17px;color:#dbb88b}.note{position:absolute;left:96px;top:907px;font-size:18px;color:#dfb887}.node{position:absolute;width:260px;height:120px;border:2px solid #62b6a8;border-radius:16px;background:#21464c;padding:24px;box-shadow:0 8px 24px #0003}.node strong{font-size:32px;display:block;line-height:1.1}.node small{font-size:20px;color:#b7d7d0;display:block;margin-top:10px}.node.active{border:3px solid #f5b448;background:#4c4030}.edge-label{position:absolute;font-size:22px;color:#f1ca8c;background:#18333b;padding:5px 12px;white-space:nowrap}.property{position:absolute;left:700px;top:205px;width:500px;background:#fbf6eb;color:#233b3c;border-radius:20px;padding:35px;font-size:25px;line-height:1.7}.property strong{font-size:36px;display:block;margin-bottom:18px}.property span{display:flex;justify-content:space-between;border-top:1px solid #b7c8c2;padding:8px 0}.property b{font-weight:600}.tile{position:absolute;width:330px;height:225px;border:1px solid #75a69b;border-radius:18px;padding:30px;background:#21464c}.tile b{font-size:33px;display:block;line-height:1.25}.tile p{font-size:24px;line-height:1.45;color:#bfd8d0}.big{font-size:68px;line-height:1.13;letter-spacing:-.035em;font-weight:700}.question{position:absolute;left:985px;top:275px;width:750px;line-height:1.15;font-size:73px;font-weight:700;color:#fff4df}.speaker-full{left:100px;top:130px;width:800px;height:780px}.split-left{left:110px;top:140px;width:790px;height:750px}.split-right{left:1020px;top:140px;width:790px;height:750px}.chapter{background:#d93625}.chapter .big{position:absolute;left:65px;top:235px;font-size:100px;max-width:1150px}.ev1-cap{gap:.24em}.ev1-cap .w{font-weight:700;text-transform:uppercase;text-shadow:0 3px 7px #000}''')
 c.css.append(""".m-stage{position:absolute;inset:0;transform-origin:650px 410px}.m-object{position:absolute;display:flex;align-items:center;gap:14px;border:1.5px solid #6ea99b;border-radius:18px;background:#21464c;padding:20px;color:#f7ead4;box-shadow:0 12px 25px #0002;transform-origin:50% 50%}.m-object b{display:block;font-size:26px;font-weight:600;line-height:1.2}.m-object small{display:block;font-size:19px;color:#bcd6ce;line-height:1.45;margin-top:10px}.m-icon{color:#9ccebb;flex:0 0 45px;display:flex;align-items:center}.m-svg{position:absolute;inset:0;width:1300px;height:750px;overflow:visible;pointer-events:none}.m-edge-label{position:absolute;font-size:23px;color:#f2ca8b;background:#18333b;padding:4px 10px;border-radius:8px}.panel{background-image:radial-gradient(ellipse at 45% 20%,#29505955,transparent 65%)}""")
 motion=OntologyMotion(c,t)
 shots=[];clips=[];mapping=[]
 def reveal(a,body,delay=0):
  i=c.uid('reveal');c.at(f'tl.fromTo("#{i}",{{opacity:0,y:18}},{{opacity:1,y:0,duration:.85,ease:"power3.out",immediateRender:false}},{fr(a+delay)});');return f'<div id="{i}" style="position:absolute;inset:0;opacity:0">{body}</div>'
 def portrait(who='Maya',cls=''):
  return f'<div data-safe="presenter" class="portrait {who.lower()} {cls}"><img src="assets/media/presenters.png"><div class="who">{who}<small>STATIC PRESENTER PLACEHOLDER</small></div></div>'
 def base():return '<div class="world"><div data-safe="header" class="brand">REELFACTORY / MICROSOFT FABRIC</div><div data-safe="header" class="status">ONTOLOGY · PREVIEW</div><div data-safe="footer" class="footer">Original illustrated example · synthetic dialogue · static presenter placeholders</div><div data-safe="footer" class="folio">FABRIC IQ</div>'
 def add(a,z,body,label,ref,note='',wipe=False):
  a,z=fr(a),fr(z);c.clip(a,z,base()+body+(f'<div data-safe="provenance" class="note">{note}</div>' if note else '')+'</div>',1);shots.append(dict(start=a,end=z,scene=label,reference=ref));sfx(c,a,'click_soft',.16)
  if wipe and a>0:
   i=c.uid('wipe');c.clip(a,fr(a+.5),f'<div id="{i}" style="position:absolute;inset:0;background:#eb8a16"></div>',90);c.at(f'tl.fromTo("#{i}",{{xPercent:0}},{{xPercent:100,duration:.5,ease:"power3.inOut",immediateRender:false}},{a});')
 def panel(title,body,sub='',light=False):return f'<div data-safe="content" class="panel {"light" if light else ""}"><h1>{title}</h1><div class="subtitle">{sub}</div>{body}</div>'+portrait()
 def node(name,sub,x,y,active=False):return f'<div class="node {"active" if active else ""}" style="left:{x}px;top:{y}px"><strong>{name}</strong><small>{sub}</small></div>'
 def graph(a,mode='all'):
  # Named relationships express business meaning; examples are synthetic, not query results.
  pos=[('Customer','Customer 101',65,235),('Order','Order 42',510,235),('Shipment','Shipment 17',955,235),('Warehouse','Warehouse 2',955,550)]
  body=''
  for k,(n,s,x,y) in enumerate(pos):
   active=mode=='trace' and k<3;body+=reveal(a,node(n,s,x,y,active),.2+k*.48)
  edges=[('M325 295 L510 295','places',355,252),('M955 295 L770 295','fulfills',790,252),('M1085 550 L1085 355','dispatches',1097,435)]
  for k,(path,label,x,y) in enumerate(edges):
   color='#ffc66c' if mode=='trace' and k<2 else '#67b9a6';eid=c.uid('edge');body+=f'<svg style="position:absolute;inset:0;width:1300px;height:750px"><path id="{eid}" d="{path}" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round" pathLength="1"/></svg>';c.at(f'tl.fromTo("#{eid}",{{strokeDasharray:1,strokeDashoffset:1,opacity:0}},{{strokeDashoffset:0,opacity:1,duration:.65,immediateRender:false}},{fr(a+2+k*.6)});');body+=reveal(a,f'<div class="edge-label" style="left:{x}px;top:{y}px">{label}</div>',2+k*.6)
  if mode=='trace':body+=reveal(a,'<div style="position:absolute;left:70px;top:500px;width:700px;color:#ffd17e;font-size:38px;line-height:1.5">Shipment 17 is late.<br>Customer 101 is connected.</div>',4)
  return body
 def cards(a,items):
  body=''
  for k,(name,desc) in enumerate(items):body+=reveal(a,f'<div class="tile" style="left:{60+400*k}px;top:270px"><b>{name}</b><p>{desc}</p></div>',.2+k*.65)
  return body
 for b in t['beats']:
  a,z=fr(b['start']),fr(b['end']);scene=b['scene'];mapping.append({'script_scene':scene,'output_start':a,'output_end':z,'reference_device':scene})
  if scene=='hook':
   cut=fr(a+2.2);add(a,cut,portrait('Maya','split-left')+portrait('Noah','split-right'),'Split-screen introduction','0:00–0:08')
   cut2=fr(a+5);add(cut,cut2,portrait('Noah','speaker-full')+'<div data-safe="title" class="question">Our shipment<br>is late.</div>','Host asks the business question','0:20–0:35')
   art='<img src="assets/media/retail.png" style="position:absolute;left:25px;top:180px;width:1250px;height:490px;object-fit:contain">'+reveal(cut2,'<div style="position:absolute;left:470px;top:570px;background:#e8a43a;color:#281f14;border-radius:12px;padding:15px 24px;font-size:31px;font-weight:700">Shipment 17 · LATE</div>',.4)
   add(cut2,z,panel('Which customers are affected?',art,light=True),'Business problem illustration','0:35–1:21',wipe=True)
  elif scene=='meaning':
   add(a,z,panel('A shared map of the business',motion.overview(a,z),'Microsoft Fabric IQ · ontology'),'Connected ontology overview / continuous build','1:50–3:29')
  elif scene in ['question','binding-question','trace-question']:
   q={'question':'More than<br>a diagram?','binding-question':'Where do the<br>values come from?','trace-question':'Follow the<br>late shipment.'}[scene];add(a,z,portrait('Noah','speaker-full')+f'<div data-safe="title" class="question">{q}</div>','Host full-frame question','1:34 / 11:52 / 20:21',wipe=True)
  elif scene=='entities':
   add(a,z,panel('From entity types to a particular shipment',motion.entities(a,z),'One continuous model: focus on a type, then inspect an instance.'),'Persistent entity objects morph into property inspection','4:10–5:34','Illustrative property values · not a live Fabric result')
  elif scene=='relationships':
   add(a,z,panel('Name what each connection means',motion.graph(a,z),'Relationships give the connections business meaning.'),'Verb-timed connections / selective focus','9:47–11:21','Illustrative business model')
  elif scene=='bindings':
   cut=fr(a+8)
   add(a,cut,panel('Bind meaning to actual data',motion.flow(a,cut,[('Orders','Business definition','order'),('Data binding','Connect the definition','link'),('Lakehouse','Actual order values','database')],lower='Eventhouse'),'The ontology adds context; source systems retain the values.'),'Source pipeline / curves and moving data pulses','9:47–11:21',wipe=True)
   add(cut,z,panel('Property → source column',motion.docs(cut,z),'A real example from Microsoft Learn: a Freezer entity.'),'Continuous documentation camera push','16:31–18:15','Microsoft Learn · Fabric ontology data bindings · CC BY 4.0')
  elif scene=='demo':
   cut=fr(a+1);add(a,cut,panel('', '<div class="big" style="position:absolute;left:65px;top:250px">Demo</div>').replace('class="panel "','class="panel chapter"'),'Red demo chapter card','12:51–12:56',wipe=True)
   for k,(s,e,src,title) in enumerate([(cut,fr(a+5.9),122.0,'Entity types and relationships'),(fr(a+5.9),z,224.5,'Properties linked to a data source')]):
    name=f'ontology-demo-{k}.mp4';target=m/name
    if not target.exists():subprocess.run(['ffmpeg','-v','error','-y','-ss',str(src),'-i',str(ROOT/'research/fabric-youtube/XEyq1qL147M/reference.mp4'),'-t',str(e-s),'-vf','fps=30','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-an',str(target)],check=True)
    add(s,e,panel(title,'','Guy in a Cube · real retail ontology demonstration'),'Real Fabric demo / '+title,'12:56–20:21','Guy in a Cube · Feb 2026 preview UI · source audio removed')
    c.video(s,e,'assets/media/'+name,0,3,style='left:107px;top:344px;width:1230px;height:510px;object-fit:contain;background:#fff;border-radius:12px')
    clips.append(dict(bounds=[107,344,1230,510],asset=name,output_start=s,output_end=e,source_in=src,source_out=src+e-s,source_url='https://www.youtube.com/watch?v=XEyq1qL147M',rights='FLAG: permission not established; local attributed review only'))
  elif scene=='trace':
   cut=fr(a+9);add(a,cut,panel('Trace the late shipment',motion.graph(a,cut,trace=True),'Shipment → Order → Customer'),'Follow-up question / highlight the answer path','18:15–20:21','Illustrative animation · not a live query result',wipe=True)
   body=reveal(cut,'<div class="big" style="position:absolute;left:65px;top:270px;color:#ffd17e">Customer 101</div><div style="position:absolute;left:65px;top:400px;font-size:35px;line-height:1.6">Connected through Order 42<br>to delayed Shipment 17.</div>',.1);add(cut,z,panel('Make the business question specific',body),'Enlarged conclusion from the same path','15:39–16:31','Illustrative animation · not a live query result')
  elif scene=='verify':
   cut=fr(a+7);add(a,cut,panel('Use the model as context',motion.flow(a,cut,[('Definitions','Meaning and bindings','meaning'),('Source query','Permitted data','database'),('Answer','Check trusted results','check')])),'Definitions to source to checked answer','14:19–16:31',wipe=True)
   body='';items=['Clear definitions','Correct source data','Answers checked against trusted results']
   for k,item in enumerate(items):body+=reveal(cut,f'<div style="position:absolute;left:65px;top:{225+k*125}px;width:1170px;display:flex;gap:30px;font-size:37px;line-height:1.35"><span style="color:#f4b64b">0{k+1}</span><span>{item}</span></div>',k*.7)
   add(cut,z,panel('An ontology does not guarantee correctness',body),'Best-practice list / sequential emphasis','32:37–34:04')
  elif scene=='recap':add(a,z,panel('Start small',motion.steps(a,z,[('One question','A real business problem'),('A few entities','Meaningful relationships'),('Real bindings','Connect to the sources')])),'Getting-started sequence','29:55–32:37',wipe=True)
  elif scene=='close':
   cut=fr(a+6.3);add(a,cut,panel('Model → connect → verify',motion.steps(a,cut,[('Model','Define the meaning'),('Connect','Bind real source data'),('Verify','Check the answer')])),'Best practices / final recap','32:37–34:04','Fabric ontology is in preview · check current Microsoft Learn documentation')
   add(cut,z,portrait('Maya','split-left')+portrait('Noah','split-right'),'Two-person closing / guest left, host right','34:04–34:23','learn.microsoft.com/fabric/iq/ontology/overview',wipe=True)
  words=[w for w in t['words'] if b['start']-.001<=w['s']<b['voice_end']+.001]
  for n in range(0,len(words),5):
   g=words[n:n+5];end=fr(words[n+5]['s']) if n+5<len(words) else z
   if g and end>fr(g[0]['s']):captions(c,[([(w['w'],w['s']) for w in g],end)],y='91%',z=60)
 add(fr(t['duration']),dur,portrait('Maya','split-left')+portrait('Noah','split-right'),'Closing hold','34:23–end')
 c.write(str(OUT/'index.html'),'assets/ev1/tokens.css',title='Fabric ontology / reference adaptation');p=OUT/'index.html';p.write_text(p.read_text().replace('window.__timelines["main"] = tl;','window.__timelines=window.__timelines||{};window.__timelines["main"] = tl;'));c.write_cues(str(OUT/'sfx-cues.txt'))
 for name,data in [('motion-design',motion.events),('shots',shots),('reference-mapping',mapping),('render-info',dict(duration=dur,width=1920,height=1080,fps=30,shots=len(shots))),('source-excerpts',dict(clips=clips,rights_status='unconfirmed; local attributed commentary review only'))]:(OUT/'work'/f'{name}.json').write_text(json.dumps(data,indent=2))
 (OUT/'PLAN.md').write_text('''# Fabric ontology: scene-based reference adaptation\n\n121-second original Fabric script compresses the visual structure of the complete 34:28 Databricks reference. Static generated fictional presenter placeholders are explicitly requested by the user, overriding the V1 kit no-placeholder convention. User also authorizes diagrams, original generated images, and local attributed demo excerpts; the requested reference style takes precedence over generic V1 documentary rapid-cut rules. No publication.\n\n| Material | Source | Rights / scope |\n|---|---|---|\n| Presenter pair, retail illustration | Locally generated original images | Original fictional placeholders; no impersonation |\n| Entity/relationship animations and toy values | Original HTML/SVG | Illustrative, no actual query result claimed |\n| Binding screenshot | Microsoft Learn / MicrosoftDocs fabric-docs, commit 8490a34f51fa84b896722afbd28984fe10997225 | CC BY 4.0; adapted placement; https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data |\n| Retail ontology demo | Guy in a Cube, February 2026, https://www.youtube.com/watch?v=XEyq1qL147M | FLAG: no verified reuse permission; attributed local review excerpts, not a cleared public release |\n| Style/reference analysis | User-supplied five-part Databricks video | Analysis only; no source host/guest frames or audio used in output |\n| Fonts/SFX | Vendored Editor V1 | OFL fonts; synthesized kit SFX; no music |\n| Dialogue | Original script, Kokoro local voices | Synthetic review narration; presenters are static |\n\nFacts: https://learn.microsoft.com/en-us/fabric/iq/ontology/overview (current preview). Do not transplant OntoRank, learned ontology claims, Databricks benchmarks, personal memory, actions, or scheduling. Reference correspondence: work/shots.json. Full source analysis: research/ontology-adaptation/FULL-VISUAL-BREAKDOWN.md.\n''')
 print('Built',dur,'seconds;',len(shots),'shots',flush=True)
if __name__=='__main__':main()
