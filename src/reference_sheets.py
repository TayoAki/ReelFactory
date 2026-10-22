"""Full-file cut detection and explicitly sampled visual review sheets."""
import concurrent.futures, json, re, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1] / 'research/references'
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)

def prepare(folder):
    video = folder / 'reference.mp4'
    if not video.exists() or (folder / 'review/index.json').exists(): return
    out = folder / 'review'; out.mkdir(exist_ok=True)
    probe = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(video)]))
    duration = float(probe['format']['duration'])
    log = subprocess.run(['ffmpeg','-hide_banner','-i',str(video),'-an','-vf',"scale=180:-2,select='gt(scene,0.28)',showinfo",'-vsync','vfr','-f','null','-'],capture_output=True,text=True,check=True).stderr
    cuts = [float(t) for t in re.findall(r'pts_time:([\d.]+)',log)]
    samples = sorted(set(round(min(duration-.5,t),3) for t in [0,.5,1,2,3,5]+[duration*i/23 for i in range(1,24)]))
    sheet = Image.new('RGB',(6*200,5*380),'#101820'); draw=ImageDraw.Draw(sheet)
    for i,t in enumerate(samples):
        file=out / f'sample-{i:02}.jpg'
        subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(video),'-frames:v','1','-vf','scale=200:356:force_original_aspect_ratio=decrease,pad=200:356:(ow-iw)/2:(oh-ih)/2,format=yuvj420p',str(file)],check=True)
        x=i%6*200;y=i//6*380;sheet.paste(Image.open(file),(x,y));draw.text((x+5,y+358),f'{t:.2f}s',font=FONT,fill='white')
    sheet.save(out/'overview.jpg',quality=90)
    (out/'index.json').write_text(json.dumps({'duration':duration,'cuts':cuts,'cut_detection':'full file, reduced-resolution scene score >0.28; candidates, not semantic scenes','samples':samples,'visual_review':'pending; sampled, not exhaustive','probe':probe},indent=2))
    print(folder.name,round(duration,2),'seconds',len(cuts),'cut candidates',flush=True)

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(prepare,[p for p in ROOT.iterdir() if p.is_dir()]))
