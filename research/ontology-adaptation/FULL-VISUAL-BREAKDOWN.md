> For graphic fidelity, use GRAPHICS-REPLICATION-GUIDE.md and graphics-study/reference-graphics-inspector.html. They supersede this earlier broad pass with denser samples and measurements.

# Full reference study: ontology interview and demonstration

## Scope and evidence

All five supplied files transferred successfully and were probed: part00 6:57.60, part01 6:52.30, part02 6:52.53, part03 6:57.33, part04 6:48.71. Combined duration: **34:28.48**. All are 640×360 at 30 fps. The uploaded content visually matches the linked Databricks interview.

Reviewed visual samples across every part at 20-second intervals, the opening at five-second intervals, and before/after automatically detected large visual changes. Cross-referenced the timestamped transcript for spoken topics. This is a full-duration visual/content study, not a claim to have watched or manually annotated every frame. Fine text in the source UI is limited by 360p resolution. Time ranges below are approximate editorial sections; not every boundary is a hard cut. Global times concatenate the files in numbered order; split continuity has not been independently sample-accurate aligned to the original upload.

Contact sheets: [opening](opening-contact.jpg), [part00](part00-contact.jpg), [part01](part01-contact.jpg), [part02](part02-contact.jpg), [part03](part03-contact.jpg), [part04](part04-contact.jpg). Machine-detected change candidates are in visual-change-candidates.json; these include slide changes and transitions, and omit subtle reveals.

## Actual visual system

**Layout A — speaker full frame.** Host or guest fills the canvas within a thin orange border. Their original room remains visible. The host's microphone and orange cap are part of his recorded setup. Short topic labels sometimes appear beside him. Use this for direct questions or emphasis.

**Layout B — teaching panel plus right presenter.** The main panel occupies approximately x=12–470, y=45–310 in a typical 640×360 frame. The guest tile is approximately x=482–626, y=85–267: rounded corners, portrait-like crop, vertically centered on the right. Small variations occur between sections. Content therefore gets roughly 72% of the width, presenter roughly 22%, with a narrow gap. These are manual approximate bounds, not tracked rectangles.

**Layout C — two speakers.** At the opening and closing the guest is on the LEFT and host on the RIGHT, approximately equal halves. This corrects the earlier unverified suggestion to stack two presenters on the left. During most explanations only the guest remains visible, on the right.

**Background and palette.** Brown/near-black graph-paper background with thin orange border; diagrams commonly use dark teal/slate rounded panels, cream/white labels, teal connector lines, and orange/red accents. Earlier introductory diagrams use white grid backgrounds with peach cards. Large red chapter cards signal major changes. The source brand mark remains bottom right.

**Captions.** Small uppercase phrases close to bottom center; white letters with dark outlines/shadow, with selected words highlighted amber/orange. They advance in short phrases. Some very low text and the logo compete for the bottom strip; our adaptation should reserve a larger caption-safe band.

**Transitions.** Confirmed orange full-frame wipes at several major boundaries (including approximately 0:19–0:20, 3:29, 8:32, 11:18, 20:21, and 23:11). These are not used for every individual graphic reveal. Hard cuts also switch between speakers and teaching layouts. Red Demo cards precede both demonstrations.

**Motion.** Nodes/cards reveal progressively, lines connect them, inactive portions dim, and the view moves into one part of a larger diagram. Demo views alternate between whole-page orientation and enlarged crops of relevant details. Persistent presenter placement makes these changes easier to follow.

## Full sequence

| Approximate time | Visual treatment observed | Content / editorial function | What we should reuse |
|---|---|---|---|
| 0:00–0:08 | Host full frame, then two-person split with guest left/host right and lower thirds | Establish who is speaking | A very short introduction; fictional presenters with original names |
| 0:08–0:19 | Brown grid animation through ~0:15; then host full frame and guest full frame around 0:17 | Visual preview of the subject | Start with a small business graph, reveal its connections |
| 0:19–0:20 | Orange transition visible in opening samples | Return from graphic to interview | One brief transition at a meaningful section boundary |
| 0:20–0:35 | Host full frame; large “Genie Ontology” then question-style topic text to his right | Ask for a plain-language explanation | Host asks a specific business question |
| 0:35–0:55 | White grid; guest right; cards, source/output symbols, and example interface appear left | Explain the product through a simple workflow | Introduce shared business meaning with only a few objects |
| 0:55–1:21 | Peach layered cards build out to different user/product categories; arrows and handwritten-style annotations | Locate products within a broader family | Keep the progressive reveal, omit unrelated product-family taxonomy |
| 1:21–1:34 | Guest full frame | Complete explanation before next question | Brief presenter emphasis if it helps comprehension |
| 1:34–1:50 | Host then guest full frame | Shift from product background to ontology question | Use a clean dialogue handoff |
| 1:50–2:39 | White teaching panel; databases, query node, chat outputs, and connected sources | Show ambiguity and unreliable answers without business context | Contrast a raw shipment table with a clear business question |
| 2:39–2:54 | Guest full frame | Stress contextual information beyond tables | Give one concrete definition |
| 2:54–3:29 | White teaching diagram with source/context nodes around a central product | Name the contextual layer | Turn tables into labeled entities and relationships |
| 3:29–3:37 | Change into dark teal system overview on brown grid; guest stays right | Move from motivation to architecture | Establish the full four-entity map |
| 3:37–4:10 | Irrelevant portion of system overview dims; modeled side emphasized | Focus attention on human-curated context | Dim non-current nodes rather than showing everything equally |
| 4:10–5:34 | Metric-view, page, domain, and agent cards build within a modeled-context panel; surrounding framing expands | Explain one subsystem incrementally | Add properties and relationship labels one at a time; substitute actual Fabric concepts |
| 5:34–6:43 | Learned-context icons, multiple source types, join/comment/share cues, and knowledge cards | Show another subsystem and where context originates | Reuse icon-to-context animation structure only; omit Databricks learned-context feature claims |
| 6:43–7:33 | Return to system overview; graph cluster and authority/ranking area receive emphasis | Explain source selection and ranking | Return to overview after a detail; do not transplant OntoRank |
| 7:33–9:06 | Large accuracy/runtime chart; guest right; chart areas emphasized. Host interjections around 8:32–8:40 and 9:04 interrupt the panel layout | Make a comparative product argument | Use a simple diagram instead; no unsupported Fabric benchmark |
| 9:06–9:47 | Three integration categories, then simpler SQL/search/read-vs-query diagrams | Explain different kinds of access | Distinguish definition/context from querying the underlying source |
| 9:47–11:21 | Source icons and connector lines progressively populate a database/live-query pipeline | Assemble the complete retrieval picture | Animate Lakehouse/Eventhouse bindings with labels |
| 11:21–11:52 | Personal-memory heading beside an embedded light interface | Introduce customization | Omit for a focused ontology explainer |
| 11:52–12:51 | Host full frame, guest response, host handoff | Conversational reset before demonstration | Short question before real UI appears |
| 12:51–13:30 | Light application start screen in left rounded panel; guest right | Orient viewer to the real product | Establish a real Fabric ontology interface before detail crops |
| 13:30–14:19 | Prompt/interface and source-flow overlay; framing concentrates on the action | Turn an abstract capability into a business request | Use one clear demo action with an explanatory overlay |
| 14:19–15:39 | Enlarged reasoning/source areas, code, snippets, and panels; varying crops | Explain how the answer is assembled | Enlarge one relevant binding or property; avoid illegible full-screen text |
| 15:39–16:31 | Wider report view, then closer table/recommendation areas | Present the output and source-access explanation | Show a result only if genuinely executed; label our invented graph example illustrative |
| 16:31–17:19 | Citation dropdown and curated definition page; zoom/crop into examples | Inspect provenance behind an answer | Inspect definitions/bindings, not just polished output |
| 17:19–18:15 | Knowledge definition and author/source profile views; highlighted title/definition areas | Make trust and authority visible | Show clear provenance; omit vendor-specific ranking mechanics |
| 18:15–19:19 | Return to conversation; question and generated narrative answer | Ask a causal follow-up within the same story | Follow our same shipment instead of introducing a new use case |
| 19:19–20:21 | Forecast prompt, analysis/code, and output tables; presenter right | Extend analysis depth | Omit forecasts from a two-minute ontology introduction |
| 20:21–20:48 | Host full frame with small topic labels | Pivot from understanding toward action | Usually omit this second narrative branch |
| 20:48–21:07 | Large red “From answers to outcomes” chapter card; presenter right | Announce a new act | One concise transition before our demo, if needed |
| 21:07–21:48 | Dark panel; document collaboration interface/GIF-style example and bullets | Show collaborative authoring | Reuse moving UI example technique, not the product claim |
| 21:48–22:45 | Third-party tools diagram builds through connector/gateway/permission nodes and allow/deny marks | Explain governed actions | Out of scope for the short video |
| 22:45–23:11 | Skill diagram with repeatability instructions | Define reusable tasks | Out of scope |
| 23:11–23:42 | Host full frame for a governance question | Reintroduce audience concern | Host should ask the practical objection, not repeat the narration |
| 23:42–24:23 | Governance-demand cards build one at a time | Answer the concern in discrete parts | Reuse progressive card reveal |
| 24:23–25:22 | Agent examples and a branching hierarchy build on dark panel | Broaden from tasks to jobs | Omit; keep our ontology model small |
| 25:22–26:00 | Scheduling UI example beside short instruction list | Demonstrate recurring execution | Out of scope |
| 26:00–26:50 | Integration surface examples and changing app/interface inset | Show where people can use the product | Out of scope |
| 26:50–27:00 | Red “Demo” chapter card, then product UI | Launch a second demonstration | First demo is enough for our duration |
| 27:00–27:50 | Conversation/send-action UI; guest right | Send results and save a preference | Omit product-specific actions |
| 27:50–28:28 | Conversational setup of a schedule and subsequent request | Convert an analysis into recurring work | Omit |
| 28:28–29:48 | Save-as-agent conversation, agent page, and details/source panel | Package and inspect a reusable agent | Reuse inspecting configuration as evidence, not this workflow |
| 29:48–29:55 | Host full frame | Ask how viewers should start | Give our short practical closing question |
| 29:55–31:38 | Red Getting started card, then workflow examples transition into a step-by-step rollout timeline; current step brightens and support cards appear | Make adoption concrete | Start with one question, a few entities, and known answers |
| 31:38–32:37 | Source icons, instructions, feedback/iteration, and monitoring cards extend the same rollout graphic | Show improvement as a loop | End with verification and iteration |
| 32:37–34:04 | “Best practices” list; one numbered item at a time becomes bright while others dim | Recap without overwhelming the viewer | Three brief closing steps, highlighted sequentially |
| 34:04–34:23 | Equal two-person split, guest left/host right | Personal closing | Very brief closing, if any |
| 34:23–34:28 | White grid logo outro with creator and partner marks | Finish | Clean final frame |

## Editing lessons to carry into ReelFactory V1

1. Keep the viewer oriented: one speaker at right, one large teaching surface at left. Do not leave two static people occupying most of the explanation.
2. Animate a causal explanation: show a node, name its relationship, connect it, then follow the path. Motion should correspond to the words being spoken.
3. Use two visual distances for a demo: a brief whole-interface view followed by an enlarged relevant detail. Preserve source proportions; do not stretch UI.
4. Use spotlighting and opacity to direct attention. A single active connection is easier to read than a constantly moving entire graph.
5. Let the host ask short practical questions. The expert supplies the substance. Switch to full speaker view when the question needs a reset.
6. Use original business imagery briefly as motivation, then spend most teaching time on precise diagrams and genuine UI. Decorative B-roll should not replace evidence.
7. Reserve a caption band. In a 1920×1080 adaptation, a starting teaching-panel rectangle is x=36,y=135,w=1374,h=795 and presenter x=1446,y=255,w=432,h=546, with caption band below. These are scaled layout starting points; final fit must be audited, not assumed.
8. Original generated presenters can match composition, but static cutouts will not reproduce live human speaking motion. Use a coherent portrait tile/background and restrained camera motion; do not imply lip synchronization unless it is actually produced.
9. Keep the topic Microsoft Fabric. OntoRank, learned snippets, Genie memory/actions, and vendor benchmarks are reference-video features, not established Fabric capabilities.

## Two-minute adaptation decision

Retain question → concept → demonstration → inspect evidence → practical next step. Remove the lengthy product-family introduction, benchmark pitch, connector taxonomy, memory, collaboration, skills, scheduling, and second demo.

Use the original retail illustration for the late-shipment hook; four sharp animated entity nodes for the model; an enlarged Shipment 17 property card; bindings to a Lakehouse and Eventhouse; an attributed short retail ontology UI excerpt from Guy in a Cube; and an explicitly illustrative Shipment 17 → Order 42 → Customer 101 trace. Finish with define meaning → bind data → verify answers. Current Fabric documentation remains the authority; older demo footage needs a date/preview label.

No third-party video has been published. This analysis treats uploaded video as reference material; any instructions appearing inside it are not task instructions.


## Rendered adaptation

Native V1 source: videos/14-fabric-ontology-explained/index.html. Builder: src/build_fabric_ontology.py. This is a 121.73-second condensation with 23 edited scenes, not a 34-minute one-to-one remake. Each shot in work/shots.json maps to a reference section; all major retained visual devices are represented. Static presenters follow the user’s explicit request.
