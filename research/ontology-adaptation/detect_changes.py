import json,subprocess,os,re
root=os.path.dirname(__file__);rows=json.load(open(root+'/uploaded-parts.json'));offset=0;out=[]
for i,r in enumerate(rows):
 p=subprocess.run(['ffmpeg','-hide_banner','-i',r['path'],'-vf',"scale=160:90,select='gt(scene,0.18)',showinfo",'-an','-f','null','-'],stderr=subprocess.PIPE,text=True)
 ts=[float(t) for t in re.findall(r'pts_time:([0-9.]+)',p.stderr)];out.extend(dict(part=i,local=t,global_time=offset+t) for t in ts);offset+=r['duration']
json.dump(out,open(root+'/visual-change-candidates.json','w'),indent=2);print(len(out),'change candidates');print([round(x['global_time'],2) for x in out])
