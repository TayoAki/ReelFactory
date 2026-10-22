"""Create a draft word-timed ASR transcript from an accessible local recording.
Does not approve quotations, identify speakers, select highlights or invent source timings.
Usage: /workspace/scratch/ev1-venv/bin/python tools/ingest_audio.py --audio /path/file.mp3
"""
import argparse,json,subprocess,wave
from pathlib import Path
import numpy as np
from faster_whisper import WhisperModel
p=argparse.ArgumentParser();p.add_argument('--audio',type=Path,required=True);p.add_argument('--out',type=Path,default=Path('short-form-batch/source-audio'));p.add_argument('--model',default='small.en');a=p.parse_args()
if not a.audio.is_file():raise SystemExit('Accessible source audio is required. No fallback recording or synthetic narration will be substituted.')
a.out.mkdir(parents=True,exist_ok=True);wav=a.out/'review-16k.wav'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(a.audio),'-vn','-ac','1','-ar','16000','-c:a','pcm_s16le',str(wav)],check=True)
# Pass decoded samples directly to avoid the older PyAV file-open incompatibility in this environment.
with wave.open(str(wav)) as w:samples=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
model=WhisperModel(a.model,device='cpu',compute_type='int8',cpu_threads=4)
segments,info=model.transcribe(samples,language='en',word_timestamps=True,vad_filter=True,initial_prompt='Microsoft Fabric, Fabric IQ, ontology, OneLake, lakehouse, eventhouse, Power BI, DAX, KQL, Lakeshore Retail.')
result=[]
for s in segments:
 result.append({'start':s.start,'end':s.end,'text':s.text,'words':[{'word':w.word,'start':w.start,'end':w.end,'probability':w.probability} for w in s.words or []]})
 (a.out/'transcript-draft.json').write_text(json.dumps({'source_audio':str(a.audio),'status':'ASR draft; technical names, quotations and speaker turns require verification','language':info.language,'segments':result},indent=2))
 print(f'{s.end:.1f}s {s.text}',flush=True)
