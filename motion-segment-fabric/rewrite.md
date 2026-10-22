# Transcript → technical rewrite → graphic

Input: section 3 of [the supplied interview](../motion-pilot-fabric/input-transcript.txt). Audience: technical practitioners and analytics leaders. Scope: one approximately 42-second illustrative walkthrough, not the full interview. Synthetic preview narration.

## Original

“A Store is an entity type. A particular store is an instance. Region and priority are properties. ‘Store operates Refrigeration Unit’ is a relationship. A data binding connects those concepts to actual source fields.”

## Proposed narration

Which refrigeration units does a store operate?

Model Store and Refrigeration Unit as entity types: reusable definitions of business concepts.

Region and priority are properties that describe a store.

Name the relationship operates. In Microsoft's example, the store's Location ID matches the unit's Store ID.

Data bindings map the definitions to their source tables in a lakehouse.

A consuming application uses these mappings to query the sources. The ontology defines the connection; source records stay in their owning systems.

## Why change it?

| Rewrite | Graphic job | Reason / evidence |
|---|---|---|
| Start with a bounded question | Persistent question heading | Makes the relationship necessary; no fabricated answer |
| Define both entity types before connecting them | Reveal Store, then Refrigeration Unit | Viewer knows the endpoints before interpreting an edge; ontology overview |
| Keep properties within Store | Region/Priority reveal in existing card | Distinguish attributes from peer entities; names illustrative from script |
| Name operates and explain matching IDs | Labelled edge, then `LocationId = StoreId` | Turns “connected” into a concrete mechanism; Microsoft's tutorial explicitly documents origin and target fields |
| Map concepts to source tables | Two lower source tiles and dashed bindings | Distinguish business relationship from source mapping; real tutorial table names |
| Separate definition and execution | Hold diagram, explain consuming application | Avoid implying schema drawing copies data or runs a query; overview describes ontology as definitions/context and consumers as execution |

The type/instance distinction, inheritance, metrics and rules are deferred. This segment explains a type-level relation and mapping, not particular returned unit instances. No guaranteed result, source freshness, permission or materialization claim is added.

## Reference choice

Subject reference: https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-1-create-ontology and https://learn.microsoft.com/en-us/fabric/iq/ontology/overview . Previously retrieved October 22, 2026; page text preserved under `../motion-pilot-fabric/research/`. This turn additionally downloaded and inspected Microsoft's actual relationship-configuration screenshot.

Teaching reference: original video's question → explanation/evidence pattern, with source screenshots and raw narration in `../reference-library/entries/question-answer-action.json`. The source's result/action step is deliberately not copied because this pilot has no executed result or configured action.

Alternative: real Fabric UI with actual query output. Better for demonstrating configuration and execution; the conceptual graphic is better for isolating entities, properties, relationship keys and bindings. A full “which store needs attention?” demo would need telemetry, approved thresholds, timestamps and actual evidence, so that claim is outside this segment.
