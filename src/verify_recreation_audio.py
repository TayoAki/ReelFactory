"""Re-transcribe final mixes to detect narration masked by editorial effects."""
import difflib,json,re,subprocess
from pathlib import Path
import numpy as np
from faster_whisper import WhisperModel

ROOT=Path(__file__).resolve().parents[1]
def words(s):return re.findall(r'[a-z0-9]+',s.lower())

if __name__=='__main__':
    model=WhisperModel('tiny.en',device='cpu',compute_type='int8',download_root='/workspace/scratch/speech-models',local_files_only=True,cpu_threads=2)
    for folder in sorted((ROOT/'videos').iterdir()):
        file=folder/'out/final.mp4';report=folder/'out/audio-review.json'
        if not file.exists() or report.exists():continue
        pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(file),'-ar','16000','-ac','1','-f','f32le','-'])
        segments,_=model.transcribe(np.frombuffer(pcm,dtype=np.float32),word_timestamps=True,beam_size=5)
        recognized=' '.join(s.text.strip() for s in segments)
        expected=(folder/'SCRIPT.txt').read_text()
        matcher=difflib.SequenceMatcher(None,words(expected),words(recognized),autojunk=False)
        changes=[{'kind':tag,'expected':' '.join(words(expected)[i:j]),'recognized':' '.join(words(recognized)[a:b])} for tag,i,j,a,b in matcher.get_opcodes() if tag!='equal']
        result={'method':'Whisper tiny.en re-transcription of final mixed MP4, compared with intended narration. ASR differences need interpretation; this is not proof of word-perfect audio.','similarity':round(matcher.ratio(),4),'transcript':recognized,'differences':changes}
        report.write_text(json.dumps(result,indent=2));print(folder.name,result['similarity'],changes,flush=True)
