"""Keep teaching choice, rejected alternative and reference limits with every graphic."""
import pathlib,json
P=pathlib.Path(__file__).resolve().parents[1]/'recording-clips';d=json.loads((P/'manifest.json').read_text())
alternatives={
 'contrast':('A single explanatory list','A list obscures that one term/value can have competing interpretations; retain a common anchor and compare the two meanings.'),
 'entities':('An unlabeled network of nodes','The lesson depends on named object kinds and a named relation, not generic connectivity.'),
 'ownership':('An unlabeled one-way data pipeline','That can imply copying or calculation ownership. Label the source and consumer and state what the reference or mapping actually does.'),
 'hierarchy':('A flat category list','A list hides inherited structure or query scope. Distinguish parent, derived type and explicit ordinary relationships.'),
 'workflow':('Parallel peer cards','Use ordering only where the recording actually has sequential processing/review; C29 instead retains parallel source routes.'),
 'boundary':('A seamless automatic execution pipeline','That would erase separate access, configuration or execution responsibilities and could imply an action occurred.'),
 'evidence':('A confident numerical result chart','No executed result is supplied. Show the evidence checks the speaker actually asks for.'),
 'graph':('A flat list of affected items','The lesson is the path joining the named entities. A path diagram makes the hypothetical traversal explicit without claiming a measured result.'),
}
for c in d['clips']:
 p=P/'storyboards'/c['id']/'storyboard.json';s=json.loads(p.read_text());alt,why=alternatives[c['family']]
 if c['id']=='C25':alt='Two separate entity nodes';why='The spoken lesson is that Shops is a synonym for the same entity type, so the labels and double-headed name relation must prevent a duplicate-entity interpretation.'
 if c['id']=='C29':alt='An ordered ingestion pipeline';why='Lakehouse, Eventhouse and semantic model are source categories, not three required sequential steps.'
 s.update({'viewer_understanding_before':c['left_label'],'viewer_understanding_after':c['focus_label'],'graphic_choice_reason':c['title']+': '+s['why'],'credible_alternative':alt,'why_alternative_rejected':why,'cannot_establish':'This illustrative diagram cannot prove an actual product interaction, executed query, security guarantee or measured improvement.','reference_images_used_for_generation':['reference-library/frames/graphic/0003510.jpg','motion-pilot-fabric/fabric-theme/master.png','short-form-batch/recording-clips/assets/host.png','short-form-batch/recording-clips/assets/guest.png'],'source_library_semantic_match':'Original reference supplies visual grammar; exact subject relationships are adapted from this recording. No claim of an exact reference-video semantic or motion match.','original_reference_url':'https://www.youtube.com/watch?v=HtR5m5VjaDQ','review_status':'Draft; representative visual samples and artifact bounds checked, human editorial approval pending.'})
 p.write_text(json.dumps(s,indent=2))
print('57 per-clip teaching and alternative decisions saved')
