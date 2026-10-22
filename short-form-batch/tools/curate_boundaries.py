from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];p=R/'recording-clips/manifest.json';D=json.loads(p.read_text());allw=[w for s in json.loads((R/'source-audio/transcript-base.json').read_text())['segments'] for w in s['words']]
def norm(s):return re.sub('[^a-z0-9]','',s.lower())
def find(phrase,t,edge):
 inds=[i for i,w in enumerate(allw) if abs(w[edge]-t)<45];s='';bounds=[]
 for i in inds:
  a=len(s);s+=norm(allw[i]['word']);bounds.append((a,len(s),i))
 q=norm(phrase);hits=[];a=s.find(q)
 while a>=0:
  b=a+len(q);ids=[i for x,y,i in bounds if y>a and x<b]
  hits.append(ids[0] if edge=='start' else ids[-1]);a=s.find(q,a+1)
 if not hits:return None
 return min(hits,key=lambda i:abs(allw[i][edge]-t))
anchors={
1:('You are sitting at your desk','collection of totally disconnected facts'),2:(None,'agnostic to your business reality'),3:('Or consider something as ubiquitous','store manager cares about today'),4:('inventory at risk is a brilliant example',None),5:('Having raw data and an LLM','functional reality for most enterprises today'),6:('A human analyst has to listen','walks right out the door with them'),7:('Microsoft fabric is an architectural attempt','reporting tools'),8:(None,'depending on their specific needs'),9:('Well shortcuts are a response','AWS or Google Cloud'),10:('Which naturally raises the question','actual concepts and connections'),11:("Let's break down the primary components",'instance of the store entity'),12:('For our store entity',None),13:('Data bindings are perhaps',None),14:(None,'Namespaces prevent those semantic collisions'),15:(None,'derive a highly specific entity called frozen product'),16:('a derived type does not automatically inherit','mapped to the tables'),17:('ordinary relationships are not automatically inherited','relationship for the derived type'),18:('The current agent does not automatically',None),19:('The system is designed so you can generate','entities and properties'),20:('You rarely have just one perfect semantic model','finance customer entities'),21:('The ontology operates entirely by reference',None),22:('To generate an ontology from a semantic model','underlying Power BI model'),23:('A relational database might have a column named',None),24:('Because if the AI assumes the temperature',None),25:(None,'they mean the exact same entity'),26:(None,None),27:('In the ontology interface you can document inventory risk',None),28:('Writing the rule supplies the strategic context','standardized for the whole company'),29:('When a data engineer sets up these bindings','Power BI semantic models'),30:(None,'appropriate native underlying engine'),31:('Data freshness depends entirely on the execution path','verify the reporting periods'),32:(None,None),33:('Before you make any meaningful change',None),34:('The prompt is review priority stores','next expected inbound delivery'),35:('The operator still has to check the receipts','a human can rigorously mathematically check'),36:(None,'using the exact same filters'),37:(None,'every matching record in the database'),38:('The built in ontology agent does not operate','underlying source databases'),39:('Lets say I am the lead data engineer','not just the developers God mode account'),40:('How do we predict tomorrows inventory risk','inside a data science notebook'),41:('before you ever display the output of a predictive model','a deterministic fact'),42:('Lets say a specific agricultural supplier calls you','currently holding them on the floor'),43:('It also absolutely requires entity keys','Not at this time no'),44:('So clarify the architecture in my head','question being asked'),45:(None,'recommend proactive responses'),46:('MCP stands for Model Context Protocol',None),47:('If you want to set up operational monitoring',None),48:(None,'against the supported data path'),49:('The source talks about using the fabric IQ','point it specifically at the Power BI report'),50:(None,'before they ever distribute that document'),51:('The source mentions a maximum conversation lifetime','in the ontology definitions themselves'),52:('The preview does support importing existing definitions',None),53:('Microsoft has established a hard retirement date','teams need to plan resources for it now'),54:('Do not borrow percentage improvement benchmarks','in your final calculation'),55:(None,None),56:(None,None),57:('What happens during a major corporate merger',None)}
issues=[]
for c in D['clips']:
 num=int(c['id'][1:]);a,b=anchors[num];ia=find(a,c['source_start'],'start') if a else None;ib=find(b,c['source_end'],'end') if b else None
 if a and ia is None:issues.append((c['id'],'start',a))
 if b and ib is None:issues.append((c['id'],'end',b))
 if ia is not None:c['source_start']=max(0,allw[ia]['start']-.14)
 if ib is not None:c['source_end']=allw[ib]['end']+.14
 if num==3:c['source_end']=308.2;c['boundary_note']='Retain the complete expected-arrival sentence.'
 if num==13:c['source_end']=841.02;c['boundary_note']='Retain the complete lakehouse-table phrase; full-file ASR dropped words at its decoder boundary.'
 if num==27:c['source_end']=1592.08;c['boundary_note']='Retain the complete downstream-agent phrase.'
 c['duration']=c['source_end']-c['source_start'];c['words']=[{**w,'start':w['start']-c['source_start'],'end':w['end']-c['source_start']} for w in allw if w['start']>=c['source_start'] and w['end']<=c['source_end']];c['transcript_asr']=' '.join(w['word'] for w in c['words'])
 c['part_ranges']=[]
 for part in json.loads((R/'source-audio/manifest.json').read_text())['parts']:
  p0=part['offset'];p1=p0+part['duration']
  if c['source_end']>p0 and c['source_start']<p1:c['part_ranges'].append({'part':part['name'],'start':max(c['source_start'],p0)-p0,'end':min(c['source_end'],p1)-p0})
 if num==43:c.update(title='Graph keys and semantic-model limits',family='boundary',left_label='Defined entity keys',right_label='Semantic-model exclusion',focus_label='Preview projection limits')
 if num==44:c['family']='contrast'
 if num==49:c['duration']=c['source_end']-c['source_start']
 if num==32:c['review_flags'].append('Source uses sandbox as a metaphor; diagram labels definition preview, not a security-isolation guarantee.')
 if num==33:c['context_label']='Ontology definition only'
 if num==38:c['context_label']='Interactive agent · signed-in user'
 if num==39:c['context_label']='Example: source RLS configured'
 if num==43:c['context_label']='Preview context · Oct 2026'
 if num==45:c['context_label']='Roles vary by supported integration'
 if num==55:c['context_label']='Preview billing · Oct 2026'
 c['boundary_review']='Reviewed for self-contained start/end; continuous source audio only'
p.write_text(json.dumps(D,indent=2));(R/'recording-clips/boundary-review.json').write_text(json.dumps({'unmatched_anchors':issues,'manual_source_boundaries':['C13','C27'],'source_audio_unchanged':True},indent=2));print('Anchor issues',issues);print('durations',min(c['duration'] for c in D['clips']),max(c['duration'] for c in D['clips']))
