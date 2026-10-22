# A year of New York's 311 requests — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/7683919006683680014. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
Recomputed results through NYC's public API. Removed claim of a Fabric execution; chart is original and backed by saved query responses. Date range is Oct 1 2025 through Sep 30 2026.

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
| 0.00–4.85 | I queried a year of New York's three one one requests. Almost four million records. | nyc-total | tile |
| 4.85–10.35 | The window is October first, twenty twenty five, through September thirtieth, twenty twenty six. | nyc-total | focus |
| 10.35–16.46 | The biggest category is illegal parking. Six hundred eleven thousand, two hundred eighty two requests. | nyc-categories | focus |
| 16.46–21.18 | Residential noise is next, with more than four hundred thirty two thousand requests. | nyc-categories | sequence |
| 21.18–26.49 | Those residential noise requests peak in the ten p m hour. Sunday is the busiest day. | nyc-hours | focus |
| 26.49–31.70 | Heat and hot water requests show a different pattern. January is far busier than August. | nyc-heat | sequence |
| 31.70–36.17 | At the other end of the list, exactly one request is filed under trapping pigeon. | nyc-rare | focus |
| 36.17–42.84 | These are request counts, not unique incidents. The queries and results are saved so you can reproduce the charts. | nyc-categories | focus |

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
| nyc-total | NYC Open Data / original visualization / saved public API results | nyc-total.png |
| nyc-categories | NYC Open Data / original visualization / saved public API results | nyc-categories.png |
| nyc-hours | NYC Open Data / original visualization / saved public API results | nyc-hours.png |
| nyc-heat | NYC Open Data / original visualization / saved public API results | nyc-heat.png |
| nyc-rare | NYC Open Data / original visualization / saved public API results | nyc-rare.png |

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only 08-nyc-311-analysis`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/08-nyc-311-analysis -q draft -f 30 -o videos/08-nyc-311-analysis/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
