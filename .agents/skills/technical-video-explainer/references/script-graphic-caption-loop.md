# Develop the explanation and graphic together

User-requested workflow, implemented in `motion-segment-fabric/` on 2026-10-22. This is an editorial method, not a universally optimal teaching formula.

1. **Analyze:** identify the audience's existing knowledge, the new distinction, supported claims and practical question. Separate spoken script from production directions.
2. **Choose an explanation recipe:** use question → definition → mechanism → concrete mapping/example → boundary when explaining how something works. Use contrast → counterexample → repair for ambiguity/failure; use purpose → inputs → transformation → outputs for a real process. Do not force every topic into the same recipe.
3. **Rewrite:** replace vague claims with the actual entities, relationship, inputs/outputs or constraints. Keep original/proposed/reason/source IDs. Match the verbal order to the order in which a viewer can understand the picture. Preserve caveats, and omit ideas that need a separate graphic rather than squeezing them into tiny labels.
4. **Retrieve two kinds of reference:** subject evidence explaining the same concept, preferably primary documentation with diagrams or real UI; and visual-teaching evidence explaining the same relationship from the video library. Read their wording and inspect images. If only a similar visual pattern exists, say so; do not claim it explains the exact target product. No false source claims or imported benchmark results.
5. **Co-design:** choose what remains visible, what each sentence introduces, and why each motion is necessary. Revise the script if the diagram exposes ambiguity; change the graphic if the script needs a different relationship. Do not distort the technical explanation to preserve an attractive template.
6. **Image-first:** apply the target-brand gate; generate a master, derive three or more meaningful coherent state images, and inspect the editable reconstruction against them. Existing authorization to make a pilot permits producing it for review; it does not establish visual approval.
7. **Narration and motion:** record actual narration, retain timing evidence, and align graphic changes to spoken concepts. Draft word-count timing is only an estimate.
8. **Words at the bottom:** when requested, burn readable phrase captions into a reserved lower band, with an optional spoken-word highlight in the target palette. Keep phrases short, use actual audio word timing where available, and retain punctuation. Preserve a stable baseline; no bouncing text or resizing per word. Provide VTT alongside the burned-in version when feasible.
9. **Verify:** check every caption phrase at its rendered size, including the widest phrase; check bounds, technical spelling, sequence and diagram/caption separation. Test audio/video duration and decoding. Timing metadata and automated fit checks do not certify human perception or visual quality.

## Fabric worked mapping example

Original excerpt: “A Store is an entity type… Store operates Refrigeration Unit is a relationship. A data binding connects those concepts to actual source fields.”

Rewritten teaching route:
- Question: Which refrigeration units does a store operate?
- Define: Store and Refrigeration Unit are entity types; properties describe them.
- Mechanism: name the `operates` relation; explain Store.LocationId matching Refrigeration Unit.StoreId in Microsoft's tutorial.
- Grounding: show the separate source bindings to the lakehouse tables.
- Boundary: consumers query the sources; definitions do not imply copying source records or executing a query.

Subject reference: Microsoft retail ontology tutorial, including its actual relationship-configuration screenshot. Teaching reference: source video's question/answer pattern; adapted into a conceptual walkthrough rather than an invented executed answer. Styling: current Fabric theme, not the reference's orange branding.

The captioned segment is a source-backed conceptual explanation, not a complete operational demo or a returned list of units. A later demo should show actual instances, query output and verification.
