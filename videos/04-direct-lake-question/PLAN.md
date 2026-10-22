# The Direct Lake interview question — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/7667345672042974481. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
Quiz is an original adaptation; the reference demonstrates SQL masking. Replaced blanket security/fallback claims with documented Direct Lake distinctions.

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
| 0.00–5.32 | A Fabric interview question. Your sales data is stored as Delta tables in OneLake. | directlake | tile |
| 5.32–10.69 | You want import style query performance without copying the entire dataset into the model. | directlake | focus |
| 10.69–14.69 | Which storage mode fits? Import? Direct Query? Or Direct Lake? | directlake | quiz |
| 14.69–16.45 | Pause here and choose your answer. | directlake | focus |
| 16.45–21.41 | Direct Lake. It loads the columns needed for queries from Delta tables in OneLake. | directlake | focus |
| 21.41–26.05 | A refresh updates metadata. It does not import the entire dataset again. | framing | sequence |
| 26.05–31.24 | Here is the detail to check. Direct Lake on SQL can fall back to Direct Query. | directlake | focus |
| 31.24–36.20 | Direct Lake on OneLake does not use that fallback. Their security behavior differs too. | framing | sequence |
| 36.20–41.95 | Read the comparison before choosing a mode. The correct design depends on the source and permissions. | directlake | focus |

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
| directlake | Microsoft Learn / Direct Lake overview / CC BY 4.0 | direct-lake-overview--direct-lake-overview.png |
| framing | Microsoft Learn / Direct Lake framing / CC BY 4.0 | direct-lake-how-it-works--direct-lake-framing.png |

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only 04-direct-lake-question`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/04-direct-lake-question -q draft -f 30 -o videos/04-direct-lake-question/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
