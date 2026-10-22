"""Reference-based motion and legibility revision. SVG surface geometry and typography stay explicit."""
from pathlib import Path
import re,shutil,json
P=Path(__file__).resolve().parent;G=P/'generated';p=G/'index.html';s=p.read_text();A=1120/30
shutil.copy('/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf',G/'assets/serif.ttf')
# Fixed design-space artwork prevents accidental double italics, text resizing and layer-order drift.
def card(id,title,lines,matrix):
 text=''.join(f'<text class="card-role" x="55" y="{85+i*8.6}"'+(' font-size="7.8"' if id=='replica-code' else '')+'>'+line+'</text>' for i,line in enumerate(lines))
 return f'<g id="{id}" transform="matrix({matrix})"><rect width="110" height="110" rx="5" fill="url(#card-gradient)"/><image href="assets/genie.svg" x="35" y="19" width="40" height="35"/><text class="card-name" x="55" y="72">{title}</text>{text}</g>'
svg='<svg id="replica-world" class="refined-family" viewBox="0 0 640 360"><defs><linearGradient id="card-gradient" x1="0" y1="0" x2=".75" y2="1"><stop stop-color="#ffe8d8"/><stop offset="1" stop-color="#ffc59a"/></linearGradient><linearGradient id="layer-gradient" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#ffe2c9"/><stop offset="1" stop-color="#ffbe8f"/></linearGradient></defs>'
for k in range(5,0,-1):svg+=f'<g id="replica-layer-{k}" transform="matrix(.85 -.02 -.31 .85 187 105)"><rect width="110" height="110" rx="5" fill="url(#layer-gradient)"/></g>'
svg+=card('replica-code','Genie Code',['Agent for technical users'],'.85 -.02 -.31 .79 211 103')
svg+=card('replica-agents','Genie Agents',['Agent for business &amp;','technical users'],'.85 -.02 -.31 .85 211 103')
svg+=card('replica-one','Genie One',['Agent for business users'],'1 0 0 1 178 129')+'</svg>'
s=s.replace('<div id="family" class="family">',svg+'<div id="family" class="family">',1)
css='''@font-face{font-family:ReplicaSerif;src:url(assets/serif.ttf)}.refined-family{position:absolute;inset:0;width:640px;height:360px;pointer-events:none;overflow:visible}.card-name,.card-role{text-anchor:middle;font-family:ReplicaSerif,"Times New Roman",serif;font-style:normal;font-weight:400}.card-name{font-size:13.8px;fill:#a84531}.card-role{font-size:8.5px;fill:#47372d}#replica-code .card-role{font-size:7.8px}#replica-code .card-name{font-size:13px}#replica-code .card-role{transform:translateX(-3px)}#data svg{fill:currentColor;stroke:none}#tools svg{fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}#data,#tools{color:#e87572}#data-line,#tool-line{stroke:#666d6c;stroke-width:1.25;marker-start:url(#connection-tip);marker-end:url(#connection-tip)}#business-label{top:59px!important;font-size:9px}#code-role{left:37px!important;top:244px!important;width:130px!important;font-size:9px;line-height:1.35}#domain-label{left:310px!important;top:276px!important;width:138px!important;font-size:8.5px;white-space:nowrap}#business-arrow,#technical-arrow,#domain-arrow{stroke:#676c69;stroke-width:1.1}#query{font-size:9.3px}#response{font-size:9px;color:#373a39}#results b{font-size:9.5px;color:#333936}#results div{color:#414643;font-size:7px}#campaign{font-size:10px;color:#bd5d20;white-space:nowrap;overflow:hidden}#chat-boundary{border-color:#39863e}#chat-boundary b{background:#4c7a45}.ev1-cap{font-family:"EV1 Grotesk",Arial,sans-serif;font-weight:700;gap:.12em;letter-spacing:-.025em}.ev1-cap .w{font-family:"EV1 Grotesk",Arial,sans-serif;font-weight:700;color:white;-webkit-text-stroke:4px #46413c;paint-order:stroke fill;text-shadow:0 1px 2px #0009;border-radius:8px;padding:0 3px}'''
s=s.replace('</style>',css+'\n</style>')
s=s.replace('Focused on<br>domain-specific work','Focused on domain-specific work')
# Restore an actual, visible tool glyph; global filled-icon rules previously erased the crossed strokes.
s=re.sub(r'(<div id="tools"[^>]*>)<svg.*?</svg>',lambda m:m[1]+'<svg viewBox="0 0 32 32"><path d="M7 4a7 7 0 0 0 7 10l12 12a2.5 2.5 0 0 0 4-4L18 10a7 7 0 0 0-10-7l5 5-5 5-5-5"/><path d="M5 29 15 19M22 10l6-6 3 3-6 6"/></svg>',s,count=1,flags=re.S)
s=s.replace('<svg class="svg-world">','<svg class="svg-world"><defs><marker id="connection-tip" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#666d6c"/></marker></defs>',1)
# Hide the obsolete CSS-transformed family after chat; its original front card still serves the opening.
s=re.sub(r'tl\.to\("#family",\{\.\.\.\{"opacity": 1\},duration:0\.35[^\n]+\n','',s)
s=s.replace('showing-replica-placeholder','')
pre='gsap.set("#replica-world",{opacity:0});gsap.set("#replica-code,#replica-agents",{opacity:0});'+''.join(f'gsap.set("#replica-layer-{k}",{{opacity:0}});' for k in range(1,6))
s=s.replace('const tl = gsap.timeline',pre+'\nconst tl = gsap.timeline') if 'const tl = gsap.timeline' in s else s
# The actual source uses const tl=... without spaces in some builder versions.
if pre not in s:s=s.replace('const tl=gsap.timeline',pre+'\nconst tl=gsap.timeline')
if pre not in s:
 match=re.search(r'(?:const|let|var) tl\s*=\s*gsap.timeline',s);assert match;s=s[:match.start()]+pre+'\n'+s[match.start():]
def at(t):return round(t-A,6)
events=[f'tl.set("#family",{{opacity:0}},{at(53.7)});',f'tl.to("#replica-world",{{opacity:1,duration:.2,ease:"power2.out"}},{at(53.8)});',f'tl.to("#replica-one",{{attr:{{transform:"matrix(.85 -.02 -.31 .85 187 105)"}},duration:.533,ease:"power2.inOut"}},{at(55.167)});',f'tl.to("#replica-one",{{attr:{{transform:"matrix(.85 -.02 -.31 .85 211 103)"}},duration:1.0,ease:"power2.inOut"}},{at(61.0)});']
for k in range(1,6):events+=[f'tl.set("#replica-layer-{k}",{{opacity:1}},{at(55.833)});',f'tl.to("#replica-layer-{k}",{{attr:{{transform:"matrix(.85 -.02 -.31 .85 {187+8*k} {105+9.5*k})"}},duration:.467,ease:"power2.out"}},{at(55.833)});']
for sel,t,target in [('replica-code',64.65,'.85 -.02 -.31 .79 127 116'),('replica-agents',72.45,'.83 -.02 -.30 .85 299 120')]:events+=[f'tl.to("#{sel}",{{opacity:1,duration:.12,ease:"none"}},{at(t)});',f'tl.to("#{sel}",{{attr:{{transform:"matrix({target})"}},duration:.85,ease:"power2.inOut"}},{at(t)});']
# Bring the answer to a readable settled state before the action begins. Typed action stays in place.
s=s.replace('duration:0.5,ease:"power2.out",immediateRender:false},10.966666666666669);','duration:0.35,ease:"power2.out",immediateRender:false},10.56666666666667);')
events+=[f'tl.fromTo("#campaign",{{width:0}},{{width:286,duration:.85,ease:"none",immediateRender:false}},{at(48.85)});']
s=s.replace('window.__timelines=window.__timelines||{};', '\n'.join(events)+'\nwindow.__timelines=window.__timelines||{};')
# The reference establishes the tool endpoint before the spoken word completes.
s=s.replace('duration:0.6,ease:"power2.out",immediateRender:false},7.533333333333331);','duration:0.35,ease:"power2.out",immediateRender:false},6.866666666666667);')
s=s.replace('duration:0.7,ease:"power2.inOut",immediateRender:false},7.286666666666669);','duration:0.45,ease:"power2.inOut",immediateRender:false},6.716666666666669);')
def retime(selector,source_time,duration):
 global s
 lines=[]
 for line in s.splitlines():
  if line.startswith('tl.to("'+selector+'",') and '"opacity": 1' in line:
   line=re.sub(r'duration:[0-9.]+','duration:'+str(duration),line)
   line=re.sub(r'},[0-9.]+\);$', '},'+str(at(source_time))+');',line)
  lines.append(line)
 s='\n'.join(lines)
retime('#tools',44.05,.35)
retime('#data',44.0,.35)
retime('#tool-line',44.1,.35)
retime('#data-line',43.35,.55)
retime('#results',47.9,.35)
retime('#query',47.65,.25)
retime('#response',47.75,.3)
p.write_text(s)
(G/'refinement.json').write_text(json.dumps({'changes':['explicit SVG card planes; fixed text metrics; no double italic or animated font size','front card separates from stationary stack','peer cards emerge from beneath front card','visible tool glyph and directional arrowheads','single-line domain annotation and stronger text contrast','caption weight and source-derived phrase alignment'], 'source_measurements':{'flat_family_card':[178,129,110,110],'tilted_front_matrix':[.85,-.02,-.31,.85,187,105],'tilt_interval':[55.167,55.7],'extrusion_interval':[55.833,56.3]},'precision':'Geometry and timings are estimates from decoded 640×360 source frames, not original project keyframes'},indent=2))
print('Applied reference-motion and readability revision')
