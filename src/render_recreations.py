"""Render native V1 projects, then mix the local voice and device-generated cues."""
import argparse, json, os, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];KIT=ROOT/'vendor/editor-v1'

def finish(project,python):
    folder=ROOT/'videos'/project['id'];out=folder/'out';info=json.loads((folder/'work/render-info.json').read_text())
    if not (out/'render.mp4').exists():raise RuntimeError('Native HyperFrames render is missing')
    with (out/'mix.log').open('w') as log:
        subprocess.run(['ffmpeg','-v','error','-y','-i',str(out/'render.mp4'),'-i',str(folder/'assets/media/vo.wav'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-af','loudnorm=I=-20:TP=-3:LRA=7,apad','-t',str(info['duration']),'-c:a','aac','-b:a','192k',str(out/'voice.mp4')],check=True,stdout=log,stderr=log)
        subprocess.run([python,str(KIT/'scripts/mix-sfx.py'),str(out/'voice.mp4'),str(folder/'sfx-cues.txt'),str(out/'final.mp4')],check=True,stdout=log,stderr=log)
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(out/'final.mp4')]))
    v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio')
    assert (v['width'],v['height'])==(info['width'],info['height'])
    assert v['r_frame_rate']=='30/1'
    assert abs(float(probe['format']['duration'])-info['duration'])<.15
    subprocess.run(['ffmpeg','-v','error','-i',str(out/'final.mp4'),'-f','null','-'],check=True)
    report={'width':v['width'],'height':v['height'],'fps':v['r_frame_rate'],'duration':float(probe['format']['duration']),'audio_codec':a['codec_name'],'decode_check':'passed','render_engine':'HyperFrames 0.8.181 with actual NextPhase V1 devices','synthetic_voice':True,'captions':'ASR alignment, interpolated words flagged; manual frame-exact verification not claimed','music':'none; voice and synthesized V1 effects only'}
    (out/'verification.json').write_text(json.dumps(report,indent=2))
    subprocess.run(['ffmpeg','-v','error','-y','-ss','1','-i',str(out/'final.mp4'),'-frames:v','1',str(out/'poster.png')],check=True)
    (out/'voice.mp4').unlink()
    print('Verified',project['id'],report['duration'],'seconds',flush=True)

def render(project,args):
    folder=ROOT/'videos'/project['id'];out=folder/'out';out.mkdir(exist_ok=True)
    if (out/'verification.json').exists() and (out/'final.mp4').exists():return
    env=dict(os.environ,HYPERFRAMES_BROWSER_PATH='/usr/bin/chromium')
    if not args.mix_only and not (out/'render.mp4').exists():
        with (out/'render.log').open('w') as log:
            subprocess.run(['npx','-y','hyperframes@0.8.181','render',str(folder),'-q','draft','-f','30','--workers',str(args.workers),'-o',str(out/'render.mp4')],env=env,stdout=log,stderr=log,check=True)
    finish(project,args.python)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--only');ap.add_argument('--project-file',type=Path,default=ROOT/'content/creator-recreations/projects.json');ap.add_argument('--skip-first',action='store_true');ap.add_argument('--mix-only',action='store_true');ap.add_argument('--workers',type=int,default=4);ap.add_argument('--python',default='/workspace/scratch/ev1-venv/bin/python');args=ap.parse_args()
    projects=json.loads(args.project_file.read_text())
    for project in projects:
        if args.only and args.only!=project['id']:continue
        if args.skip_first and project['number']==1:continue
        render(project,args)
