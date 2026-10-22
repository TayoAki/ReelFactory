"""Editable vector display-list scenes for the complete reference.
Coordinates are in decoded source pixels, rendered at 3x. Product UI is a separate authentic evidence layer.
"""
from pathlib import Path
from functools import lru_cache
import math,json,io
from PIL import Image,ImageDraw,ImageFont,ImageOps
R=Path(__file__).resolve().parent;A=R/'assets';S=3;W,H=1920,1080
DARK='#1b3038';WHITE='#fbfdfb';TEAL='#70c3c3';PALE='#c6dfe0';INK='#f1f5f5';RED='#f56a58';BROWN='#280c00'
def clamp(x):return max(0,min(1,x))
def ease(x):x=clamp(x);return x*x*(3-2*x)
def reveal(t,a,d=.65):return ease((t-a)/d)
@lru_cache(None)
def rgb(c):return tuple(Image.new('RGB',(1,1),c).getpixel((0,0)))
def blend(a,b,f):return tuple(round(x*(1-f)+y*f) for x,y in zip(rgb(a),rgb(b)))
@lru_cache(None)
def font(size,bold=False,serif=False):return ImageFont.truetype(str(A/('serif.ttf' if serif else 'bold.ttf' if bold else 'sans.ttf')),max(1,round(size)))
@lru_cache(None)
def icon_image(name,size,color='light'):
 p=A/(name+'-'+color+'.png')
 if not p.exists():p=A/'document-light.png'
 return Image.open(p).convert('RGBA').resize((max(1,int(size)),max(1,int(size))),Image.Resampling.LANCZOS)
class C:
 def __init__(self,bg=DARK,camera=(1,0,0)):
  self.bg=bg;self.im=Image.new('RGB',(1374,786),bg);self.d=ImageDraw.Draw(self.im);self.z,self.tx,self.ty=camera
  if bg=='white':
   for q in range(0,1374,95):self.d.line((q,0,q,786),fill='#f1f3ee',width=1)
   for q in range(0,786,95):self.d.line((0,q,1374,q),fill='#f1f3ee',width=1)
 def xy(self,x,y):return ((x*self.z+self.tx)*S,(y*self.z+self.ty)*S)
 def color(self,c,a=1):return blend(self.bg,c,clamp(a))
 def rect(self,x,y,w,h,fill=None,stroke=None,r=4,a=1,width=1):
  if a<=0 or w<=0 or h<=0:return
  xx,yy=self.xy(x,y);ww,hh=w*self.z*S,h*self.z*S;self.d.rounded_rectangle((round(xx),round(yy),round(xx+ww),round(yy+hh)),radius=max(0,round(r*self.z*S)),fill=self.color(fill,a) if fill else None,outline=self.color(stroke,a) if stroke else None,width=max(1,round(width*self.z*S)))
 def text(self,text,x,y,size=10,color=INK,bold=False,a=1,anchor='la',serif=False,width=None,leading=1.17):
  if a<=0:return
  f=font(size*self.z*S,bold,serif);xx,yy=self.xy(x,y)
  if width:
   words=text.split();lines=[];line=''
   for word in words:
    trial=(line+' '+word).strip()
    if line and self.d.textlength(trial,font=f)>width*self.z*S:lines.append(line);line=word
    else:line=trial
   if line:lines.append(line)
   text='\n'.join(lines)
  self.d.multiline_text((round(xx),round(yy)),text,font=f,fill=self.color(color,a),anchor=anchor,spacing=round(size*self.z*S*(leading-1)),align='center' if anchor.startswith('m') else 'left',stroke_width=0)
 def icon(self,name,x,y,size=20,a=1,color='light'):
  if a<=0:return
  xx,yy=self.xy(x,y);im=icon_image(name,round(size*self.z*S),color)
  if a<1:im=im.copy();im.putalpha(im.getchannel('A').point(lambda p:round(p*a)))
  self.im.paste(im,(round(xx),round(yy)),im)
 def genie(self,x,y,size=26,a=1):
  im=Image.open(A/'genie.png').convert('RGBA').resize((max(1,round(size*self.z*S)),max(1,round(size*self.z*S*.83))),Image.Resampling.LANCZOS);xx,yy=self.xy(x,y)
  if a<1:im.putalpha(im.getchannel('A').point(lambda p:round(p*a)))
  self.im.paste(im,(round(xx),round(yy)),im)
 def wire(self,points,p=1,color=TEAL,a=1,width=1.1,arrow=False):
  if p<=0 or a<=0:return
  pts=[self.xy(*q) for q in points];lengths=[math.dist(pts[i],pts[i+1]) for i in range(len(pts)-1)];remaining=sum(lengths)*clamp(p);out=[pts[0]]
  for i,length in enumerate(lengths):
   if remaining>=length:out.append(pts[i+1]);remaining-=length
   else:
    if length:out.append(tuple(pts[i][j]+(pts[i+1][j]-pts[i][j])*remaining/length for j in [0,1]))
    break
  if len(out)>1:self.d.line(out,fill=self.color(color,a),width=max(1,round(width*S*self.z)),joint='curve')
  if arrow and p>=.99 and len(pts)>1:
   x,y=pts[-1];px,py=pts[-2];ang=math.atan2(y-py,x-px);r=4*S*self.z;self.d.polygon([(x,y),(x-r*math.cos(ang-.45),y-r*math.sin(ang-.45)),(x-r*math.cos(ang+.45),y-r*math.sin(ang+.45))],fill=self.color(color,a))
 def dot(self,x,y,r=2,color=TEAL,a=1):
  xx,yy=self.xy(x,y);r=r*S*self.z;self.d.ellipse((xx-r,yy-r,xx+r,yy+r),fill=self.color(color,a))
 def card(self,x,y,w,h,title,body='',icon=None,a=1,pale=False,accent=False):
  fill=PALE if pale else '#0c303c' if not accent else '#234b52';self.rect(x,y,w,h,fill=fill,stroke=None,r=5,a=a);fg='#28434a' if pale else INK;muted='#425c61' if pale else '#bdd4d7'
  if icon:self.icon(icon,x+8,y+8,min(18,h*.28),a,'dark' if pale else 'teal')
  tx=x+8+(24 if icon and h<65 else 0);ty=y+9+(22 if icon and h>=65 else 0)
  self.text(title,tx,ty,9 if w>110 else 8.5,fg,True,a,width=w-(tx-x)-7)
  if body:self.text(body,x+8,y+46 if icon and h>=65 else y+29 if icon else y+25,7.5,muted,a=a,width=w-16)
 def pill(self,x,y,w,label,a=1,active=False):self.rect(x,y,w,17,fill='#007b7f' if active else '#0c2631',r=8,a=a);self.text(label,x+8,y+4,7.3,INK,a=a)
 def group(self,t,a,x,y,w,h,title,body='',icon=None,pale=False):
  p=reveal(t,a);self.card(x,y+(1-p)*7,w,h,title,body,icon,p,pale);return p
 def photo(self,src,box):
  x,y,w,h=box;im=Image.open(src).convert('RGB').resize((round(w*S*self.z),round(h*S*self.z)),Image.Resampling.LANCZOS);xx,yy=self.xy(x,y);self.im.paste(im,(round(xx),round(yy)))

def stage(theme='dark',speaker='guest'):
 if theme=='white':im=Image.new('RGB',(W,H),'white');grid='#edf0ec'
 else:im=Image.new('RGB',(W,H),BROWN);grid='#482611'
 d=ImageDraw.Draw(im)
 for x in range(0,W,96):d.line((x,0,x,H),fill=grid,width=1)
 for y in range(0,H,96):d.line((0,y,W,y),fill=grid,width=1)
 if theme!='white':d.rounded_rectangle((36,150,1410,936),radius=51,fill=DARK)
 tile=Image.open(A/(speaker+'-tile.png')).convert('RGBA');x,y=(1425,273) if theme=='white' else (1446,252);tile=tile.resize((435,537));mask=Image.new('L',tile.size);ImageDraw.Draw(mask).rounded_rectangle((0,0,434,536),radius=39,fill=255);im.paste(tile,(x,y),mask)
 d=ImageDraw.Draw(im);d.rectangle((0,0,W-1,H-1),outline='#ff6600',width=9);return im
@lru_cache(None)
def base(theme='dark',speaker='guest'):return stage(theme,speaker)
def finish(c,theme='dark'):
 im=base(theme).copy();mask=Image.new('L',c.im.size);ImageDraw.Draw(mask).rounded_rectangle((0,0,c.im.width-1,c.im.height-1),radius=51 if theme=='dark' else 0,fill=255);im.paste(c.im,(36,150),mask);return im

def master(c,t,highlight=None,dim=.95):
 c.text('Business & Technical Users',230,10,7.5,a=dim,anchor='ma');c.wire([(58,15),(405,15)],a=.45)
 for x,w,title in [(58,156,'Genie  ONE · AGENTS · CODE'),(220,94,'Agent Bricks'),(320,85,'Any Agent / Client / App')]:c.rect(x,26,w,28,stroke='#6b7660',a=dim);c.text(title,x+w/2,35,7.4,bold=True,a=dim,anchor='ma')
 c.rect(58,72,347,118,stroke='#486c70',a=dim);c.genie(202,76,17,dim);c.text('Genie Ontology',238,79,10,bold=True,a=dim,anchor='ma');c.text('Continuously learned context for enterprise AI',232,94,6.9,RED,a=dim,anchor='ma')
 c.text('Learned\nOntology',68,120,10,bold=True,a=dim if highlight!='modeled' else .2);c.text('Modeled\nOntology',377,120,10,bold=True,a=dim if highlight!='learned' else .2,anchor='ma');c.text('Metric views, pages\nand domains',377,147,7.1,a=dim,anchor='ma')
 # Stable deterministic knowledge map: no random frame-to-frame movement.
 points=[]
 for i in range(20):ang=i*2.39996;rad=15+(i%5)*5;points.append((232+math.cos(ang)*rad,143+math.sin(ang)*rad*.58))
 for i,(x,y) in enumerate(points):
  for j in [(i+3)%20,(i+7)%20]:c.wire([(x,y),points[j]],color='#557d7d',a=dim*.5,width=.5)
 for i,(x,y) in enumerate(points):c.dot(x,y,2 if i%4 else 3,RED if i%4==0 else '#668f91',dim)
 for x,y,text in [(231,110,'Authority'),(188,164,'Relevance'),(278,164,'Permissions')]:c.text(text,x,y,6.5,'#b6a64b',a=dim,anchor='ma')
 c.text('OntoRank',232,177,7,bold=True,a=dim,anchor='ma');c.rect(58,195,347,18,stroke='#367a77',a=dim);c.text('Unity Catalog       ·       Unity Gateway',232,200,7,a=dim,anchor='ma')
 c.rect(58,218,347,37,stroke='#3c6b7a',a=dim)
 for i,text in enumerate(['Lakehouse Data','Federated Data','Workspace Assets','Business Apps & Knowledge']):
  x=64+i*86;c.text(text,x+40,222,6,a=dim,anchor='ma');c.icon(['database','globe','document','plug'][i],x+30,233,13,dim)
 for x in [135,265,360]:c.wire([(x,72),(x,56)],arrow=True,a=dim*.6)

def feature(c,title,points,active=0):
 c.text(title,24,57,17,bold=True,width=133)
 for i,text in enumerate(points):c.pill(22,117+i*23,146,text,1 if active==i else .65,active==i)

def native(scene,t):
 id=scene['id'];a=scene['source_start'];theme='white' if id in ['wrong-source','ambiguity','context-repair'] else 'dark';c=C('white' if theme=='white' else DARK);dark=theme=='dark';fg=INK if dark else '#4e4c45';muted='#aac4c8' if dark else '#726a61';peach='#ffdabd'
 if scene['kind']=='speaker':
  who='host' if id in ['opening','host-topic','host-benchmark','host-memory','host-outcomes','host-governance','host-start'] else 'guest'
  im=Image.open(A/(who+'-full.png')).convert('RGB').copy();d=ImageDraw.Draw(im)
  if id=='closing':
   g=ImageOps.fit(Image.open(A/'guest-full.png'),(960,1080));h=ImageOps.fit(Image.open(A/'host-full.png'),(960,1080));im.paste(g,(0,0));im.paste(h,(960,0));d=ImageDraw.Draw(im)
  if id=='host-topic' and t>=28:d.text((1240,205),'Genie Ontology',font=font(48,True),fill='white',stroke_width=2,stroke_fill='#172129')
  if id=='host-outcomes':
   for i,(tm,label) in enumerate([(1229,'Visibility'),(1238,'Business context')]):
    p=reveal(t,tm);x,y=55,150+i*100;d.rounded_rectangle((x,y,x+390*p,y+65),radius=28,fill=blend('#24313a','#526451',p));
    if p>.4:d.text((x+25,y+12),label,font=font(30,True),fill='white')
  d.rectangle((0,0,W-1,H-1),outline='#ff6600',width=9);return im
 if scene['kind']=='chapter':
  title='From answers\nto outcomes' if id=='outcomes-title' else 'Getting started' if id=='getting-started-title' else 'Demo';c=C('#ff3521');c.text(title,30,95,30,bold=True)
  for k in range(3):
   x=305+k*33;c.wire([(x+65,15),(x,115),(x+65,225)],color='#d9291d',width=17,a=.35)
  return finish(c)
 if scene['kind'] in ['demo','demo-overlay']:
  # Preview uses a source still. Final video replaces this region with the moving authentic source UI.
  im=Image.open(A/(id+'-ui.png'));c.photo(A/(id+'-ui.png'),(0,0,458,262)) if False else None
  c.im=im.crop((12,30,470,312)).resize((1374,786),Image.Resampling.LANCZOS);c.d=ImageDraw.Draw(c.im)
  if id=='demo-context-overlay':
   c.rect(6,0,446,128,fill='#fafbf8',r=0)
   for i,(label,ico) in enumerate([('Tables','table'),('Documents','document'),('Metrics','chart'),('Apps','plug')]):
    p=c.group(t,822+i*1.5,55+i*94,15,72,43,label,icon=ico,pale=True);c.wire([(91+i*94,58),(91+i*94,78),(232,78),(232,94)],p)
   c.card(195,95,74,28,'Genie',icon='search',pale=True)
   if t>837:
    for x,txt in [(124,'Definitions'),(270,'Sources')]:c.pill(x,126,95,txt,reveal(t,837),True)
  return finish(c)
 if id=='intro-map':
  c=C(BROWN);z=1+.2*reveal(t,9);c.rect(175,70,110,100,stroke='#b76b38',r=12);c.genie(213,86,38);c.text('Genie Ontology',230,138,10,anchor='ma')
  for i,(ico,tm) in enumerate([('settings',10),('chart',11),('people',12),('document',13)]):
   y=35+i*52;p=reveal(t,tm);c.rect(54,y,24,24,fill='#5c2d0e',stroke='#8e4a21',a=p);c.icon(ico,59,y+5,14,p);c.wire([(78,y+12),(123,y+12),(123,120),(175,120)],p,color='#bd9d7d')
  p=reveal(t,13.7);c.wire([(285,120),(348,120)],p,color='#bd9d7d');c.rect(348,96,65,48,stroke='#b76b38',a=p);c.genie(368,102,24,p);c.text('Genie',381,132,8,a=p,anchor='ma');return finish(c)
 if id in ['wrong-source','ambiguity','context-repair']:
  if id=='wrong-source':
   if t<125:
    for x,tm,title,ico in [(80,115,'User query','globe'),(205,110,'Generic model','search'),(330,118,'Business results','check')]:
     p=reveal(t,tm);c.card(x,105,74,70,title,icon=ico,pale=True,a=p)
    c.wire([(154,140),(205,140)],reveal(t,115.5),color='#867b6c',arrow=True);c.wire([(279,140),(330,140)],reveal(t,118.5),color='#867b6c',arrow=True)
   else:
    for i in range(4):
     x=32+i*75;p=reveal(t,125+i*.3);c.icon('database',x,45,26,p,'red' if i==0 else 'dark');c.text(['First table','Dashboard','Sales','Finance'][i],x+13,78,7,'#5b554c',a=p,anchor='ma')
    c.rect(27,39,38,48,stroke='#df7059');c.dot(67,85,4,'#d74736');c.wire([(45,90),(45,115),(168,115),(168,145)],reveal(t,126),color='#a6774a');c.card(133,146,77,65,'Generic model',icon='search',pale=True)
    p=reveal(t,128);c.rect(341,30,109,193,fill='#20566a',a=p);c.text('Chatbot 1',352,42,9,a=p,bold=True);c.text('What was last\nquarter’s revenue?',352,70,9,a=p);c.text('Last quarter’s revenue\nwas $48.2M.',352,115,9,a=p);c.text('✕ pulled the wrong data',350,194,7.8,'#e58973',a=p)
  elif id=='ambiguity':
   campaign=t>=147
   c.card(173,111,74,64,'Generic model',icon='search',pale=True)
   if not campaign:
    c.card(40,120,73,39,'Free trials',icon='people',pale=True);c.wire([(113,139),(170,139)],reveal(t,139),color='#b19973');c.card(145,200,130,35,'CHURN RATE','Excludes free trials',pale=True);c.wire([(210,175),(210,200)],reveal(t,141),color='#b19973')
   else:
    c.icon('person',190,24,24,color='red');c.card(147,67,126,32,'USER QUERY','Which campaign performed best?',pale=True);c.wire([(210,99),(210,111)],reveal(t,147),color='#b19973');p=reveal(t,152);c.icon('calendar',34,151,23,p,'red');c.text('Campaigns table',46,181,7.8,'#61574c',a=p,anchor='ma');c.wire([(58,165),(173,145)],p,color='#b19973');c.pill(84,152,62,'Stale data',p,True)
   c.rect(326,39,123,190,fill='#20566a');c.text('Chatbot '+('3' if campaign else '2'),337,49,9,bold=True);c.text('Which campaign performed\nbest?' if campaign else 'What’s our churn rate?',336,78,8.4);c.text('Spring Promo performed best.' if campaign else 'Your churn rate is 7.6%.',336,120,8.2);c.text('✕ based on stale data' if campaign else '✕ ignores free trials',337,203,8,RED)
  else:
   if t<183:
    for i,(title,ico) in enumerate([('Table renamed','table'),('Outdated','document'),('Resigned','people')]):c.group(t,174.5+i*2,65+i*127,111,92,63,title,icon=ico,pale=True)
   else:
    for x,y,title,ico,tm in [(60,70,'Company data','database',183),(204,70,'Generic model','search',184),(348,70,'Business results','check',184),(204,193,'Genie','document',189),(60,193,'Context','document',188)]:c.group(t,tm,x,y,80,59,title,icon=ico,pale=True)
    c.wire([(140,98),(204,98)],1,color='#69b947');c.wire([(284,98),(348,98)],1,color='#cc5c53');c.wire([(244,129),(244,193)],reveal(t,189),color='#69b947');c.wire([(140,222),(204,222)],reveal(t,190),color='#c5ab6c')
    if t>=198:
     c.pill(340,188,109,'Data sources',reveal(t,198),True);c.pill(340,220,109,'Definitions',reveal(t,202),True);c.wire([(284,221),(327,221),(327,196),(340,196)],reveal(t,198),color='#ce6d5c');c.wire([(327,221),(340,228)],reveal(t,202),color='#ce6d5c')
  return finish(c,'white')
 if id=='architecture':
  if t<236.1:
   p=reveal(t,234.367,1.733);cam=(1+.76*p,-500*p,-90*p);c=C(camera=cam);master(c,t,'modeled',1-.45*reveal(t,228));
   if t>=221:c.rect(342,111,61,66,stroke=TEAL,a=1 if t<228 else .45)
  else:
   master(c,t,dim=.08);c.text('Modeled\nOntology',102,117,15,bold=True,anchor='ma');c.text('Metric views, pages,\nand domains',102,154,9,anchor='ma');c.card(263,82,114,70,'METRIC VIEWS','Governed KPI definitions\nReusable across questions',icon='chart',pale=True,a=reveal(t,238))
  return finish(c)
 if id=='modeled':
  c.text('Modeled\nOntology',100,115,15,bold=True,anchor='ma');c.text('Metric views, pages,\nand domains',100,151,9,anchor='ma')
  c.group(t,249,252,79,118,71,'METRIC VIEWS','Certified definitions of\nkey business metrics',icon='chart',pale=True)
  if t>=256:
   p=reveal(t,256);c.rect(252,39,183,18,fill='#ffe5be',a=p);c.text('UNITY CATALOG',344,44,8,'#394746',True,p,anchor='ma');c.wire([(312,57),(312,79)],p)
  if t>=263:
   # The metric card shrinks into an equal peer column before Pages appears.
   c.rect(252,79,118,71,fill=DARK);c.card(252,79,86,72,'METRIC VIEWS','Governed reusable\nmetric definitions',icon='chart',pale=True);c.group(t,263,348,79,86,72,'PAGES','Business concepts,\ncontext and meaning',icon='book',pale=True);c.wire([(344,57),(390,57),(390,79)],reveal(t,263))
  if t>=281:
   c.group(t,281,294,169,98,55,'DOMAINS','Logical collections of assets',icon='folder',pale=True);c.wire([(298,151),(298,160),(344,160),(344,169)],reveal(t,282));c.wire([(391,151),(391,160),(344,160)],reveal(t,282))
  if t>=307:
   c.rect(252,237,183,18,fill='#ffe5be',a=reveal(t,307));c.text('AI AGENTS',344,242,8,'#394746',True,reveal(t,307),anchor='ma');c.wire([(344,224),(344,237)],reveal(t,307))
  if t>=315:c.rect(243,24,201,235,stroke='#b3a04c',a=reveal(t,315));c.text('CERTIFIED AUTHORITATIVE BASELINE',344,15,7,'#c7b85e',True,reveal(t,315),anchor='ma')
  return finish(c)
 if id=='learned':
  master(c,t,highlight='learned',dim=.08);c.text('Learned\nOntology',372,117,16,bold=True,anchor='ma')
  if t<353:
   for i,(ico,tm) in enumerate([('table',337),('document',340),('search',343),('book',346)]):x=44+i*67;p=reveal(t,tm);c.icon(ico,x,90,23,p,'teal');c.wire([(x+12,115),(x+12,148),(160,148),(160,179)],p)
   c.card(109,180,106,21,'ONTOLOGY SNIPPETS',pale=True,a=reveal(t,348))
  elif t<379:
   examples=[('JOIN TABLES','A query joins table A & table B',353),('ADD COMMENTS','Additional business explanation',359),('SHARE THE QUERY','Useful knowledge reaches colleagues',365),('POPULAR QUERY','Usage provides a signal',371)]
   for i,(title,body,tm) in enumerate(examples):c.group(t,tm,48,53+i*45,225,36,title,body,'document')
  else:
   for i,(title,body,ico,tm) in enumerate([('BUSINESS RULE','A lead qualifies when a\nmeeting is booked','document',379),('TRUSTED DATA','Revenue comes from the\ncurated Finance catalog','database',386),('METRIC DEFINITION','How our team defines\ncustomer churn','chart',394)]):c.group(t,tm,24+i*94,97,86,83,title,body,ico)
  return finish(c)
 if id=='ranking':
  master(c,t,dim=.48 if 409<t<438 else 1)
  if 409<t<430:
   c.rect(131,64,194,143,fill=DARK);c.genie(179,69,23);c.text('Genie Ontology',242,75,13,bold=True,anchor='ma');
   for i in range(18):ang=i*2.4;rad=24+i%4*9;x=225+math.cos(ang)*rad;y=145+math.sin(ang)*rad*.6;c.wire([(225,145),(x,y)],color='#547d7d',a=.8,width=.7);c.dot(x,y,3 if i%4 else 4,RED if i%4==0 else TEAL)
   for x,y,label in [(225,105,'Authority'),(157,171,'Relevance'),(294,171,'Permissions')]:c.text(label,x,y,8,'#c4b04d',anchor='ma')
   c.text('OntoRank',225,196,11,bold=True,anchor='ma')
  if t>=438:c.rect(45,18,365,44,stroke='#d6b46d');c.text('Consumers share the same context layer',230,66,9,TEAL,anchor='ma')
  return finish(c)
 if id in ['benchmark','benchmark-return']:
  c.text('Superior accuracy and latency',6,18,21,bold=True)
  for j,(title,vals,suffix) in enumerate([('Accuracy',[84.5,52.4,40.5,25.0],'%'),('Runtime',[8,15,7,24],' min')]):
   x=18+j*230;c.rect(x,61,215,155,fill='#2d414c',r=5);c.text(title,x+108,67,10,bold=True,anchor='ma');mx=100 if j==0 else 26
   for i,val in enumerate(vals):
    p=reveal(t,454+i*.15,1) if id=='benchmark' else 1;bh=val/mx*125*p;xx=x+10+i*51;c.rect(xx,204-bh,33,bh,fill='#ff5c48' if i==0 else '#429cda',r=4);c.text((f'{val:.2f}%' if j==0 else f'{int(val)} mins'),xx+16.5,211-bh,6.4,bold=True,anchor='ma');c.text('Genie' if i==0 else f'Agent #{i}',xx+16.5,220,6.8,anchor='ma')
  c.text('Source-reported evaluation on sampled real-world production questions.\nAgents equipped with Databricks DBSQL MCP. Values reproduced for reference study.',17,241,6.7,'#b7c8ce')
  if t>=469 and id=='benchmark':
   c.rect(71,105,151,11,stroke='#76bae2',width=.8);c.text('More than 30 percentage-point improvement',21,98,6.2,'#a6cfe6')
  return finish(c)
 if id=='connectors':
  if t<557:
   for i,(label,ico,body) in enumerate([('Lakehouse Connectors','database','Structured and\nfederated data'),('MCP connections','plug','Query tools live'),('Search connectors','search','Find and rank across\nknowledge sources')]):c.card(25+i*145,126,132,106,label,body,ico,pale=True)
   c.genie(216,33,26)
   for x in [90,235,380]:c.wire([(x,126),(x,76),(230,76),(230,58)],reveal(t,547))
  elif t<604:
   c.card(180,20,102,28,'TEXT TO SQL','Unity Catalog data',icon='table')
   if t<577:
    c.icon('document',201,104,25,color='teal');c.text('Search a document',214,154,11,anchor='ma');c.text('A static answer may not already exist',214,178,8,anchor='ma')
   else:
    for i,(x,title,tm,ico) in enumerate([(114,'Existing documents',577,'document'),(315,'Live operational data',581,'database')]):
     c.icon(ico,x,103,23,reveal(t,tm),'teal');c.pill(x-46,156,120,title,reveal(t,tm));c.text('Read what is documented' if i==0 else 'Calculate what matters now',x+14,187,8,a=reveal(t,tm),anchor='ma')
    if t>=587:c.text('Community connectors',233,230,11,TEAL,True,reveal(t,587),anchor='ma')
  else:
   labels=[('TEXT TO SQL',604),('MCP CONNECTORS',615),('SEARCH INDEX',640)]
   for i,(label,tm) in enumerate(labels):c.group(t,tm,29+i*147,15,127,26,label,icon=['table','plug','search'][i])
   for i,(name,ico) in enumerate([('Data','database'),('Documents','document'),('Jira','calendar'),('CRM','people')]):
    p=reveal(t,604+i*.5);c.rect(28,67+i*41,22,22,fill=PALE,a=p);c.icon(ico,32,71+i*41,14,p,'dark');c.text(name,57,74+i*41,7.5,a=p);c.wire([(94,78+i*41),(135,78+i*41),(135,142),(185,142)],p)
   c.rect(185,116,50,51,stroke=TEAL);c.icon('database',200,130,21,color='teal');c.wire([(235,142),(340,142)],reveal(t,610),arrow=True);c.rect(340,126,105,30,stroke=TEAL);c.text('Query live data',392,136,9,anchor='ma')
   if t>=624:c.icon('plug',273,129,23,reveal(t,624),'teal')
   if t>=644:
    c.pill(239,63,133,'Search index',reveal(t,644),True);c.wire([(306,80),(306,142)],reveal(t,644));c.pill(228,209,155,'Source permissions respected',reveal(t,652),True);c.wire([(306,166),(306,209)],reveal(t,652));c.icon('shield',293,181,17,reveal(t,652),'teal')
  return finish(c)
 if id=='skills' and 1363<=t<1380:
  c.text('Save repeatable\ntasks as skills',268,42,17,bold=True)
  c.pill(277,105,158,'Skill sharing and version control',1,True)
  c.pill(277,130,158,'UC for governance')
  c.genie(74,25,28);c.text('Genie One',88,57,9,anchor='ma')
  c.wire([(88,78),(88,110)],reveal(t,1363));c.card(31,110,115,34,'UNITY GATEWAY',icon='shield')
  for j in range(3):
   y=179+j*28;c.icon('people',180,y,18,color='teal');c.wire([(88,144),(88,y+8),(180,y+8)],reveal(t,1364+j*.6))
  return finish(c)
 if id in ['memory','documents','skills','agent-intro','orchestration','surfaces']:
  configs={'memory':('Save personal\nmemory',['Preferences, definitions, etc.','Cross-chat persistence'],[679,696]),'documents':('Collaborate\non docs',['Ask Genie to draft documents','Start from a template','Use tools to send it','Collaborate in comments'],[1266,1273,1280,1287]),'skills':('Save repeatable\ntasks as skills',['Skill sharing and version control','UC for governance'],[1355,1363]),'agent-intro':('Build custom\nagents',['Create context, instructions, and skills','Then run work with colleagues'],[1464,1470]),'orchestration':('Orchestrate\nautomatically',['Schedule tasks','Use event-based triggers','Monitor and improve your workflows'],[1523,1533,1543]),'surfaces':('Use Genie\nhowever you want',['Use Genie on iOS and Android','Use Genie in desktop apps','Explore in Slack, Teams, Sheets, Excel','Use Genie via MCP and API'],[1553,1576,1584,1594])}
  title,points,times=configs[id];active=max([i for i,tm in enumerate(times) if t>=tm] or [0]);feature(c,title,points,active)
  crop=ui_box(id);src=Image.open(A/(id+'-ui.png')).crop((crop[0],crop[1],crop[0]+crop[2],crop[1]+crop[3]));c.im.paste(src.resize((crop[2]*3,crop[3]*3),Image.Resampling.LANCZOS),((crop[0]-12)*3,(crop[1]-50)*3));return finish(c)
 if id=='external-tools':
  feature(c,'Take action on\nthird-party tools',['Write via MCP','Control permissions for each tool'])
  for i,(title,ico) in enumerate([('SharePoint','document'),('Drive','folder'),('Slack','people'),('Jira','calendar'),('Confluence','book'),('Gmail','mail'),('GitHub','code'),('CRM','building')]):x=230+i%3*75;y=40+i//3*70;c.icon(ico,x,y,25,color='teal');c.text(title,x+13,y+33,8,anchor='ma')
  return finish(c)
 if id=='actions':
  feature(c,'Take action on\nthird-party tools',['Write via MCP','Control permissions at each level'])
  c.genie(293,22,28);c.icon('plug',299,82,23,color='teal');c.wire([(310,50),(310,82)],reveal(t,1318),arrow=True);c.wire([(310,105),(310,142)],reveal(t,1321),arrow=True);c.card(253,143,114,29,'UNITY GATEWAY',icon='shield',a=reveal(t,1321));c.wire([(253,157),(225,157),(225,218),(310,218)],reveal(t,1326));c.icon('lock',213,174,17,reveal(t,1326),'teal');c.icon('plug',299,207,22,reveal(t,1326),'teal')
  if t>=1332:
   c.wire([(367,157),(400,157),(400,117)],reveal(t,1332));c.wire([(400,157),(400,219)],reveal(t,1332))
   for i,(color,label) in enumerate([('#81c75a','Allowed'),('#d95044','Denied'),('#81c75a','This branch')]):y=125+i*35;c.dot(400,y,4,color,reveal(t,1332+i));c.text(label,411,y-4,7.5,a=reveal(t,1332+i))
  return finish(c)
 if id=='governance':
  p=reveal(t,1429.23,.6);y=130-95*p;c.rect(134,y,191,20,fill='#007b7f');c.text('Governance Demands for Skills',229,y+5,9,bold=True,anchor='ma')
  data=[('Baseline Skills','Give every team a standard\nset of skills','settings',1430.53),('Custom Workflows','Tailor Genie to company\nprocesses','flow',1444),('Skill-Sharing Controls','Control how users share\nskills','shield',1452)]
  for i,(title,body,ico,tm) in enumerate(data):
   p=reveal(t,tm,.9);w=89*max(.02,p);x=55+i*135+(89-w)/2
   if p>0:c.rect(x,94,w,91,fill=PALE,r=7)
   if p>.65:c.icon(ico,84+i*135,113,26,(p-.65)/.35,'dark');c.text(title,99+i*135,146,8.3,'#31565b',True,(p-.65)/.35,anchor='ma');c.text(body,99+i*135,161,7,'#4d696c',a=(p-.65)/.35,anchor='ma')
  return finish(c)
 if id=='agents':
  if t<1484:
   for i,(title,ico) in enumerate([('Sources','database'),('Instructions','document'),('Skills','settings'),('Memory','book')]):
    x=70+i*88;p=reveal(t,1475+i*.65);c.card(x,40,63,55,title,icon=ico,a=p);c.wire([(x+32,95),(x+32,129),(234,129),(234,164)],p)
   c.genie(218,168,33);c.text('Custom Genie Agent',235,217,12,bold=True,anchor='ma')
  elif t<1503:
   c.rect(315,16,83,76,stroke=TEAL,a=1);c.genie(341,24,30);c.text('Custom Genie\nAgent',357,58,9,bold=True,anchor='ma')
   for i,(title,body,tm) in enumerate([('RENEWALS AGENT','Prepare teams for QBRs',1484),('LAUNCH AGENT','Track feature status',1493),('FINANCE AGENT','Answer questions about KPIs',1496)]):
    x=23+i*145;p=reveal(t,tm);c.card(x,195,130,40,title,body,icon='document',a=p);c.wire([(357,92),(357,153),(x+65,153),(x+65,195)],p)
  else:
   c.rect(195,10,74,60,stroke=TEAL);c.genie(219,19,26);c.text('Genie One',232,53,8,anchor='ma');c.wire([(232,70),(232,105)],1)
   c.rect(195,106,74,66,stroke=TEAL);c.genie(219,115,26);c.text('Genie Agents',232,150,8,anchor='ma');c.wire([(232,172),(232,208)],reveal(t,1510));
   for i,(title,tm) in enumerate([('Volume connections',1511),('MCP connectors',1517)]):c.pill(304,127+i*29,133,title,reveal(t,tm),True);c.wire([(269,140+i*16),(304,135+i*29)],reveal(t,tm))
   for x in [80,232,384]:c.wire([(232,208),(x,208),(x,255)],reveal(t,1510))
  return finish(c)
 if id=='starting-summary':
  cards=[('1','Pick a workflow','Choose one team, a recurring workflow,\nand a few common questions.'),('2','Ground the data','Certify the short list of concepts,\nand let Genie learn the long tail.'),('3','Land and expand','Launch with the team, iterate on gaps,\nand expand to the next workflows.')]
  for i,(n,title,body) in enumerate(cards):
   p=reveal(t,1796.5+i*.6);x=13+i*150;c.rect(x,38,140,185,fill='#2e444d',r=3,a=p);c.text(n,x+70,54,18,bold=True,a=p,anchor='ma');c.text(title,x+12,98,11,RED,True,p);c.text(body,x+12,122,8.8,a=p,width=116)
  return finish(c)
 if id in ['rollout-one','rollout-two']:
  milestones=[('Pick One Team\n& Workflow','people',1805),('Find Benchmarking\nQuestions','search',1825),('Record Current\nBaseline','chart',1848),('Bring Domain\nExperts','settings',1871),('Connect Your\nSources','database',1890),('Roll Out to\nthe Team','people',1932)]
  active=max([i for i,(_,_,tm) in enumerate(milestones) if t>=tm] or [0]);pan=80*reveal(t,1932,1);xs=[40+i*90-pan for i in range(6)]
  if t<1825:
   c.dot(227,40,3);c.icon('people',215,56,25,color='teal');c.text('Pick One Team\n& Workflow',227,91,10,bold=True,anchor='ma')
   for i,(title,body,ico) in enumerate([('LEGAL','Review incoming contracts','book'),('FINANCE','Produce monthly budgets','building'),('SALES','Prepare account briefs','settings')]):c.group(t,1807+i*.2,38+i*142,158,105,40,title,body,ico,pale=True)
  else:
   c.wire([(xs[0],32),(xs[active],32)],1,a=.65)
   for i,(title,ico,tm) in enumerate(milestones):
    if t<tm:continue
    alpha=1 if i==active else .55;c.dot(xs[i],32,2.5,a=alpha);c.icon(ico,xs[i]-9,44,18,alpha,'teal');c.text(title,xs[i],68,7.4,a=alpha,anchor='ma')
   details={1:[('Questions','Representative real questions'),('Known answers','Definitions and sources'),('Reasoning','What should be used?')],2:[('Track accuracy in the existing process','How long does it take?'),('Where do people get stuck?','Straightforward and ambiguous cases')],3:[('Write benchmarking questions','Understand team, workflow & data')],4:[('SharePoint','Gmail'),('Jira','Slack')],5:[('Track successes and failures','Identify where Genie gets confused'),('Find gaps in the ontology','Refine business semantics')]}
   if active==1:
    for i,(title,body) in enumerate(details[1]):c.card(58+i*126,131,111,57,title,body,icon='document',pale=True);c.wire([(114+i*126,188),(114+i*126,213),(240,213),(240,235)])
    c.genie(228,234,25)
   elif active==4:
    for i,(name,ico) in enumerate([('SharePoint','document'),('Gmail','mail'),('Jira','calendar'),('Slack','people')]):c.card(48+i*106,133,73,55,name,icon=ico,pale=True)
    for i,label in enumerate(['Read','Write','Add instructions']):c.pill(100+i*116,222,100,label,reveal(t,1901+i*6),True)
   else:
    dd=details.get(active,[])
    for row,pair in enumerate(dd):
     for col,label in enumerate(pair):c.card(44+col*207,135+row*50,187,33,label,icon=['search','document','book','settings'][(row*2+col)%4])
  return finish(c)
 if id=='best-practices':
  c.text('Best\npractices',19,20,25,bold=True)
  items=[('Build a benchmark set','Test representative questions and known-good answers'),('Model critical semantics','Define essential KPIs in Metric Views and concepts in Pages'),('Certify gold assets','Mark authoritative tables, dashboards, queries, and Genie Agents'),('Connect your sources','Give Genie access to the data and context each workflow requires'),('Validate access end to end','Ensure users can see every source and certified asset Genie needs')]
  active=-1 if t<1963 else 0 if t<1989.733 else 1 if t<2006 else 2 if t<2019 else 3 if t<2029 else 4
  for i,(title,body) in enumerate(items):
   alpha=1 if active in [-1,i] else .55;y=22+i*47;c.text(str(i+1),166,y,19,bold=True,a=alpha);c.wire([(181,y-3),(181,y+34)],color='#45636c',a=alpha);c.text(title,194,y,11.5,'#ee897e',True,alpha);c.text(body,194,y+15,8.7,a=alpha,width=251)
  return finish(c)
 return finish(c,theme)

def ui_box(id):
 return {'memory':(168,55,300,250),'documents':(174,95,294,205),'skills':(220,90,248,210),'agent-intro':(185,100,283,200),'orchestration':(190,86,278,214),'surfaces':(180,75,288,225)}.get(id,(12,30,458,282))

def cache_time(scene,t):
 # Identical hold frames are reused. Animation remains 30fps near events and camera moves.
 extras={'intro-map':[9,10,11,12,13,13.7],'wrong-source':[110,115.5,118.5,126],'ambiguity':[139,141,152],'context-repair':[176.5,178.5,183,188,190,198],'architecture':[238],'learned':[337,343,346],'connectors':[581,640],'actions':[1318,1334],'skills':[1364,1364.6,1365.2],'agents':[1493],'rollout-one':[1807,1807.2,1807.4],'rollout-two':[1907,1913],'demo-context-overlay':[823.5,825,826.5,837],'documents':[1273,1280,1287]}
 events=sorted(set(scene['event_anchors']+extras.get(scene['id'],[])));last=max([v for v in events if v<=t] or [scene['source_start']])
 if scene['id']=='best-practices':return last+.05
 return t if t-last<2.0 else last+2.0
