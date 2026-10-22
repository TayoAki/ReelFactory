# Use the original-source graphic library

Project directory: `reference-library/`. It contains original-video evidence, not screenshots from the rejected recreation. `library.json` is authoritative; `README.md` and `entries/*.md` render the source images and narration in GitHub; `index.html` is searchable in the running project.

## What to retrieve

1. Analyze the target narration's teaching action: definition, input/mechanism/output, wrong source, ambiguous metric, stale context, governed hierarchy, ranking, comparison, delegation, rollout, evidence or another relationship.
2. Read the candidate template's `choose_when` and `choose_something_else_when`. Compare its paired source quote and screenshots. A keyword such as “agent” does not establish a delegation relationship.
3. Read the entry's `source_specific_observation`. Distinguish settled reading direction from actual reveal order. The original web/model/results diagram introduces the model before its web input; the initial generated web-first board was an inference and was corrected from source evidence.
4. Inspect the original primary style anchor and useful earlier/build frames. Use the full-frame link when a crop or source camera move hides context. A before/during/after window is sampled evidence, not exact original keyframes or precise speech alignment.
5. Create an image-reference packet using `select.py`. Pass its `imagegen_request.referenced_image_paths` into image generation along with the verified target narration. Do not supply only textual style instructions when original visual evidence is available.

```bash
python reference-library/select.py \
  --template input-output \
  --instance constrained-web-flow \
  --mode reconstruction \
  --out reference-library/packets/constrained-web-flow.json
```

For a new subject, use `--mode adaptation`, `--narration` and `--slots` containing verified target roles. Source-role bindings are supplied only for reconstruction; adaptation must not silently inherit source product claims or benchmark values. Unfilled sentence slots remain explicit. The selector retrieves a chosen teaching family; it is not a trained automatic classifier or factual verifier.

## Evidence and interpretation

Original full frames and graphic-region crops are extracted from the uploaded 640×360 video. They are not generated or enlarged. The raw rolling transcript remains quoted separately, including overlapping times and transcription errors. Sentence scaffolds and their source-role bindings are editorial paraphrases. Selection/misuse rules and reusable motion grammar are interpretations; source-specific visual observations take precedence for reconstruction.

The library indexes 58 curated examples and 25 teaching families, with 280 selected state samples and windows around the earlier 206 estimated anchors. This is broad whole-video coverage, not proof that every micro-transition has been annotated. Chapter cards and authentic UI evidence are separate categories, not all counted as explanatory motion graphics. Some source clips intentionally crop objects during camera focus; inspect the full evidence frame.

## Generate and review

Generate one candidate settled master using the selected original references. Derive three or more coherent storyboard states from that master, matching reveal order to narration. Record the selected library entry, frame times, actual reference images and reasons in the storyboard. Review the images, reconstruct editable layers, compare the still, then animate and compare again. If no library relationship fits, record a coverage gap and design another graphic; do not force the reference.

The rejected renderer is useful as a failure example. It is not an approved style source, motion source or reference image for future art direction.
