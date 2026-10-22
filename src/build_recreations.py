"""Build native HyperFrames projects with the user's actual Editor V1 devices.

The 16:9 kit is adapted explicitly to 9:16. Source assets and timing remain editable.
"""
import argparse, json, math, os, shutil, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];KIT=ROOT/'vendor/editor-v1';CONTENT=ROOT/'content/creator-recreations'
sys.path.insert(0,str(KIT/'components'))
import ev1_devices as ev
ev.W,ev.H=1080,1920
from ev1_more import Comp,still,tile_reveal,keyword,captions,finish,sfx,fr

def build(project):
    out=ROOT/'videos'/project['id'];timing=out/'work/timeline.json'
    if not timing.exists():return False
    timeline=json.loads(timing.read_text());assets=json.loads((CONTENT/'asset-map.json').read_text())
    (out/'assets/ev1').mkdir(parents=True,exist_ok=True)
    shutil.copytree(KIT/'assets',out/'assets/ev1',dirs_exist_ok=True)
    (out/'assets/img').mkdir(exist_ok=True);(out/'out').mkdir(exist_ok=True)
    for beat in timeline['beats']:
        for file in assets[beat['asset']]['variants']:shutil.copyfile(CONTENT/'prepared'/file,out/'assets/img'/file)
    dur=fr(timeline['duration']+.6);c=Comp(dur);shots=[]
    c.css.append('''html,body{width:1080px;height:1920px}.ev1-layer,.ev1-fill,.ev1-grid,.ev1-vignette,.ev1-flash{width:1080px;height:1920px}.ev1-cap{width:1080px}:root{--ev1-cap-size:48px;--ev1-key-size:96px;--ev1-title-size:100px;--ev1-shock-size:128px}.ev1-cap{gap:.26em}.credit{position:absolute;left:72px;bottom:80px;font:20px var(--ev1-sans);color:var(--ev1-paper-edge)}''')
    for bi,beat in enumerate(timeline['beats']):
        start,end=fr(beat['start']),fr(beat['end']);key=beat['asset'];source=assets[key]
        # Reference layouts govern macro beats; V1's cuts and pushes govern internal motion.
        n=max(1,math.ceil((end-start)/1.35))
        for j in range(n):
            a=fr(start+(end-start)*j/n);b=fr(start+(end-start)*(j+1)/n)
            file=source['variants'][j%2];src='assets/img/'+file
            _,iid=still(c,a,b,src,z=1,push=1.04,origin='50% 44%',size=(1080,1920))
            if j==0 and bi in [0,3]:tile_reveal(c,a,src,z=2,seed=bi+1,size=(1080,1920))
            else:sfx(c,a,'click_soft',.65)
            c.at(f'tl.fromTo("#{iid}",{{filter:"blur(4px)"}},{{filter:"blur(0px)",duration:0.2,ease:"none",immediateRender:false}},{a:.4f});')
            shots.append({'start':a,'end':b,'source':key,'image':src,'device':'tile_reveal + still' if j==0 and bi in [0,3] else 'still + rack focus','reference':project['reference']})
        if key=='agent-select':
            # Real moving documentation footage, not an invented product execution.
            demo=CONTENT/'assets/agent-select-demo.mp4'
            if demo.exists():
                shutil.copyfile(demo,out/'assets/media/agent-select-demo.mp4')
                c.video(start,end,'assets/media/agent-select-demo.mp4',0,z=10,style='left:72px;top:410px;width:936px;height:850px;object-fit:contain')
        if beat.get('key'):
            size=min(94,int(920/max(1,len(beat['key']))/.57))
            keyword(c,start,end,beat['key'],z=40,x=540,y=275,kind='title' if bi%2 else 'key',size=size,blur_in=True)
        if project['number']==4 and bi in [2,3]:
            # Keep the choices visible through the deliberate pause, without showing
            # a source diagram that already labels the correct answer.
            c.clip(start,end,'<div style="position:absolute;left:72px;top:480px;width:936px;height:720px;background:var(--ev1-black)"></div>',z=30)
            words_for_beat=[w for w in timeline['words'] if start-.05<=w['s']<end]
            for qi,(label,token) in enumerate([('Import','Import'),('Direct Query','Query'),('Direct Lake','Lake')]):
                onset=next((w['s'] for w in words_for_beat if w['w'].strip('.,?!').lower()==token.lower()),start)
                keyword(c,onset,end,label,z=40,x=540,y=620+qi*190,kind='key',size=80,blur_in=False)
        # Preserve source timing. Unmatched ASR names are flagged in timeline.json.
        words=[w for w in timeline['words'] if beat['start']-.001<=w['s']<beat['voice_end']+.001]
        for wi in range(0,len(words),4):
            group=words[wi:wi+4];group_end=fr(words[wi+4]['s']) if wi+4<len(words) else end
            if not group or group_end<=fr(group[0]['s']):continue
            captions(c,[([(w['w'],w['s']) for w in group],group_end)],y='77%',z=60)
    c.clip(fr(timeline['duration']),dur,'<div class="ev1-layer ev1-black"></div>',z=1)
    finish(c,0,dur,z=80,grid=False,vignette=False)
    # Rotate the kit's own click variants instead of repeating a single transient.
    rotation=[('ev1kit/click_1',.20),('ev1kit/click_2',.19),('ev1kit/click_3',.20),('ev1kit/click_4',.18)];ri=0
    for i,(t,name,gain) in enumerate(c.cues):
        if name=='ev1kit/click_1':name,g=rotation[ri%4];ri+=1;c.cues[i]=(t,name,g)
    c.write(str(out/'index.html'),'assets/ev1/tokens.css',title=project['title'])
    doc=(out/'index.html').read_text().replace('width:1920px;height:1080px','width:1080px;height:1920px')
    doc=doc.replace('window.__timelines["main"] = tl;','window.__timelines=window.__timelines||{}; window.__timelines["main"] = tl;')
    (out/'index.html').write_text(doc);c.write_cues(str(out/'sfx-cues.txt'))
    (out/'kit.json').write_text(json.dumps({'skill':'../../vendor/editor-v1','format':'9:16 portrait adaptation','renderer':'hyperframes@0.8.181'},indent=2))
    (out/'work/shots.json').write_text(json.dumps(shots,indent=2));(out/'work/render-info.json').write_text(json.dumps({'duration':dur,'width':1080,'height':1920,'fps':30,'shots':len(shots),'synthetic_voice':True,'word_alignment':'automatic, some interpolated; see timeline.json'},indent=2))
    # Self-contained reproduction entry point, with no embedded credential or absolute kit path.
    (out/'build.py').write_text('from pathlib import Path\nimport subprocess,sys\nroot=Path(__file__).resolve().parents[2]\nsubprocess.run([sys.executable,str(root/"src/build_recreations.py"),"--only",Path(__file__).resolve().parent.name],check=True)\n')
    source_rows=[]
    for key in dict.fromkeys(b['asset'] for b in timeline['beats']):
        source_rows.append(f'| {key} | {assets[key]["credit"]} | {assets[key]["file"]} |')
    beat_rows=[f'| {b["start"]:.2f}–{b["end"]:.2f} | {b["text"]} | {b["asset"]} | {b["device"]} |' for b in timeline['beats']]
    plan=f'''# {project['title']} — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/{project['reference']}. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
{project['changes']}

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
{chr(10).join(beat_rows)}

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
{chr(10).join(source_rows)}

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only {project['id']}`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/{project['id']} -q draft -f 30 -o videos/{project['id']}/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
'''
    (out/'PLAN.md').write_text(plan)
    print('Built',project['id'],len(shots),'shots',dur,'seconds',flush=True)
    return True

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--only');args=ap.parse_args()
    for project in json.loads((CONTENT/'projects.json').read_text()):
        if not args.only or args.only==project['id']:build(project)
