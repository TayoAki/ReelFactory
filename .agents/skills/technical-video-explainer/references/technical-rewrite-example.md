# Example: rewrite for technical practitioners

This is a proposed adaptation example, not replacement narration for the reference reconstruction. The longer wording requires a longer duration; it does not fit the original 46-second practice window.

**Original:** “Genie One is our AI co-worker for business users. It connects to your data and tools. It answers questions about your business.”

**Proposed:** “Genie One gives business users a natural-language interface to their data. When a question matches an available Genie Agent, chat uses that agent; otherwise it searches relevant data assets. The distinction matters: the interface is the entry point, while domain context helps determine how the question is answered.”

**Why:** Replace the broad coworker metaphor with the interface, routing behavior and relationship between the entry point and domain context. The proposed mechanism is supported by current documentation; it must not be presented as an archived description of every historical release.

**Evidence:** https://docs.databricks.com/aws/en/genie-one/chat

**Graphic:** Begin with a labelled Genie One entry point and a user question. Retain that question while revealing two explicitly labelled routes: matching agent; relevant assets when no agent matches. This is `connector-network` / mechanism, not `product-family`.

**Alternative:** A screen recording is better if teaching exact UI interaction rather than the routing model. A three-product comparison would distract from this sentence.

**Do not infer:** that every agent is searched sequentially, that the diagram specifies internal implementation, that data access is unrestricted, or that the answer is always correct.

**Proposed ontology continuation:** “Genie Ontology supplies shared business context for Genie One and Genie Code. It combines governed definitions—such as metric views and domains—with context inferred from existing assets and usage. Retrieved context is subject to permissions.”

**Evidence:** https://docs.databricks.com/aws/en/genie/genie-ontology

**Graphic:** Two clearly labelled input categories converge into shared context; a definition such as ‘active customer’ supplies a concrete example. Show which context is modeled versus inferred. Do not rename this diagram ‘Fabric ontology’ without researching Fabric's own mechanisms.

**Proposed time budget:** about 40–55 seconds for this expanded explanation, depending on delivery and pauses. Estimate only; measure against actual narration before animation.
