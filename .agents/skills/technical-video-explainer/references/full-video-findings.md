# Whole-video extension: findings and limits

The supplied five-part source runs 34:28. A whole-source 1fps scan expanded the earlier 27 sampled sequences into 44 continuous intervals. The interval manifest includes presenter holds, chapter cards and authentic UI demonstrations so coverage can be audited without implying that every interval is a new motion graphic.

Observed in the source scan: the benchmark chart returns after a host question; the skills explanation alternates between UI evidence and a governance diagram; a short three-column summary precedes the rollout rail; chapter cards and host callouts sit between the previously indexed sequences. These additions prevent a catalog of isolated examples from being mistaken for a complete timeline.

Editorial interpretation: the graphics teach a small number of relationships repeatedly—convergence, cause and repair, hierarchy, peer comparison, evidence, delegation, rollout progress and fixed-list emphasis. Select by that relationship and by what the viewer must understand next. A literal keyword match is insufficient.

Observed in generated keyframe review: implicit SVG fills made some generic icons black; the short-card header/body baselines overlapped; UI evidence crops could overwrite the left-side title; a stale caption remained on a reused portrait; stretching two wide portraits into narrow closing tiles distorted faces. The revision explicitly colors the icon paths, separates header/body baselines, limits title width, removes the stale portrait caption, uses a centered host crop and crops closing tiles with preserved proportions.

Proposed reusable checks: inspect active and inactive text at the intended player size, keep diagram cameras independent of the stage, test small cards with the longest real labels, verify each composited UI viewport against the live footage, and distinguish retained evidence from regenerated explanations. Do not use arbitrary global pixel similarity to grade a reconstruction with intentional placeholder faces.

Measured readability check: inactive best-practice body text at 55% blend has approximately 4.89:1 contrast against the dark panel. This checks that specific text/background pair, not every element in the video.

Measured implementation facts: the timeline has 44 continuous intervals and 206 estimated event anchors. Output is 1920×1080 at 30fps, with original narration and source UI retained where declared. Optional captions derive from overlapping transcript segments and are approximate. Media integrity and storyboard validation results belong in the project's `full-video/verification.json` and `storyboard-validation.json`.

Limits: most source events are estimated from 1fps sampling, with denser earlier evidence for selected transitions. Native diagram geometry, silhouettes, content compression, camera curves and event timing are approximations. A rendered complete timeline does not certify every micro-transition or human fidelity approval. Source-reported product claims and benchmarks remain source claims. They must be researched again before adaptation to Microsoft Fabric or another product.
