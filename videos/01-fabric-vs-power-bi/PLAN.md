# Fabric vs Power BI — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/7638031376217853205. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
Removed unsupported most-searched hook and no-refresh absolute. Direct Lake refreshes metadata; this isn't a live Fabric demo.

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
| 0.00–5.09 | Microsoft Fabric versus Power BI? Power BI is already inside Fabric. | architecture | tile |
| 5.09–10.07 | Power BI handles reports. Fabric covers the workflow around those reports. | architecture | focus |
| 10.07–14.24 | Getting data in. Storing it. Transforming it. Then serving the result. | onelake | sequence |
| 14.24–17.86 | OneLake gives those workloads a shared, logical data lake. | onelake | focus |
| 17.86–22.71 | Direct Lake can read Delta tables without importing an entire copy into the model. | directlake | focus |
| 22.71–28.59 | A Direct Lake refresh still exists. It updates metadata, rather than copying the whole dataset. | framing | sequence |
| 28.59–34.17 | Already know Power BI? Keep it. Add SQL, a lakehouse, and an ingestion pipeline. | architecture | sequence |
| 34.17–38.36 | Start with one end to end workflow. Follow the data into the report. | onelake | focus |

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
| architecture | Microsoft Learn / What is Microsoft Fabric? / CC BY 4.0 | microsoft-fabric-overview--fabric-architecture.png |
| onelake | Microsoft Learn / OneLake architecture / CC BY 4.0 | microsoft-fabric-overview--onelake-architecture.png |
| directlake | Microsoft Learn / Direct Lake overview / CC BY 4.0 | direct-lake-overview--direct-lake-overview.png |
| framing | Microsoft Learn / Direct Lake framing / CC BY 4.0 | direct-lake-how-it-works--direct-lake-framing.png |

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only 01-fabric-vs-power-bi`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/01-fabric-vs-power-bi -q draft -f 30 -o videos/01-fabric-vs-power-bi/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
