"""Transcript-first practice: preserve source narration; plan visuals by explanatory function."""
from pathlib import Path
import json,sys,shutil,re,subprocess,html
R=Path(__file__).resolve().parent;ROOT=R.parents[1];KIT=ROOT/'vendor/editor-v1';sys.path.insert(0,str(KIT/'components'))
from ev1_more import Comp,captions,fr
A=1120/30;Z=2511/30;D=fr(Z-A);c=Comp(D);shutil.copytree(KIT/'assets',R/'assets/ev1',dirs_exist_ok=True);shutil.copy(ROOT/'content/fabric-ontology/presenters.png',R/'assets/presenters.png');shutil.copy('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',R/'assets/regular.ttf');shutil.copy('/usr/share/doc/fonts-liberation/copyright',R/'assets/font-license.txt')
src=json.loads((ROOT/'research/ontology-adaptation/uploaded-parts.json').read_text())[0]['path'];audio=R/'assets/narration.wav'
if not audio.exists():subprocess.run(['ffmpeg','-v','error','-y','-ss',str(A),'-i',src,'-t',str(D),'-vn','-ar','48000','-ac','1',str(audio)],check=True)
raw=json.loads((R/'source-words.json').read_text());words=[];i=0
while i<len(raw):
 w=raw[i];txt=w['w'];j=i+1
 if A<=w['start']<Z:
  clean=txt.strip('.,?!').lower()
  if j<len(raw) and (clean,raw[j]['w'].strip('.,?!').lower()) in [('co','-worker'),('co','-workers'),('data','bricks'),('lake','house'),('domain','-specific')]:
   pair=(clean,raw[j]['w'].strip('.,?!').lower());txt={('co','-worker'):'co-worker',('co','-workers'):'co-workers',('data','bricks'):'Databricks.',('lake','house'):'lakehouse.',('domain','-specific'):'domain-specific'}[pair];j+=1
  elif clean=='genie':txt='Genie'
  elif clean=='one':txt='One'+('' if txt[-1].isalnum() else txt[-1])
  elif clean=='code' and words and words[-1]['w']=='Genie':txt='Code'
  elif clean=='agents' and words and words[-1]['w']=='Genie':txt='Agents,'
  words.append({'w':txt,'s':fr(w['start']-A),'e':fr(raw[j-1]['end']-A),'source_start':w['start']})
 i=j
(R/'words.json').write_text(json.dumps(words,indent=2));(R/'transcript.txt').write_text(' '.join(w['w'] for w in words)+'\n')
beats=[
 ('define',38.46,43.66,'Define the product','Genie One is an AI co-worker for business users.','Establish one product node; attach its audience.','The viewer needs one stable referent before its capabilities are expanded.'),
 ('connect',43.66,46.06,'Explain connections','It connects to your data and tools.','Add data and tool nodes; draw connections to the existing product.','A relationship is easier to follow when both endpoints and their link are visible.'),
 ('question-action',46.06,50.34,'Explain a capability and its consequence','It answers questions about your business; it acts on the answers.','Transition into an illustrative chat: typed question, response totals, then a campaign action.','Express the causal progression without changing the product being discussed.'),
 ('governance',50.34,53.74,'Bound the mechanism','All within the governance framework that you already have.','Scale down the same chat panel and draw its green governance boundary.','Containment expresses the scope of the claim; no new product is introduced.'),
 ('family',53.74,61.24,'Expand the category','Genie One sits in a larger stack of AI co-workers and tools on Databricks.','Keep the same product card; tilt it and reveal related layers.','Extend the known object into a family instead of resetting the viewer’s context.'),
 ('compare',61.24,72.08,'Distinguish sibling roles','Genie One serves business users; Genie Code serves technical users.','Keep One central over the stack, reveal Code on the left, and annotate their distinct roles.','Position encodes sibling status; labels encode the actual difference.'),
 ('shared-specialist',72.08,81.04,'Add a shared specialist','Genie Agents can be used by both audiences and focus on domain-specific work.','Add the third sibling; label its shared audience; attach its domain role.','Make shared access and specialization separate visible relationships.'),
 ('hold',81.04,Z,'Elaborate and close','The speaker offers to cover it in more depth.','Cut back to the full-frame static presenter placeholder at source 81.53s.','The reference returns attention to the speaker as she offers to elaborate.')]
plan=[]
for id,a,z,job,spoken,visual,why in beats:plan.append(dict(id=id,start=fr(max(A,a)-A),end=fr(z-A),source_start=a,source_end=z,teaching_job=job,spoken_summary=spoken,visual=visual,why=why,certainty='Teaching purpose is an interpretation; word timing is local ASR alignment, not manually frame-certified'))
(R/'storyboard.json').write_text(json.dumps({'mode':'transcript-first','source':'HtR5m5VjaDQ / user-supplied part00','source_in':A,'source_out':Z,'duration':D,'narration':'original source audio, not synthetic or cloned','word_alignment':'Whisper tiny.en, merged product terms; approximate','beats':plan},indent=2))
(R/'STORYBOARD.md').write_text('# Transcript-first practice 01\n\nOriginal Databricks narration is preserved. Graphics are planned from explanatory function using the reference’s visual grammar; this is not a certified pixel-for-pixel reconstruction.\n\n| Time | Teaching job | Visual change | Why |\n|---|---|---|---|\n'+'\n'.join(f'| {b["start"]:.2f}–{b["end"]:.2f}s | {b["teaching_job"]} | {b["visual"]} | {b["why"]} |' for b in plan)+'\n\nAudio is from the user-supplied reference. The fictional static presenter is a placeholder and is not the source speaker. Diagrams are illustrative; no actual product UI or execution result is claimed. Product claims are those of the source passage, not independently verified current documentation. Original Genie symbol is approximated as a vector. This is local practice; nothing has been published.\n')
# All state changes use timeline properties and attributes; no event-dependent animation callbacks.
def local(t):return fr(max(0,t-A))
def tween(sel,props,t,d=.8,ease='power2.inOut'):
 c.at('tl.to('+json.dumps(sel)+',{...'+json.dumps(props)+',duration:'+str(d)+',ease:'+json.dumps(ease)+',immediateRender:false},'+str(local(t))+');')
def show(sel,t,d=.7,dy=14):
 c.pre.append('gsap.set('+json.dumps(sel)+',{opacity:0,y:'+str(dy)+'});');tween(sel,{'opacity':1,'y':0},t,d,'power2.out')
def draw(sel,t,d=.75):
 c.pre.append('document.querySelector('+json.dumps(sel)+').setAttribute("stroke-dasharray","1");document.querySelector('+json.dumps(sel)+').setAttribute("stroke-dashoffset","1");');tween(sel,{'attr':{'stroke-dashoffset':0},'opacity':1},t,d)
logo=re.search(r"logo='''(.*?)'''",(ROOT/'motion-studies/01-ontology-map/build.py').read_text(),re.S).group(1)
(R/'assets/genie.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="42 25 70 63">'+logo+'</svg>')
c.css.append('''@font-face{font-family:PracticeSans;src:url(assets/regular.ttf)}*{box-sizing:border-box}html,body{width:1920px;height:1080px}:root{--ev1-cap-size:43px}.world{position:absolute;inset:0;background-color:#fffefa;background-image:linear-gradient(#b9c6bc20 1px,transparent 1px),linear-gradient(90deg,#b9c6bc20 1px,transparent 1px);background-size:94.5px 94.5px}.border{position:absolute;inset:0;border:9px solid #ff6600;pointer-events:none}.stage{position:absolute;left:0;top:0;width:640px;height:360px;transform:scale(3);transform-origin:0 0;font-family:PracticeSans,Arial,sans-serif;color:#5d4e43;perspective:1100px}.speaker{position:absolute;left:1434px;top:276px;width:438px;height:534px;border-radius:36px;overflow:hidden;background:linear-gradient(120deg,#e3e7de,#b1c6b4)}.speaker img{position:absolute;width:480%;height:auto;max-width:none;left:-310%;bottom:-506px}.family{position:absolute;left:175px;top:108px;width:124px;height:124px;transform-style:preserve-3d;transform-origin:62px 62px}.product,.layer{position:absolute;width:124px;height:124px;border-radius:5px;background:linear-gradient(135deg,#ffe3ce,#ffcba4);box-shadow:0 3px 7px #8c755b12;backface-visibility:hidden}.product{text-align:center;padding:23px 8px 10px;z-index:20}.product img{width:34px;height:34px;object-fit:contain}.product strong{display:block;font-size:13px;font-weight:400;line-height:1.3;margin-top:8px;color:#b65c48}.product small{display:block;font-size:8px;line-height:1.4;margin-top:4px;color:#805c4c}.layer{z-index:1;background:linear-gradient(140deg,#ffe7d6,#f8b989)}#code{left:144px;z-index:20}#agents{left:288px;z-index:20}.symbol{height:34px;color:#d76b55;font-size:29px;line-height:34px}.svg-world{position:absolute;inset:0;width:640px;height:360px;pointer-events:none}.node{position:absolute;top:145px;width:65px;height:65px;border:1px solid #e1e4df;border-radius:6px;background:#fffefb;color:#ad5b42;text-align:center;padding:12px 6px;font-size:11px}.node svg{display:block;margin:0 auto 5px;width:24px;height:24px;stroke:currentColor;fill:none;stroke-width:1.5}.bubble{position:absolute;border:1px solid #dfdfd8;border-radius:7px;background:#fffdf9;box-shadow:0 4px 11px #4e5b4d12;padding:11px 14px;font-size:12px;line-height:1.4;color:#55564e;text-align:center}.label{position:absolute;font-size:10px;line-height:1.4;color:#58614f;text-align:center}.outline{fill:none;stroke:#6f8a54;stroke-width:1.4;stroke-linecap:round}.line{fill:none;stroke:#b49b82;stroke-width:1.05;stroke-linecap:round}.ev1-cap{gap:.22em}.ev1-cap .w{font-weight:800;text-transform:uppercase;color:#fff;-webkit-text-stroke:2.5px #342b22;paint-order:stroke fill;text-shadow:0 2px 3px #342b22}.ev1-cap{max-width:1800px}''')
body='<div class="world"></div><div class="stage">'
body+='''<svg class="svg-world"><path id="data-line" class="line" d="M100 177H175" pathLength="1"/><path id="tool-line" class="line" d="M299 177H350" pathLength="1"/><path id="question-line" class="line" d="M237 108V99" pathLength="1"/><path id="answer-line" class="line" d="M237 232V255" pathLength="1"/><path id="action-line" class="line" d="M340 279Q382 279 382 210" pathLength="1"/><rect id="governance" x="18" y="42" width="430" height="279" rx="12" class="outline" pathLength="1"/></svg>'''
body+='''<div id="data" class="node" style="left:35px"><svg viewBox="0 0 32 32"><ellipse cx="16" cy="7" rx="10" ry="4"/><path d="M6 7v17c0 6 20 6 20 0V7M6 15c0 6 20 6 20 0"/></svg>Data</div><div id="tools" class="node" style="left:350px"><svg viewBox="0 0 32 32"><path d="M5 5 27 27M6 27 27 6M4 4l7 2-4 5ZM22 22l6 2-4 4Z"/></svg>Tools</div><div id="question" class="bubble" style="left:125px;top:58px;width:224px">Questions about your business</div><div id="answer" class="bubble" style="left:130px;top:255px;width:210px">Answers</div><div id="action" class="label" style="left:345px;top:235px;width:83px">Acts on<br>the answers</div><div id="gov-label" class="label" style="left:128px;top:30px;width:210px;background:#fffefa">Your existing governance framework</div><div id="family" class="family">'''
for k in range(5,0,-1):body+=f'<div id="layer{k}" class="layer"></div>'
body+='''<div id="one" class="product"><img src="assets/genie.svg"><strong>Genie One</strong><small id="one-role">AI co-worker</small><small id="one-audience">Business users</small></div><div id="code" class="product"><div class="symbol">{ }</div><strong>Genie Code</strong><small>Technical users</small></div><div id="agents" class="product"><div class="symbol">◇</div><strong>Genie Agents</strong><small id="both-label">Both audiences</small></div></div>'''
body+='''<svg class="svg-world"><path id="business-arrow" class="line" d="M162 125Q162 79 175 66" pathLength="1"/><path id="technical-arrow" class="line" d="M274 146Q274 89 316 66" pathLength="1"/><path id="both-branch" class="line" d="M151 230V251H406V230M278 230V251" pathLength="1"/><path id="domain-arrow" class="line" d="M389 274V289" pathLength="1"/></svg><div id="business-label" class="label" style="left:122px;top:46px;width:104px">Business users</div><div id="technical-label" class="label" style="left:264px;top:46px;width:104px">Technical users</div><div id="domain-label" class="label" style="left:328px;top:293px;width:122px">Domain-specific work</div><div id="code-role" class="label" style="left:213px;top:263px;width:117px">Write code · lakehouse</div></div><div class="speaker" data-safe="presenter"><img src="assets/presenters.png"></div><div class="border"></div>'''
# Reconstruct the reference's illustrative question -> results -> action UI.
chat='''<div id="chat"><div id="chat-boundary"><b>◈</b></div><div id="query">Which products generated the most sales?</div><div id="response"><span>☻</span> Here are the products that generated most sales:</div><div id="results"><div><b>$40,800</b><br>Laptops</div><div><b>$20,540</b><br>Monitors</div><div><b>$10,200</b><br>Accessories</div></div><div id="campaign">+ Create campaign for top-selling products →</div><div id="input"><em id="input-text" style="font-style:normal">Which products generated the most sales?</em><span>➤</span></div></div>'''
body=body.replace('<div class="stage">','<div class="stage">'+chat)
body=body.replace('<div class="border"></div>','<div id="full-speaker" class="full-speaker"><img src="assets/presenters.png"></div><div id="intro-speaker" class="full-speaker"><img src="assets/presenters.png"></div><div class="border"></div>')
body=body.replace('<div class="symbol">{ }</div>','<img src="assets/genie.svg">').replace('<div class="symbol">◇</div>','<img src="assets/genie.svg">')
body=body.replace('AI co-worker</small>','Agent for business users</small>').replace('Business users</small>','</small>').replace('Technical users</small>','Agent for technical users</small>').replace('Both audiences</small>','Agent for business &amp;<br>technical users</small>')
body=body.replace('Business users</div>','For Business Users</div>').replace('Write code · lakehouse','Writes code &amp; works within<br>the Lakehouse').replace('Domain-specific work','Focused on<br>domain-specific work')
body=body.replace('M162 125Q162 79 175 66','M259 96Q261 70 285 65').replace('M274 146Q274 89 316 66','M118 208Q95 218 97 239').replace('M389 274V289','M369 216Q390 231 377 262')
c.css.append(''' .world{background-color:#fff;background-image:linear-gradient(#a5b4b520 1px,transparent 1px),linear-gradient(90deg,#a5b4b520 1px,transparent 1px)}.speaker{left:1425px;top:273px}.family{left:173px;top:108px;transform-style:flat}.product,.layer{width:140px;height:140px;transform-origin:center center}.product{padding:24px 6px 8px}.product strong{font-family:Georgia,serif;font-style:italic;font-size:13px;margin-top:5px}.product small{font-family:Georgia,serif;font-style:italic;font-size:8px;margin-top:3px}.product img{width:43px;height:43px}.layer{background:linear-gradient(135deg,#ffdec7,#ffbd8c)}#one{z-index:30}#code{left:-88px;top:12px;z-index:21;transform:skewX(-20deg) rotate(-2deg) scale(.66,.64)}#agents{left:88px;top:17px;z-index:21;transform:skewX(-20deg) rotate(-2deg) scale(.66,.64)}#one-audience,#technical-label{display:none}.label{color:#353735;font-size:10px}#business-label{left:287px!important;top:57px!important;width:110px!important;text-align:left}#code-role{left:35px!important;top:244px!important;width:135px!important}#domain-label{left:307px!important;top:267px!important;width:120px!important}.line{stroke:#6a6c68;stroke-width:1.15}#data,#tools{border:0;background:transparent;padding:15px 0;font-size:0;color:#ee777d}#data{left:63px!important}#tools{left:348px!important}#data svg,#tools svg{width:29px;height:29px;stroke-width:2.4}#data-line{d:path('M119 177H184')}#tool-line{d:path('M284 177H350')}#chat{position:absolute;left:51px;top:45px;width:378px;height:258px;border-radius:8px;background:radial-gradient(ellipse at 50% 90%,#ffe2cc,#f7f7f6 85%);box-shadow:0 0 7px #0003;transform-origin:center center;color:#494949;font-size:10px}#query{position:absolute;right:34px;top:30px;background:#ececeb;box-shadow:0 0 5px #0002;border-radius:3px;padding:9px 18px;font-size:9px}#response{position:absolute;left:32px;top:86px;font-size:9px}#response span{display:inline-block;color:#ee8e69;background:#ffd0aa;border-radius:50%;padding:4px;margin-right:5px}#results{position:absolute;left:59px;top:110px;display:flex;gap:10px}#results div{width:72px;height:44px;background:white;box-shadow:0 1px 4px #0001;border-radius:4px;text-align:center;padding-top:11px;font-size:7px}#results b{font-size:9px}#campaign{position:absolute;left:59px;top:169px;color:#c36b24;font-size:10px}#input{position:absolute;left:32px;bottom:20px;width:310px;height:27px;background:white;border-radius:3px;box-shadow:0 0 5px #0002;padding:8px 12px;font-size:9px}#input span{position:absolute;right:9px;color:#d66a4d}#chat-boundary{position:absolute;inset:-2px;border:2px solid #438848;border-radius:12px;box-shadow:0 0 4px #438848}#chat-boundary b{position:absolute;left:48%;top:-15px;border-radius:50%;background:#666c64;color:white;width:27px;height:27px;text-align:center;padding-top:4px;font-size:16px}.full-speaker{position:absolute;inset:9px;overflow:hidden;background:linear-gradient(120deg,#dce4d7,#869c83)}.full-speaker img{position:absolute;width:250%;max-width:none;left:-146%;top:-25%}.ev1-cap .w{font-weight:900;text-shadow:0 1px 3px #000}''')
c.css.append('#question,#answer,#action,#gov-label{display:none}.ev1-cap .w{opacity:1!important;padding:0 3px;border-radius:6px}')
body=body.replace('<svg class="svg-world"><path id="business-arrow"','<svg class="svg-world"><defs><marker id="arrowtip" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10L3 5Z" fill="#6a6c68"/></marker></defs><path id="business-arrow"')
c.css.append('#business-arrow,#technical-arrow,#domain-arrow{marker-end:url(#arrowtip)}#input-text{display:inline-block;overflow:hidden;white-space:nowrap;vertical-align:top}')
c.pre.append('gsap.set("#input-text",{width:0});')
tween('#input-text',{'width':245},46.2,1.,'none')
c.clip(0,D,body,1)
tween('#intro-speaker',{'opacity':0},39.2,.033)
tween('#input-text',{'opacity':0},47.65,.033)
# The known referent persists through mechanism, governance, family and comparison.
show('#family',38.46,1,20);show('#one-audience',42.46,.55,5)
for sel,t in [('#data',44.34),('#tools',44.86)]:show(sel,t,.6,7)
draw('#data-line',43.74,.7);draw('#tool-line',44.62,.7)
# Chat demonstration replaces the connection diagram below.


for sel in ['#data','#tools','#question','#answer','#action','#gov-label','#data-line','#tool-line','#question-line','#answer-line','#action-line','#governance']:tween(sel,{'opacity':0},53.8,.65)
# Card plane matches the source's left-leaning parallelogram; siblings stay in canvas coordinates.
tween('#one',{'scale':.58},43.5,.65)
for sel in ['#data','#tools','#data-line','#tool-line']:tween(sel,{'opacity':0},46.0,.3)
tween('#family',{'opacity':0},46.0,.3)
show('#chat',46.0,.5,0)
show('#query',47.65,.35,0);show('#response',48.05,.45,0);show('#results',48.3,.5,6);show('#campaign',48.85,.4,0)
tween('#chat',{'scale':.83},50.45,.7)
show('#chat-boundary',50.6,.65,0)
tween('#chat',{'opacity':0},53.7,.35)
tween('#family',{'opacity':1},53.8,.35)
tween('#one',{'scale':1},53.8,.4)
tween('#family',{'y':-25},55.167,.533)
tween('#one',{'skewX':-20,'rotationZ':-2,'scaleY':.64,'scaleX':.66},55.167,.533)
for k in range(1,6):
 c.pre.append(f'gsap.set("#layer{k}",{{opacity:0,skewX:-20,rotationZ:-2,scaleY:.64,scaleX:.66}});');tween('#layer'+str(k),{'opacity':1,'x':k*7,'y':k*10},55.833,.467)
show('#business-label',63.52,.5,0);draw('#business-arrow',63.52,.5)
show('#code',64.94,.8,0);show('#code-role',68.56,.55,0);draw('#technical-arrow',68.56,.55)
show('#agents',72.58,.8,0);show('#both-label',75.16,.55,0);draw('#domain-arrow',77.0,.65);show('#domain-label',77.92,.55,0)
show('#full-speaker',81.53,.033,0)
# Pre-seed all drawn strokes hidden and all future cards/labels before their timeline events.
for sel in ['#data-line','#tool-line','#question-line','#answer-line','#action-line','#governance','#business-arrow','#technical-arrow','#both-branch','#domain-arrow']:c.pre.append('gsap.set('+json.dumps(sel)+',{opacity:0});')
# Phrase blocks remain legible; only the currently spoken word receives amber emphasis.
phrase_starts=[37.44,38.46,39.82,40.66,43.66,46.06,47.,48.48,49.3,50.34,51.46,53.74,55.26,57.4,58.4,60.4,61.66,63.28,64.94,65.96,67.82,69.28,72.08,73.76,75.16,76.4,77.92,79.6,81.04,82.2,Z]
for n,(aa,bb) in enumerate(zip(phrase_starts,phrase_starts[1:])):
 g=[w for w in words if aa-.015<=w['source_start']<bb-.015]
 if not g:continue
 spans=''.join(f'<span id="cap-{n}-{j}" class="w">{html.escape(w["w"])}</span>' for j,w in enumerate(g))
 c.clip(local(aa),local(bb),'<div class="ev1-cap" style="top:calc(95% - .6 * var(--ev1-cap-size))">'+spans+'</div>',60,cls='',style='position:absolute;inset:0;width:1920px;height:1080px')
 for j,w in enumerate(g):
  c.at(f'tl.set("#cap-{n}-{j}",{{backgroundColor:"#ae6200"}},{w["s"]});')
  end=g[j+1]['s'] if j+1<len(g) else local(bb)
  c.at(f'tl.set("#cap-{n}-{j}",{{backgroundColor:"transparent"}},{end});')
for sel in ['#chat','#query','#response','#results','#campaign','#chat-boundary','#full-speaker']:
 c.pre.append('gsap.set('+json.dumps(sel)+',{opacity:0});')
# Source switches from the large product card into a small connected node.
# Caption grouping remains ASR based; highlight active spoken words.

c.write(str(R/'index.html'),'assets/ev1/tokens.css',title='Transcript-first practice / Databricks product family');p=R/'index.html';p.write_text(p.read_text().replace('window.__timelines["main"] = tl;','window.__timelines=window.__timelines||{};window.__timelines["main"] = tl;'))
(R/'render-info.json').write_text(json.dumps(dict(duration=D,width=1920,height=1080,fps=30),indent=2));print('Built',D,'seconds;',len(plan),'teaching beats;',len(words),'aligned words')
