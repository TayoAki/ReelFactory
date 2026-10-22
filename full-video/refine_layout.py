from render import *
# Frame the existing fictional host as a centered bust rather than a floating cutout.
im=Image.open(R.parent/'content/fabric-ontology/presenters.png').convert('RGBA');person=im.crop((0,0,im.width//2,im.height));person=person.crop(person.getbbox());person=person.resize((round(person.width*1480/person.height),1480),Image.Resampling.LANCZOS);host=Image.new('RGB',(1920,1080),'#24313a');host.paste(person,((1920-person.width)//2,-40),person);host.save(R/'assets/host-full.png')
# Correct short-card icon/title/body spacing after reviewing the first full-size keyframes.
scenes=[s for s in P['scenes'] if s['kind'] in ['native','hybrid','speaker','demo-overlay']]
for s in scenes:(O/(s['id']+'.mp4')).unlink(missing_ok=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for f in concurrent.futures.as_completed([ex.submit(render,s) for s in scenes]):print('Layout pass:',f.result(),flush=True)
previews()
run(['ffmpeg','-y','-f','concat','-safe','0','-i',str(R/'render-concat.txt'),'-i',str(R/'original.mp4'),'-map','0:v','-map','1:a','-c:v','copy','-c:a','copy','-t',str(P['source_duration']),'-movflags','+faststart',str(R/'full-reconstruction.mp4')])
