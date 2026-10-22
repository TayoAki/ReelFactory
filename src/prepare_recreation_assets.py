"""Prepare attributed documentation images and original charts from retained real data."""
import html, json, shutil, subprocess, textwrap
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

ROOT=Path(__file__).resolve().parents[1];CONTENT=ROOT/'content/creator-recreations';ASSETS=CONTENT/'assets'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def face(n,b=False):return ImageFont.truetype(BOLD if b else FONT,n)
def lines(draw,text,width,font):
    out=[];line=''
    for word in text.split():
        candidate=(line+' '+word).strip()
        if draw.textlength(candidate,font=font)>width and line:out.append(line);line=word
        else:line=candidate
    if line:out.append(line)
    return out

def excerpt(name,title,quote,url):
    im=Image.new('RGB',(1400,1000),'#f1f0ec');d=ImageDraw.Draw(im)
    d.text((70,65),'SOURCE EXCERPT',font=face(22,True),fill='#0e5560')
    y=130
    for line in lines(d,title,1250,face(54,True)):d.text((70,y),line,font=face(54,True),fill='#121214');y+=70
    y+=35
    for line in lines(d,quote,1240,face(35)):d.text((70,y),line,font=face(35),fill='#121214');y+=52
    d.text((70,910),url,font=face(19),fill='#0e5560')
    im.save(ASSETS/(name+'.png'))

def chart(name,labels,values,title,subtitle,horizontal=False):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17})
    fig,ax=plt.subplots(figsize=(12,8),dpi=150);fig.patch.set_facecolor('#f1f0ec');ax.set_facecolor('#f1f0ec')
    colors=['#0e5560']*len(values);colors[values.index(max(values))]='#d9822b'
    if horizontal:
        ax.barh(labels,values,color=colors);ax.invert_yaxis();ax.set_xlabel('Requests');ax.bar_label(ax.containers[0],fmt='{:,.0f}',padding=8,fontsize=14);ax.set_xlim(0,max(values)*1.25)
    else:
        ax.bar(labels,values,color=colors);ax.set_ylabel('Requests');ax.tick_params(axis='x',labelsize=12)
    ax.spines[['top','right']].set_visible(False);ax.set_title(title,loc='left',fontsize=24,fontweight='bold',pad=28)
    fig.text(.08,.025,subtitle,fontsize=11,color='#555');fig.tight_layout(rect=(.01,.06,.99,.96));fig.savefig(ASSETS/(name+'.png'));plt.close(fig)

def main():
    ASSETS.mkdir(exist_ok=True)
    excerpt('pause-excerpt','Pause and resume your Fabric capacity','When you pause your capacity, the remaining cumulative overages and smoothed operations on your capacity are summed, and added to your Azure bill.','learn.microsoft.com/en-us/fabric/enterprise/pause-resume')
    excerpt('claude-source','Claude Dashboards','Claude Dashboards connects to a data platform like BigQuery, Databricks or Snowflake, or a CRM tool like Salesforce, and is in beta on paid plans.','claude.com/resources/articles/dashboards-and-motion')
    excerpt('claude-connect','Connect your data','Connect your company’s data platform, such as Amazon Redshift, BigQuery, ClickHouse, Databricks, or Snowflake, and ask a question in plain language.','claude.com/resources/articles/dashboards-and-motion')
    excerpt('claude-question','Ask a specific question','Dashboards work well for quick, exploratory questions, like how this week’s signups compare with last month’s.','claude.com/resources/articles/dashboards-and-motion')
    excerpt('claude-query','Inspect the answer','Click any number to see the query behind it, or ask Claude to explain it. Each chart shows when its data was last refreshed.','claude.com/resources/articles/dashboards-and-motion')
    raw=json.loads((CONTENT/'nyc-results.json').read_text())['results'];total=sum(int(r['total']) for r in raw)
    excerpt('nyc-total','NYC 311 Service Requests',f'{total:,} requests\nOctober 1, 2025 through September 30, 2026. Aggregated directly through NYC Open Data’s public API; no Fabric execution.','data.cityofnewyork.us/resource/erm2-nwe9.json')
    subtitle='NYC Open Data · Oct 1 2025–Sep 30 2026 · requests, not unique incidents'
    chart('nyc-categories',[r['complaint_type'] for r in raw[:5]],[int(r['total']) for r in raw[:5]],'What New Yorkers reported',subtitle,True)
    hours=json.loads((CONTENT/'noise_hours.json').read_text())['results'];hours=sorted(hours,key=lambda r:int(r['hour']))
    chart('nyc-hours',[str(r['hour']) for r in hours],[int(r['total']) for r in hours],'Residential noise by hour of day',subtitle)
    heat=json.loads((CONTENT/'heat_months.json').read_text())['results'];heat=sorted(heat,key=lambda r:int(r['month']))
    chart('nyc-heat',[str(r['month']) for r in heat],[int(r['total']) for r in heat],'Heat / hot water requests by month',subtitle)
    rare=[r for r in raw if r['complaint_type'] in ['Trapping Pigeon','Squeegee','Radioactive Material']]
    chart('nyc-rare',[r['complaint_type'] for r in rare],[int(r['total']) for r in rare],'The small categories',subtitle,True)
    sources={
      'architecture':('microsoft-fabric-overview--fabric-architecture.png','Microsoft Learn / What is Microsoft Fabric? / CC BY 4.0'),
      'onelake':('microsoft-fabric-overview--onelake-architecture.png','Microsoft Learn / OneLake architecture / CC BY 4.0'),
      'hierarchy':('microsoft-fabric-overview--hierarchy-within-tenant.png','Microsoft Learn / Fabric hierarchy / CC BY 4.0'),
      'directlake':('direct-lake-overview--direct-lake-overview.svg','Microsoft Learn / Direct Lake overview / CC BY 4.0'),
      'framing':('direct-lake-how-it-works--direct-lake-framing.svg','Microsoft Learn / Direct Lake framing / CC BY 4.0'),
      'agent-create':('how-to-create-data-agent--create-data-agent.png','Microsoft Learn / Create a Fabric data agent / CC BY 4.0'),
      'agent-sources':('how-to-create-data-agent--change-datasource.png','Microsoft Learn / Add data sources / CC BY 4.0'),
      'agent-select':('how-to-create-data-agent--data-agent-table-selection-and-search.gif','Microsoft Learn / Select tables / CC BY 4.0'),
      'agent-ask':('how-to-create-data-agent--ask.png','Microsoft Learn / Ask questions / CC BY 4.0'),
      'trial':('fabric-trial--me-control.png','Microsoft Learn / Fabric trial / CC BY 4.0'),
      'trial-home':('fabric-trial--fabric-home-page.png','Microsoft Learn / Fabric trial / CC BY 4.0'),
      'dp700':('dp700-page.png','Microsoft Learn / DP-700 / captured HTML, restyled'),
      'assessment':('assessment-page.png','Microsoft Learn / DP-700 / captured HTML, restyled'),
      'reservation':('fabric-reservations-page.png','Microsoft Learn / Fabric reservations / captured HTML, restyled'),
      'pause':('pause-excerpt.png','Microsoft Learn / Pause and resume / quoted excerpt, CC BY 4.0'),
    }
    shutil.copyfile(ROOT/'content/fabric-watermark/assets/connect-lookup-copy.png',ASSETS/'pipeline.png')
    sources['pipeline']=('pipeline.png','Microsoft Learn / Incremental copy tutorial / CC BY 4.0')
    for name in ['claude-source','claude-connect','claude-question','claude-query']:sources[name]=(name+'.png','Anthropic / announcement, Oct 8 2026 / attributed short quotation')
    for name in ['nyc-total','nyc-categories','nyc-hours','nyc-heat','nyc-rare']:sources[name]=(name+'.png','NYC Open Data / original visualization / saved public API results')
    # Rasterize the original SVGs through Chromium; preserve all original labels.
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=browser.new_page(viewport={'width':1600,'height':1100})
        for name,(file,credit) in list(sources.items()):
            if file.endswith('.svg'):
                svg=(ASSETS/file).read_text();page.set_content('<style>body{margin:0;background:#f1f0ec}svg{width:1600px;height:1000px}</style>'+svg)
                raster=ASSETS/(Path(file).stem+'.png');page.screenshot(path=str(raster));sources[name]=(raster.name,credit)
        browser.close()
    out=CONTENT/'prepared';out.mkdir(exist_ok=True)
    for name,(file,credit) in sources.items():
        raw=Image.open(ASSETS/file).convert('RGB')
        # Crop only real captured pixels. Never replace values or fabricate UI results.
        if name=='dp700':raw=raw.crop((20,185,1180,1090))
        if name=='assessment':raw=raw.crop((20,370,1180,1090))
        for version in [0,1]:
            canvas=Image.new('RGB',(1080,1920),'#060607');draw=ImageDraw.Draw(canvas)
            draw.text((72,92),'REELFACTORY / EDITOR V1',font=face(21,True),fill='#f1f0ec')
            draw.line((72,140,1008,140),fill='#0e5560',width=2)
            fitted=raw.copy();fitted.thumbnail((936,850))
            # Documentation stays readable; color treatment is a restrained teal split.
            gray=ImageOps.grayscale(fitted);toned=ImageOps.colorize(gray,'#0e3035','#f1f0ec')
            treated=Image.blend(fitted,toned,.22 if version==0 else .38)
            if version and name not in ['claude-source','claude-connect','claude-question','claude-query','pause','reservation','dp700','assessment','trial'] and not name.startswith('nyc'):
                # Detail crop enlarges the evidence while retaining the original pixels.
                box=(int(treated.width*.08),int(treated.height*.06),int(treated.width*.92),int(treated.height*.94))
                treated=treated.crop(box);treated.thumbnail((936,850))
                scale=min(936/treated.width,850/treated.height);treated=treated.resize((round(treated.width*scale),round(treated.height*scale)))
            x=(1080-treated.width)//2;y=410+(850-treated.height)//2
            canvas.paste(treated,(x,y));draw.rectangle((x-2,y-2,x+treated.width+2,y+treated.height+2),outline='#b9b8b4',width=2)
            for j,line in enumerate(lines(draw,credit,936,face(20))):draw.text((72,1665+j*30),line,font=face(20),fill='#b9b8b4')
            label='PUBLIC DATA QUERY / ORIGINAL CHART' if name.startswith('nyc') else 'SOURCE EXCERPT / NOT A PRODUCT EXECUTION' if name.startswith('claude') else 'DOCUMENTATION REFERENCE / NOT A LIVE DEMO'
            draw.text((72,1790),label,font=face(18),fill='#b9b8b4')
            canvas.save(out/f'{name}-{version}.jpg',quality=95)
    (CONTENT/'asset-map.json').write_text(json.dumps({k:{'file':v[0],'credit':v[1],'variants':[f'{k}-0.jpg',f'{k}-1.jpg']} for k,v in sources.items()},indent=2))
    shutil.copyfile('/workspace/attachments/6fa212e9-96c0-4dcf-999e-b6645cee15a8/Pasted text.txt',CONTENT/'ORIGINAL-SCRIPTS.md')
    print('Prepared',len(sources),'sources and',len(sources)*2,'portrait variants')

if __name__=='__main__':main()
