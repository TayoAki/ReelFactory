# The Fabric workflow beyond charts — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/7635415703377448212. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
Removed predictions about all analysts, one-bill oversimplification, hiring guarantees and universal job-posting claims.

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
| 0.00–4.32 | If you already build Power BI reports, learn what happens before the chart. | architecture | tile |
| 4.32–10.18 | Fabric brings ingestion, engineering, storage, analytics and reporting into one platform. | architecture | sequence |
| 10.18–15.29 | Start with a lakehouse. Understand where the data lands and how its tables are organized. | hierarchy | focus |
| 15.29–20.97 | Then trace an ingestion pipeline. What arrives, what changes, and what happens when a run fails? | pipeline | sequence |
| 20.97–25.27 | Keep SQL and Power BI. Add the shared data layer underneath them. | onelake | focus |
| 25.27–30.51 | Fabric data agents can turn questions into queries against supported data sources. | agent-ask | focus |
| 30.51–35.00 | That makes a clean model and clear permissions useful beyond the report itself. | agent-sources | sequence |
| 35.00–40.09 | Build one small workflow from source to report. Explain each step and show its output. | architecture | focus |

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
| architecture | Microsoft Learn / What is Microsoft Fabric? / CC BY 4.0 | microsoft-fabric-overview--fabric-architecture.png |
| hierarchy | Microsoft Learn / Fabric hierarchy / CC BY 4.0 | microsoft-fabric-overview--hierarchy-within-tenant.png |
| pipeline | Microsoft Learn / Incremental copy tutorial / CC BY 4.0 | pipeline.png |
| onelake | Microsoft Learn / OneLake architecture / CC BY 4.0 | microsoft-fabric-overview--onelake-architecture.png |
| agent-ask | Microsoft Learn / Ask questions / CC BY 4.0 | how-to-create-data-agent--ask.png |
| agent-sources | Microsoft Learn / Add data sources / CC BY 4.0 | how-to-create-data-agent--change-datasource.png |

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only 03-analyst-fabric-workflow`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/03-analyst-fabric-workflow -q draft -f 30 -o videos/03-analyst-fabric-workflow/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
