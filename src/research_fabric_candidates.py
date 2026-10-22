from pathlib import Path
import concurrent.futures,json,os,urllib.request,urllib.parse
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'research/fabric-youtube'
def get(ident):
 folder=OUT/ident;folder.mkdir(exist_ok=True);url='https://www.youtube.com/watch?v='+ident
 for name,endpoint,params in [('metadata','/v1/youtube/video',{'url':url}),('transcript','/v1/youtube/video/transcript',{'url':url})]:
  file=folder/(name+'.json')
  try:
   if file.exists():v=json.loads(file.read_text())
   else:
    req=urllib.request.Request('https://api.scrapecreators.com'+endpoint+'?'+urllib.parse.urlencode(params),headers={'x-api-key':os.environ['SCRAPECREATORS_API_KEY']})
    with urllib.request.urlopen(req,timeout=60) as r:v=json.load(r)
    file.write_text(json.dumps(v,indent=2))
   if name=='metadata':print(ident,v.get('title'),v.get('channel'),v.get('durationFormatted'),{k:v[k] for k in v if 'licen' in k.lower()},flush=True)
   else:print(ident,'transcript',list(v)[:8],flush=True)
  except Exception as e:print(ident,name,type(e).__name__,str(e),flush=True)
if __name__=='__main__':
 import sys
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(get,sys.argv[1:] or ['mFoSVcj6tLw','rWCAwo9jRqw']))
