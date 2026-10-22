from pathlib import Path
import json,subprocess,wave,time,concurrent.futures,os
import numpy as np
from faster_whisper import WhisperModel
R=Path(__file__).resolve().parents[1];m=json.loads((R/'source-audio/manifest.json').read_text())
model_path=str(next(Path('/workspace/scratch/speech-models/models--Systran--faster-whisper-tiny.en/snapshots').iterdir()))
def run(row):
 out=R/'source-audio'/f'part{row["part"]:02}';out.mkdir(exist_ok=True);wav=out/'review.wav'
 subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(R/'source-audio/original-parts'/row['name']),'-vn','-ac','1','-ar','16000','-c:a','pcm_s16le',str(wav)],check=True)
 with wave.open(str(wav)) as w:samples=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
 model=WhisperModel(model_path,device='cpu',compute_type='int8',cpu_threads=2,num_workers=1)
 segments,info=model.transcribe(samples,language='en',beam_size=5,word_timestamps=True,vad_filter=True,initial_prompt='Microsoft Fabric. Fabric IQ. Fabric ontology, ontologies. OneLake. Lakehouse. Eventhouse. Power BI semantic model. DAX. KQL. SQL. Real-Time Intelligence. Lakeshore Retail. Ontology agent. Activator.')
 result=[];last=0;start=time.time()
 for s in segments:
  result.append({'start':s.start,'end':s.end,'text':s.text.strip(),'avg_logprob':s.avg_logprob,'no_speech_prob':s.no_speech_prob,'words':[{'word':w.word.strip(),'start':w.start,'end':w.end,'probability':w.probability} for w in s.words or []]})
  (out/'transcript.json').write_text(json.dumps({'part':row['part'],'offset':row['offset'],'source':row['name'],'model':'tiny.en first-pass ASR','status':'draft; technical terms and final clip quotations require review','segments':result},indent=2))
  if s.end-last>120:print(f'part{row["part"]:02}: {s.end:.0f}/{row["duration"]:.0f}s transcribed; wall {time.time()-start:.0f}s',flush=True);last=s.end
 print(f'COMPLETE part{row["part"]:02}: {len(result)} segments, wall {time.time()-start:.0f}s',flush=True)
 return row['part']
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 list(pool.map(run,m['parts']))
all_segments=[]
for row in m['parts']:
 d=json.loads((R/'source-audio'/f'part{row["part"]:02}'/'transcript.json').read_text())
 for s in d['segments']:
  all_segments.append({**s,'part':row['part'],'part_start':s['start'],'part_end':s['end'],'start':s['start']+row['offset'],'end':s['end']+row['offset'],'words':[{**w,'start':w['start']+row['offset'],'end':w['end']+row['offset']} for w in s['words']]})
(R/'source-audio/transcript-first-pass.json').write_text(json.dumps({'duration':m['total_duration'],'model':'tiny.en','status':'first-pass ASR, not yet certified verbatim','segments':all_segments},indent=2))
(R/'source-audio/transcript-first-pass.txt').write_text('\n'.join(f'[{s["start"]:.2f}–{s["end"]:.2f}] {s["text"]}' for s in all_segments))
print('COMPLETE ALL',len(all_segments),'segments',flush=True)
