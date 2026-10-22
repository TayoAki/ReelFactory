"""Generate the approved reference-study board from the existing editable reconstruction.
This is a reference renderer adapter, not an arbitrary-script-to-video compiler.
"""
from pathlib import Path
import shutil,json
P=Path(__file__).resolve().parent;R=P.parent;G=P/'generated';G.mkdir(exist_ok=True)
shutil.copytree(R/'assets',G/'assets',dirs_exist_ok=True)
s=(R/'index.html').read_text()
s=s.replace('.family{left:173px;top:108px;', '.family{left:165px;top:105px;')
s=s.replace('tl.to("#family",{...{"y": -25}', 'tl.to("#family",{...{"y": -22, "x": 8}')
# Reproduce the source's smaller stack extrusion while keeping the front card stable.
for k in range(1,6):s=s.replace('"x": '+str(k*7)+', "y": '+str(k*10)+', "z"', '"x": '+str(k*7)+', "y": '+str(k*8)+', "z"')
# Generic database symbol uses the sourced, consistent Fluent asset; product identity stays distinct.
import re
fluent=(R.parents[1]/'content/visual-language/assets/database.svg').read_text()
# Existing diagram geometry is retained; replacing its SVG is safe within the fixed node container.
s=re.sub(r'(<div id="data"[^>]*>)<svg.*?</svg>',lambda m:m[1]+fluent,s,count=1,flags=re.S)
# Findings from the matched source-frame comparison, not transcript timing guesses.
s=s.replace('gsap.set("#family",{opacity:0,y:20});','gsap.set("#family",{opacity:0,y:0,scale:0.02});')
s=s.replace('tl.to("#family",{...{"opacity": 1, "y": 0},duration:1,ease:"power2.out",immediateRender:false},1.1333333333333333);','tl.to("#family",{...{"opacity": 1, "y": 0, "scale": 1},duration:0.6,ease:"power2.out",immediateRender:false},2.466666666666667);')
s=s.replace('tl.to("#intro-speaker",{...{"opacity": 0},duration:0.033,ease:"power2.inOut",immediateRender:false},1.8666666666666667);','tl.to("#intro-speaker",{...{"opacity": 0},duration:0.033,ease:"power2.out",immediateRender:false},2.066666666666663);')
s=s.replace('"y": -22, "x": 8','"y": -30, "x": 8')
# Readable plane contents: retain the initial flat-card sizes, enlarge text as its plane tilts.
s=s.replace('</style>', '#code strong,#agents strong{font-size:16px}#code small{font-size:9.5px}#agents small{font-size:12px}#code img,#agents img{width:50px;height:50px}.node svg{fill:currentColor;stroke:none}#chat-boundary b svg{width:17px;height:17px;display:block;margin:1px auto;fill:currentColor}\n</style>')
s=s.replace('window.__timelines=window.__timelines||{};', 'tl.to("#one strong",{fontSize:16,duration:.533},17.833333333333332);tl.to("#one small",{fontSize:12,duration:.533},17.833333333333332);tl.to("#one img",{width:50,height:50,duration:.533},17.833333333333332);\nwindow.__timelines=window.__timelines||{};')
shield=(R.parents[1]/'content/visual-language/assets/permissions.svg').read_text()
s=s.replace('<b>◈</b>','<b>'+shield+'</b>')
(G/'index.html').write_text(s)
plan=json.loads((P/'storyboard.json').read_text());plan['status']='generation_requested';plan['production_allowed']=True
plan['authorization']='User explicitly requested generating all storyboard graphics for comparison in the latest message.'
for scene in plan['scenes']:
 scene['status']='generation_requested';scene['generation_authorized_by_user']=True
 # Authorization to generate is not a fidelity or final-review approval.
 scene['approved_by_user']=False
(P/'storyboard.json').write_text(json.dumps(plan,indent=2))
(G/'generation.json').write_text(json.dumps({'scope':'all 12 scenes of the current storyboard','source':'editable V1/GSAP reference reconstruction reused and adjusted; no new synthetic presenter images','output':'fresh render, three keyframes and source comparisons per scene','source_in':1120/30,'source_out':83.7,'renderer':'V1/GSAP + Hyperframes; not Remotion','approval':'generation authorized, final fidelity not approved'},indent=2))
print('Generated editable graphics composition for all 12 storyboard scenes')
