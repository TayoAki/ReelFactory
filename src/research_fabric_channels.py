"""Bounded channel discovery; credentials stay in environment headers."""
from pathlib import Path
import json,os,urllib.request,urllib.parse,concurrent.futures
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'research/fabric-youtube';OUT.mkdir(exist_ok=True)
def get(handle,sort):
 file=OUT/f'{handle}-{sort}.json'
 if file.exists():data=json.loads(file.read_text())
 else:
  url='https://api.scrapecreators.com/v1/youtube/channel-videos?'+urllib.parse.urlencode({'handle':handle,'sort':sort});req=urllib.request.Request(url,headers={'x-api-key':os.environ['SCRAPECREATORS_API_KEY']})
  with urllib.request.urlopen(req,timeout=60) as r:data=json.load(r)
  file.write_text(json.dumps(data,indent=2))
 print(handle,sort,'retrieved',len(data.get('videos',[])),'videos',flush=True)
 return data
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(lambda p:get(*p),[(h,s) for h in ['MicrosoftReactor','GuyInACube','MicrosoftFabric'] for s in ['latest','popular']]))
