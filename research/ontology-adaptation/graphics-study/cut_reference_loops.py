from pathlib import Path
import subprocess,json
root=Path(__file__).resolve().parent;parts=json.loads((root.parent/'uploaded-parts.json').read_text());offsets=[];off=0
for p in parts:offsets.append(off);off+=p['duration']
clips=[('A-stack','Card tilt and layer extrusion',54,58.5),('B-camera','Fixed window, moving architecture world',233,241.5),('C-connectors','Existing hub, source reveal, drawn branches',602,615),('D-ui-inspection','Live interface reframing and source inspection',1002,1022),('E-flip','Heading relocates; card flips into place',1428,1434.5),('F-agent','Parent reframing and branching agent graph',1484,1492),('G-emphasis','Single-frame list emphasis switch',1988.8,1991.8)]
rows=[]
for name,title,a,z in clips:
 k=max(i for i,o in enumerate(offsets) if o<=a);target=root/(name+'.mp4');subprocess.run(['ffmpeg','-v','error','-y','-ss',str(a-offsets[k]),'-i',parts[k]['path'],'-t',str(z-a),'-c:v','libx264','-preset','fast','-crf','18','-c:a','aac','-b:a','96k','-movflags','+faststart',str(target)],check=True);rows.append(dict(id=name,title=title,start=a,end=z,part=k,file=target.name))
(root/'reference-loops.json').write_text(json.dumps(rows,indent=2));print('7 reference motion loops across all five files')
