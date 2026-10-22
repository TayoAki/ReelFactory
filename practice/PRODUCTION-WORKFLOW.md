# Transcript → approved storyboard → graphics → motion

User-directed workflow, adopted 2026-10-22. The latest user explicitly authorized generating every scene of the current storyboard for comparison; this overrides the pending production stop for that scope, without asserting final fidelity approval. Applies to subsequent new or revised production. Existing renders are retained as prior experiments; they do not constitute approval of a new storyboard.

## Stage 1 — understand and storyboard (HITL 1)

Read the full supplied transcript before dividing it into teaching beats. Research unfamiliar product concepts against primary sources. Identify the audience, prerequisite knowledge, explanatory arc, ambiguous language and claims that need verification. Distinguish the speaker's claim, independent evidence and our interpretation.

Declare the mode: reference reconstruction, adaptation, or an original explanation. For the present Databricks practice, default to reference reconstruction. Alternative visual ideas are recommendations for review, not silent replacements for source graphics.

For every beat supply:

- Exact transcript excerpt and approximate time window.
- Intended understanding: what the viewer should know after this beat.
- Concrete visual proposal: diagram, interface example, image, product screenshot, comparison, presenter hold, or no additional graphic.
- Text, symbols, images and source assets required; what is official, illustrated or a placeholder.
- Rough composition and hierarchy; what persists from the previous beat.
- Start → change → settled state, speech trigger and hold; include connector meanings.
- Reason for the choice, a credible alternative, and why the proposal is preferable for the declared mode.
- Clarity check: does the image teach the sentence, imply unsupported functionality, confuse a metaphor with architecture, overload the available time, or compete with narration?
- Source citations, uncertainties, any proposed transcript rewrite, and approval status.

Deliver a complete, reviewable storyboard. Do not generate new final images, scene assets, animations or a new video until the user approves that storyboard. A proposed rewrite is shown alongside the original; it is not applied silently. User changes can approve individual scenes; track approval at scene level. Do not manufacture approval from elapsed time or older feedback.

## Stage 2 — generate approved assets and compose stills

Generate or source only the assets described in approved scenes. Use the approved icon family, official product assets and required static presenter placeholders. Assemble keyframes to check hierarchy, scale, text fit, visual continuity and small-player legibility before animation. Report discrepancies against the approved plan; substantial conceptual changes return to HITL 1. Offer these assembled stills as the second review checkpoint before investing in full motion.

## Stage 3 — animate the approved explanation

Implement the approved start/change/settled states against speech timing, using reusable components where appropriate. Remotion is a candidate implementation layer; adopting it does not replace concept planning or require migrating existing work. Use measured reference motion for reconstruction. Keep transitions purposeful and text readable through intermediate frames.

## Stage 4 — review and verify

Review narration and visual meaning together. For reference reconstruction, provide synchronized source/reconstruction comparison. Verify crop safety, overlap, connector attachment, text readability, caption synchronization and representative intermediate frames. Distinguish measured checks from subjective fidelity judgments. Return for review before publication; local rendering is not publishing.

## Per-scene statuses

`draft` → `awaiting_storyboard_review` → `storyboard_approved` → `assets_ready` → `awaiting_keyframe_review` → `keyframes_approved` → `motion_ready` → `reviewed`.

Only the user can provide the human approval transitions. Store approved scope and requested changes explicitly. Stop dependent production at a pending human checkpoint while continuing unrelated research or documentation when useful.
