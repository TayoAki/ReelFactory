import json,subprocess
from pathlib import Path
from lab import run
root=Path(__file__).resolve().parents[1]
e=run();assert all(e['checks'].values())
p=root/'output/fabric-watermark-silent.mp4'
r=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
v=next(s for s in r['streams'] if s['codec_type']=='video')
assert (v['width'],v['height'])==(1080,1920)
assert v['codec_name']=='h264'
assert not any(s['codec_type']=='audio' for s in r['streams'])
assert abs(float(r['format']['duration'])-40)<.1
assert v['avg_frame_rate']=='24/1'
subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True)
print('PASS: 3 lab assertions; 40-second 1080x1920 H.264 at 24 fps; silent; full video decoded.')
