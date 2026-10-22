"""An original, result-first data story using actual V1 devices and retained NYC data.

No generated film, creator footage, false app execution, or rasterized text animation.
"""
import html,json,math,shutil,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];KIT=ROOT/'vendor/editor-v1';DATA=ROOT/'content/creator-recreations';ID='10-nyc-parker-pilot';OUT=ROOT/'videos'/ID
sys.path.insert(0,str(KIT/'components'))
import ev1_devices as ev
ev.W,ev.H=1080,1920
from ev1_more import Comp,captions,fr,sfx

def esc(x):return html.escape(str(x))
def load(name):return json.loads((DATA/name).read_text())['results']
def span(text,style='',cls=''):return f'<div class="{cls}" style="{style}">{esc(text)}</div>'

def main():
    timeline=json.loads((OUT/'work/timeline.json').read_text());beats=timeline['beats'];dur=fr(timeline['duration']+.55);c=Comp(dur)
    (OUT/'assets/ev1').mkdir(parents=True,exist_ok=True);(OUT/'out').mkdir(exist_ok=True)
    shutil.copytree(KIT/'assets',OUT/'assets/ev1',dirs_exist_ok=True)
    categories=load('nyc-results.json');hours=sorted(load('noise_hours.json'),key=lambda x:int(x['hour']));months=sorted(load('heat_months.json'),key=lambda x:int(x['month']));days=load('noise_days.json');total=sum(int(x['total']) for x in categories);sunday=next(int(x['total']) for x in days if x['day']=='0');january=int(months[0]['total']);august=int(months[7]['total'])
    c.css.append('''html,body{width:1080px;height:1920px}.ev1-layer,.ev1-fill{width:1080px;height:1920px}.ev1-cap{width:1080px;gap:.25em}:root{--ev1-cap-size:48px}.scene{position:absolute;inset:0;background:var(--ev1-black);color:var(--ev1-white);font-family:var(--ev1-sans)}.top{position:absolute;left:66px;top:68px;font-size:26px;letter-spacing:.09em}.date{position:absolute;right:66px;top:72px;font-size:22px;color:var(--ev1-paper-edge)}.h{position:absolute;left:66px;top:160px;font-size:72px;line-height:1.08;letter-spacing:-.035em;font-weight:700;width:950px}.hero{position:absolute;left:66px;top:250px;font:700 144px/.95 var(--ev1-grotesk);letter-spacing:-.05em}.sub{position:absolute;left:72px;top:420px;font-size:30px;color:var(--ev1-paper-edge)}.panel{position:absolute;left:56px;top:490px;width:968px;height:1030px;border:1px solid var(--ev1-teal);border-radius:30px;background:linear-gradient(155deg,var(--ev1-teal),var(--ev1-black) 38%);overflow:hidden}.panel-label{position:absolute;left:32px;top:30px;font-size:25px;letter-spacing:.03em;color:var(--ev1-paper-edge)}.foot{position:absolute;left:66px;top:1800px;font-size:23px;line-height:1.6;color:var(--ev1-paper-edge)}.row{position:absolute;left:36px;right:36px;height:116px}.label{font-size:31px;line-height:38px}.value{position:absolute;right:0;top:0;font:700 36px/1.1 var(--ev1-grotesk)}.track{position:absolute;left:0;top:57px;height:35px;width:892px;border-radius:7px;background:var(--ev1-teal)}.fill{position:absolute;inset:0;background:var(--ev1-paper-edge);border-radius:7px;transform-origin:0 50%}.accent{color:var(--ev1-amber)}.query{position:absolute;left:34px;top:115px;font:28px/1.75 var(--ev1-mono);white-space:pre-wrap;color:var(--ev1-paper);width:900px}.pill{position:absolute;left:34px;top:90px;padding:14px 22px;border:1px solid var(--ev1-amber);border-radius:30px;font-size:28px;color:var(--ev1-paper)}.small{font-size:25px;color:var(--ev1-paper-edge)}.metric{position:absolute;font:700 88px/1 var(--ev1-grotesk);letter-spacing:-.03em}.source-table{position:absolute;left:34px;top:600px;right:34px;font:24px/1.8 var(--ev1-mono)}.source-table div{display:flex;justify-content:space-between;border-bottom:1px solid var(--ev1-teal);padding:12px 0}.highlight{color:var(--ev1-amber)}''')
    shots=[]
    def atword(text,beat,default=None):
        return next((w['s'] for w in timeline['words'] if beat['start']-.01<=w['s']<beat['voice_end'] and w['w'].strip('.,?!').lower()==text.lower()),beat['start'] if default is None else default)
    def frame(title,hero='',sub=''):
        return '<div class="scene">'+span('NYC / 311',cls='top')+span('12 MONTHS OF PUBLIC DATA',cls='date')+span(title,cls='h')+(span(hero,cls='hero') if hero else '')+span(sub,cls='sub')+span('NYC Open Data · Oct 1, 2025 – Sep 30, 2026\nRequest counts · saved public API results',style='white-space:pre-line',cls='foot')
    def show(t0,t1,inner,device,label):
        cid=c.clip(t0,t1,inner+'</div>',z=1);shots.append({'start':fr(t0),'end':fr(t1),'scene':label,'device':device,'evidence':'retained NYC API responses'});return cid
    def ranking(start,accent=False):
        rows=''
        for i,r in enumerate(categories[:5]):
            value=int(r['total']);ratio=value/int(categories[0]['total']);bid=c.uid('bar')
            color='var(--ev1-amber)' if i==0 else 'var(--ev1-paper-edge)'
            rows+=f'<div class="row" style="top:{126+i*166}px">{span(r["complaint_type"],cls="label")}{span(f"{value:,}",cls="value")}<div class="track"><div id="{bid}" class="fill" style="background:{color};transform:scaleX(0)"></div></div></div>'
            c.at(f'tl.fromTo("#{bid}",{{scaleX:0}},{{scaleX:{ratio:.6f},duration:0.8,ease:"power2.out",immediateRender:false}},{start+.12+i*.11:.4f});')
        return '<div class="panel">'+span('REQUESTS BY CATEGORY',cls='panel-label')+rows+'</div>'
    def columns(data,xkey,start,kind='hours',sunday_card=False):
        values=[int(r['total']) for r in data];maximum=max(values);count=len(data);width=870/count;pieces=[];bottom=805 if not sunday_card else 715;height=470 if not sunday_card else 390
        for i,r in enumerate(data):
            val=int(r['total']);h=height*val/maximum;x=51+i*width;label=str(r[xkey]);bid=c.uid('column');peak=val==maximum;fill='var(--ev1-amber)' if peak else 'var(--ev1-paper-edge)'
            pieces.append(f'<rect id="{bid}" x="{x:.1f}" y="{bottom-h:.1f}" width="{max(12,width-10):.1f}" height="{h:.1f}" rx="4" fill="{fill}" style="opacity:0"/>')
            # Opacity reveal preserves the actual baseline and relative data geometry.
            # SVG scale origins vary across Chrome/GSAP and can distort the baseline.
            c.at(f'tl.fromTo("#{bid}",{{opacity:0}},{{opacity:1,duration:0.35,ease:"none",immediateRender:false}},{start+.2+i*.018:.4f});')
            if kind!='hours' or i%4==0 or label=='22':pieces.append(f'<text x="{x+width/2-5:.1f}" y="{bottom+42}" fill="var(--ev1-paper-edge)" font-size="25" text-anchor="middle">{label}</text>')
        title='RESIDENTIAL NOISE / BY HOUR' if kind=='hours' else 'HEAT / HOT WATER / BY MONTH'
        axis='Hour of day (0–23)' if kind=='hours' else 'Calendar month (1–12)'
        pieces.append(f'<text x="50" y="{bottom-height-32}" fill="var(--ev1-paper-edge)" font-size="25">Peak: {maximum:,} requests</text>')
        inner='<div class="panel">'+span(title,cls='panel-label')+f'<div class="pill">{esc("Noise - Residential" if kind=="hours" else "HEAT/HOT WATER")}</div>'
        inner+=f'<svg viewBox="0 0 968 1030" style="position:absolute;inset:0;width:968px;height:1030px;font-family:var(--ev1-sans)">{"".join(pieces)}<text x="484" y="{bottom+93}" text-anchor="middle" font-size="26" fill="var(--ev1-paper-edge)">{axis}</text></svg>'
        if sunday_card:inner+=f'<div style="position:absolute;left:34px;right:34px;top:850px;border-top:1px solid var(--ev1-teal);padding-top:22px">{span("Sunday",style="font-size:40px;font-weight:700")}{span(f"{sunday:,} requests",style="position:absolute;right:0;top:28px;font-size:35px",cls="accent")}</div>'
        return inner+'</div>'
    for i,b in enumerate(beats):
        a,z=fr(b['start']),fr(b['end']);scene=b['scene'];sfx(c,a,'click_soft',.6)
        if scene=='overview':show(a,z,frame('Almost four million',f'{total:,}','The biggest category wasn’t noise.')+ranking(a), 'ranked result reveal','Overview / real result first')
        elif scene=='parking':show(a,z,frame('Illegal parking',f'{int(categories[0]["total"]):,}','The largest category in the same dataset.')+ranking(a,True),'same chart, value emphasis','Parking result')
        elif scene=='query':
            q="created_date >= '2025-10-01T00:00:00'\nAND\ncreated_date <  '2026-10-01T00:00:00'"
            content=frame('One year of 311 data','', 'The actual date filter used for the public API query.')+'<div class="panel">'+span('EXECUTED QUERY / DATE WINDOW',cls='panel-label')+f'<div class="query">{esc(q)}</div>'
            content+='<div style="position:absolute;left:34px;top:470px;font-size:36px;line-height:1.6">October 1, 2025<br><span class="small">through</span><br>September 30, 2026</div>'
            content+='<div style="position:absolute;left:34px;top:800px;font-size:30px" class="accent">data.cityofnewyork.us</div></div>';show(a,z,content,'query evidence card','Retained query window')
        elif scene=='noise':show(a,z,frame('Residential noise','','One category. Requests grouped by hour.')+columns(hours,'hour',a),'filter and chart transition','Noise hourly distribution')
        elif scene=='noise-proof':
            content=frame('10–11 p.m.','42,705','Residential noise requests in the busiest hour.')+columns(hours,'hour',a,sunday_card=True)
            show(a,z,content,'same chart, peak annotation and weekday proof','Noise peak + Sunday')
            sfx(c,atword('Sunday',b),'click_soft',.6)
        elif scene=='heat':show(a,z,frame('Heat / hot water','','Same dataset. A different seasonal pattern.')+columns(months,'month',a,kind='months'),'category switch, same visual grammar','Heat seasonality')
        elif scene=='contrast':
            split=fr(atword('And',b,default=a+(z-a)*.5));split=max(a+1, min(z-1,split));ratio=january/august
            rows=''
            for j,(label,val) in enumerate([('January',january),('August',august)]):
                bid=c.uid('comparison');rows+=f'<div class="row" style="top:{180+j*230}px">{span(label,cls="label")}{span(f"{val:,}",cls="value")}<div class="track"><div id="{bid}" class="fill" style="background:var(--ev1-amber);transform:scaleX(0)"></div></div></div>'
                c.at(f'tl.fromTo("#{bid}",{{scaleX:0}},{{scaleX:{val/january:.6f},duration:.8,ease:"power2.out",immediateRender:false}},{a+.2+j*.2:.4f});')
            show(a,split,frame('January / August',f'{ratio:.1f}×','Heat / hot water requests')+'<div class="panel">'+span('A SEASONAL COMPARISON',cls='panel-label')+rows+'</div>','two-value comparison','January compared with August')
            show(split,z,frame('Trapping pigeon','1','One request in the same twelve-month window.')+'<div class="panel">'+span('THE OTHER END OF THE DISTRIBUTION',cls='panel-label')+'<div style="position:absolute;left:38px;top:200px;font-size:44px">Radioactive Material <span class="accent">15</span><br><br>Squeegee <span class="accent">6</span><br><br>Trapping Pigeon <span class="accent">1</span></div></div>','contrast reveal','Rare category: one pigeon request');sfx(c,split,'click_soft',.8)
        else:
            rows=''.join(f'<div><span>{esc(r["complaint_type"])}</span><span>{int(r["total"]):,}</span></div>' for r in categories[:3])
            content=frame('Requests',f'{total:,}','Counts of requests, not unique incidents.')+'<div class="panel">'+span('KEEP THE EVIDENCE WITH THE STORY',cls='panel-label')+'<div class="query">Source: NYC Open Data\nWindow: 2025-10-01 to 2026-10-01\nGroup by: complaint_type\nOrder by: total DESC</div><div class="source-table">'+rows+'</div></div>'
            show(a,z,content,'return to result with query/response evidence','Close the proof loop')
        group=[w for w in timeline['words'] if b['start']-.001<=w['s']<b['voice_end']+.001]
        for n in range(0,len(group),4):
            words=group[n:n+4];end=fr(group[n+4]['s']) if n+4<len(group) else z
            if words and end>fr(words[0]['s']):captions(c,[([(w['w'],w['s']) for w in words],end)],y='86%',z=60)
    c.clip(fr(timeline['duration']),dur,'<div class="scene"></div>',z=1)
    c.write(str(OUT/'index.html'),'assets/ev1/tokens.css',title='NYC 311 / Parker-informed pilot')
    doc=(OUT/'index.html').read_text().replace('width:1920px;height:1080px','width:1080px;height:1920px').replace('window.__timelines["main"] = tl;','window.__timelines=window.__timelines||{};window.__timelines["main"] = tl;');(OUT/'index.html').write_text(doc)
    c.write_cues(str(OUT/'sfx-cues.txt'));(OUT/'work/shots.json').write_text(json.dumps(shots,indent=2));(OUT/'work/render-info.json').write_text(json.dumps({'duration':dur,'width':1080,'height':1920,'fps':30,'shots':len(shots),'synthetic_voice':True,'word_alignment':'automatic, see timeline.json'},indent=2))
    (OUT/'kit.json').write_text(json.dumps({'skill':'../../vendor/editor-v1','format':'9:16','renderer':'HyperFrames 0.8.181','study':'../../research/parker-prompts/STUDY.md'},indent=2))
    (OUT/'PLAN.md').write_text('''# A result-first NYC data story — Parker-informed pilot

The complete channel study and evidence limitations are in ../../research/parker-prompts/STUDY.md. This pilot carries its own data, identity and composition through meaningful transformations, replacing the previous screenshot-flip cadence. The original nine drafts are preserved.

## Sources and rights
All quantitative graphics are original SVG/HTML charts generated from the retained NYC Open Data responses in ../../content/creator-recreations/{nyc-results,noise_hours,noise_days,heat_months}.json. Public API query parameters and actual results are retained there. The date range is October 1, 2025 through September 30, 2026. There are 3,963,898 requests, including 611,282 illegal-parking requests; the residential-noise hourly peak is 22:00–22:59 with 42,705 requests, Sunday has 87,909, and heat/hot-water requests are 79,928 in January versus 3,682 in August (21.7×). Exactly one request is categorized Trapping Pigeon. These are request counts, not unique incident counts. No Fabric execution is claimed.

Parker's video is research material only. None of the creator's face, voice, films, footage, graphics, private prompts or music is reused. Fonts and synthesized effect sounds are from the licensed V1 kit. Narration is a local Kokoro synthetic draft voice. No music bed or external paid generation was used.

## Edit decisions
1. Reveal actual results in the opening scene.
2. Carry the same categories, colors and geometry from overview to the parking result.
3. Show the retained query window as the evidence interlude.
4. Change one data state at a time: category, hour grouping, weekday proof, then monthly grouping.
5. Pair January/August before revealing the rare pigeon category as a contrasting scale.
6. Finish on the result and reproducible query rather than a generic title card.

Every semantic shot has a purpose in work/shots.json and narration timings in work/timeline.json. Caption timing is automatic and not claimed to be manually verified within one frame. The visible charts are explanatory graphics, not a fabricated recording of a vendor application. All figures use the retained query results rather than invented illustrative values.

## Build
Run python src/build_parker_pilot.py from ReelFactory after creating the local voice/timeline with src/voice_recreations.py --project-file content/parker-pilot/projects.json. Render this native project with the vendored V1/HyperFrames workflow. No publication is performed.
''')
    print('Built original data-graphic pilot:',len(shots),'meaningful scenes,',dur,'seconds; January/August',round(january/august,2),flush=True)

if __name__=='__main__':main()
