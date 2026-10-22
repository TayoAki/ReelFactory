from pathlib import Path
import shutil,subprocess,json
root=Path('/workspace/ReelFactory');folder=root/'videos/14-fabric-ontology-explained';out=folder/'out'
shutil.copy(out/'final.mp4',out/'fabric-ontology-smooth-v2.mp4')
subprocess.run(['ffmpeg','-v','error','-y','-ss','20.2347','-i',str(out/'final.mp4'),'-t','22.57','-c:v','libx264','-preset','fast','-crf','19','-c:a','aac','-movflags','+faststart',str(out/'smooth-motion-preview.mp4')],check=True)
subprocess.run(['python',str(root/'src/package_fabric_ontology_review.py')],check=True,cwd=root)
shutil.copy(root/'fabric-ontology-review.html',root/'fabric-ontology-smooth-review.html')
p=root/'studio.html';s=p.read_text().replace('href="fabric-ontology-review.html"','href="fabric-ontology-smooth-review.html"');p.write_text(s)
print('Packaged uniquely named revision and 22.57-second motion preview')
