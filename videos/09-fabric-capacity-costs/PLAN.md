# Before you pause Fabric capacity — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/7671004519790054678. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
Kept reservation and smoothed-usage caveats; clarified that pausing does not stop the reservation charge. Original reference is a cumulative list, not a visual myth/reveal.

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
| 0.00–5.17 | Pausing Fabric capacity does not stop the charge for a reservation you already bought. | reservation | tile |
| 5.17–10.41 | A reservation discount applies hour by hour. Unused hours do not carry forward. | reservation | focus |
| 10.41–15.14 | So check how your reservation benefit is being used before you pause capacity. | reservation | sequence |
| 15.14–22.42 | There is a second check. Remaining cumulative overages and smoothed operations are added to your Azure bill when you pause. | pause | focus |
| 22.42–26.21 | Use the Capacity Metrics app to inspect the capacity's usage. | pause | sequence |
| 26.21–33.86 | Before pausing, check the reservation and pending usage together. A green pause button does not erase an existing commitment. | reservation | focus |

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
| reservation | Microsoft Learn / Fabric reservations / captured HTML, restyled | fabric-reservations-page.png |
| pause | Microsoft Learn / Pause and resume / quoted excerpt, CC BY 4.0 | pause-excerpt.png |

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only 09-fabric-capacity-costs`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/09-fabric-capacity-costs -q draft -f 30 -o videos/09-fabric-capacity-costs/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
