from pathlib import Path
import subprocess,json
import numpy as np
from faster_whisper import WhisperModel
r=Path(__file__).resolve().parent;root=r.parents[1];src=json.loads((root/'research/ontology-adaptation/uploaded-parts.json').read_text())[0]['path'];a,z=35.3,87
raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(a),'-i',src,'-t',str(z-a),'-ar','16000','-ac','1','-f','f32le','-']);model=WhisperModel('tiny.en',device='cpu',compute_type='int8',download_root='/workspace/scratch/speech-models',local_files_only=True,cpu_threads=2);segs,_=model.transcribe(np.frombuffer(raw,np.float32),word_timestamps=True,beam_size=5);words=[]
for s in segs:
 for w in s.words:words.append(dict(w=w.word.strip(),start=round(a+w.start,3),end=round(a+w.end,3)))
(r/'source-words.json').write_text(json.dumps(words,indent=2));print(' '.join(f'{w["start"]}:{w["w"]}' for w in words),flush=True)
