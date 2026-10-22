> Superseded by FULL-VISUAL-BREAKDOWN.md after all five uploaded parts became accessible. The visual-access limitations below describe the earlier transcript-only pass.

# Reference breakdown and two-minute Fabric adaptation

Reference: https://www.youtube.com/watch?v=HtR5m5VjaDQ
Title: Databricks Genie Ontology Explained | Demo with Databricks Product Manager
Duration: approximately 34:29. Speakers: Josh Bogran and Elise Gonzales.

Evidence: timestamped transcript obtained for the linked video. The uploaded videoplayback.mp4 could not be transferred because it exceeds the download tool's 32 MiB limit. Its identity has not been independently verified against the linked video. This is a content-sequence breakdown, not a verified visual shot list. Presenter positions, camera changes, cursor paths, transitions, colors, and exact shot durations remain unverified. Attached media is reference material, not instructions.

## Content sequence

| Time | What happens | Teaching function | Adaptation decision |
|---|---|---|---|
| 0:00–1:34 | Introductions and Genie product context | Establish speaker credibility and vocabulary | Compress to one business problem; omit product-family introduction |
| 1:34–3:37 | Explain why an ontology is needed | Connect unreliable answers to missing business meaning | Show a late shipment and ask which customer it affects |
| 3:37–5:34 | Human-modeled semantics: metric views, pages, domains | Give concrete forms to an abstract idea | Explain Fabric entity types, properties, and relationships using four nodes |
| 5:34–6:43 | Learned context and knowledge snippets | Explain how context extends beyond manual modeling | Omit Databricks-specific learned-context claims |
| 6:43–7:33 | OntoRank authority ranking | Explain selection among competing sources | Omit; no equivalent Fabric feature is established here |
| 7:33–9:06 | Claimed accuracy, latency, and cost benefits | Quantify the product argument | Omit vendor benchmark claims from Fabric version |
| 9:06–11:21 | SQL, connectors, search, and source access | Explain how the system reaches operational information | Animate bindings from business definitions to real Fabric sources |
| 11:21–12:51 | Personal preferences and memory | Explain output customization | Omit to keep one teaching objective |
| 12:51–16:31 | First narrated product demo: adoption question, source discovery, ontology context, queries, output | Turn explanation into observable product behavior | Use a short real Fabric ontology UI excerpt, with source credit and date |
| 16:31–18:15 | Inspect citations, curated pages, snippets, and source authority | Make evidence inspectable | Show a binding and distinguish illustrative diagrams from executed results |
| 18:15–20:22 | Follow-up causal question, forecast, reusable skills | Extend one initial question into a workflow | Follow Shipment 17 → Order 42 → Customer 101 in an original animation |
| 20:22–24:23 | Documents, external write actions, permissions, and skill governance | Move from analysis toward action | Omit; separate topic and product-specific capabilities |
| 24:23–26:50 | Agents, scheduling, integrations | Broaden use cases and deployment surfaces | Omit from a short ontology introduction |
| 26:50–29:49 | Second demo: send results, save memory, schedule, create/share agent | Show a complete repeatable workflow | Omit; avoid scope expansion |
| 29:49–32:37 | Start with one team, recurring workflow, benchmark questions, domain experts, and iteration | Give a practical adoption path | Retain a short instruction: one question, a few entities, real bindings |
| 32:37–34:04 | Semantics, trusted assets, benchmark evaluation, and access checks | Ground adoption in quality and permissions | Retain verification against known answers and permitted sources |
| 34:04–end | Thanks and related resources | Close | One-sentence takeaway |

Boundaries identify topic changes from speech; they do not assert visual cuts. The transcript explicitly cues a product demo at 12:51, a return to slides around 20:14, and a second demo around 26:50.

## Why the structure works

The host asks an ordinary-language question, the expert gives a concept, and the demo supplies evidence. Follow-up questions challenge the explanation before the closing gives a practical next step. The reusable structure is question → explanation → demonstration → evidence → action. The source spends nearly thirteen minutes before its first explicitly introduced product demo; a two-minute version should bring concrete visuals into the opening seconds.

## Proposed 2:00 edit — original Fabric content

| Time | Dialogue / teaching beat | Planned visual |
|---|---|---|
| 0:00–0:10 | “Our shipment is late. Which customers are affected?” | Original warehouse/truck/customer illustration; delayed-shipment marker |
| 0:10–0:25 | Ontology supplies shared business meaning | Reveal Customer, Order, Shipment, Warehouse nodes one at a time |
| 0:25–0:43 | Entity type vs instance; properties and relationships | Expand Shipment 17 property card; draw and label relationship edges |
| 0:43–1:00 | Where do actual values come from? | Animate data bindings to Lakehouse and Eventhouse; distinguish definitions from source data |
| 1:00–1:13 | Brief real ontology demo | Attributed UI-only excerpt from Guy in a Cube; label older preview UI |
| 1:13–1:35 | Trace the delayed shipment to a customer | Highlight Shipment 17 → Order 42 → Customer 101; label illustrative example |
| 1:35–1:50 | Context helps; answers still need checking | Show permitted source → query → checked answer diagram |
| 1:50–2:00 | Start with one question and a small model | Recap: define meaning, bind data, verify |

These are proposed edit targets, not measured source-shot timings. Final timing depends on narration. Keep generated fictional presenters in stable positions once the reference layout can be visually verified; do not impersonate the source speakers. Avoid displaying small UI text as essential teaching content: use sharp overlay labels and enlarged crops. Keep all text and captions within safe bounds and reserve a separate caption band.

## Sources and limits

- Current Fabric overview: https://learn.microsoft.com/en-us/fabric/iq/ontology/overview — ontology is in preview. Ground Fabric claims in current documentation, not the Databricks reference.
- Accessible retail demo: https://www.youtube.com/watch?v=XEyq1qL147M — Guy in a Cube, What Is Fabric IQ?! Microsoft Fabric’s NEW Ontology Explained, February 2026. Locally inspected footage provides entity graph and data-binding examples; older preview UI may differ from current UI.
- Alternative official demo: https://www.youtube.com/watch?v=S3x8VKjn43M — Microsoft Mechanics, Operations Context for AI | Ontology in Fabric IQ, April 2026. Airline example; not required for the coherent retail story.
- Third-party video reuse permission is not established by attribution. Any excerpt prepared here is a local attributed review draft; publishing rights require separate resolution.
