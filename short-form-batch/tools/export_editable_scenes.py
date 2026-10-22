"""Save portable, editable HTML/SVG scenes outside the disposable render cache."""
import pathlib,json,importlib.util,re,html
R=pathlib.Path(__file__).resolve().parents[2];P=R/'short-form-batch/recording-clips';path=pathlib.Path(__file__).with_name('build_recording_clips.py');spec=importlib.util.spec_from_file_location('builder',path);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
for c in b.D['clips']:
 cache=P/'render-cache'/c['id'];layers=json.loads((cache/'layers.json').read_text());doc=(cache/'base.html').read_text();rel=(cache/'relation.html').read_text().split('<body>',1)[1].split('</body>',1)[0];body='<div style="animation:arrive .42s 1s both">'+rel+'</div>'
 for l in layers:body+=f'<div data-label="{b.esc(l["label"])}" data-on="{l["on"]}" style="position:absolute;left:{l["x"]}px;top:{l["y"]}px;animation:arrive .45s cubic-bezier(.16,1,.3,1) {l["on"]}s both">'+b.card(l['label'],l['sub'],l['w'],l['h'],l['focal'],c['family'])+'</div>'
 body+='''<style>@keyframes arrive{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}audio{position:fixed;bottom:14px;left:80px;width:920px;z-index:100}</style>'''
 body+=f'<audio id="voice" controls preload="metadata" src="../../exports/{c["id"]}.mp4"></audio>'
 cues=[]
 for line in (P/'captions'/f'{c["id"]}.ass').read_text().splitlines():
  if not line.startswith('Dialogue:'):continue
  row=line.split(',',9)
  def seconds(t):
   h,m,s=t.split(':');return int(h)*3600+int(m)*60+float(s)
  txt=html.escape(row[9]);txt=txt.replace(html.escape('{\\c&H00657811&\\b1}'),'<span style="color:#117865;font-weight:700">').replace(html.escape('{\\c&H002A2B17&\\b0}'),'</span>');txt=re.sub(r'\{[^}]*\}','',txt).replace('\\N','<br>')
  cues.append({'start':seconds(row[1]),'end':seconds(row[2]),'html':txt})
 body+='<div id="captions" style="position:absolute;left:105px;top:1405px;width:870px;height:218px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:55px;line-height:1.2"><div id="words"></div></div>'
 body+='<script>const cues='+json.dumps(cues).replace('</','<\\/')+';'+'''const voice=document.getElementById('voice');fetch(voice.src).then(r=>{if(!r.ok)throw new Error(r.status);return r.blob()}).then(blob=>{voice.src=URL.createObjectURL(blob);voice.dataset.blob='ready';voice.load()}).catch(()=>{});const animations=document.getAnimations();animations.forEach(a=>a.pause());let previous=null;function sync(){const t=voice.currentTime;animations.forEach(a=>a.currentTime=t*1000);const cue=cues.find(c=>t>=c.start&&t<c.end);if(cue!==previous){document.getElementById('words').innerHTML=cue?cue.html:'';previous=cue}requestAnimationFrame(sync)}sync();</script>'''

 doc=doc.replace('</body>',body+'</body>').replace(b.ASURL,'../../assets');(P/'storyboards'/c['id']/'scene.html').write_text(doc)
print('Saved 57 editable layered scenes; audio controls are review-only, outside the production caption band.')
