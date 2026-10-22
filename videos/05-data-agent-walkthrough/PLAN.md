# Ask Fabric data questions in plain English — Editor V1 review draft

Uses the actual NextPhase V1 Comp, still, tile_reveal, keyword, captions, finish and sound devices, adapted from 16:9 to 9:16. Native HyperFrames HTML, editable scene JSON and cue sheet are included.

Reference: https://www.tiktok.com/@_/video/7636938088559758593. See ../../research/reference-analysis.json for observed scene mechanics and the sampled-review limitation.

## Editorial changes
Removed unsupported fixed cost, language and trial absolutes. Uses official documentation captures; no fabricated execution or answer.

Original supplied scripts are retained in ../../content/creator-recreations/ORIGINAL-SCRIPTS.md. These are concise, source-checked adaptations rather than verbatim readings.

## Beat plan
| In–out seconds | Narration | Evidence asset | Planned device |
|---|---|---|---|
| 0.00–4.73 | Your Power BI semantic model can also be a source for a Fabric data agent. | agent-create | tile |
| 4.73–10.41 | Microsoft's documented setup starts by creating the agent and choosing its data sources. | agent-create | focus |
| 10.41–13.60 | You can add up to five supported sources in one agent. | agent-sources | sequence |
| 13.60–18.07 | Select the tables it should use. Give columns and tables descriptive names. | agent-select | focus |
| 18.07–24.25 | Then ask a concrete question. For example, what were total sales in California in twenty twenty three? | agent-ask | focus |
| 24.25–29.31 | The agent can generate SQL, DAX or KQL, depending on the data source. | agent-ask | sequence |
| 29.31–35.13 | It uses your data access permissions. Clear descriptions and a clean model help it choose the right query. | agent-sources | focus |
| 35.13–41.51 | Before a real demo, check capacity prerequisites, permissions, and the generated query against a known answer. | agent-ask | focus |

## Source and rights plan
| Asset | Attribution / use | Local original |
|---|---|---|
| agent-create | Microsoft Learn / Create a Fabric data agent / CC BY 4.0 | how-to-create-data-agent--create-data-agent.png |
| agent-sources | Microsoft Learn / Add data sources / CC BY 4.0 | how-to-create-data-agent--change-datasource.png |
| agent-select | Microsoft Learn / Select tables / CC BY 4.0 | how-to-create-data-agent--data-agent-table-selection-and-search.gif |
| agent-ask | Microsoft Learn / Ask questions / CC BY 4.0 | how-to-create-data-agent--ask.png |

Microsoft repository images are CC BY 4.0; cropped, resized and lightly color-treated. Microsoft Learn HTML is captured with local readability styling. Anthropic material is limited to short, attributed quotations rendered as original source cards, with no copied creator frames or vendor film. NYC charts are original and use saved public-data responses. No creator face, voice, music or footage is reused in the production. Reference files remain research only. Font licenses ship beside the fonts; sound effects are the kit's synthesized files. No music bed was supplied or used.

## Review limits
Local Kokoro synthetic voice. Whisper word alignment is automatic; interpolated words are flagged in work/timeline.json. This does not claim manually verified frame-exact captions. Source images are documentation references, not a recorded Fabric or Claude product execution. No user recording was supplied, so no presenter or matte is fabricated. The source's continuous live-demo motion cannot be reproduced faithfully from still documentation alone.

## Rebuild
From ReelFactory, run `python src/build_recreations.py --only 05-data-agent-walkthrough`. Then source `vendor/editor-v1/scripts/env.sh` and run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf render videos/05-data-agent-walkthrough -q draft -f 30 -o videos/05-data-agent-walkthrough/out/render.mp4`. `src/render_recreations.py` renders and mixes the synthetic narration and device cues into out/final.mp4. No publishing is performed.
