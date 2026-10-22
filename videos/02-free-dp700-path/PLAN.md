# The free DP-700 preparation path — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/7659620910105677076. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
Replaced expired voucher promotion and unverified historical frequency with currently documented preparation resources. No promise of future vouchers.

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
| 0.00–5.90 | Want to prepare for DP seven hundred without buying a course? Start with Microsoft's own resources. | dp700 | tile |
| 5.90–10.84 | First, open the Fabric Data Engineer certification page on Microsoft Learn. | dp700 | focus |
| 10.84–14.03 | Use the study guide to see the skills the exam measures. | dp700 | sequence |
| 14.03–18.11 | Then work through the free, self paced learning material linked from that page. | dp700 | focus |
| 18.11–22.39 | Use the free practice assessment to find the areas you still need to study. | assessment | focus |
| 22.39–26.79 | Try the exam sandbox so the interface is familiar before exam day. | assessment | sequence |
| 26.79–32.35 | Preparation is free. An exam booking is a separate purchase unless you have a valid offer. | dp700 | focus |
| 32.35–38.70 | Save the official certification page. Check any voucher's eligibility and deadline before relying on it. | dp700 | focus |

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
| dp700 | Microsoft Learn / DP-700 / captured HTML, restyled | dp700-page.png |
| assessment | Microsoft Learn / DP-700 / captured HTML, restyled | assessment-page.png |

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only 02-free-dp700-path`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/02-free-dp700-path -q draft -f 30 -o videos/02-free-dp700-path/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
