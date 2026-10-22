# Fabric ontology reference adaptation

Review deliverable: `out/final.mp4` (1920×1080, 30 fps, ~2:02).
Portable embedded player: `../../fabric-ontology-review.html`.

This condenses the analyzed 34:28 reference to the user's earlier couple-minute brief. The 22 shot records in `work/shots.json` map the retained scenes to reference sections. Fictional presenter images are intentionally static placeholders. Original dialogue uses two synthetic voices; there is no lip synchronization or source-speaker impersonation.

The edit uses a left teaching panel/right presenter tile, two-person opening and closing, full host question shots, original animated diagrams, orange wipes, a red demo card, real documentation imagery, and two attributed source UI excerpts. The retail example's entity instances and values are illustrative.

Sources, rights flags, and current Fabric claim limits: `PLAN.md`. Third-party video excerpts are for a local attributed review draft; publication permission is not established. Nothing has been published.

Rebuild from the ReelFactory root:

```
python src/build_fabric_ontology.py
python src/render_recreations.py --project-file content/fabric-ontology/projects.json --workers 4
python src/package_fabric_ontology_review.py
```

The renderer caches output: remove `out/render.mp4` and `out/verification.json` before rendering visual edits. Source excerpt files are cached too; remove the changed excerpt asset if its in/out point changes.

Checks: `out/verification.json`, `out/frame-fit-audit.json`, `out/panel-fit-audit.json`, `out/motion-check.json`, `out/audio-review.json`. Visual reviews are sampled, not an every-frame annotation.

Motion revision: src/ontology_motion.py replaces pop-in cards with persistent object morphs, narrated connector draws, moving route highlights, context dimming, and eased detail zooms. Prior output retained at out/previous-version/pop-in-version.mp4. See work/motion-design.json and out/motion-curve-audit.json.
