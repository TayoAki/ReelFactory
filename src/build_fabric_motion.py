"""Fine edit: genuine Microsoft GIFs, safe contain framing, semantic motion and edit markers."""
import json,html,shutil,subprocess,sys
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];KIT=ROOT/'vendor/editor-v1';SRC=ROOT/'content/fabric-parker';OUT=ROOT/'videos/12-fabric-motion-refined'
sys.path.insert(0,str(KIT/'components'))
from ev1_more import Comp,captions,fr,sfx

def main():
 t=json.loads((OUT/'work/timeline.json').read_text());duration=fr(t['duration']+.4);c=Comp(duration);media=OUT/'assets/media';shutil.copytree(KIT/'assets',OUT/'assets/ev1',dirs_exist_ok=True)
 for f in SRC.glob('*.png'):shutil.copy(f,media/f.name)
 crops={'create-focus':('create-data-agent.png',(.45,.02,1,.47)),'name-focus':('name-data-agent.png',(.408,.365,.591,.582)),'ask-focus':('ask.png',(.35,.815,.86,.915)),'answer-focus':('answer-steps.png',(.30,.20,.91,.96))}
 for name,(file,box) in crops.items():
  im=Image.open(SRC/file);w,h=im.size;im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(media/(name+'.png'))
 films=[('table-selection',SRC/'data-agent-table-selection-and-search.gif'),('source-config',SRC/'motion/add-data-sources-configurations-to-data-agent.gif'),('advanced-query',SRC/'motion/data-agent-advanced-sql.gif')]
 for name,file in films:
  target=media/(name+'.mp4')
  if not target.exists():subprocess.run(['ffmpeg','-v','error','-y','-i',str(file),'-vf','fps=30,scale=1440:-2','-c:v','libx264','-crf','19','-pix_fmt','yuv420p','-an',str(target)],check=True)
 c.css.append('''*{box-sizing:border-box}html,body{width:1920px;height:1080px;font-family:var(--ev1-sans)}:root{--film-purple:#24103e;--film-bright:#b9a0ff;--ev1-cap-size:36px}.scene{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,#4a2873 0%,#24103e 55%,#130b21 100%);font-family:var(--ev1-sans);color:white}.brand{position:absolute;left:72px;top:32px;font-size:20px;letter-spacing:.13em;color:#d6c6f5}.tag{position:absolute;right:72px;top:32px;font-size:19px;color:#d6c6f5}.headline{position:absolute;left:72px;top:87px;width:1776px;height:90px;max-height:90px;font-size:52px;line-height:1.25;letter-spacing:-.035em;font-weight:700}.screen{position:absolute;background:#f7f7f7;border:2px solid #d6c6f5;border-radius:16px;box-shadow:0 22px 65px #09040b66}.screen img{width:100%;height:100%;object-fit:contain;display:block;border-radius:14px}.bottom{position:absolute;left:72px;top:1032px;font-size:16px;color:#d6c6f5}.step{position:absolute;top:290px;width:490px;height:310px;border:2px solid #9e7cd0;border-radius:30px;background:linear-gradient(145deg,#65448e,#2d1849);padding:40px}.num{font-size:25px;color:#d7c1ff}.verb{font-size:64px;font-weight:700;margin-top:34px}.detail{font-size:27px;margin-top:22px;color:#e1d4f4}.note{position:absolute;font-size:29px;line-height:1.45;color:#e1d4f4}.big{font-size:78px;line-height:1.15;font-weight:700;letter-spacing:-.035em}.label{font-size:24px;color:#d7c1ff}.badge{position:absolute;left:96px;top:904px;color:#e1d4f4;font-size:19px;line-height:1.3}.ev1-cap{gap:.22em}.cursor{position:absolute;width:42px;height:50px;filter:drop-shadow(0 2px 3px #1118)}.rail{position:absolute;left:72px;top:1018px;width:1776px;height:3px;background:#ffffff22}.progress{height:3px;background:#b9a0ff;transform-origin:0 50%}.flowline{position:absolute;height:4px;background:#b9a0ff;transform-origin:0 50%}.metric{font-size:42px;font-weight:700}.chip{padding:14px 22px;border:1px solid #9e7cd0;border-radius:28px;display:inline-block;font-size:26px}''')
 shots=[];motions=[];regions=[];cut_times=set()
 def word(b,text,default=None):return fr(next((w['s'] for w in t['words'] if b['start']<=w['s']<b['voice_end'] and w['w'].strip('.,?!').lower()==text.lower()),b['start'] if default is None else default))
 def base(title,stage='MICROSOFT FABRIC'):
  return '<div class="scene"><div data-safe="header" class="brand">REELFACTORY / FABRIC LAB</div><div data-safe="header" class="tag">'+html.escape(stage)+'</div><div data-safe="title" class="headline">'+html.escape(title)+'</div><div class="rail"><div id="'+c.uid('progress')+'" class="progress"></div></div><div data-safe="footer" class="bottom">Microsoft Learn · CC BY 4.0 · Documentation examples · Animated and annotated</div>'
 def reveal(ident,a):c.at(f'tl.fromTo("#{ident}",{{y:16,scale:.98,opacity:0}},{{y:0,scale:1,opacity:1,duration:.3,ease:"power2.out",immediateRender:false}},{a:.4f});')
 def img(file,x,y,w,h,a):
  ident=c.uid('screen');reveal(ident,a);regions.append({'file':file,'x':x,'y':y,'width':w,'height':h,'fit':'contain','image_scale':'1; wrapper reveal 0.98 → 1, no source clipping'})
  return f'<div id="{ident}" data-safe="content" class="screen" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="assets/media/{file}"></div>'
 def add(a,z,body,label,source):
  if a not in cut_times:sfx(c,a,'click_soft',.30);cut_times.add(a)
  c.clip(a,z,body+'</div>',z=1);shots.append({'start':fr(a),'end':fr(z),'scene':label,'evidence':source})
  # Progress line uses absolute film time; captions have their own unobstructed band.
  ident=c.uid('playhead');c.clip(a,z,f'<div style="position:absolute;left:72px;top:1018px;width:1776px;height:3px;background:#ffffff22"><div id="{ident}" style="height:3px;background:#b9a0ff;transform-origin:0 50%"></div></div>',z=55)
  c.at(f'tl.fromTo("#{ident}",{{scaleX:{a/duration:.6f}}},{{scaleX:{z/duration:.6f},duration:{z-a:.4f},ease:"none",immediateRender:false}},{a:.4f});')
 def ring(a,z,x,y,w,h):
  ident=c.uid('ring');c.clip(a,z,f'<div id="{ident}" data-safe="annotation" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border:4px solid #9d75e0;border-radius:10px;box-shadow:0 0 0 5px #b9a0ff33"></div>',z=9);c.at(f'tl.fromTo("#{ident}",{{opacity:0,scale:1.04}},{{opacity:1,scale:1,duration:.18,immediateRender:false}},{a:.4f});');sfx(c,a,'click_soft',.32)
 def cursor(a,z,points):
  ident=c.uid('cursor');svg='<svg viewBox="0 0 42 50"><path d="M5 3L34 29L21 31L17 46L5 3Z" fill="white" stroke="#2b1746" stroke-width="3"/></svg>'
  c.clip(a,z,f'<div id="{ident}" class="cursor" style="left:0;top:0">{svg}</div>',z=10)
  c.at(f'gsap.set("#{ident}",{{x:{points[0][0]},y:{points[0][1]}}});')
  for i,p in enumerate(points[1:]):c.at(f'tl.to("#{ident}",{{x:{p[0]},y:{p[1]},duration:.65,ease:"power2.inOut"}},{a+.2+i*.95:.4f});')
 def film(a,z,name,start,x=240,y=190,w=1440,h=700):
  c.video(a,z,f'assets/media/{name}.mp4',start,3,style=f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:contain;background:#f7f7f7;border-radius:14px');motions.append({'start':a,'end':z,'asset':name+'.mp4','source_start':start,'type':'actual Microsoft animated screen demo','bounds':[x,y,w,h]})
 def pills(a):
  body=''
  for i,(verb,detail) in enumerate([('Create','A Fabric data agent'),('Choose','Your source + tables'),('Verify','The question + query')]):
   ident=c.uid('step');body+=f'<div id="{ident}" data-safe="content" class="step" style="left:{150+i*555}px"><div class="num">0{i+1}</div><div class="verb">{verb}</div><div class="detail">{detail}</div></div>';reveal(ident,a+.1+i*.35)
   if i<2:
    lid=c.uid('link');body+=f'<div id="{lid}" class="flowline" style="left:{650+i*555}px;top:445px;width:45px"></div>';c.at(f'tl.fromTo("#{lid}",{{scaleX:0}},{{scaleX:1,duration:.35,immediateRender:false}},{a+.45+i*.35:.4f});')
  return body
 for b in t['beats']:
  a,z=fr(b['start']),fr(b['end']);scene=b['scene']
  if scene=='hook':
   title=base('Ask your Fabric data. Inspect the answer.')
   lines=''
   for i,(label,delay) in enumerate([('A question.',.3),('An answer.',1.2),('The query.',2.1)]):
    ident=c.uid('hook');lines+=f'<div id="{ident}" data-safe="content" class="big" style="position:absolute;left:96px;top:{270+i*120}px;width:560px;color:{"#b9a0ff" if i==2 else "white"}">{label}</div>';reveal(ident,a+delay)
   add(a,z,title+lines+img('answer-focus.png',780,195,1035,680,a)+'<div data-safe="provenance" class="badge">Walkthrough of Microsoft’s documented example</div>','Staggered hook + finished answer','answer-steps.png')
  elif scene=='preview':
   mid=word(b,'answer',a+3.5);add(a,mid,base('First, see the question.','DOCUMENTED EXAMPLE')+img('ask.png',240,195,1440,680,a),'Full question orientation','ask.png')
   add(mid,z,base('Then inspect how the answer was produced.','MICROSOFT MOTION DEMO')+'<div data-safe="provenance" class="badge">Advanced NL2SQL example · preview runtime · separate Microsoft sample</div>','Moving result-to-query preview','data-agent-advanced-sql.gif');film(mid,z,'advanced-query',9.5)
  elif scene=='steps':add(a,z,base('Three steps. One checkable result.')+pills(a)+'<div data-safe="content" class="note" style="left:150px;top:690px;width:1600px">Setup: supported paid capacity · required tenant settings · read access</div>','Linked three-step system','Original teaching graphic; Microsoft prerequisites')
  elif scene=='create':
   search=word(b,'search',a+1.9);name=word(b,'give',z-1.2)
   add(a,search,base('01 / Start in your Fabric workspace')+img('create-data-agent.png',240,195,1440,680,a),'Full app, New Item visible','create-data-agent.png');cursor(a,search,[(560,480),(350,245)]);ring(a+.7,search,300,230,155,55)
   add(search,name,base('Search for Fabric data agent.')+img('create-focus.png',340,195,1240,680,search),'Search and complete card, fully contained','create-data-agent.png');cursor(search,name,[(1250,390),(660,540)])
   add(name,z,base('Give your agent a name.')+img('name-focus.png',450,195,1020,680,name),'Complete naming dialog','name-data-agent.png')
  elif scene=='sources':
   add(a,z,base('02 / Choose your source','ONELAKE CATALOG')+img('change-datasource.png',650,195,1120,680,a)+'<div data-safe="content" class="note" style="left:100px;top:300px;width:490px;font-size:38px;line-height:1.7">Lakehouse<br>Warehouse<br>Power BI<br>semantic model</div>','Catalog with guided filter highlight','change-datasource.png');cursor(a+.6,z,[(1100,470),(1550,280),(1200,420)]);ring(a+1.5,a+3.3,1495,244,130,42)
  elif scene=='tables':
   mid=fr(a+3.5);add(a,mid,base('Choose the tables the agent can use.','MICROSOFT MOTION DEMO')+'<div data-safe="provenance" class="badge">AdventureWorks example · Microsoft documentation recording</div>','Table-selection recording, full app','data-agent-table-selection-and-search.gif');film(a,mid,'table-selection',10.5)
   add(mid,z,base('Watch the Explorer checkboxes.','MICROSOFT MOTION DEMO')+'<div data-safe="provenance" class="badge">Same recording · enlarged Explorer view</div>','Moving Explorer detail','same source recording; spatial crop preserves full table tree')
   # Actual recording, source crop done offline; no CSS overflow or fake checkbox animation.
   target=media/'table-detail.mp4'
   if not target.exists():subprocess.run(['ffmpeg','-v','error','-y','-i',str(media/'table-selection.mp4'),'-vf','crop=374:680:62:100,scale=700:-2','-c:v','libx264','-crf','19','-pix_fmt','yuv420p',str(target)],check=True)
   film(mid,z,'table-detail',14,x=240,y=195,w=650,h=690)
   c.clip(mid,z,'<div data-safe="content" class="note" style="left:1030px;top:340px;width:700px;font-size:42px;line-height:1.6">Choose the relevant tables.<br><br>Only selected tables<br>are available to the agent.</div>',z=4)
  elif scene=='instructions':
   mid=fr(a+2.4);add(a,mid,base('Define terms. Give source-specific guidance.','MICROSOFT MOTION DEMO')+'<div data-safe="provenance" class="badge">Source configuration in Microsoft’s ontology example · separate sample</div>','Actual source-instructions panel opening','add-data-sources-configurations-to-data-agent.gif');film(a,mid,'source-config',3.8)
   target=media/'config-detail.mp4'
   if not target.exists():subprocess.run(['ffmpeg','-v','error','-y','-i',str(media/'source-config.mp4'),'-vf','crop=740:650:390:150,scale=1440:-2','-c:v','libx264','-crf','19','-pix_fmt','yuv420p',str(target)],check=True)
   add(mid,z,base('Show the source-specific instructions.','MICROSOFT MOTION DEMO')+'<div data-safe="provenance" class="badge">Same recording · source instructions panel enlarged</div>','Moving instructions panel detail','same Microsoft source-configuration recording');film(mid,z,'config-detail',6.2,x=240,y=215,w=1440,h=650)
  elif scene=='ask':
   mid=word(b,'example',a+2.5);add(a,mid,base('03 / Ask a concrete question.')+img('ask.png',240,195,1440,680,a),'Full application orientation','ask.png')
   add(mid,z,base('Make the question specific.')+img('ask-focus.png',200,310,1520,310,mid)+'<div data-safe="content" class="note" style="left:220px;top:700px;width:1480px">Microsoft’s example: users who played Contoso games<br>and users who purchased items in those games.</div>','Complete prompt enlarged with no clipped text','ask.png');cursor(mid,z,[(1450,580),(1200,480)])
  elif scene=='inspect':
   add(a,z,base('Expand the steps. Inspect the generated query.','03 / VERIFY')+img('answer-focus.png',650,195,1120,690,a)+'<div data-safe="content" class="note" style="left:100px;top:315px;width:470px;font-size:37px">Check the filters.<br><br>Check the tables.<br><br>Check the answer.</div>','Query inspection with word-timed guides','answer-steps.png')
   # Match source geometry with contain scaling; convert source crop pixel coordinates to film pixels.
   iw,ih=Image.open(media/'answer-focus.png').size;scale=min(1120/iw,690/ih);ox=650+(1120-iw*scale)/2;oy=195+(690-ih*scale)/2
   original=Image.open(SRC/'answer-steps.png');ow,oh=original.size
   for key,box in [('filters',(.372,.528,.625,.552)),('tables',(.372,.51,.447,.532)),('answer',(.347,.266,.83,.313))]:
    on=word(b,key,z-1);l,top,r,bot=box;x=ox+(l-.30)*ow*scale;y=oy+(top-.20)*oh*scale;w=(r-l)*ow*scale;h=(bot-top)*oh*scale;ring(on,min(z,on+.85),round(x),round(y),round(w),round(h))
  elif scene=='limits':
   body=base('Retrieving a number does not prove its cause.')
   for i,(label,question,action) in enumerate([('STRUCTURED ANSWER','“What were<br>total sales?”','Retrieve + verify'),('NEEDS MORE EVIDENCE','“Why did<br>sales change?”','Investigate causes')]):
    ident=c.uid('contrast');body+=f'<div id="{ident}" data-safe="content" style="position:absolute;left:{140+i*900}px;top:280px;width:740px;height:450px"><div class="label">{label}</div><div class="big" style="font-size:63px;margin-top:42px">{question}</div><div class="chip" style="margin-top:36px">{action}</div></div>';reveal(ident,a+.2+i*1.2)
   add(a,z,body,'Staggered contrast; retrieval versus causality','Microsoft Ask questions guidance; original teaching questions')
  else:add(a,z,base('Your first Fabric data agent.')+pills(a)+'<div data-safe="content" class="note" style="left:150px;top:680px;width:1600px;font-size:36px">Start with one question you can check.<br>Test more questions before you publish.</div>','Resolve to the same three-step system','Original system graphic; Microsoft publishing guidance')
  words=[w for w in t['words'] if b['start']-.001<=w['s']<b['voice_end']+.001]
  # Four/five-word captions protect margins; each group ends at the next spoken group.
  for n in range(0,len(words),5):
   group=words[n:n+5];end=fr(words[n+5]['s']) if n+5<len(words) else z
   if group and end>fr(group[0]['s']):captions(c,[([(w['w'],w['s']) for w in group],end)],y='91%',z=60)
 c.clip(fr(t['duration']),duration,'<div class="scene"></div>',z=1);c.write(str(OUT/'index.html'),'assets/ev1/tokens.css',title='Microsoft Fabric / refined motion edit');p=OUT/'index.html';p.write_text(p.read_text().replace('window.__timelines["main"] = tl;','window.__timelines=window.__timelines||{};window.__timelines["main"] = tl;'))
 c.write_cues(str(OUT/'sfx-cues.txt'));(OUT/'work/shots.json').write_text(json.dumps(shots,indent=2));(OUT/'work/render-info.json').write_text(json.dumps({'duration':duration,'width':1920,'height':1080,'fps':30,'shots':len(shots)},indent=2));(OUT/'work/motion-and-framing.json').write_text(json.dumps({'motion':motions,'regions':regions,'safe_layout':{'content':[72,190,1848,900],'caption_band':[72,950,1848,1005],'footer':[72,1030,1848,1060]},'genuine_screen_motion_seconds':round(sum(m['end']-m['start'] for m in motions),2)},indent=2))
 (OUT/'PLAN.md').write_text((ROOT/'videos/11-fabric-data-agent/PLAN.md').read_text()+'''\n\n## Fine-edit revision\nThree distinct Microsoft GIF sources provide actual moving UI: table selection (AdventureWorks), source configuration (HawaiianTourismInsightsAgent / ontology-context example), and Advanced NL2SQL query inspection (preview runtime). They are separate examples, explicitly identified on screen; no claim that one dataset/session connects them. The advanced runtime clip is visual illustration, not a promise that preview-only features are enabled by default. Source pages: https://learn.microsoft.com/en-us/fabric/data-science/data-agent-ontology-sources and https://learn.microsoft.com/en-us/fabric/data-science/data-agent-sql-sources . Retrieved GIF URLs are retained in the motion manifest. All Microsoft media uses CC BY 4.0 attribution.\n\nFine editing: semantic cut points, moving source footage, guided cursor overlays (editorial annotation, not actual clicks), entrance easing on wrappers, timed highlights, linked step cards, progress rail, and smaller caption groups. Images use object-fit:contain with no zooming inside a clipped viewport. Source crops isolate complete relevant controls; full-app views establish orientation first. The script and voice are retained from the previous cut.\n\nThe prior version is preserved in ../11-fabric-data-agent. Bounds audit: out/frame-fit-audit.json. Rendered sample sheet: out/snaps/contact-sheet.jpg.\n''')
 print('Built motion refinement:',len(shots),'shots;',round(sum(m['end']-m['start'] for m in motions),1),'seconds genuine UI footage',flush=True)
if __name__=='__main__':main()
