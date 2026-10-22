from pathlib import Path
import tarfile,json,subprocess,shutil,io
from PIL import Image,ImageDraw
import cairosvg
R=Path(__file__).resolve().parent;ROOT=R.parent;A=R/'assets';A.mkdir(exist_ok=True)
for name,src in [('sans.ttf','LiberationSans-Regular.ttf'),('bold.ttf','LiberationSans-Bold.ttf'),('serif.ttf','LiberationSerif-Regular.ttf')]:shutil.copy('/usr/share/fonts/truetype/liberation/'+src,A/name)
shutil.copy(ROOT/'content/visual-language/assets/LICENSE-fluent.txt',A/'LICENSE-fluent.txt')
t=tarfile.open('/workspace/scratch/fluentui-svg-icons-1.1.344.tgz');names=set(t.getnames());icons={'database':'database','document':'document','people':'people','shield':'shield_lock','search':'search','settings':'settings','calendar':'calendar','code':'code','table':'table','chart':'chart_multiple','globe':'globe','plug':'plug_connected','mail':'mail','check':'checkmark_circle','lock':'lock_closed','book':'book','branch':'branch','flow':'flowchart','person':'person','building':'building','folder':'folder','phone':'phone','arrow':'arrow_right','cloud':'cloud'}
manifest=[]
for key,name in icons.items():
 path='package/icons/'+name+'_24_regular.svg'
 if path not in names:continue
 svg=t.extractfile(path).read().decode();(A/(key+'.svg')).write_text(svg)
 for color,label in [('#eaf3f4','light'),('#58b5b0','teal'),('#eb795f','red'),('#35585f','dark')]:
  svg2=svg.replace('currentColor',color);png=cairosvg.svg2png(bytestring=svg2.encode(),output_width=144,output_height=144);(A/(key+'-'+label+'.png')).write_bytes(png)
 manifest.append({'id':key,'package':'@fluentui/svg-icons@1.1.344','file':path,'license':'MIT'})
(A/'icons.json').write_text(json.dumps(manifest,indent=2))
svg=(ROOT/'practice/databricks-01/assets/genie.svg').read_bytes();(A/'genie.png').write_bytes(cairosvg.svg2png(bytestring=svg,output_width=180,output_height=150))
# Reuse already-generated fictional presenter footage; these are ordinary video-layout assets.
subprocess.run(['ffmpeg','-v','error','-y','-ss','5','-i',str(ROOT/'practice/databricks-01/planning/generated/graphics-refined-v2.mp4'),'-frames:v','1','-vf','crop=438:534:1425:273',str(A/'guest-tile.png')],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-ss','45','-i',str(ROOT/'practice/databricks-01/planning/generated/graphics-refined-v2.mp4'),'-frames:v','1',str(A/'guest-full.png')],check=True)
im=Image.open(ROOT/'content/fabric-ontology/presenters.png').convert('RGBA');w,h=im.size
# Static fictional host, composited into a frame rather than synthesized lip motion.
host=Image.new('RGB',(1920,1080),'#24313a');crop=im.crop((0,0,w//2,h));crop.thumbnail((1300,1300));host.paste(crop,(300,0),crop);host.save(A/'host-full.png')
mask=Image.new('L',(438,534));ImageDraw.Draw(mask).rounded_rectangle((0,0,437,533),radius=36,fill=255);hosttile=im.crop((100,20,700,750)).resize((438,534));tile=Image.new('RGBA',(438,534),'#bac9bb');tile.alpha_composite(hosttile);tile.putalpha(mask);tile.save(A/'host-tile.png')
plan=json.loads((R/'plan.json').read_text())
for s in plan['scenes']:
 if s['kind'] in ['hybrid','demo','demo-overlay']:
  mid=(s['source_start']+s['source_end'])/2
  subprocess.run(['ffmpeg','-v','error','-y','-ss',str(mid),'-i',str(R/'original.mp4'),'-frames:v','1',str(A/(s['id']+'-ui.png'))],check=True)
print('Prepared',len(manifest),'consistent generic icons, fonts, static presenters and authentic UI evidence')
