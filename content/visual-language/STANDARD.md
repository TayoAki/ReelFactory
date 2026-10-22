# Explanatory graphics standard

Research date: 2026-10-22. This standard applies to new explanatory scenes. Reference reconstruction studies retain measured source choices where matching them is the goal.

## Symbols and identity

- **Brand check before storyboard generation:** separate the reference's visual grammar from its product colors. Fabric videos use the sourced green/teal project theme in `fabric-brand/theme.json`; read `fabric-brand/README.md` for evidence and editorial tints. Do not inherit Databricks orange/peach in a technical adaptation. Exact source colors remain appropriate only for explicitly requested reconstruction/comparison. Retained serif typography is our editorial style, not claimed Microsoft brand typography.

- Use official Fabric SVGs for named Fabric products and items, with a nearby text label. Preserve the published colors and geometry; do not crop, flip, rotate or distort the product mark. Source and permitted training/documentation uses: https://learn.microsoft.com/en-us/fabric/fundamentals/icons
- Use Fluent System Icons, 24 regular, for generic concepts. These are MIT-licensed. Start with database, document, people, search, shield-lock and settings. Preserve one visual weight and optical size across a scene. Official guidance: https://fluent2.microsoft.design/iconography
- Treat symbols as established conventions rather than universal meanings. A shield is a literal metaphor; a label and visible access rule explain permissions. A gear means configuration, not every automated process.
- Ontology: a labelled entity/relationship diagram plus a concrete business definition. Agent: a labelled role with inputs and outputs. Do not invent a product logo or substitute a brain/diamond for a technical explanation.
- Record source URL, collection, icon variant, license and intended meaning in the asset manifest. Use real product screenshots when teaching actual UI, and visibly distinguish conceptual examples from executed results.

## Explanation and motion

- Each scene declares the spoken claim, intended understanding, known entities, new relationship and resulting visible state.
- Keep entities stable across beats; reveal the new distinction. A change of layout must express a change of meaning.
- Use enter/exit, emphasis, connector reveal, container transform, camera focus and hold as a small motion vocabulary. Do not apply springs to everything or continuously move a readable diagram.
- Give each connector a direction and meaning. Product-family arrangement is not automatically software architecture.
- Limit motion to the current focus. Dim supporting elements only enough to preserve orientation; do not remove information needed to understand the next beat.
- Default prototype timings at 30fps: emphasis 6–10 frames, short enter/exit 12–18, connector reveal 18–24, major reframe 24–45. These are editorial starting points, not Fluent-prescribed durations or source measurements. Measured reference timings and narration take precedence.
- At 1920×1080, start with labels 36–48px, explanations 32–38px, 72–96px page insets and a reserved caption band. Check the actual output at 640×360. Remove text or split beats when it cannot be read at that size.
- Verify beginning, middle and settled frames for clipping, overlaps and readable text. Preserve hierarchy during movement, not only at endpoints.
- Motion inspiration: https://fluent2.microsoft.design/motion (functional, natural, consistent motion; meaningful hierarchy and choreography). These are UI principles adapted to video, not a claim that UI timings automatically suit narration.

## Remotion decision

Recommendation: pilot Remotion for new reusable scenes; preserve the existing V1/GSAP/Hyperframes work and measured reference studies. No migration has been performed by this research.

Why: React components can accept scene-plan data; `useCurrentFrame` makes state an explicit function of frame; `interpolate` and optional `spring` support controlled animation; compositions and sequences provide fixed dimensions and timing. This fits transcript-derived scenes and repeatable frame comparison. The current renderer can also be deterministic; changing engines does not itself improve the design.

Proposed components: `EntityNode`, `LabeledConnector`, `DefinitionReveal`, `ProductFamily`, `ChatExample`, `GovernanceBoundary`, `CameraFocus`, `PresenterTile`, `CaptionPhrase`. Keep concepts, assets, timing and sources in JSON outside component implementation.

Pilot scope: port one 10–15-second measured reference scene, render at 1920×1080/30fps, compare the same frame samples against the source and current renderer, verify caption synchronization and intermediate-frame bounds, then decide whether to extend the library. Use reference-derived easing when available; use springs selectively.

Relevant docs: https://www.remotion.dev/docs/the-fundamentals · https://www.remotion.dev/docs/use-current-frame · https://www.remotion.dev/docs/interpolate · https://www.remotion.dev/docs/sequence

Licensing: the currently retrieved license permits individuals, for-profit organizations with up to three employees, nonprofits, and noncommercial evaluation under the Free License. Other commercial organizations require a Company License. Confirm applicable terms when implementing: https://www.remotion.dev/license

## Production contract

Transcript → verified concept/claim → explanatory beat → generated master still → multiple coherent storyboard state images → human visual review → editable layer reconstruction → still comparison → per-layer motion tracks → one-scene motion review → scale the approved recipe.

The renderer consumes the plan. It does not decide whether a product claim is true or whether a metaphor communicates the intended concept.


## Image-first quality checkpoint

Follow `storyboard-first/PROCESS.md` for new visual work. Each explanatory graphic needs actual state images before animation. The full-video flat-card reconstruction was rejected by the user as a visual-quality baseline; its technical validation does not establish design approval. Reconstruct the chosen image as editable layers and compare the still before animating. Preserve the actual reference's filled icon weight, centered serif labels, soft card depth and semantic color treatment when reconstructing the supplied white-card example. Generic icon defaults must not override this observed style.
