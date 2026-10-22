# Complete reference-video study

The source is 34:28, not 30:00. Forty-four continuous timeline sections cover the uploaded five parts. The reconstruction uses static fictional presenters, source narration and authentic source UI. Native explanatory diagrams are rebuilt at 1920×1080, 30 fps. The previously refined product-family passage is reused.

Open `review.html` for section-by-section original/reconstruction samples, motion excerpts, narration and selection reasoning. Play `full-comparison.mp4` for the complete synchronized comparison, or `full-reconstruction.mp4` for the complete reconstruction. `transcript-captions.srt` is an optional caption file derived from rolling transcript segments; timing is approximate.

`recipes.json` records the teaching relationship, choice, alternative, persistent objects, motion roles and misuse risk for each section. `event-atlas.html` provides 206 matched source/reconstruction images. `reconstruction-state-map.json` records added, removed and emphasized text in 164 native display-list samples, explicitly distinct from source annotations. `event-map.json` links 206 estimated visual anchors to nearby transcript segments and prior source-frame evidence. These are not exact spoken triggers or original animation keyframes. `coverage.json` separates rendered coverage from pending fidelity review.

The live UI is retained evidence, not newly generated or newly executed product behavior. Geometry, icons, some content compression and animation timing differ from the source. The full source was scanned at 1fps, with prior dense samples for selected transitions; this does not certify every micro-transition. Captions are not globally rebuilt word by word. No trained model or arbitrary-transcript compiler is claimed.

## Editable implementation

- `graphics.py`: native vector/display-list components, diagram geometry and frame-derived motion.
- `render.py`: section render and authentic UI compositing; needs Pillow and FFmpeg.
- `plan.json`: source-clock timeline, kinds and estimated event anchors.
- `build_review.py`: synchronized full comparison, section comparisons and portable HTML review.
- `build_recipes.py`, `build_event_map.py`: teaching taxonomy and transcript links.
- `assets/`: consistent Fluent generic symbols (MIT), fonts and presenter/UI evidence assets.

For a new technical script, choose a visual because its relationship matches the teaching task. Verify the product claims, adapt the content, storyboard for human review, then time it to the new narration. Historical Databricks benchmark values and product behavior must not be transferred into Microsoft Fabric without independent evidence.
