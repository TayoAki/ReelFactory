import asyncio,json,subprocess,os
from pathlib import Path
import edge_tts
root=Path(__file__).parent
parts=[
'Which refrigeration units does a store operate?',
'Model Store and Refrigeration Unit as entity types: reusable definitions of business concepts.',
'Region and priority are properties that describe a store.',
"Name the relationship operates. In Microsoft's example, the store's Location ID matches the unit's Store ID.",
'Data bindings map the definitions to their source tables in a lakehouse.',
'A consuming application uses these mappings to query the sources. The ontology defines the connection; source records stay in their owning systems.'
]
async def main():
 timeline=[];t=0
 for i,text in enumerate(parts):
  audio=root/'assets'/f'voice-{i}.mp3';events=[]
  c=edge_tts.Communicate(text,'en-US-JennyNeural',rate='-4%',proxy=os.environ.get('HTTPS_PROXY'),boundary='WordBoundary')
  with open(audio,'wb') as f:
   async for item in c.stream():
    if item['type']=='audio':f.write(item['data'])
    elif item['type']=='WordBoundary':events.append(item)
  duration=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(audio)]))
  timeline.append({'start':t,'duration':duration,'text':text,'words':events});t+=duration+.55
 (root/'narration.json').write_text(json.dumps({'voice':'Microsoft Edge en-US-JennyNeural; synthetic preview narration','segments':timeline,'duration':t+.5},indent=2))
 print('Duration',t+.5)
asyncio.run(main())
