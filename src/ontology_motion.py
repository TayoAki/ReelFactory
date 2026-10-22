"""Narration-timed diagrams: persistent objects, eased morphs, drawn connectors and focus."""
import re
class OntologyMotion:
 def __init__(self,c,t):self.c=c;self.t=t;self.events=[]
 def when(self,word,a,z,default):
  word=word.lower();return next((w['s'] for w in self.t['words'] if a<=w['s']<z and re.sub(r'[^a-z0-9]','',w['w'].lower())==word),a+default)
 def tween(self,sel,props,at,d=1,ease='power2.inOut'):
  import json
  self.c.at(f'tl.to("{sel}",{{...{json.dumps(props)},duration:{d:.4f},ease:"{ease}",immediateRender:false}},{at:.4f});')
 def show(self,body,at,dx=0,dy=24,d=.85):
  i=self.c.uid('motion');self.c.at(f'tl.fromTo("#{i}",{{opacity:0,x:{dx},y:{dy},scale:.96}},{{opacity:1,x:0,y:0,scale:1,duration:{d},ease:"power3.out",immediateRender:false}},{at:.4f});');return f'<div id="{i}" style="position:absolute;inset:0;opacity:0;transform-origin:650px 410px">{body}</div>',i
 def icon(self,kind,size=62):
  paths={'customer':'<circle cx="32" cy="18" r="9"/><path d="M13 53v-8c0-18 38-18 38 0v8"/>','order':'<rect x="15" y="9" width="34" height="46" rx="5"/><path d="M24 22h16M24 32h16M24 42h10"/>','shipment':'<path d="M7 21 32 8l25 13v28L32 61 7 49ZM7 21l25 13 25-13M32 34v27M20 15l25 13"/>','warehouse':'<path d="M5 28 32 7l27 21v31H5ZM21 59V34h22v25M5 28h54"/>','database':'<ellipse cx="32" cy="13" rx="23" ry="9"/><path d="M9 13v36c0 13 46 13 46 0V13M9 31c0 13 46 13 46 0"/>','check':'<circle cx="32" cy="32" r="25"/><path d="m18 32 10 10 20-23"/>','meaning':'<circle cx="32" cy="32" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="52" cy="12" r="5"/><circle cx="12" cy="52" r="5"/><circle cx="52" cy="52" r="5"/><path d="m16 16 10 10m12 0 10-10M16 48l10-10m12 0 10 10"/>','link':'<path d="m26 21 8-8c17-17 36 2 19 19l-9 9M38 43l-8 8C13 68-6 49 11 32l9-9M22 42l20-20"/>'}
  return f'<svg width="{size}" height="{size}" viewBox="0 0 64 68" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">{paths.get(kind,paths["meaning"])}</svg>'
 def card(self,n,sub,x,y,w=240,h=142,kind='meaning',cid=None):
  i=cid or self.c.uid('object');return f'<div id="{i}" class="m-object" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><div class="m-icon">{self.icon(kind,45)}</div><div><b>{n}</b><small>{sub}</small></div></div>',i
 def edge(self,path,at,d=1,color='#74c4b3',label='',lx=0,ly=0,flow=True):
  i=self.c.uid('stroke');dot=self.c.uid('flow');markup=f'<svg class="m-svg" viewBox="0 0 1300 750"><path id="{i}" d="{path}" style="opacity:0" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" pathLength="1"/>'
  self.c.at(f'tl.fromTo("#{i}",{{strokeDasharray:1,strokeDashoffset:1,opacity:0}},{{strokeDashoffset:0,opacity:1,duration:{d},ease:"power2.inOut",immediateRender:false}},{at:.4f});')
  # A short illuminated dash follows the already-drawn route. All motion is renderer-seekable.
  if flow:
   markup+=f'<path id="{dot}" d="{path}" style="opacity:0" fill="none" stroke="#ffcf83" stroke-width="6" stroke-linecap="round" pathLength="1"/>'
   self.c.at(f'tl.fromTo("#{dot}",{{strokeDasharray:"0.06 0.94",strokeDashoffset:.07,opacity:0}},{{strokeDashoffset:-1,opacity:1,duration:1.65,ease:"none",immediateRender:false}},{at+d:.4f});');self.tween('#'+dot,{'opacity':0},at+d+1.55,.3)
  markup+='</svg>'
  if label:
   m,_=self.show(f'<div class="m-edge-label" style="left:{lx}px;top:{ly}px">{label}</div>',at+d*.5,dy=5,d=.6);markup+=m
  return markup
 def camera(self,body,a,z,scale=1.035):
  i=self.c.uid('camera');self.c.at(f'tl.fromTo("#{i}",{{scale:1}},{{scale:{scale},duration:{max(.1,z-a):.4f},ease:"sine.inOut",immediateRender:false}},{a:.4f});');return f'<div id="{i}" class="m-stage">{body}</div>'
 def overview(self,a,z):
  center,cid=self.card('Ontology','Shared business meaning',470,330,w=360,h=150,kind='meaning');body,_=self.show(center,a+.15,dy=35,d=1.1)
  specs=[('Concepts','Customer · Order',75,235,'customer',1.5,'M315 306 C380 306 380 380 470 400'),('Properties','Status · Delivery time',75,510,'order',3.4,'M315 581 C390 581 390 450 470 415'),('Relationships','Places · Fulfills',955,370,'link',5.6,'M830 405 C890 405 890 441 955 441')]
  for name,sub,x,y,kind,delay,path in specs:
   card,_=self.card(name,sub,x,y,w=315 if name=='Relationships' else 240,kind=kind);re,_=self.show(card,a+delay,dx=-30 if x<400 else 30,dy=0,d=1);body+=re+self.edge(path,a+delay+.55,d=1,flow=True)
  self.events.append(dict(scene='overview',device='Hub builds into connected business context',start=a,end=z));return self.camera(body,a,z,1.02)
 def entities(self,a,z):
  body='';ids=[];names=['Customer','Order','Shipment','Warehouse']
  for k,name in enumerate(names):
   card,i=self.card(name,'Entity type',60+310*k,310,w=250,h=155,kind=name.lower());ids.append(i);at=self.when(name,a,z,2+k*.45);re,_=self.show(card,max(a+.2,at-.35),dy=40,d=.9);body+=re
  focus=self.when('particular',a,z,5.3)
  for k,i in enumerate(ids):
   if k!=2:self.tween('#'+i,{'opacity':.13,'scale':.9},focus,1)
   else:self.tween('#'+i,{'x':-520,'y':25,'scale':1.08,'borderColor':'#f2be71'},focus,1.2)
  p=self.c.uid('property');rows=['<strong>Shipment 17</strong>','<span>Instance <b>17</b></span>','<span>Status <b>Late</b></span>','<span>Promised delivery <b>14:00</b></span>'];prop=f'<div id="{p}" class="property" style="left:690px;top:220px;width:520px">'+''.join(f'<div id="{p}r{k}">{r}</div>' for k,r in enumerate(rows))+'</div>';re,_=self.show(prop,focus+.4,dx=80,dy=0,d=1.15);body+=re+self.edge('M430 410 C540 410 540 335 690 335',focus+.3,d=1.2,flow=False)
  for k,word in [(1,'instance'),(2,'status'),(3,'promised')]:
   at=self.when(word,a,z,7+k);self.c.at(f'tl.fromTo("#{p}r{k}",{{opacity:0,y:12}},{{opacity:1,y:0,duration:.7,ease:"power2.out",immediateRender:false}},{max(focus+.6,at-.2):.4f});')
  self.events.append(dict(scene='entities',device='Four types persist; selected Shipment moves into the property inspection',start=a,end=z));return body
 def graph(self,a,z,trace=False):
  body='';ids=[];pos=[('Customer','Customer 101',65,255),('Order','Order 42',510,255),('Shipment','Shipment 17',955,255),('Warehouse','Warehouse 2',955,555)]
  for k,(n,s,x,y) in enumerate(pos):
   card,i=self.card(n,s,x,y,w=260,h=135,kind=n.lower());ids.append(i);body+=card.replace('class="m-object" style="','class="m-object" style="opacity:.25;')
  # The overview exists at the cut; relationships build as their verbs are spoken.
  if not trace:
   for i in ids:self.c.at(f'tl.fromTo("#{i}",{{opacity:.25}},{{opacity:1,duration:.9,ease:"power2.inOut",immediateRender:false}},{a+.15:.4f});')
   specs=[('places','M325 322 C390 322 445 322 510 322',355,275),('fulfills','M955 322 C895 322 830 322 770 322',790,275),('dispatches','M1085 555 C1085 495 1085 450 1085 390',1100,455)]
   for k,(word,path,x,y) in enumerate(specs):
    at=self.when(word,a,z,2+k*2)-.25;body+=self.edge(path,at,d=1.1,label=word,lx=x,ly=y)
    # The visual spotlight follows the relationship currently being described.
    involved=([0,1],[1,2],[2,3])[k]
    for j,i in enumerate(ids):self.tween('#'+i,{'opacity':1 if j in involved else .28,'borderColor':'#f2be71' if j in involved else '#466b6d'},at,.85)
   for i in ids:self.tween('#'+i,{'opacity':1,'borderColor':'#70baaa'},z-1.4,1)
  else:
   body+=self.edge('M325 322 L510 322',a,.65,label='places',lx=355,ly=275,flow=False)+self.edge('M955 322 L770 322',a,.65,label='fulfills',lx=790,ly=275,flow=False)+self.edge('M1085 555 L1085 390',a,.65,label='dispatches',lx=1100,ly=455,flow=False)
   for i in ids:self.tween('#'+i,{'opacity':.24},a,.6)
   stages=[(2,a+.5),(1,self.when('order',a,z,1.8)),(0,self.when('customer',a,z,3.4))]
   for j,at in stages:self.tween('#'+ids[j],{'opacity':1,'borderColor':'#ffc76a','backgroundColor':'#4b4030'},at,1)
   body+=self.edge('M955 322 C890 322 830 322 770 322',a+1,d=1.4,color='#ffc76a',flow=True)+self.edge('M510 322 C445 322 390 322 325 322',a+2.6,d=1.4,color='#ffc76a',flow=True)
   msg='<div style="position:absolute;left:80px;top:545px;color:#ffd08a;font-size:38px;line-height:1.4">Shipment 17 is late.<br>Follow the connections to Customer 101.</div>';re,_=self.show(msg,a+4.6,dy=20,d=1);body+=re
  self.events.append(dict(scene='trace' if trace else 'relationships',device='Verb-timed lines, moving route highlight, selective dimming',start=a,end=z));return self.camera(body,a,z,1.025)
 def flow(self,a,z,items,lower=''):
  body='';ids=[];points=[85,530,975]
  for k,(name,desc,kind) in enumerate(items):
   card,i=self.card(name,desc,points[k],305,w=250,h=180,kind=kind);ids.append(i);re,_=self.show(card,a+.25+k*1.35,dx=-45,dy=0,d=1.1);body+=re
   if k:body+=self.edge(f'M{points[k-1]+250} 395 C{points[k-1]+330} 395 {points[k]-80} 395 {points[k]} 395',a+.7+(k-1)*1.35,d=1.25)
  if lower:
   card,i=self.card('Eventhouse','Live shipment updates',780,565,w=410,h=120,kind='database');re,_=self.show(card,a+4.3,dx=40,dy=0,d=1);body+=re+self.edge('M655 485 C655 625 680 625 780 625',a+4.6,d=1.1)
   label,_=self.show('<div style="position:absolute;left:90px;top:595px;width:530px;font-size:27px;color:#efd0a0">The data stays in its source.</div>',a+5.1,dy=12);body+=label
  # Guide focus over the complete flow after it has been assembled.
  if z-a>6:
   for k,i in enumerate(ids):self.tween('#'+i,{'borderColor':'#ffd08a','backgroundColor':'#345457'},a+4.8+k*.55,.7)
  self.events.append(dict(scene='bindings' if lower else 'verification',device='Rounded source icons, curved drawn connectors, travelling data pulse',start=a,end=z));return self.camera(body,a,z,1.02)
 def steps(self,a,z,items):
  body='<div style="position:absolute;left:175px;top:340px;width:935px;height:2px;background:#547e7b"></div>'
  for k,(name,desc) in enumerate(items):
   i=self.c.uid('step');x=80+k*420;card=f'<div id="{i}" style="position:absolute;left:{x}px;top:250px;width:290px;opacity:.25"><div style="width:150px;height:150px;border:2px solid #76b6a9;border-radius:50%;background:#18333b;margin:auto;display:grid;place-items:center;color:#e7c38a">{self.icon(["meaning","database","check"][k],70)}</div><b style="display:block;text-align:center;font-size:34px;margin-top:30px">{name}</b><p style="font-size:23px;line-height:1.5;text-align:center;color:#b7d1c9">{desc}</p></div>';body+=card
   at=a+.25+k*max(1.2,(z-a-1)/3);self.tween('#'+i,{'opacity':1,'y':-8},at,1)
   if k:self.tween('#'+prev,{'opacity':.42,'y':0},at,1)
   prev=i
  self.events.append(dict(scene='recap',device='Timeline steps stay in place; active step brightens while previous step dims',start=a,end=z));return body
 def docs(self,a,z):
  i=self.c.uid('doc');body=f'<div style="position:absolute;left:35px;top:190px;width:1230px;height:500px;overflow:hidden;border-radius:14px;background:#fff"><img id="{i}" src="assets/media/entity-doc.png" style="position:absolute;width:1230px;height:auto;left:0;top:0;transform-origin:55% 42%"></div>'
  self.c.at(f'tl.fromTo("#{i}",{{scale:1,x:0,y:0}},{{scale:1.36,x:-80,y:-25,duration:{min(3.8,z-a-1)},ease:"power2.inOut",immediateRender:false}},{a+.4:.4f});')
  self.events.append(dict(scene='documentation',device='Smooth continuous camera push from source context into property-column bindings',start=a,end=z));return body
