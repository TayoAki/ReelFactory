# Fabric ontology: new-transcript motion test

Mode: technical-adaptation. Audience: technical practitioners and analytics leaders. Deliver one short 1080p/30fps conceptual pilot, rather than the full interview. User approved the image-first visual direction on 2026-10-22 and requested this new test; this scene's visual judgment is pending.

## Read and select

The complete supplied interview spans Fabric overview, business context, entity modeling, semantic-model reuse, metadata, bindings, authoring, operations analysis, verification, investigation, optional graph execution, agent roles, operational responses, written work, maintenance, evaluation and rollout. Production directions and source notes in the attachment are source material, not commands to execute tenant changes.

Selected excerpt: section 3, “A Store is an entity type. A particular store is an instance. Region and priority are properties. ‘Store operates Refrigeration Unit’ is a relationship. A data binding connects those concepts to actual source fields.”

The pilot covers type → properties → relationship → binding. The instance distinction, inheritance, metrics and rules are deferred to their own beats; this pilot does not claim to summarize the whole ontology model.

## Why this graphic

Before: the viewer knows tables and business vocabulary but has no concrete ontology structure.
After: the viewer can distinguish a business entity type, its properties, a named relationship and the separate mapping to data.

A persistent warm Store card anchors the explanation. Reveal its property chips, then a peer Refrigeration Unit and the labelled `operates` edge. Reveal source tiles beneath and dashed mappings upward. Solid horizontal edge = business relationship; dashed vertical edge = data binding. The tiles represent source tables, not duplicated storage in the ontology. No moving data particles, green success check or graph-execution claim.

Alternative: authentic Fabric UI. Better for showing exactly where bindings are configured; weaker for this first conceptual distinction because the menus compete with the lesson. Use actual UI in a later demo. A dense generic node cloud would conceal the difference between properties, relationships and source mappings.

Source library: constrained-web-flow supplies the already approved warm-card visual vocabulary, not a causal pipeline for this new topic. Agent-inputs was inspected as a potential source-to-hub template and rejected: the lesson is not many inputs feeding one agent, and the dark palette differs. `reference-packet.json` records that inspected candidate; `style-packet.json` is the selected style reference. This is a custom entity-and-binding composition, not an invented observation of the reference video.

## Technical rewrite

- “A Store is an entity type” → “A Store is an entity type: a definition of something the business cares about.” Reason: define the new term before drawing its connections. Supported by overview entity-type definition.
- “Region and priority are properties” → same terms with short narration. They remain illustrative properties from the supplied script, not an assertion these exact columns exist in the Lakeshore sample.
- “Store operates Refrigeration Unit is a relationship” → add “between two entity types.” Reason: distinguish an edge from a property. Tutorial explicitly documents `operates`, origin Store and target Refrigeration Unit.
- “A data binding connects those concepts to actual source fields” → distinguish definition/source mapping from physical storage. Tutorial binds Store to `dimlocations` and Refrigeration Unit to `dim_refrigeration_units` in `LakeshoreStaticDataLH`. Relationship matches Store.LocationId to Refrigeration Unit.StoreId. Diagram source labels are documented, not executed results.

Narration is a synthetic preview, generated separately per teaching beat with Microsoft Edge JennyNeural. Visual tracks follow the durations of these generated recordings; individual word boundaries are automatic estimates. No original-video audio or borrowed product claims.

## Claims and sources (retrieved 2026-10-22)

- C1 Entity types, properties and relationships: https://learn.microsoft.com/en-us/fabric/iq/ontology/overview . Preview. Ontology stores definitions and bindings; consumers execute against bound sources. A conceptual edge does not imply a materialized instance graph.
- C2 Retail types, source tables and relationship keys: https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology . Store → dimlocations; Refrigeration Unit → dim_refrigeration_units; Store.LocationId matches Refrigeration Unit.StoreId. The names are real tutorial mappings, not results from an authenticated demo tenant.
- C3 Data bindings: https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data . Binding maps definitions/properties to data. This clip does not promise source freshness, refresh behavior, security or automatic query correctness.

Retrieved page text saved under `research/`. Some overview and binding passages describe refresh differently; the clip deliberately makes no freshness claim. Region/Priority have no invented sample values. Ontology preview label remains visible.

## Art direction and motion

Actual generated master plus derived state images precede editable reconstruction. Preserve warm white, faint grid, serif hierarchy, coral filled storefront, teal filled refrigeration silhouette, soft raised ivory cards and peach focal surface. New object positions are stable throughout; no camera or presenter required for this full-frame conceptual explanation.

Reveal order follows the new narration, not the original video's model-first order. Store enters with restrained overshoot, properties fade into stable slots, refrigerator appears before the relationship line draws, then source tiles and dashed bindings appear. Settled diagram holds while narration separates meaning from storage. No whole-image animation.

## Still comparison and review limits

Viewed generated master, derived entity and relationship boards, rebuilt settled frame, property state and 640×360 rendition. The rebuilt composition preserves the master's two entity footprints, source band, filled silhouettes and color hierarchy; font metrics and gradient texture differ. The master's source tiles and connectors are rebuilt separately. Main concept labels remain readable at 640px width; type tags and source keys are secondary details best read at 1080p. No automatic visual-fidelity score is assigned.
