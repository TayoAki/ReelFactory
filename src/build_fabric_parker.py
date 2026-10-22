"""Parker-informed widescreen Fabric tutorial, using attributed Microsoft source screens."""
import html,json,shutil,sys,subprocess
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]; KIT=ROOT/'vendor/editor-v1'; ID='11-fabric-data-agent'; OUT=ROOT/'videos'/ID; SRC=ROOT/'content/fabric-parker'
sys.path.insert(0,str(KIT/'components'))
from ev1_more import Comp,captions,fr,sfx

def main():
 t=json.loads((OUT/'work/timeline.json').read_text());duration=fr(t['duration']+.4);c=Comp(duration);media=OUT/'assets/media';shutil.copytree(KIT/'assets',OUT/'assets/ev1',dirs_exist_ok=True)
 for f in SRC.glob('*.png'):shutil.copy(f,media/f.name)
 # Source-provided moving screen demonstration, transcoded for frame-accurate seeking.
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(SRC/'data-agent-table-selection-and-search.gif'),'-vf','fps=30,scale=1440:-2','-c:v','libx264','-crf','19','-pix_fmt','yuv420p','-an',str(media/'table-selection.mp4')],check=True)
 # Crops enlarge the actual source pixels, retaining their content rather than retyping a fake UI.
 crops={'create-focus':('create-data-agent.png',(.45,.02,1,.47)), 'name-focus':('name-data-agent.png',(.34,.28,.72,.66)), 'ask-focus':('ask.png',(.29,.76,.89,.92)), 'answer-focus':('answer-steps.png',(.30,.20,.91,.96)), 'explorer-focus':('select-adding-instructions.png',(0,.03,.48,.68))}
 for name,(file,box) in crops.items():
  im=Image.open(SRC/file);w,h=im.size;im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(media/(name+'.png'))
 c.css.append('''html,body{width:1920px;height:1080px}:root{--film-purple:#24103e;--film-bright:#b9a0ff;--film-violet:#7550bb;--ev1-cap-size:36px}.scene{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,#4a2873 0%,var(--film-purple) 55%,#130b21 100%);font-family:var(--ev1-sans);color:white}.brand{position:absolute;left:70px;top:34px;font-size:20px;letter-spacing:.13em;color:#d6c6f5}.tag{position:absolute;right:70px;top:34px;font-size:19px;color:#d6c6f5}.headline{position:absolute;left:72px;top:86px;font-size:55px;line-height:1.1;letter-spacing:-.035em;font-weight:700}.screen{position:absolute;background:white;border:2px solid #d6c6f5;border-radius:16px;overflow:hidden;box-shadow:0 24px 80px #09040b88}.screen img{width:100%;height:100%;object-fit:contain;display:block}.bottom{position:absolute;left:72px;bottom:22px;font-size:17px;color:#d6c6f5}.pill{position:absolute;top:280px;width:490px;height:330px;border:2px solid #9e7cd0;border-radius:30px;background:linear-gradient(145deg,#65448e,#2d1849);padding:40px;box-sizing:border-box}.num{font-size:25px;color:#d7c1ff}.verb{font-size:65px;font-weight:700;margin-top:38px}.detail{font-size:27px;margin-top:22px;color:#e1d4f4}.note{position:absolute;font-size:27px;color:#e1d4f4;line-height:1.5}.ribbon{position:absolute;left:80px;top:870px;font-size:24px;color:#e1d4f4}.marker{position:absolute;border:5px solid #b9a0ff;border-radius:12px;box-shadow:0 0 0 9999px #11092033;pointer-events:none}.big{font-size:82px;font-weight:700;letter-spacing:-.04em;line-height:1.12}.chip{display:inline-block;border:1px solid #a98bcf;padding:16px 26px;border-radius:40px;font-size:27px;margin:15px 15px 0 0}.ev1-cap{gap:.23em}.ev1-cap .w{text-shadow:0 2px 7px #000}''')
 shots=[]
 def base(title,stage='MICROSOFT FABRIC'):
  return '<div class="scene"><div class="brand">REELFACTORY / FABRIC LAB</div><div class="tag">'+stage+'</div><div class="headline">'+html.escape(title)+'</div><div class="bottom">Microsoft Learn · CC BY 4.0 · Source screens, enlarged and annotated</div>'
 def image(file,x,y,w,h,ident=''):
  return f'<div class="screen" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img '+(f'id="{ident}" ' if ident else '')+f'src="assets/media/{file}"></div>'
 def add(a,z,body,label,source):
  cid=c.clip(a,z,body+'</div>',z=1);shots.append({'start':a,'end':z,'scene':label,'evidence':source});return cid
 def move(ident,a,z,scale=1.055):
  c.at(f'tl.fromTo("#{ident}",{{scale:1}},{{scale:{scale},duration:{max(.2,z-a):.4f},ease:"none",immediateRender:false}},{a:.4f});')
 def pills(a,close=False):
  body=''
  for i,(verb,detail) in enumerate([('Create','A Fabric data agent'),('Choose','Your source + tables'),('Verify','The question + query')]):
   ident=c.uid('pill');body+=f'<div id="{ident}" class="pill" style="left:{150+i*555}px"><div class="num">0{i+1}</div><div class="verb">{verb}</div><div class="detail">{detail}</div></div>'
   c.at(f'tl.fromTo("#{ident}",{{y:30,opacity:0}},{{y:0,opacity:1,duration:.35,immediateRender:false}},{a+.1+i*.28:.4f});')
  return body
 for b in t['beats']:
  a,z=fr(b['start']),fr(b['end']);scene=b['scene'];sfx(c,a,'click_soft',.45)
  if scene=='hook':
   ident=c.uid('opening');body=base('Ask your Fabric data. Inspect the answer.')+image('answer-steps.png',760,200,1080,670,ident)+'<div style="position:absolute;left:85px;top:290px;width:610px" class="big">A question.<br>An answer.<br><span style="color:#b9a0ff">The query.</span></div><div class="ribbon">A walkthrough using Microsoft’s documented example</div>';move(ident,a,z);add(a,z,body,'Problem + finished-result teaser','answer-steps.png')
  elif scene=='preview':
   mid=fr(a+(z-a)*.45);add(a,mid,base('First, see the result.','DOCUMENTED EXAMPLE')+image('ask.png',240,190,1440,740),'Question preview','ask.png');ident=c.uid('answer');add(mid,z,base('An answer you can inspect.','DOCUMENTED EXAMPLE')+image('answer-focus.png',450,180,1020,750,ident),'Answer + query preview','answer-steps.png');move(ident,mid,z,1.025)
  elif scene=='steps':add(a,z,base('Three steps. One checkable result.')+pills(a)+'<div class="note" style="left:150px;top:700px">Setup: supported paid capacity · required tenant settings · read access to your data</div>','Three-step process graphic','Microsoft Learn prerequisites and workflow')
  elif scene=='create':
   mid=fr(next((w['s'] for w in t['words'] if a<=w['s']<z and w['w'].lower()=='give'),a+(z-a)*.7));add(a,mid,base('01 / Create your Fabric data agent')+image('create-focus.png',340,185,1240,715),'Locate Fabric data agent','create-data-agent.png');add(mid,z,base('Give the agent a name.')+image('name-focus.png',400,190,1120,710),'Name the agent','name-data-agent.png')
  elif scene=='sources':add(a,z,base('02 / Choose your source','ONELAKE CATALOG')+image('change-datasource.png',640,180,1130,710)+'<div class="note" style="left:100px;top:300px;font-size:40px;line-height:2">Lakehouse<br>Warehouse<br>Power BI<br>semantic model</div>','Choose source from catalog','change-datasource.png')
  elif scene=='tables':
   add(a,z,base('Choose the tables the agent can use.','02 / CHOOSE')+'<div class="screen" style="left:240px;top:190px;width:1440px;height:720px"></div>','Moving table-selection demonstration','Microsoft documentation animated GIF')
   length=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(media/'table-selection.mp4')]))
   offset=0.;pos=a
   while pos<z-.01:
    end=min(z,pos+length);c.video(pos,end,'assets/media/table-selection.mp4',0,3,style='left:240px;top:190px;width:1440px;height:720px;object-fit:contain;border-radius:14px');pos=end
  elif scene=='instructions':add(a,z,base('Define your business terms.','02 / CHOOSE')+image('explorer-focus.png',90,190,1000,710)+'<div class="note" style="left:1170px;top:290px;width:620px;font-size:42px">“Which source should answer this question?”<br><br>“What do our business terms mean?”</div>','Instructions focus with original teaching prompts','select-adding-instructions.png; side prompts are original examples')
  elif scene=='ask':add(a,z,base('03 / Ask a concrete question.')+image('ask.png',160,180,1600,610)+image('ask-focus.png',280,775,1360,112),'Full app orientation → enlarged actual question','ask.png')
  elif scene=='inspect':
   ident=c.uid('inspect');add(a,z,base('Expand the steps. Inspect the generated query.','03 / VERIFY')+image('answer-focus.png',460,175,1000,745,ident)+'<div class="note" style="left:80px;top:340px;width:330px;font-size:36px">Filters<br><br>Tables<br><br>Answer</div>','Read the actual generated-query evidence','answer-steps.png');move(ident,a,z,1.035)
   for word,box in [('filters',(558,503,780,47)),('tables',(558,480,200,36)),('answer',(520,242,825,78))]:
    onset=next((w['s'] for w in t['words'] if a<=w['s']<z and w['w'].strip('.,').lower()==word),z-.6)
    x,y,w,h=box;c.clip(fr(onset),min(z,fr(onset+1)),f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border:4px solid #7550bb;border-radius:6px;box-shadow:0 0 0 5px #b9a0ff44"></div>',z=8)
  elif scene=='limits':add(a,z,base('Retrieving a number does not prove its cause.')+'<div style="position:absolute;left:140px;top:260px;width:740px"><div class="num">STRUCTURED ANSWER</div><div class="big" style="margin-top:35px;font-size:64px">“What were<br>total sales?”</div><div class="chip">Retrieve + verify</div></div><div style="position:absolute;left:1040px;top:260px;width:740px"><div class="num">NEEDS MORE EVIDENCE</div><div class="big" style="margin-top:35px;font-size:64px">“Why did<br>sales change?”</div><div class="chip">Investigate causes</div></div>','Useful limitation and concrete contrast','Microsoft Learn Ask questions section; original illustrative question wording')
  else:add(a,z,base('Your first Fabric data agent.')+pills(a)+'<div class="note" style="left:150px;top:700px;font-size:36px">Start with one question you can check.<br>Test more questions before you publish.</div>','Return to the reusable system','Microsoft Learn Publish and share section')
  words=[w for w in t['words'] if b['start']-.001<=w['s']<b['voice_end']+.001]
  for n in range(0,len(words),7):
   group=words[n:n+7];end=fr(words[n+7]['s']) if n+7<len(words) else z
   if group and end>fr(group[0]['s']):captions(c,[([(w['w'],w['s']) for w in group],end)],y='92%',z=60)
 c.clip(fr(t['duration']),duration,'<div class="scene"></div>',z=1)
 c.write(str(OUT/'index.html'),'assets/ev1/tokens.css',title='Microsoft Fabric data agent / three-step walkthrough')
 p=OUT/'index.html';p.write_text(p.read_text().replace('window.__timelines["main"] = tl;','window.__timelines=window.__timelines||{};window.__timelines["main"] = tl;'))
 c.write_cues(str(OUT/'sfx-cues.txt'));(OUT/'work/shots.json').write_text(json.dumps(shots,indent=2));(OUT/'work/render-info.json').write_text(json.dumps({'duration':duration,'width':1920,'height':1080,'fps':30,'shots':len(shots)},indent=2))
 (OUT/'PLAN.md').write_text('''# Microsoft Fabric: build a data agent

A widescreen, Parker-informed tutorial: problem + finished-result teaser → documented output preview → three numbered purple process cards → source-backed application walkthrough → query inspection → honest limitation → return to the system. This replaces the unrelated NYC data-story topic and vertical chart format. Purple framing is intentionally adopted to meet the user’s closer visual-reference request; the V1 native renderer, fonts, captions and sound devices remain in use. No copied creator likeness, voice, footage or private prompt kit.

## Evidence and rights
https://learn.microsoft.com/en-us/fabric/data-science/how-to-create-data-agent
Retrieved October 22, 2026 using Firecrawl; retained in ../../research/parker-prompts/fabric-live-docs.json. Page date May 20, 2026. Microsoft screenshots and animated table-selection demonstration, CC BY 4.0 per MicrosoftDocs/fabric-docs license. Images are cropped, enlarged and annotated, with attribution in the picture. All source images are retained in ../../content/fabric-parker and assets/media. Microsoft trademarks remain their owners’.

This is an animated documentation walkthrough, not a recording of an authenticated Fabric session. Actual source application pixels and source animation are used; no fabricated app answers or claimed execution. The documented question asks how many users played Contoso games and how many purchased items. No specific answer count is invented. Capacity, tenant settings and read-access prerequisites appear in the setup graphic. The table-selection recording uses Microsoft’s AdventureWorks example; question/answer screenshots use Microsoft’s GamingDataAgent example. They demonstrate UI steps and are not presented as one executed data session.

Narration: local Kokoro synthetic review voice. Word alignment: Whisper tiny.en, unmatched words flagged; frame-exact manual verification not claimed. No music, paid model generation, Fabric connection or external publication. Side teaching questions are original illustrative wording, not Microsoft UI text.

## Validation
Native editable composition: index.html. Narration and word timings: SCRIPT.txt and work/timeline.json. Semantic edit list: work/shots.json. Final stream/decode checks: out/verification.json. Representative final frames: out/snaps/contact-sheet.jpg.
''')
 print('Built',duration,'seconds',len(shots),'shots',flush=True)
if __name__=='__main__':main()
