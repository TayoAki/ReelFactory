"""Reproducible image-first reconstruction: editable SVG scene -> independent raster layers -> FFmpeg motion.
Original source audio is preserved; no generated speech. Run with system Python (Playwright).
"""
import json, pathlib, html, re, asyncio, subprocess, concurrent.futures, os, math, time
from playwright.async_api import async_playwright
from PIL import ImageFont
ROOT=pathlib.Path(__file__).resolve().parents[2]; P=ROOT/'short-form-batch/recording-clips'; AS=P/'assets'; CACHE=P/'render-cache'; CACHE.mkdir(exist_ok=True)
D=json.loads((P/'manifest.json').read_text())
ASURL='http://127.0.0.1:8765/short-form-batch/recording-clips/assets'
FONTS=f'@font-face{{font-family:Serif;src:url({ASURL}/SourceSerif4.ttf)}} @font-face{{font-family:Sans;src:url({ASURL}/CaptionSans.ttf)}}'
def esc(s):return html.escape(str(s))
def lines(s,n=23):
 out=[];line=''
 for w in s.split():
  if len(line+' '+w)>n and line:out.append(line);line=w
  else:line=(line+' '+w).strip()
 if line:out.append(line)
 return out
# Filled, self-authored generic symbols, chosen by meaning. Product branding uses official assets only.
ICONS={
 'factory':'<path d="M8 90V43l25-17v21l25-17v17l24-17V7h10v83z"/><path d="M20 62h10v13H20zm24 0h10v13H44zm24 0h10v13H68z" fill="white"/>',
 'truck':'<path d="M5 23h56v49H5zm59 16h18l15 18v15H64z"/><path d="M70 45h10l10 12H70z" fill="white"/><circle cx="23" cy="77" r="12"/><circle cx="78" cy="77" r="12"/><circle cx="23" cy="77" r="5" fill="white"/><circle cx="78" cy="77" r="5" fill="white"/>',

 'sun':'<circle cx="50" cy="50" r="23"/><path d="M46 0h8v18h-8zm0 82h8v18h-8zM0 46h18v8H0zm82 0h18v8H82zM12 18l6-6 13 13-6 6zm57 57 6-6 13 13-6 6zM12 82l13-13 6 6-13 13zm57-57 13-13 6 6-13 13z"/>',
 'fridge':'<path d="M22 7h56v86H22z"/><path d="M22 43h56M34 20v12m0 23v17" stroke="white" stroke-width="5"/>',

 'database':'<ellipse cx="50" cy="22" rx="33" ry="13"/><path d="M17 25v23c0 19 66 19 66 0V25c-14 15-52 15-66 0zm0 31v22c0 19 66 19 66 0V56c-14 15-52 15-66 0z"/>',
 'context':'<path d="M18 12h45l20 20v56H18z"/><path d="M30 45h40M30 58h40M30 71h28" stroke="white" stroke-width="5"/>',
 'store':'<path d="M15 43h70v44H15zM9 17h82l7 23c-2 14-19 17-25 4-5 13-22 13-27 0-5 13-22 13-27 0-6 11-20 8-17-4z"/><path d="M29 59h18v28H29zm29 0h17v15H58z" fill="white"/>',
 'person':'<circle cx="50" cy="29" r="19"/><path d="M15 90V76c0-38 70-38 70 0v14z"/>',
 'clock':'<circle cx="50" cy="50" r="38"/><path d="M50 24v29l21 12" stroke="white" stroke-width="7" fill="none"/>',
 'shield':'<path d="M50 7 86 23v30c0 23-17 35-36 43C31 88 14 76 14 53V23z"/><path d="m31 49 13 13 26-29" fill="none" stroke="white" stroke-width="7"/>',
 'link':'<path d="M46 20c28-29 61 5 34 31L65 66 54 55l15-15c12-12-4-25-14-15L39 41 28 30zm8 60C26 109-7 75 20 49l15-15 11 11-15 15c-12 12 4 25 14 15l16-16 11 11z"/>',
 'thermometer':'<path d="M35 58V24c0-26 30-26 30 0v34c31 27-12 64-35 34-8-11-7-24 5-34z"/><path d="M50 23v47" stroke="white" stroke-width="7"/><circle cx="50" cy="77" r="10" fill="white"/>',
 'cube':'<path d="m50 5 42 23-42 23L8 28zm-42 32 37 21v38L8 75zm47 21 37-21v38L55 96z"/>',
 'search':'<path d="m65 59 31 30-8 8-30-31z"/><circle cx="39" cy="39" r="29" fill="none" stroke="currentColor" stroke-width="12"/>',
 'chart':'<path d="M12 55h18v35H12zm28-27h18v62H40zm28-20h18v82H68z"/>',
 'graph':'<circle cx="50" cy="16" r="12"/><circle cx="18" cy="78" r="12"/><circle cx="82" cy="78" r="12"/><path d="M46 27 23 67m31-40 23 40M30 78h40" fill="none" stroke="currentColor" stroke-width="8"/>',
}
def symbol(label,family):
 s=label.lower()
 if 'outside' in s:return 'sun'
 if s=='supplier':return 'factory'
 if s=='shipments':return 'truck'
 if 'refrigeration' in s:return 'fridge'
 for words,key in [('temperature outside refrigeration °f °c','thermometer'),('store shops location','store'),('source table data records onelake lakehouse eventhouse','database'),('permission access identity account user authentication','shield'),('time refresh monitoring dates arrival cycle','clock'),('report dax calculation measure power bi metric','chart'),('supplier products product shipments inventory','cube'),('query question inspect review evidence','search'),('binding shortcut reference mapping synonyms','link'),('relationship graph','graph')]:
  if any(w in s for w in words.split()):return key
 return 'context'
def icon(label,family):
 if 'power bi' in label.lower() or label=='Semantic model':return f'<img width=95 height=95 src="{ASURL}/semantic_model_48_item.svg">'
 if label=='Lakehouse':return f'<img width=95 height=95 src="{ASURL}/lakehouse_48_item.svg">'
 key=symbol(label,family)
 return f'<svg width="95" height="95" viewBox="0 0 100 100" style="color:#117865;fill:currentColor">{ICONS[key]}</svg>'
def card(label,sub,w,h,focal=False,family=''):
 horizontal=w>=600;ls=lines(label,23 if horizontal else 21);size=44 if horizontal else 43
 iconhtml=icon(label,family)
 if h<160:iconhtml=iconhtml.replace('width="95"','width="65"').replace('height="95"','height="65"')
 if h<160:size=34
 text=f'<div><div class="label" style="font-size:{size}px">'+ '<br>'.join(map(esc,ls))+f'</div><div class="sub" style="margin-top:16px">{esc(sub)}</div></div>'
 sty='flex-direction:row;align-items:center;justify-content:flex-start;gap:28px' if horizontal else ''
 if h<160:sty+=';padding:22px' 
 return f'<div class="card {"focal" if focal else ""}" style="width:{w}px;height:{h}px;{sty}"><div style="flex-shrink:0">{iconhtml}</div>{text}</div>'
def document(body,w=1080,h=1920,transparent=False):
 return f'''<html><head><meta charset="utf-8"><style>{FONTS}*{{box-sizing:border-box}}html,body{{margin:0;width:{w}px;height:{h}px;overflow:hidden;background:{'transparent' if transparent else '#fcfefd'};color:#172b2a;font-family:Sans}}.card{{border:1.5px solid #dbe8e2;border-radius:25px;background:linear-gradient(135deg,#fff,#f4f8f6);box-shadow:0 12px 25px #164b3d15;padding:32px;display:flex;flex-direction:column;justify-content:center;gap:19px}}.focal{{background:linear-gradient(140deg,#f0faf6,#d3efe5);border-color:#aed8cb}}.label{{font-family:Serif;line-height:1.12;letter-spacing:-1px}}.sub{{font-size:21px;letter-spacing:1px;color:#477069;line-height:1.45}}.grid{{position:absolute;inset:0;background-image:linear-gradient(#35796b07 1px,transparent 1px),linear-gradient(90deg,#35796b07 1px,transparent 1px);background-size:80px 80px}}</style></head><body>{body}</body></html>'''
def timecode(t):return f'{int(t)//60:02d}:{int(t)%60:02d}'
def onset(c,label,fallback):
 tokens=re.findall(r'[a-z0-9]+',label.lower()); ws=c['words'];matches=[]
 stop={'the','and','with','from','source','data','business','current','own','different','example','a','of','to','is','one','same'}
 for token in tokens:
  if token in stop or len(token)<4:continue
  for w in ws:
   if token in re.findall(r'[a-z0-9]+',w['word'].lower()):matches.append(w['start']);break
 return max(.25,min(matches)) if matches else fallback

def plan(c):
 f=c['family'];a=c['left_label'];b=c['right_label'];focus=c['focus_label'];dur=c['duration'];q=min(3,dur*.16)
 if f=='contrast':
  specs=[(focus,'CONTEXT / QUESTION',180,660,720,180,True),(a,'INTERPRETATION A',60,935,455,370,True),(b,'INTERPRETATION B',565,935,455,370,False)]
  relation='Compare the meaning';connector=False
 elif f=='graph':
  specs=[(x,['SUPPLIES PRODUCTS','INCLUDED IN SHIPMENTS','RECEIVED BY STORES','OPERATE REFRIGERATION UNITS','RELEVANT UNITS TO INSPECT'][i],140,650+i*140,800,120,i==0) for i,x in enumerate(['Supplier','Products','Shipments','Stores','Refrigeration units'])];relation='Trace connected entities';connector=True
 elif f=='workflow':
  mid=focus
  if c['id']=='C32':a,mid,b='Plan','Inspect and revise','Act'
  elif c['id']=='C33':a,mid,b='Save current version','Choose a named version','Restore definitions'
  elif c['id']=='C26':a,mid,b='Inspect supported sources','Draft proposal','Human review'
  elif c['id']=='C56':a,mid,b='One recurring decision','Test against known answers','Expand deliberately'
  elif c['id']=='C29':a,mid,b='Lakehouse','Eventhouse','Semantic model'
  specs=[(x,('SUPPORTED SOURCE' if c['id']=='C29' else ['START','REVIEW / CONTEXT','NEXT'][i]),100,660+i*230,880,188,i==1) for i,x in enumerate([a,mid,b])];relation='Source routes' if c['id']=='C29' else 'Keep each step explicit';connector=c['id']!='C29'
 else:
  subs={'ownership':('DEFINITION / SOURCE','CONSUMER / MAPPING'),'entities':('ENTITY / CONCEPT','RELATED CONCEPT'),'hierarchy':('PARENT / DEFINED TYPE','DERIVED TYPE / EXPLICIT SCOPE'),'boundary':('FIRST RESPONSIBILITY','SEPARATE RESPONSIBILITY'),'evidence':('CHECK THE BASIS','VERIFY THE RESULT')}.get(f,('CONCEPT','CONTEXT'))
  if c['id']=='C11':subs=('ENTITY TYPE','PHYSICAL INSTANCE')
  if c['id']=='C12':subs=('ENTITY TYPE','ENTITY TYPE')
  if c['id']=='C17':subs=('BASE TYPE RELATIONSHIP','DERIVED TYPE · REDEFINE RELATIONSHIP')
  if c['id']=='C18':subs=('BASE TYPE QUERY SCOPE','NAME RELEVANT DERIVED TYPE')
  if c['id']=='C25':subs=('ENTITY TYPE','SYNONYM · SAME ENTITY TYPE')
  specs=[(a,subs[0],100,680,880,250,True),(b,subs[1],100,1050,880,250,False)];relation=focus;connector=f not in ['boundary','evidence']
 layers=[]
 for i,(label,sub,x,y,w,h,focal) in enumerate(specs):
  on=onset(c,label,.7+i*q);on=min(on,max(.4,dur-2));on=min(on,.7) if i==0 else on;layers.append(dict(label=label,sub=sub,x=x,y=y,w=w,h=h,focal=focal,on=round(on,3),timing='keyword onset or editorial fallback',kind='card'))
 return layers,relation,connector

async def build():
 import sys
 ids=[x for x in sys.argv if re.fullmatch(r'C\d\d',x)]
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--allow-file-access-from-files']);page=await browser.new_page(viewport={'width':1080,'height':1920},device_scale_factor=1)
  for c in D['clips']:
   if ids and c['id'] not in ids:continue
   out=CACHE/c['id'];out.mkdir(exist_ok=True);state=P/'storyboards'/c['id'];state.mkdir(exist_ok=True)
   layers,relation,connect=plan(c);context=c.get('context_label') or 'Concept illustration · original discussion audio'
   title='<br>'.join(map(esc,lines(c['title'],29)));titlesize=64 if len(lines(c['title'],29))<=2 else 55
   base=f'''<div class="grid"></div><div style="position:absolute;left:72px;top:50px;display:flex;align-items:center;gap:18px;font-size:19px;letter-spacing:3px;color:#225b62"><img width="36" src="{ASURL}/fabric.svg">MICROSOFT FABRIC · ONTOLOGY</div><div style="position:absolute;left:72px;top:125px;width:936px;font-family:Serif;font-size:{titlesize}px;line-height:1.05;letter-spacing:-2px">{title}</div><div style="position:absolute;left:78px;top:355px;display:flex;gap:14px"><img src="{ASURL}/host.png" style="width:150px;height:185px;object-fit:cover;border-radius:18px"><img src="{ASURL}/guest.png" style="width:150px;height:185px;object-fit:cover;border-radius:18px"></div><div style="position:absolute;left:435px;top:395px;font-size:24px;line-height:1.7;color:#477069">Original discussion audio<br>Static portrait placeholders</div><div style="position:absolute;left:75px;top:575px;width:930px;text-align:center;font-size:29px;color:#117865;font-family:Serif">{esc(c['focus_label'])}</div><div style="position:absolute;left:80px;top:1405px;width:920px;height:218px;border-radius:25px;background:#eef7f3e8"></div><div style="position:absolute;left:80px;top:1660px;width:920px;font-size:21px;line-height:1.5;color:#477069">{esc(context)}<br>{c['id']} · Recording {timecode(c['source_start'])}–{timecode(c['source_end'])} · Draft</div>'''
   # Base has no explanatory cards; cards remain independent alpha layers.
   htmlpath=out/'base.html';htmlpath.write_text(document(base));await page.goto('http://127.0.0.1:8765/'+str(htmlpath.relative_to(ROOT))+'?v='+str(time.time_ns()));await page.evaluate('document.fonts.ready');await page.screenshot(path=str(out/'base.png'))
   for i,l in enumerate(layers):
    body='<div style="position:absolute;left:28px;top:28px">'+card(l['label'],l['sub'],l['w'],l['h'],l['focal'],c['family'])+'</div>'
    path=out/f'layer{i}.html';path.write_text(document(body,l['w']+56,l['h']+56,True));await page.set_viewport_size({'width':l['w']+56,'height':l['h']+56});await page.goto('http://127.0.0.1:8765/'+str(path.relative_to(ROOT))+'?v='+str(time.time_ns()));await page.evaluate('document.fonts.ready');await page.screenshot(path=str(out/f'layer{i}.png'),omit_background=True)
   # Relation stays explicit; do not imply that every comparison is a pipeline.
   relation_html=''
   if len(layers)==2 and c['family']!='contrast':
    arrow='↔' if c['id']=='C25' else ('↑' if c['id'] in ['C09','C21','C49'] else ('↓' if connect else '·'))
    relation_html=f'<div style="position:absolute;left:90px;top:947px;width:900px;text-align:center;color:#225b62;font-size:24px">{esc(relation)} <span style="font-size:40px">{arrow}</span></div>'
   elif connect and len(layers)>2:
    for l in layers[:-1]:relation_html+=f'<div style="position:absolute;left:500px;top:{l["y"]+l["h"]}px;color:#117865;font-size:20px">↓</div>'
   rp=out/'relation.html';rp.write_text(document(relation_html,transparent=True));await page.set_viewport_size({'width':1080,'height':1920});await page.goto('http://127.0.0.1:8765/'+str(rp.relative_to(ROOT))+'?v='+str(time.time_ns()));await page.screenshot(path=str(out/'relation.png'),omit_background=True)
   for s,count in [('01-initial',1),('02-build',max(1,len(layers)-1)),('03-settled',len(layers))]:
    body=base+relation_html
    for l in layers[:count]:body+=f'<div style="position:absolute;left:{l["x"]}px;top:{l["y"]}px">'+card(l['label'],l['sub'],l['w'],l['h'],l['focal'],c['family'])+'</div>'
    # Two-node diagrams need a distinct build frame: relationship present, second node translucent.
    if s=='02-build' and len(layers)==2:
     l=layers[1];body+=f'<div style="position:absolute;opacity:.45;transform:translateY(10px);left:{l["x"]}px;top:{l["y"]}px">'+card(l['label'],l['sub'],l['w'],l['h'],l['focal'],c['family'])+'</div>'
    p=out/'state.html';p.write_text(document(body));await page.goto('http://127.0.0.1:8765/'+str(p.relative_to(ROOT))+'?v='+str(time.time_ns()));await page.evaluate('document.fonts.ready');await page.screenshot(path=str(state/f'{s}.jpg'),type='jpeg',quality=86)
   payload={'id':c['id'],'family':c['family'],'master_image':f'../master-{c["family"]}.png','visual_workflow':'image-first','state_images':['01-initial.jpg','02-build.jpg','03-settled.jpg'],'layers':layers,'relation':relation,'source_quote':c['transcript_asr'],'why':{'contrast':'Compare interpretations without implying causation.','ownership':'Separate the source of meaning or data from its consumer.','entities':'Keep the named concepts and their relationship visible.','hierarchy':'Distinguish type structure from instances and explicit relationship scope.','workflow':'Expose intermediate review or processing steps.','boundary':'Show separate responsibilities; no implied automatic execution.','evidence':'Show what must be checked rather than an invented successful result.','graph':'Trace a hypothetical recall along named relationships.'}[c['family']],'alternative':'Authentic tenant UI would be preferable for proving an executed product action; this clip is a concept illustration.','visual_review':'Draft, not human approved. Generated symbols corrected in editable reconstruction.','source_reference':'reference-library/frames/graphic/0003510.jpg','motion':'independent card alpha reveal + 16px eased settling, timed to recording keywords; fixed grid and presenter rail'}
   (state/'storyboard.json').write_text(json.dumps(payload,indent=2));(out/'layers.json').write_text(json.dumps(layers));print('BUILD',c['id'],flush=True)
  await browser.close()

def ass_time(t):
 t=max(0,t);return f'{int(t)//3600}:{int(t)//60%60:02d}:{int(t)%60:02d}.{int(t*100)%100:02d}'
def subtitles(c):
 words=c['words'];groups=[];g=[];n=0
 font=ImageFont.truetype(str(AS/'CaptionSans.ttf'),55)
 boldpath=pathlib.Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
 bold=ImageFont.truetype(str(boldpath if boldpath.exists() else AS/'CaptionSans.ttf'),55)
 def row_width(ws):
  return font.getlength(' '.join(w['word'] for w in ws))+max([bold.getlength(w['word'])-font.getlength(w['word']) for w in ws] or [0])
 for w in words:
  text=w['word'].replace('{','').replace('}','');w={**w,'word':text};n+=len(text)+1;g.append(w)
  if len(g)>=6 or n>=35 or (text.endswith(('.', '?','!')) and len(g)>=3):groups.append(g);g=[];n=0
 if g:groups.append(g)
 header='''[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Default,DejaVu Sans,55,&H002A2B17,&H00657811,&H00F3F7EE,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,105,105,370,1\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'''
 events=[];vtt=['WEBVTT',''];trans=[]
 for gi,g in enumerate(groups):
  # Short lines remain readable in the fixed caption band.
  split=min(range(1,len(g)),key=lambda k:max(row_width(g[:k]),row_width(g[k:]))) if len(g)>1 and row_width(g)>840 else 999
  for j,w in enumerate(g):
   next_group=groups[gi+1][0]['start'] if gi+1<len(groups) else c['duration']
   end=g[j+1]['start'] if j+1<len(g) else min(next_group,c['duration'],max(w['end']+.12,w['start']+.08))
   if end<=w['start']:continue
   ss=[]
   for k,ww in enumerate(g):
    ss.append(('{\\c&H00657811&\\b1}'+ww['word']+'{\\c&H002A2B17&\\b0}') if k==j else ww['word'])
   txt=' '.join(ss[:split])+('\\N'+' '.join(ss[split:]) if split<999 else '')
   events.append(f'Dialogue: 0,{ass_time(w["start"])},{ass_time(end)},Default,,0,0,0,,{{\\pos(540,1513)}}{txt}')
  def vt(t):
   t=max(0,t);return f'{int(t)//3600:02d}:{int(t)//60%60:02d}:{int(t)%60:02d}.{int(t*1000)%1000:03d}'
  vtt += [f'{vt(g[0]["start"])} --> {vt(min(c["duration"],g[-1]["end"]+.12,groups[gi+1][0]['start'] if gi+1<len(groups) else c['duration']))}',' '.join(w['word'] for w in g),'']
 (P/'captions'/f'{c["id"]}.ass').write_text(header+'\n'.join(events));(P/'captions'/f'{c["id"]}.vtt').write_text('\n'.join(vtt))
 (P/'captions'/f'{c["id"]}.srt').write_text('\n'.join(f'{i//3+1}\n{vtt[i].replace(".",",")}\n{vtt[i+1]}\n' for i in range(2,len(vtt)-1,3)))
 (P/'captions'/f'{c["id"]}.txt').write_text(f'{c["title"]}\nOriginal recording {timecode(c["source_start"])}–{timecode(c["source_end"])}\nASR draft; technical-name spelling normalized.\n\n'+c['transcript_asr'])

def render(c):
 cp=P/'captions'/f'{c["id"]}-words.json'
 if cp.exists():c=json.loads(cp.read_text())
 out=CACHE/c['id'];layers=json.loads((out/'layers.json').read_text());target=P/'exports'/f'{c["id"]}.mp4'
 subtitles(c)
 if target.exists():return c['id']+' exists'
 cmd=['ffmpeg','-y','-v','error','-filter_complex_threads','1','-loop','1','-framerate','1','-i',str(out/'base.png')]
 for i,l in enumerate(layers):cmd+=['-loop','1','-framerate','1','-i',str(out/f'layer{i}.png')]
 cmd+=['-loop','1','-framerate','1','-i',str(out/'relation.png'),'-ss',str(c['source_start']),'-i',str(ROOT/'short-form-batch/source-audio/combined-working.m4a')]
 fs=['[0:v]fps=30[bg]'];prev='bg'
 for i,l in enumerate(layers):
  on=l['on'];fs.append(f'[{i+1}:v]fps=30,format=rgba,fade=t=in:st={on}:d=0.42:alpha=1[a{i}]');n=f'v{i}'
  fs.append(f"[{prev}][a{i}]overlay=x={l['x']-28}:y='{l['y']-28}+16*pow(1-min(max((t-{on})/0.45,0),1),3)':enable='gte(t,{on})'[{n}]");prev=n
 idx=len(layers)+1;fs.append(f'[{idx}:v]fps=30,format=rgba,fade=t=in:st=1:d=0.4:alpha=1[rel]');fs.append(f'[{prev}][rel]overlay=0:0[all]');fs.append(f"[all]ass={P/'captions'/str(c['id']+'.ass')}:fontsdir={AS},format=yuv420p[final]")
 cmd+=['-filter_complex',';'.join(fs),'-map','[final]','-map',f'{idx+1}:a','-t',str(c['duration']),'-r','30','-c:v','libx264','-threads','2','-preset','veryfast','-crf','20','-c:a','aac','-b:a','128k','-movflags','+faststart',str(target)]
 r=subprocess.run(cmd,capture_output=True,text=True)
 if r.returncode:raise RuntimeError(c['id']+r.stderr[-2500:])
 return c['id']+' rendered'
if __name__=='__main__':
 import sys
 if '--build' in sys.argv:asyncio.run(build())
 if '--render' in sys.argv:
  clips=D['clips'];ids=[x for x in sys.argv if re.fullmatch(r'C\d\d',x)]
  if ids:clips=[c for c in clips if c['id'] in ids]
  with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
   for result in pool.map(render,clips):print(result,flush=True)
