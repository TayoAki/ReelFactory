import asyncio,json,subprocess,os
from pathlib import Path
import edge_tts
R=Path(__file__).parent
D=json.loads((R/'dialogue.json').read_text())
async def main():
 timeline=[];t=0
 for i,s in enumerate(D['segments']):
  audio=R/'assets'/f'voice-{i}.mp3';events=[]
  voice='en-US-GuyNeural' if s['role']=='host' else 'en-US-JennyNeural'
  c=edge_tts.Communicate(s['text'],voice,rate='-2%',proxy=os.environ.get('HTTPS_PROXY'),boundary='WordBoundary')
  with open(audio,'wb') as f:
   async for item in c.stream():
    if item['type']=='audio':f.write(item['data'])
    elif item['type']=='WordBoundary':events.append(item)
  dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(audio)]))
  timeline.append({**s,'start':t,'duration':dur,'voice':voice,'words':events});t+=dur+.18
 (R/'narration.json').write_text(json.dumps({'voice':'Two synthetic preview voices; static fictional portrait placeholders','segments':timeline,'duration':t+.6},indent=2));print('Duration',t+.6,flush=True)
asyncio.run(main())
