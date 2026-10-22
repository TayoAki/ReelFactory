# Three free Fabric learning resources — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/7660163521614777620. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
Removed promise of identical exam wording/difficulty and stale trial exclusions. Trial availability remains subject to Microsoft's eligibility rules.

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
| 0.00–5.05 | Three free Microsoft resources for learning Fabric. Save these official pages. | dp700 | tile |
| 5.05–10.15 | One. A Fabric trial gives eligible users sixty days to explore the platform. | trial | focus |
| 10.15–16.48 | Use it to practice lakehouses, ingestion and reporting. Check the current trial limits before you start. | trial-home | sequence |
| 16.48–21.95 | Two. The DP seven hundred practice assessment is available free on Microsoft Learn. | assessment | focus |
| 21.95–27.25 | Use the feedback to find gaps. It is a study tool, not a guarantee of an exam result. | assessment | sequence |
| 27.25–32.30 | Three. The exam sandbox lets you explore the exam interface before booking your test. | assessment | focus |
| 32.30–38.92 | Start with the certification page and follow its official links. Keep the resources together for your next study session. | dp700 | focus |

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
| dp700 | Microsoft Learn / DP-700 / captured HTML, restyled | dp700-page.png |
| trial | Microsoft Learn / Fabric trial / CC BY 4.0 | fabric-trial--me-control.png |
| trial-home | Microsoft Learn / Fabric trial / CC BY 4.0 | fabric-trial--fabric-home-page.png |
| assessment | Microsoft Learn / DP-700 / captured HTML, restyled | assessment-page.png |

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only 06-free-fabric-resources`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/06-free-fabric-resources -q draft -f 30 -o videos/06-free-fabric-resources/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
