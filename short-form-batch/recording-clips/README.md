# Fabric recording: 57 rendered short-form drafts

Five original AAC uploads total 62m30s. These 57 distinct continuous excerpts retain the original voices; no TTS, invented spoken hooks, background music or social posting. Portraits are static fictional placeholders, not recorded speakers.

Open [the gallery](index.html), [catalog](clip-catalog.csv), [timestamped clip example bank](example-bank.json), [103 full-recording example-cue passages](full-recording-example-cues.json), and [export checks](export-validation.json). Exports are 1080×1920, 30fps H.264/AAC with bottom word-highlight captions. Each clip has three storyboard states, editable reconstruction source, timing metadata and caption sidecars. Eight generated masters establish the Fabric visual direction; precise symbols/text are corrected in editable layers.

## Review limits

ASR captions were decoded twice over the whole recording and refined with actual audio context before and after each cut, without a technical-name prompt that could contaminate silence. Technical spellings were normalized, but this is not a certified verbatim transcript. Window joins and source claim flags are recorded in manifest.json. Hypothetical examples are illustrations, not tenant results. Product preview/authentication/migration/billing statements are dated speaker claims, not independently certified current behavior. Clips are review drafts; codec validation does not establish visual approval. Very short definition excerpts remain micro-clips rather than being padded.

## Rebuild

Run from repo root: `python short-form-batch/tools/build_recording_clips.py --build`, then `--render`, then `python short-form-batch/tools/package_recording_clips.py`. Serve repo on localhost:8765 for browser assets. Requires Chromium, Playwright, Pillow, FFmpeg/libass and the bundled fonts. Run export_editable_scenes.py to save per-clip HTML/SVG scenes with original-audio review controls; these are editable reconstructions, not native HyperFrames project exports. Recreate combined-working.m4a with tools/join_audio.py. Speech refinement additionally uses faster-whisper base.en, NumPy and 16kHz mono WAV working inputs. Render cache is disposable; final storyboard images, masters, scripts and media are versioned.

## Selection and visual choices

Each selected range has source part mappings, source-global in/out and its actual ASR quote. Compare meaning with contrast panels; show source ownership with references; distinguish types, instances and relationships; show review gates or separate execution; verify evidence instead of inventing charts. The recall is a hypothetical named path. No borrowed Databricks colors, unlicensed demo footage or fabricated UI. An authentic tenant recording is the stronger choice when proving a product interaction.
