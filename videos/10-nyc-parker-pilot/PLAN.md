# A result-first NYC data story — Parker-informed pilot

The complete channel study and evidence limitations are in ../../research/parker-prompts/STUDY.md. This pilot carries its own data, identity and composition through meaningful transformations, replacing the previous screenshot-flip cadence. The original nine drafts are preserved.

## Sources and rights
All quantitative graphics are original SVG/HTML charts generated from the retained NYC Open Data responses in ../../content/creator-recreations/{nyc-results,noise_hours,noise_days,heat_months}.json. Public API query parameters and actual results are retained there. The date range is October 1, 2025 through September 30, 2026. There are 3,963,898 requests, including 611,282 illegal-parking requests; the residential-noise hourly peak is 22:00–22:59 with 42,705 requests, Sunday has 87,909, and heat/hot-water requests are 79,928 in January versus 3,682 in August (21.7×). Exactly one request is categorized Trapping Pigeon. These are request counts, not unique incident counts. No Fabric execution is claimed.

Parker's video is research material only. None of the creator's face, voice, films, footage, graphics, private prompts or music is reused. Fonts and synthesized effect sounds are from the licensed V1 kit. Narration is a local Kokoro synthetic draft voice. No music bed or external paid generation was used.

## Edit decisions
1. Reveal actual results in the opening scene.
2. Carry the same categories, colors and geometry from overview to the parking result.
3. Show the retained query window as the evidence interlude.
4. Change one data state at a time: category, hour grouping, weekday proof, then monthly grouping.
5. Pair January/August before revealing the rare pigeon category as a contrasting scale.
6. Finish on the result and reproducible query rather than a generic title card.

Every semantic shot has a purpose in work/shots.json and narration timings in work/timeline.json. Caption timing is automatic and not claimed to be manually verified within one frame. The visible charts are explanatory graphics, not a fabricated recording of a vendor application. All figures use the retained query results rather than invented illustrative values.

## Build
Run python src/build_parker_pilot.py from ReelFactory after creating the local voice/timeline with src/voice_recreations.py --project-file content/parker-pilot/projects.json. Render this native project with the vendored V1/HyperFrames workflow. No publication is performed.
