import asyncio,json,subprocess,os
from pathlib import Path
import edge_tts
root=Path(__file__).parent
parts=[
'A Store is an entity type: a definition of something the business cares about.',
'Region and priority are properties.',
'Store operates Refrigeration Unit is a relationship between two entity types.',
'Data bindings map these definitions to source fields. The ontology supplies meaning and mappings; the data stays in its source.'
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
