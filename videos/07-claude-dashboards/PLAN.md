# Claude dashboards: connect, ask, inspect — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/7695498034079108359. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
Verified first-party feature text via Firecrawl. Original source cards replace unlicensed creator footage. Not a recorded product execution; omitted categorical Power BI export exclusion.

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
| 0.00–4.34 | Claude Dashboards can connect to Databricks and build a dashboard from a question. | claude-source | tile |
| 4.34–9.51 | Anthropic announced it on October eighth. The announcement describes a beta on paid plans. | claude-source | focus |
| 9.51–15.03 | Step one. Connect a supported data platform, such as Databricks, Snowflake or Big Query. | claude-connect | sequence |
| 15.03–21.21 | Step two. Ask a specific question in plain English, like this week's signups compared with last month's. | claude-question | focus |
| 21.21–27.32 | Claude retrieves the data and builds the dashboard. This is a source based walkthrough of the announced feature. | claude-source | focus |
| 27.32–32.49 | Step three. Inspect the answer. The announcement says you can click a number to see its query. | claude-query | sequence |
| 32.49–35.89 | Each chart also shows when its data was last refreshed. | claude-query | focus |
| 35.89–42.41 | Enterprise admins must enable the feature. Check access and verify the query before sharing the result. | claude-source | focus |

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
| claude-source | Anthropic / announcement, Oct 8 2026 / attributed short quotation | claude-source.png |
| claude-connect | Anthropic / announcement, Oct 8 2026 / attributed short quotation | claude-connect.png |
| claude-question | Anthropic / announcement, Oct 8 2026 / attributed short quotation | claude-question.png |
| claude-query | Anthropic / announcement, Oct 8 2026 / attributed short quotation | claude-query.png |

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only 07-claude-dashboards`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/07-claude-dashboards -q draft -f 30 -o videos/07-claude-dashboards/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
