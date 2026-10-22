from pathlib import Path
import json,subprocess,concurrent.futures
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent;R=P.parent;G=P/'generated';A=1120/30;D=83.7-A
plan=json.loads((P/'storyboard.json').read_text())
subprocess.run(['ffmpeg','-v','error','-y','-i',str(G/'render.mp4'),'-i',str(R/'assets/narration.wav'),'-map','0:v','-map','1:a','-c:v','copy','-af','loudnorm=I=-18:TP=-2:LRA=7','-t',str(D),'-c:a','aac','-b:a','192k','-movflags','+faststart',str(G/'graphics.mp4')],check=True)
f="[0:v]scale=640:360,pad=640:392:0:32:color=0x172129,drawtext=text='ORIGINAL':x=12:y=8:fontsize=18:fontcolor=white[a];[1:v]scale=640:360,pad=640:392:0:32:color=0x172129,drawtext=text='REVISED GRAPHICS':x=12:y=8:fontsize=18:fontcolor=white[b];[a][b]hstack[v]"
subprocess.run(['ffmpeg','-v','error','-y','-i',str(R/'source.mp4'),'-i',str(G/'graphics.mp4'),'-filter_complex',f,'-map','[v]','-map','1:a','-c:v','libx264','-crf','19','-preset','fast','-c:a','aac','-movflags','+faststart','-shortest',str(G/'comparison.mp4')],check=True)
variants=['presenter-to-product','product-definition','data-tools-connections','question-to-answer','answer-to-action','governance-enclosure','card-to-family','audience-annotation','technical-role','shared-access','domain-specialization','speaker-return']
templates=['product-mechanism-example']*6+['product-family']*5+['product-mechanism-example']
sourceids=['02-white-system']*6+['03-layered-cards']*5+['03-layered-cards']
manifest=[]
def make_scene(item):
 i,s=item;folder=G/('scene-'+s['id']);folder.mkdir(exist_ok=True);start=max(0,round((s['source_start']-A)*30)/30);end=min(D,round((s['source_end']-A)*30)/30);dur=end-start
 times=[min(end-1/30,start+1/30),(start+end)/2,max(start,end-2/30)]
 for phase,t in zip(['start','middle','end'],times):
  for role,file in [('original',R/'source.mp4'),('generated',G/'graphics.mp4')]:
   out=folder/f'{role}-{phase}.png';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(file),'-frames:v','1',str(out)],check=True)
  im=Image.new('RGB',(1280,392),'#172129');d=ImageDraw.Draw(im)
  for col,role in enumerate(['original','generated']):im.paste(Image.open(folder/f'{role}-{phase}.png').resize((640,360)),(col*640,32));d.text((col*640+12,9),f'{role.upper()} | source {t+A:.3f}s',fill='white')
  im.save(folder/f'comparison-{phase}.jpg',quality=92)
 # Standalone keyframe graphic: native rendered output, not an AI image edit.
 im=Image.open(folder/'generated-end.png')
 if s['id'] not in ['01','12']:im=im.crop((24,72,1395,972))
 im.save(folder/'graphic.png')
 for name,file in [('motion',G/'graphics.mp4'),('comparison',G/'comparison.mp4')]:subprocess.run(['ffmpeg','-v','error','-y','-ss',str(start),'-i',str(file),'-t',str(dur),'-c:v','libx264','-crf','19','-preset','fast','-c:a','aac','-movflags','+faststart',str(folder/(name+'.mp4'))],check=True)
 return {**s,'template_id':templates[i],'template_variant':variants[i],'reference_sequence':sourceids[i],'render_start':start,'render_end':end,'duration':dur,'sample_source_times':{phase:round(t+A,4) for phase,t in zip(['start','middle','end'],times)},'folder':str(folder.relative_to(G)),'output_status':'rendered_for_review','reuse_parameters':['product names','audience labels','question','evidence/result values','action text','permission constraint','domain role'],'fixed_structure':'See scene composition and reference-derived template; replace content only after semantic validation','state_plan':s['motion_plan'],'reconstruction_claim':'structural reconstruction with static fictional presenter; not pixel-exact'}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:manifest=list(pool.map(make_scene,enumerate(plan['scenes'])))
(G/'manifest.json').write_text(json.dumps({'duration':D,'fps':30,'scenes':manifest,'coverage':'All 12 scenes in the current 46-second storyboard; 27 source sequences catalogued separately'},indent=2))
for g in range(3):
 im=Image.new('RGB',(1280,392*4),'#172129')
 for row,s in enumerate(manifest[g*4:g*4+4]):im.paste(Image.open(G/s['folder']/'comparison-end.jpg'),(0,row*392))
 im.save(G/f'comparison-sheet-{g+1}.jpg',quality=92)
print('Exported all 12 scene motions, 36 matched frame pairs, 12 isolated graphic keyframes and combined comparison')
