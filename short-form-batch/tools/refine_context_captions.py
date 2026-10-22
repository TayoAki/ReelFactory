from pathlib import Path
import json,subprocess,wave,concurrent.futures,threading,re
import numpy as np
from faster_whisper import WhisperModel
R=Path(__file__).resolve().parents[1];P=R/'recording-clips';D=json.loads((P/'manifest.json').read_text());wav=R/'source-audio/combined-review.wav'
if not wav.exists():subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(R/'source-audio/combined-working.m4a'),'-ac','1','-ar','16000','-c:a','pcm_s16le',str(wav)],check=True)
with wave.open(str(wav)) as w:audio=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
path=str(next(Path('/workspace/scratch/speech-models/models--Systran--faster-whisper-base.en/snapshots').iterdir()));local=threading.local()
def norm(s):return re.sub('[^a-z0-9]','',s.lower())
def work(c):
 if not hasattr(local,'model'):local.model=WhisperModel(path,device='cpu',compute_type='int8',cpu_threads=2)
 ws=[];joins=[]
 for core in np.arange(0,c['duration'],20):
  a=max(-2,core-2);b=min(c['duration']+3,core+24)
  data=audio[round((c['source_start']+a)*16000):round((c['source_start']+b)*16000)]
  ss,_=local.model.transcribe(data,language='en',beam_size=5,word_timestamps=True,vad_filter=False)
  out=[{'word':w.word.strip(),'start':w.start+a,'end':w.end+a,'probability':w.probability} for s in ss for w in s.words or []]
  # Keep the central window, away from its decoder edges. Repeated adjacent words are not deduplicated.
  keep=[w for w in out if core<=((w['start']+w['end'])/2)<min(core+20,c['duration']-.06)]
  if ws and keep and keep[0]['start']<ws[-1]['end']-.05:
   if norm(keep[0]['word'])==norm(ws[-1]['word']):keep=keep[1:]
   else:joins.append({'at':float(core),'review':'word windows overlap slightly'})
  ws+=keep
 corrections=[]
 orthography={'fabric':'Fabric','fabriciq':'Fabric IQ','onelake':'OneLake','dax':'DAX','sql':'SQL','sequel':'SQL','kql':'KQL','mcp':'MCP','rdf':'RDF','owl':'OWL','tertil':'Turtle','turtle':'Turtle','activator':'Activator','copilot':'Copilot','cowork':'Cowork','powerbi':'Power BI'}
 for w in ws:
  k=norm(w['word'])
  if k in orthography:
   old=w['word'];punct=re.search(r'[^A-Za-z0-9]+$',old);new=orthography[k]+(punct.group() if punct else '')
   if new!=old:corrections.append({'from':old,'to':new,'reason':'technical-name orthography, not an audio change'});w['word']=new
 for i,w in enumerate(ws):
  if norm(w['word'])=='principle' and i and norm(ws[i-1]['word'])=='service':old=w['word'];w['word']=old.replace('principle','principal').replace('Principle','principal');corrections.append({'from':old,'to':w['word'],'reason':'service principal spelling'})
 # Stitch paired names into the normal product orthography, preserving their original audio span.
 merged=[];i=0
 while i<len(ws):
  if i+1<len(ws) and (norm(ws[i]['word']),norm(ws[i+1]['word'])) in [('one','lake'),('lake','house'),('event','house')]:
   name={('one','lake'):'OneLake',('lake','house'):'Lakehouse',('event','house'):'Eventhouse'}[(norm(ws[i]['word']),norm(ws[i+1]['word']))];punc=re.search(r'[^A-Za-z0-9]+$',ws[i+1]['word']);merged.append({**ws[i],'word':name+(punc.group() if punc else ''),'end':ws[i+1]['end']});i+=2
  else:merged.append(ws[i]);i+=1
 c['words']=merged;c['transcript_asr']=' '.join(w['word'] for w in merged);c['caption_corrections']=corrections;c['caption_join_review']=joins;c['transcript_status']='Contextual clip-local ASR with source audio before and after cut boundaries; technical-name orthography normalized. Not a certified human transcript.'
 (P/'captions').mkdir(exist_ok=True);(P/'captions'/f'{c["id"]}-words.json').write_text(json.dumps(c,indent=2))
 print(c['id'],round(c['duration'],1),len(merged),'words',len(joins),'window flags',flush=True)
 return c
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:D['clips']=list(pool.map(work,D['clips']))
(P/'manifest.json').write_text(json.dumps(D,indent=2));print('COMPLETE LOCAL CAPTIONS',len(D['clips']),flush=True)
