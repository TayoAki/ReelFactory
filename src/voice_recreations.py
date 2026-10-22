"""Local draft narration and word alignment; never calls a paid voice API."""
import argparse, difflib, hashlib, json, re, subprocess
from pathlib import Path
import numpy as np
import onnxruntime as ort
import soundfile as sf
from kokoro_onnx import Kokoro
from faster_whisper import WhisperModel

ROOT=Path(__file__).resolve().parents[1]
CONTENT=ROOT/'content/creator-recreations'

def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())

def align(text, recognized, duration):
    tokens=text.split(); a=[norm(w) for w in tokens]; b=[norm(w.word) for w in recognized]
    pairs={}
    for block in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks():
        for k in range(block.size):pairs[block.a+k]=recognized[block.b+k]
    # Missing names inherit the local ASR replacement interval; flag these for review.
    times={i:max(0,float(w.start)) for i,w in pairs.items()}
    for i in range(len(tokens)):
        if i in times:continue
        left=max((j for j in pairs if j<i),default=-1);right=min((j for j in pairs if j>i),default=len(tokens))
        lo=float(pairs[left].end) if left>=0 else 0
        hi=float(pairs[right].start) if right<len(tokens) else duration
        times[i]=max(lo,lo+(hi-lo)*(i-left-1)/max(1,right-left))
    return [{'w':word,'s':round(min(duration,times[i]),4),'e':round(min(duration,times.get(i+1,duration)),4),'alignment':'asr' if i in pairs else 'interpolated'} for i,word in enumerate(tokens)]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--only');ap.add_argument('--project-file',type=Path,default=CONTENT/'projects.json');ap.add_argument('--models',type=Path,default=Path('/workspace/scratch/voice-models'));args=ap.parse_args()
    options=ort.SessionOptions();options.intra_op_num_threads=4;options.inter_op_num_threads=1
    session=ort.InferenceSession(str(args.models/'kokoro-v1.0.onnx'),sess_options=options,providers=['CPUExecutionProvider'])
    model=Kokoro.from_session(session,str(args.models/'voices-v1.0.bin'))
    stt=WhisperModel('tiny.en',device='cpu',compute_type='int8',download_root='/workspace/scratch/speech-models',local_files_only=True,cpu_threads=4)
    projects=json.loads(args.project_file.read_text())
    for project in projects:
        if args.only and args.only!=project['id']:continue
        out=ROOT/'videos'/project['id'];(out/'assets/media').mkdir(parents=True,exist_ok=True);(out/'work').mkdir(exist_ok=True)
        fingerprint=hashlib.sha256(json.dumps(project['beats'],sort_keys=True).encode()).hexdigest()
        if (out/'work/timeline.json').exists() and json.loads((out/'work/timeline.json').read_text()).get('script_sha256')==fingerprint:continue
        chunks=[];words=[];beats=[];offset=0.;sr=24000
        for i,beat in enumerate(project['beats']):
            cache=out/'work'/f'voice-{i:02}.wav'
            text_cache=cache.with_suffix('.txt');voice_cache=cache.with_suffix('.voice.json');requested_voice=beat.get('voice','af_heart');voice_matches=(json.loads(voice_cache.read_text())==requested_voice) if voice_cache.exists() else requested_voice=='af_heart'
            if cache.exists() and text_cache.exists() and text_cache.read_text()==beat['text'] and voice_matches:audio,sr=sf.read(cache,dtype='float32')
            else:
                audio,sr=model.create(beat['text'],voice=requested_voice,speed=beat.get('speed',1.08))
                sf.write(cache,audio,sr)
                text_cache.write_text(beat['text']);voice_cache.write_text(json.dumps(requested_voice))
            pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(cache),'-ar','16000','-ac','1','-f','f32le','-'])
            segments,_=stt.transcribe(np.frombuffer(pcm,dtype=np.float32),word_timestamps=True,beam_size=3,initial_prompt=beat['text'])
            rec=[word for seg in segments for word in seg.words]
            length=len(audio)/sr
            aligned=align(beat['text'],rec,length)
            for w in aligned:w['s']+=offset;w['e']+=offset
            words.extend(aligned)
            beats.append(dict(beat,start=round(offset,4),end=round(offset+length+.16,4),voice_end=round(offset+length,4)))
            chunks.extend([audio,np.zeros(round(sr*.16),dtype=np.float32)])
            offset+=length+.16
            print(project['id'],i+1,'/',len(project['beats']),flush=True)
        combined=np.concatenate(chunks)
        sf.write(out/'assets/media/vo.wav',combined,sr)
        timeline={'id':project['id'],'title':project['title'],'script_sha256':fingerprint,'duration':round(offset,4),'beats':beats,'words':words,'voice':'Local Kokoro synthetic review narration; per-beat voices: '+', '.join(sorted(set(b.get('voice','af_heart') for b in beats))),'alignment_note':'Whisper tiny.en word timestamps, with interpolated unmatched words explicitly flagged. Not manually verified to +/- one frame.'}
        (out/'work/timeline.json').write_text(json.dumps(timeline,indent=2))
        (out/'SCRIPT.txt').write_text('\n\n'.join(b['text'] for b in beats))
        print('Saved',project['id'],round(offset,2),'seconds',flush=True)

if __name__=='__main__':main()
