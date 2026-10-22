"""First isolated reconstruction: editable SVG objects and a source-measured camera track."""
from pathlib import Path
import json,sys,shutil,re
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent;KIT=ROOT/'vendor/editor-v1';sys.path.insert(0,str(KIT/'components'))
from ev1_more import Comp
D=218/30;c=Comp(D);shutil.copytree(KIT/'assets',OUT/'assets/ev1',dirs_exist_ok=True)
def icon(name):
 s=(OUT/'assets'/f'{name}.svg').read_text();view=re.search(r'viewBox="([^"]+)"',s).group(1);paths=''.join(re.findall(r'<path[^>]+>',s));size={'brain':14,'copy':15}.get(name,19);pos=(54-size)/2
 return f'<svg x="{pos}" y="{pos}" width="{size}" height="{size}" viewBox="{view}" fill="#fff5e8">{paths}</svg>'
logo='''<g fill="#f7b8a8"><path d="M64 58C60 54 53 55 50 59C46 64 48 71 53 71C58 71 58 67 55 65C52 62 56 60 60 63L68 70C76 78 87 73 94 66C100 60 103 54 105 49C100 50 97 54 92 56C85 59 82 57 76 58C70 59 68 61 66 64C66 61 65 59 64 58Z"/></g><path fill="#ed705c" d="M75 31C77 40 80 43 87 45C80 47 77 50 75 58C73 50 70 47 63 45C70 43 73 40 75 31ZM67 78H80Q84 79 85 82H64Q65 79 67 78Z"/>'''
logo='<g transform="translate(7.7 5.8) scale(.9)">'+logo+'</g>'
body='''<div id="study"><svg width="640" height="360" viewBox="0 0 640 360"><defs><pattern id="grid" x="19.5" y="29" width="31.45" height="31.45" patternUnits="userSpaceOnUse"><path d="M0 0H31.45M0 0V31.45" fill="none" stroke="#68432c" stroke-opacity=".55" stroke-width=".6"/></pattern><radialGradient id="background" cx="75%" cy="95%" r="90%"><stop stop-color="#3c1800"/><stop offset="1" stop-color="#230900"/></radialGradient><linearGradient id="small-card" x2="1" y2="1"><stop stop-color="#9c4d0e" stop-opacity=".80"/><stop offset="1" stop-color="#7b360a" stop-opacity=".55"/></linearGradient><linearGradient id="main-card" x2="1" y2="1"><stop stop-color="#482009" stop-opacity=".35"/><stop offset="1" stop-color="#3b1505" stop-opacity=".15"/></linearGradient><filter id="line-glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1.2"/></filter><filter id="border-glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation=".8"/></filter><marker id="arrow" viewBox="0 0 8 8" markerWidth="4" markerHeight="4" refX="6" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8Z" fill="#fff5db"/></marker></defs><rect width="640" height="360" fill="url(#background)"/><rect width="640" height="360" fill="url(#grid)"/><g id="diagram">'''
paths=['M245 181H200Q160 181 160 141V67Q160 27 120 27H64','M245 181H200Q160 181 160 169Q160 129 122 129H64','M245 181H200Q160 181 160 193Q160 231 122 231H64','M245 181H200Q160 181 160 221V293Q160 333 120 333H64']
for k,path in enumerate(paths):body+=f'<g id="route{k}" opacity="0"><path id="glow{k}" d="{path}" fill="none" stroke="#fff4dc" stroke-opacity=".08" stroke-width="4" filter="url(#line-glow)" pathLength="1"/><path id="edge{k}" d="{path}" fill="none" stroke="#e9ddc8" stroke-width="1.1" pathLength="1"/></g>'
for k,name in enumerate(['gear','chart-column','brain','copy']):body+=f'<g transform="translate(10 {102*k})"><g id="input{k}" opacity="0"><rect x="0" y="0" width="54" height="54" rx="8" fill="url(#small-card)" stroke="#bd681f" stroke-width="1.4"/>{icon(name)}</g></g>'
body+=f'''<g id="main" transform="translate(245 104)" opacity="0"><rect width="154" height="154" rx="22" fill="none" stroke="#e58b6c" stroke-width="2.8" opacity=".20" filter="url(#border-glow)"/><rect width="154" height="154" rx="22" fill="url(#main-card)" stroke="#9e5945" stroke-width="1.2"/><g id="main-logo">{logo}</g><text id="main-label" x="77" y="114" text-anchor="middle" fill="#f2e0ce" font-size="14.2" font-family="Arimo,Arial,sans-serif"></text></g><g id="output-route" opacity="0"><path id="output-edge" d="M406 181H498" fill="none" stroke="#f7ecd1" stroke-width="1" marker-start="url(#arrow)" marker-end="url(#arrow)" pathLength="1"/></g><g transform="translate(505 129)"><g id="output" opacity="0"><rect width="108" height="108" rx="15" fill="url(#main-card)" stroke="#9c8362" stroke-width="1.3"/><g transform="translate(0 -1) scale(.70)">{logo}</g><text id="output-label" x="54" y="80" text-anchor="middle" fill="#e8dbc5" font-size="11" font-family="Arimo,Arial,sans-serif"></text></g></g></g><rect x="1.5" y="1.5" width="637" height="357" fill="none" stroke="#ff6600" stroke-width="3"/></svg></div>'''
c.css.append('''@font-face{font-family:Arimo;src:url('assets/ev1/fonts/../../reference-sans.ttf')}html,body{width:1920px;height:1080px}#study{width:640px;height:360px;transform:scale(3);transform-origin:0 0}#study svg{display:block}''')
# Camera geometry from observed central-card bounds; points with incomplete contour detection are excluded.
track=[(0,321.5,180.5,0),(.2,321.5,180.5,78),(.4,321.5,180.5,127),(.6,321.5,180.5,149),(.8,321.5,180.5,153),(2.3,321.5,180.5,153),(2.4,322,180.5,154),(2.8,329,181,152),(3,338.5,180.5,149),(3.2,356,181,144),(3.6,390.5,181.5,133),(4,399,182,128),(4.4,399,182,128),(4.8,397,182,126),(5,392.5,182,125),(5.2,383.5,182.5,121),(5.4,364.5,182.5,119),(5.6,344,182.5,114),(5.8,330,183,112),(6,323.5,183,111),(6.2,321.5,182.5,109),(D,321.5,182.5,109)]
# Explicit visibility and line events remain independent from the camera fit.
events={'main_opacity':[.0,.65],'main_logo':[.2,.7],'main_label':[.4,1.05],'input_starts':[2.65,2.95,3.2,3.35],'input_duration':.9,'route_starts':[2.5,2.8,2.95,3.1],'route_duration':.85,'output_route':[5.25,5.85],'output_card':[5.25,6.25],'output_label':[5.78,6.55]}
c.pre.append('const cameraTrack='+json.dumps(track)+';const events='+json.dumps(events)+';')
def clamp(v):return max(0,min(1,v))
def smooth(t,a,b):
 u=clamp((t-a)/(b-a));return u*u*(3-2*u)
def slope(k,col):
 if k<=0 or k>=len(track)-1:return 0
 d0=(track[k][col]-track[k-1][col])/(track[k][0]-track[k-1][0]);d1=(track[k+1][col]-track[k][col])/(track[k+1][0]-track[k][0]);return 0 if d0*d1<=0 else 2*d0*d1/(d0+d1)
def val(t,col):
 k=0
 while k<len(track)-2 and t>track[k+1][0]:k+=1
 a,b=track[k:k+2];h=b[0]-a[0];u=clamp((t-a[0])/h);return(2*u**3-3*u*u+1)*a[col]+(u**3-2*u*u+u)*h*slope(k,col)+(-2*u**3+3*u*u)*b[col]+(u**3-u*u)*h*slope(k+1,col)
def state(t):
 w=val(t,3);scale=w/154;x=val(t,1)-w/2;y=val(t,2)-w/2;out={'diagram':{'transform':f'matrix({scale:.6f} 0 0 {scale:.6f} {x-245*scale:.6f} {y-104*scale:.6f})'},'main':{'opacity':round(smooth(t,*events['main_opacity']),5)},'main-logo':{'opacity':round(smooth(t,*events['main_logo']),5)}}
 for k in range(4):
  u=smooth(t,events['input_starts'][k],events['input_starts'][k]+events['input_duration']);p=smooth(t,events['route_starts'][k],events['route_starts'][k]+events['route_duration']);out['input'+str(k)]={'opacity':round(u,5),'transform':f'translate({27*(1-u):.6f} {27*(1-u):.6f}) scale({u:.6f})'};out['route'+str(k)]={'opacity':round(min(1,p*5),5)}
  for name in ['edge','glow']:out[name+str(k)]={'stroke-dashoffset':round(1-p,5)}
 o=smooth(t,*events['output_card']);q=smooth(t,*events['output_route']);out['output']={'opacity':round(o,5),'transform':f'translate({54*(1-o):.6f} {54*(1-o):.6f}) scale({o:.6f})'};out['output-route']={'opacity':round(q,5)};out['output-edge']={'stroke-dashoffset':round(1-q,5)};return out
initial=state(0)
c.pre.append('const initialGraphicState='+json.dumps(initial)+';for(const [id,attrs] of Object.entries(initialGraphicState))for(const [name,value]of Object.entries(attrs))document.getElementById(id).setAttribute(name,value);for(const el of document.querySelectorAll("[pathLength]")){el.setAttribute("stroke-dasharray","1");el.setAttribute("stroke-dashoffset","1")}')
prev=initial
for frame in range(1,219):
 now=state(frame/30)
 for id,attrs in now.items():
  changed={k:v for k,v in attrs.items() if prev[id].get(k)!=v}
  if changed:c.at('tl.to('+json.dumps('#'+id)+',{attr:'+json.dumps(changed)+',duration:0.033333333,ease:"none",immediateRender:false},'+str((frame-1)/30)+');')
 prev=now
for id,text,event in [('main-label','Genie Ontology','main_label'),('output-label','Genie','output_label')]:
 for n in range(1,len(text)+1):c.at('tl.set('+json.dumps('#'+id)+',{textContent:'+json.dumps(text[:n])+'},'+str(events[event][0]+(events[event][1]-events[event][0])*n/len(text))+');')
c.clip(0,D,body,1);c.write(str(OUT/'index.html'),'assets/ev1/tokens.css',title='Study 01 / opening ontology map');p=OUT/'index.html';p.write_text(p.read_text().replace('window.__timelines["main"] = tl;','window.__timelines=window.__timelines||{};window.__timelines["main"] = tl;'))
(OUT/'timing.json').write_text(json.dumps({'duration':D,'source_in':8,'source_out':8+D,'camera_samples':track,'events':events,'status':'First reconstruction study; geometry partly measured, reveal timing visually fitted; not certified exact'},indent=2))
(OUT/'README.md').write_text('''# Motion study 01 — opening ontology map\n\nReconstructs the 8.000–15.267s graphic from the user-supplied reference. Editable native SVG boxes, paths, text, icon groups and shared camera; no source video is used inside the reconstructed animation. Source video is used only in the comparison player.\n\nCamera bounds were measured from the main card at multiple times; intermediate motion uses monotone cubic interpolation. Reveal timings are fitted from inspected frames. The Genie lamp is a hand-drawn vector approximation and the font is Liberation Sans (Arial-metric compatible); neither is claimed to be the original source asset. Four generic icons are Font Awesome Free 6.x (CC BY 4.0 icons), downloaded from https://github.com/FortAwesome/Font-Awesome. Original source captions and creator mark are excluded from the graphic-only comparison.\n\nThis is a first matching study, not a completed exact replica and not the Fabric adaptation. Timing and camera samples: timing.json.\n''')
print('Built study',D,'seconds')
