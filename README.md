# ReelFactory — first production prototype

A reproducible 40-second silent vertical technical explainer, based on the uploaded Fabric content-gap audit's W03 pilot. No avatar, speech, paid API, credentials or Fabric workspace is required.

## Run
Requires Python 3 with Pillow and FFmpeg with libx264. Tested with the tools already provided in this workspace.

```sh
cd /workspace/ReelFactory
python src/lab.py
python src/render.py
python src/verify.py
```

`render.py` runs the evidence fixture before rendering. It writes eight review frames, a contact sheet, and a 1080×1920 / 24fps MP4. Use `--stills-only` for layout review. Inputs and timings live in `content/fabric-watermark/scenes.json`.

Open `index.html` using a local static server to review the video, storyboard, script and evidence together. The page uses no external scripts or assets.

## Scope
This is a working first production, not a general autonomous research/editor product. Content Machine's evidence-led script structure and NextPhase's editorial planning informed the workflow. For this original pilot, native NextPhase/HyperFrames integration, arbitrary topic ingestion, retrieved stock footage, voiceover, publishing and Fabric execution were not implemented. The nine-video V1 workflow below now adds native V1 devices and local draft narration. See PLAN.md for provenance and SCRIPT.md for claim boundaries.

The rendered technical B-roll illustrates actual local SQLite fixture results. It does not impersonate the Microsoft Fabric UI or claim to demonstrate an executed Fabric pipeline.

## Official documentation revision
`python src/render.py --version v2` renders the 50-second revision with original Microsoft documentation images and attribution. Source inventory: `content/fabric-watermark/official-assets.json`. Creator video review status: `research/CREATOR-REVIEW.md`. `src/inspect_video.py` extracts timestamped contact sheets from locally available reference videos; extraction alone is not visual analysis.


## Nine-video Editor V1 recreation pack

Open `studio.html` through a local HTTP server to review all nine drafts beside their supplied references. The actual uploaded NextPhase Editor V1 kit is in `vendor/editor-v1`; each project in `videos/` contains native HyperFrames HTML, its source assets, revised narration, automatic word timing, device-generated sound cues, and `PLAN.md`. Rendered MP4s are in each project's `out/final.mp4`.

The original scripts are preserved in `content/creator-recreations/ORIGINAL-SCRIPTS.md`; production changes are recorded in `projects.json` and the per-video plans. These are source-based, faceless review drafts with local Kokoro synthetic speech. No presenter recording or licensed music was supplied. The drafts adapt the observed scene mechanisms rather than reproducing a creator's face, voice or footage.

11 TikTok references were downloaded through the environment-bound ScrapeCreators credential and visually sampled. Seven available subtitle tracks were saved. Full-file cut detection supplements 29 visual samples per reference; this is not exhaustive human frame-by-frame review. `research/SCENE-BY-SCENE.md` records the observed scenes, mismatches with the supplied notes, and two YouTube footage blockers.

NYC charts use retained public API query results for Oct 1 2025 through Sep 30 2026. The NYC narration describes that query, not an unperformed Fabric execution. Microsoft imagery is attributed; Anthropic material is limited to short attributed source quotations. No creator footage is included in the production exports.

To serve locally: `python -m http.server 8765 --directory /workspace/ReelFactory`. Open `http://127.0.0.1:8765/studio.html`. To open one native project in the V1/HyperFrames editor: source `vendor/editor-v1/scripts/env.sh`, then run `HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium hf preview videos/01-fabric-vs-power-bi`.

Reproduction scripts: `src/acquire_references.py`, `src/reference_sheets.py`, `src/prepare_recreation_assets.py`, `src/voice_recreations.py`, `src/build_recreations.py`, `src/render_recreations.py`, `src/verify_recreation_audio.py`. Local model and interpreter paths are command-line defaults for this workspace; install the free Kokoro/Whisper dependencies and supply model paths when running on another machine. No API key is embedded in a project or render. Native renders use HyperFrames 0.8.181 and Chromium.


## Parker Prompts study and revised pilot

`pilot.html` compares the revised result-first NYC data story with the earlier source-card draft. `research/parker-prompts/STUDY.md` distinguishes the one sampled visual reference from three transcript-only references and records the actual timestamped lessons. `VIDEO-STANDARD.md` turns those findings into reusable production rules. The revised native V1 project is `videos/10-nyc-parker-pilot/`, built by `src/build_parker_pilot.py` from the retained real data and `content/parker-pilot/projects.json`. The original nine drafts remain intact. No Higgsfield generation or connection is claimed.


Microsoft Fabric revision: `videos/11-fabric-data-agent/` is the closer Parker-informed widescreen tutorial. Its portable review page is `fabric-review.html` (video embedded, no localhost dependency). Rebuild with `src/build_fabric_parker.py`; voice/render project file: `content/fabric-parker/projects.json`.


Fine-edit revision: `videos/12-fabric-motion-refined/` preserves the Fabric script and adds three source GIFs, clean app-to-detail cuts, contained screens, timed annotations, linked cards and frame-safe captions. Build: `src/build_fabric_motion.py`; project: `content/fabric-parker/motion-project.json`. The portable main review page remains `fabric-review.html`, updated to this revision.


YouTube demo-analysis cut: `videos/13-fabric-youtube-case-study/`. It examines Guy in a Cube's real May 2025 demonstration with original narration and source credits. `research/fabric-youtube/CONTENT-BRIEF.md` contains the three-channel shortlist, timestamped passages and reuse-status flags. This cut is local editorial review; footage reuse rights remain unconfirmed. Portable review: `fabric-youtube-review.html`.


## Complete Databricks reference study

The uploaded reference runs 34:28. The whole-video study includes 44 continuous sections, 206 estimated visual anchors, editable diagrams, static fictional presenter placeholders and source-clock comparisons.

- [Section review](full-video/review.html)
- [Full original/reconstruction comparison](full-video/full-comparison.mp4)
- [Full reconstruction](full-video/full-reconstruction.mp4)
- [Visual-anchor atlas](full-video/event-atlas.html)
- [Teaching and motion recipes](full-video/RECIPES.md)
- [Reusable technical-video skill](.agents/skills/technical-video-explainer/SKILL.md)

Source UI and narration are retained evidence. Diagram geometry and timing are approximate; complete timeline coverage does not certify exact micro-transition fidelity. See [study details](full-video/README.md).
