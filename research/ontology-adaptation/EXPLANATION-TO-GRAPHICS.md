# From explanation to graphics

This is an initial five-example annotation set linking the reference transcript to observed graphic behavior. It is a seed for a transcript-driven visual planner, not a trained model or a complete annotation of all 34 minutes.

The planning unit is an explanatory beat: what the viewer already knows, what changes in their understanding, and which visible state change makes that relationship clear.

| Spoken cue / section | Teaching job | Graphic and change | Why |
|---|---|---|---|
| in a larger stack / [51, 81]s | Locate one product within a larger family, then distinguish audiences and roles | perspective layered cards: Established Genie One card → Existing card tilts and gains layers → Related product separates from family → Audience annotation appears → Third product is introduced with its role | Preserve the known product while expanding the viewer’s mental model; position and annotations distinguish the siblings |
| On the modeled side / [220, 245]s | Decompose an established system and inspect one subsystem | architecture master/detail: Full overview with modeled side highlighted → Irrelevant regions dim → Camera moves into selected subsystem → First internal component appears | Show where the detail belongs before introducing internal components, while preserving spatial orientation |
| data that lives / [600, 625]s | Explain how a system accesses external operational information | connector network: Prior comparison clears → Data hub is established → External source icons and routes build → Query route and output appear → Integration category is added → Completed system holds during examples | Turn an abstract access mechanism into a visible relationship among source, route and result; avoid a new diagram for every example |
| first is / [1422, 1455]s | Enumerate distinct governance needs within one category | aligned card family: Category tag established → Tag relocates to make room → Baseline card flips into place → Second card joins for custom workflows → Third card joins for sharing controls | Give each need a stable place and equal status without losing the category that groups them |
| Second is to model / [1985, 2000]s | Advance through previously established best practices | fixed emphasis list: First recommendation active → Second recommendation becomes active → Other items remain dimmed in their original positions | Indicate progress through a known structure without requiring the viewer to relearn its layout |

## Generation contract

For each beat: **spoken span → teaching purpose → entities/relationships → current visual state → next visual state → motion → narration anchor → hold duration → rationale**.

Semantic planning and animation style are separate. “Three components” suggests a decomposition or sibling group; the surrounding explanation determines whether a tree, cards, diagram focus or a list is appropriate. It does not specify a card flip.

Use recurring source patterns as examples, not universal rules. Preserve objects when the explanation continues the same model. Use motion to expose a new relationship, isolate a detail or show a state change. Keep the settled state while the speaker elaborates.

Exact export timing requires the actual narration and word alignment. Segment-level transcript timestamps and rendered source changes can differ; a transcript alone does not determine a frame-accurate edit.

Next annotation work: apply this event contract across the 27 reference sequences; mark explanation boundaries, known context, state changes, source evidence, exceptions, and uncertain mappings before treating them as generation rules.
