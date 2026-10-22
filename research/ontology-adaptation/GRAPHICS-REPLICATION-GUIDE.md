# Reference graphics: structure, hierarchy, motion, and replication specification

Source: https://www.youtube.com/watch?v=HtR5m5VjaDQ (Databricks ontology interview and demo).

This replaces the earlier broad style summaries as the construction reference. It analyzes the supplied video; it does not build another Fabric edit.

## Evidence and precision

All five files are 640×360 at 30 fps, totaling 34:28.48. This pass inspected **27 graphic sequences (216 source frames)**, **six denser motion sequences (72 source frames)**, regional change measurements at 4 fps, and selected motion windows at the source 30 fps. Seven short reference excerpts retain actual motion across all five files. Timings below use the files concatenated in numbered order; they are not a new alignment against YouTube's clock.

Layout bounds are manual measurements supported by decoded pixels, typically accurate to about 1–2 source pixels. Colors are approximate decoded colors, affected by compression and color conversion. Template tracking and OCR provide approximate camera scale and text bounds. The MP4 does **not** establish the original font files, authoring software, vector paths, camera pivot, or easing curves. Those must be visually matched rather than claimed recovered. Observations, measurements, and proposed implementation choices are distinguished below.

## What the earlier recreations misunderstood

The reference is a collection of specific visual systems with a consistent editorial frame. A brown background, presenter tile, and eased cards reproduce only a small part of it.

- There is no permanent brand header or large added title above every graphic. A diagram frequently occupies the teaching area by itself.
- A title sometimes sits in the **left column**, while the evidence occupies the right. Other scenes use a small central label or the source UI's own hierarchy.
- Several diagram sequences preserve a larger system and move a **camera inside a fixed viewport**. Replacing the viewport's contents with a new group of cards loses that continuity.
- The pale governance cards visibly rotate about a vertical axis. A fade-and-slide is a different effect.
- The introductory peach card tilts into perspective and gains offset layers. Scaling a flat rectangle cannot reproduce that depth.
- The speaker tiles show head and shoulders, with the face relatively large. Waist-up people inside large decorative cards produce different proportions.
- Graphics often settle and hold. Motion is concentrated at changes of idea. A continuous decorative push on every scene changes the reference's rhythm.
- A measured best-practice transition is a one-frame emphasis change, not a slow fade. Smooth visual organization does not imply that every change is eased.

## 1. Outer composition: measure this before drawing content

Canonical coordinates below refer to the **640×360 source**. Multiply by three for a 1920×1080 implementation. Do not mix these with independent design coordinates inside the diagram.

| Element | Source bounds / size | 1920×1080 equivalent | Confidence |
|---|---|---|---|
| Orange outer frame | approximately 3 px thick, at canvas edge | approximately 9 px | Measured / compression softens edge |
| Main dark content window | x≈12, y≈50, w≈458, h≈262 | x≈36, y≈150, w≈1374, h≈786 | Measured typical layout |
| Content corner radius | approximately 16–18 px | approximately 48–54 px | Manual estimate |
| Right speaker tile | x≈482, y≈84, w≈145, h≈179 | x≈1446, y≈252, w≈435, h≈537 | Measured typical layout |
| Speaker corner radius | approximately 12–14 px | approximately 36–42 px | Manual estimate |
| Gap between main window and speaker | approximately 12 px | approximately 36 px | Measured |
| Right canvas margin | approximately 13 px | approximately 39 px | Measured |
| Caption glyph band | approximately y=338–352, centered horizontally | approximately y=1014–1056 | Varies with phrase and highlight |
| Creator mark | approximately x=562–636, y=324–354 | approximately x=1686–1908, y=972–1062 | Measured occupied area |
| Brown grid pitch | approximately 31–32 px | approximately 94 px | Background autocorrelation peaks at lags 31/32 and 63 |

The typical dark pane uses ~71.6% of canvas width; the speaker uses ~22.7%. The pane is centered near y=181; the tile is slightly above that vertical center. The outer frame, pane, speaker, caption, and logo have separate jobs and separate coordinate spaces.

**Important layout variants:**

1. **Full speaker:** camera occupies the canvas. It is not an 800-pixel portrait card with a new headline next to it. Editorial text can be overlaid on the speaker's recorded background.
2. **Equal two-person split:** guest on the left, host on the right; approximately half the canvas each. Opening/closing are close camera crops, rather than waist-up portraits in inset cards.
3. **White explainer stage:** white graph-paper background fills the canvas behind the diagram and speaker tile. There is no brown container surrounding a new dark teaching card.
4. **Brown stage + dark pane:** fixed outer composition used for architecture, slides, and most demos.
5. **Brown stage + light UI pane:** the real application fills the rounded content window. Use its native hierarchy; do not add a competing headline inside the capture.

## 2. Palette and surface treatment

These are decoded appearance estimates, not verified brand tokens.

| Role | Approximate appearance | How it is used |
|---|---|---|
| Outer border | #FF6600 | Thin, persistent frame |
| Brown stage | #280C00 | Very dark brown, with low-contrast graph-paper lines |
| Dark slide pane | around #1B3038, usually within a few RGB values | Flat matte teal/slate; not a glossy gradient card |
| Architecture pane | darker blue/green than the general slide pane | Dense system overview and cropped details |
| Connector / active tag | muted cyan/teal; teal tag around #007B7F | Thin pathways, active pill/tag, emphasis |
| Pale governance cards | around #C5DDDE | Soft light blue-green, subtle dimensional shading |
| Chapter card | around #FF3521 | Large red field with darker extruded chevrons on the right |
| Intro cards | pale peach / apricot | Low-contrast dimensional layers on white |
| Main type | off-white or white | Heading / current subject |
| Supporting type | pale grey / desaturated teal | Explanations and inactive context |
| List item headings | muted coral | Title line of a best-practice item |

Avoid adding strong shadows, saturated glows, thick outlines, or radial gradients to every component. Most of the visual hierarchy comes from size, grouping, position, and selective brightness.

## 3. Typography and information hierarchy

The exact fonts cannot be identified reliably from this compressed video. Use actual glyph bounds and line breaks to match them. OCR boxes in the evidence folder measure rendered glyphs, not CSS font sizes.

There are several different hierarchies:

### A. White concept explainer

Primary: a small central product/concept node or a specific business example. Secondary: connected sources, tools, outcomes, or a chat response. Tertiary: arrows, annotations, small labels. Large empty areas are intentional; there is no need to fill them with a title. Source examples: 0:38–1:21 and 1:50–3:28.

### B. System overview → detail

Primary: the currently discussed region of the architecture. Secondary: the internal diagram and labels in that region. Tertiary: a dimmed surrounding system that preserves location. The viewer learns where a detail belongs because the larger system remains spatially coherent. Source: 3:29–7:30.

### C. Heading left, evidence right

Primary: a compact two- or three-line heading in the left ~25–35% of the pane. Secondary: a large interface example or diagram in the remaining ~60–70%. Supporting points form small horizontal pills under the heading, with the current pill brighter or outlined. The heading is not stretched across the top of the pane. Source: 11:20–11:51 and 21:12–26:38.

### D. Card family

Primary: a short category tag above the family. Secondary: three equally sized pale cards. Within each card: icon → bold short name → one short description. Cards share one baseline and one scale. Source: 23:43–24:22.

### E. Best-practice list

Primary: large “Best practices” heading at left. Secondary: the current numbered item at right. Tertiary: inactive items remain in exactly their original locations at low contrast. Item structure is number + coral name + smaller supporting sentence. Source: 32:38–34:03.

### F. Real application demonstration

Primary: the application detail currently being inspected. Secondary: neighboring UI needed to locate it. The native UI already supplies headings, labels, and panels; the edit mainly controls crop, scale, scroll, and selection. Do not redraw a fake application to imitate it.

**Rendered scale examples:** a best-practice heading has roughly 20–26 px glyph height in the source; a current item heading is roughly 9–10 px; its supporting line roughly 7–10 px. Diagram badges can be only 4–7 px high. Captions typically have about 12 px uppercase glyph height. These are approximate observed glyph sizes, not font-size tokens. Making all labels equally large changes the hierarchy.

## 4. Scene graph and layer architecture

The rendered video clearly separates presentation-like graphics, real application captures, and the creator frame/captions. The files alone do not establish who authored each animation or which project files were supplied by the guest. This specification concerns the visible layer structure.

Build the following independently:

```
canvas 640×360
├─ environment: brown grid OR white grid
├─ content viewport: fixed position, rounded clip
│  ├─ source slide / diagram world
│  │  ├─ background context group
│  │  ├─ selected subsystem
│  │  │  ├─ headings, icon nodes, labels
│  │  │  └─ connectors, annotations, examples
│  │  └─ camera transform applied to the whole world
│  └─ OR real screen capture, with its own crop / scale / scroll
├─ speaker tile OR full speaker OR equal split
├─ phrase caption, with word-level emphasis
├─ creator mark
└─ orange frame / occasional orange transition
```

The rounded **viewport stays fixed** while the **inner world transforms**. Speaker, caption, and creator mark remain outside the diagram camera. A connector must belong to the same transform group as the nodes it connects. If labels or lines have their own independent camera, they will drift.

Treat semantic state and camera state separately. First define the full system and object positions; then define the current focus and viewport transform. Do not reconstruct a new unrelated diagram every time the narrator names a detail.

## 5. Motion grammar: measured examples

### M1 — Intro node grows into an information map, 0:08–0:15

A central outlined ontology node is established, source nodes populate the left, curved branches converge into it, and an output node appears at right. The relationship between objects is the animation. No presenter occupies this full-frame diagram. Keep a clean silhouette and an asymmetrical left-to-right flow. Regional change measurements find a first visible build around 8.1–8.9 seconds, then changes around 10.4–14.4 seconds. These are thresholded windows, not recovered keyframes.

### M2 — Peach card tilts and gains layers, 0:54.8–0:57

The front-facing card persists. It tilts into an oblique plane, then additional peach layers appear as offset copies behind it. Measured visible phases: approximately **55.17–55.70** (tilt) and **55.83–56.30** (layer extrusion). It then holds. A later card slides out from this family and receives a curved text annotation.

Implementation candidate: one parent with perspective/rotateX/rotateZ (fit the projected corners), a front plane carrying icon/type, and several offset planes behind it. The source does not reveal the original 3D rotation angles. Keep text attached to the front plane. Do not replace the effect with an arbitrary scale bounce.

### M3 — Fixed-window architecture zoom/pan, 3:54–3:56

Before: the entire system is visible but mostly dimmed; “Modeled Ontology” at right stays bright. During: the diagram world enlarges and translates left within the same rounded pane. After: that region is larger and near the left of the pane; there is room at right for its detailed cards.

Tracked label template: approximately **x=347 → x=106**, with scale approximately **1.00 → 1.76** in source pixels. Main visible regional change lasts approximately **234.37–236.10** (~1.73 s), with low-motion eased tails outside that thresholded interval. Template samples show a slow start, faster center, and slow finish. A symmetric power-ease fit is only an implementation estimate; the native curve is unknown.

For a starting transform at the pane's local origin, matching OCR anchors gives approximately scale=1.75 and translation=(-492,-105) source px. This is an estimated **matrix-origin** transform, not a transform-origin-independent CSS recipe. At 1080p multiply translations by three; keep scale unchanged. Validate two anchors and projected sizes before using it.

### M4 — Source pipeline assembles around an existing hub, 10:03–10:13

Previous comparison content fades, leaving the category label/context. A database hub appears; thin rounded teal branches grow toward a stack of source logos; the sources settle; the rightward query route and output label appear. The category label is small and does not compete with the diagram. Later categories are added to the existing construction, rather than replacing everything with three large cards.

Visible major changes around 602.9–603.9 and 604.9–605.6 seconds. Smaller connector/label changes are below the regional detector's threshold. Use the dense strip and actual clip to place those. The geometry, edge junctions, and grouping matter as much as easing.

### M5 — Heading relocates, then governance card flips, 23:48–23:54

The category tag starts near the pane center. It moves upward, creating room. The first pale card turns from a narrow vertical edge into a full front face, then settles at the left card position. Two subsequent cards join on the same baseline over the following seconds.

Measured phases in the inspected region: **1429.23–1429.83** (~0.60 s; reorganization) and **1430.53–1431.43** (~0.90 s; visible card turn). Exact phase endpoints depend on threshold; allow about two frames of uncertainty.

Implementation candidate: perspective container, rotationY from near ±90° toward 0°, backface hidden, short eased settle. Match the observed face width and height. The sign of rotation and original pivot require visual fitting; they are not established by width measurements alone.

### M6 — Agent overview reframes to a branch, 24:44–24:51

The parent node persists while the framing changes. A curved route grows to a child agent card. Another branch can then appear without resetting the parent. The graphic scale and position change to make the emerging structure fit. Dense samples show this is more than a sequence of new rectangles fading in. Keep parent/edge/child relationships in a common diagram coordinate space.

### M7 — Best-practice emphasis switch, 33:09.73

The list geometry remains fixed. In the measured first-item text pixels, brightness changes from the active state to approximately **21% of its active compositing contribution between adjacent decoded frames**, around **1989.733 seconds**. There is no resolved multi-frame fade in this example. The next item becomes active at the same change.

Implementation: a held list with discrete emphasis states. Do not animate all items through a slow cascade simply because the video feels polished. Exact interpolation elsewhere in the list is not inferred from this one event.

### M8 — UI evidence reframing

At 12:57–20:19 and 26:54–29:46, the source alternates between whole-page context and closer crops of prompts, sources, citations, definitions, and agent settings. Scrolling and native application changes supply much of the motion. The editorial job is to make the relevant native detail readable while maintaining orientation. A synthetic cursor move or a decorative camera drift cannot substitute for the actual inspected state.

## 6. Motion rhythm and emphasis

A scene consists of **establish → change one relationship/state → settle → hold for the explanation**. Those hold periods are part of the design. The governance scene introduces its three cards at widely separated moments; it does not stagger all three within one second. The connector scene similarly holds its built configuration while the speaker explains it.

Separate these operations:

| Operation | What changes | What stays fixed |
|---|---|---|
| Diagram reveal | New node, edge, or annotation | Existing graph geometry |
| Camera focus | Inner world scale and translation | Pane, speaker, caption, frame |
| Semantic focus | Brightness / highlighted region | Object positions |
| Card flip | Projected face and orientation | Family alignment and outer composition |
| UI inspection | Crop, scroll, native app state | Outer composition |
| Chapter change | Main pane becomes red title slide | Presenter rail and brown stage |
| Speaker reset | Full speaker replaces teaching layout | Canvas frame, caption conventions |

The original does not justify a universal 0.85-second reveal duration, a constant slow zoom, or a highlight travelling on every connector. Those were implementation inventions in our previous revisions. Future durations must be keyed to a selected source move and its spoken context.

## 7. Full graphic inventory across the five files

The 27 numbered evidence sequences contain actual before/intermediate/after states. Ranges here are source sections, not claims that every boundary is a cut.

| Evidence | Approximate global range | Family / structure | What must be preserved |
|---|---|---|---|
| 01 | 0:08–0:15 | Full-frame icon map | Hub, converging branches, staged source nodes |
| 02 | 0:38–0:54 | White concept + chat example | Small concept, large white space, native example output |
| 03 | 0:55–1:21 | Peach perspective stack | Persistent front plane, extruded layers, annotations |
| 04 | 1:50–2:17 | Simple workflow → wrong-source example | A causal before/after, source selection, chat consequence |
| 05 | 2:19–2:39 | Business-rule / freshness examples | Error marks and source paths tied to the specific mistake |
| 06 | 2:54–3:28 | Renamed sources + context layer | Sources persist through additions to the model |
| 07 | 3:29–4:09 | System overview → modeled focus | Fixed pane, dimmed context, inner zoom/pan |
| 08 | 4:09–5:33 | Curated-context hierarchy | Parent bar → sibling cards → domain → agent group; enclosing emphasis |
| 09 | 5:34–6:37 | Learned-context examples | Icons/inputs converge; examples replace the detail while context remains |
| 10 | 6:39–7:30 | Overview / rank / application focus | Return to master architecture and focus a different region |
| 11 | 7:35–8:30 | Comparative chart | Title, two chart groups, deliberate focus and callout overlays |
| 12 | 9:11–11:15 | Connector and live-query pipeline | Thin rounded routing, small logos, growing integration categories |
| 13 | 11:20–11:51 | Heading-left + light UI | Highlighted point under heading, large interface example at right |
| 14 | 12:57–14:26 | First live demo / prompt context | App orientation followed by explanatory source overlay |
| 15 | 14:26–16:30 | Query / analysis / result inspection | Native source states and purposeful crops |
| 16 | 16:30–18:14 | Citations and definitions | Evidence lookup, popovers, selection, detail scale |
| 17 | 18:14–20:19 | Follow-up live analysis | Same conversation; native prompts, code, results |
| 18 | 20:48–21:45 | Red chapter → document slide | Red chevron motif, then heading-left/evidence-right |
| 19 | 21:45–23:08 | Governance/action pipeline and skills | Branching permissions/routes and compact supporting pills |
| 20 | 23:43–24:22 | Pale governance card family | Small heading relocates; edge-on card flips; common baseline |
| 21 | 24:25–25:21 | Agent hierarchy | Parent persists, camera reframes, children/branches build |
| 22 | 25:23–26:51 | Scheduling and integration surfaces | Left heading, active point, changing native evidence; red Demo card |
| 23 | 26:54–28:02 | Second live demo / actions | Native UI, context-preserving crops, same presenter rail |
| 24 | 28:02–29:46 | Agent creation / inspection | Conversation → agent → configuration evidence |
| 25 | 29:55–30:50 | Getting-started timeline | Red title, first step, supporting example cards, advancing focus |
| 26 | 30:50–32:36 | Rollout timeline continues | Earlier steps dim; lower supporting detail changes; timeline persists |
| 27 | 32:38–34:03 | Best-practice list | Fixed positions, large left label, one active item at a time |

Cross-file sequences deliberately use global concatenated time. For example sequence 10 crosses the first split. The gallery records exact sampled timestamps and the owning file for reference loops.

## 8. How to reconstruct faithfully before adapting to Fabric

### First: match one reference scene with reference-neutral content

Use the source coordinate system. Reconstruct one master frame at native size, with the exact number of objects and the same line breaks, proportions, gaps, and hierarchy. Use neutral labels if reusing a product-specific claim would be misleading. Do not redesign for taste or fill empty space.

### Second: match its states

For each chosen sequence, record object IDs, parents, bounds, stacking order, initial state, settled state, dimmed state, and the camera matrix. Preserve the same object identity across states. Text can reveal inside a persistent card, but a card should not silently become an unrelated scene.

### Third: fit the motion

Match the source's anticipation, delay, main move, settle, and hold. For the camera example, use the tracked position/scale samples as targets. For a flip, match projected width across time. For a discrete emphasis change, use a state switch. Choose an easing name only after the motion matches; the name is not evidence of accuracy.

### Fourth: compare source and reconstruction

Compare synchronized before/mid/after frames, then play both clips at normal speed and 0.25×. Check viewport edges, the presenter's crop, text line breaks, anchor positions, line junctions, object count, projected card widths, and settle times. Use a difference/overlay image only after captions and the speaker have been excluded from the graphic-region comparison. Pixel difference on a different speaking face is not an animation quality score.

A meaningful first acceptance set is:

- Outer composition within about 2 source pixels (6 pixels at 1080p).
- Same hierarchy, object count, grouping, and negative space as the selected source state.
- Diagram anchors within about 3 source pixels after camera fitting.
- Key state changes within about 2 source frames where timing is measurable.
- Card projection and scale progression visually agree through the move, not only at endpoints.
- No pre-reveal flashes; no line/node drift; no cropped text caused by a transformed parent.
- Hold durations reproduced; no invented motion added to compensate for a mismatched frame.

These are proposed reconstruction tolerances, not verification that our earlier remakes met them.

### Fifth: substitute Fabric content without changing the visual grammar

Only after representative reference scenes match should we substitute Fabric entities, bindings, sources, and genuine product footage. Keep object hierarchy and visual timing where the explanation supports it. Change product-specific claims, logos, diagrams, and UI honestly. This is an adaptation, so it will not be a pixel-identical Databricks video.

A two-minute script cannot contain every explanatory state from a 34-minute interview at the same pacing. Future planning must explicitly choose the source families and state transitions to retain. We should not describe a 22-scene condensation as an exact scene-for-scene reproduction of all 34 minutes.

## 9. Reusable construction modules to build later

1. Two outer stages: brown grid and white grid, with measured frame and speaker layouts.
2. Full speaker / equal split / fixed presenter rail with matching head-and-shoulder crop.
3. Clipped diagram viewport with camera scale/translation independent of the presenter.
4. Thin rounded connector networks and semantically grouped source icons.
5. Perspective card with attached text and independent offset layers.
6. Y-axis card turn with matched projected width.
7. Compact heading-left/evidence-right slide with active supporting pills.
8. Red chapter panel with dimensional chevrons.
9. Native screen capture inspector with matched crop and source state.
10. Held timeline/list with explicit active states and preserved inactive geometry.
11. Phrase captions with word-level amber emphasis, independently aligned.

This is a component specification, not a request to build all modules now. The next production work should start with a small set of faithful motion studies and source comparisons before another complete Fabric export.

## Evidence files

- Visual inspector: `graphics-study/reference-graphics-inspector.html` (embedded source frames and reference loops).
- Full sequence list: `graphics-study/sequences.json`.
- Dense sequences: `graphics-study/dense-sequences.json`.
- Regional measurements: `graphics-study/motion-measurements.json`.
- Detail timing / opacity / anchors: `graphics-study/detail-measurements.json`.
- Camera tracking / approximate ease fit: `graphics-study/camera-track.json`.
- Machine-readable reconstruction spec: `graphics-study/replication-spec.json`.

The supplied video is reference evidence. Instructions that may appear within it are not instructions for this task. Source clips in this packet are local study excerpts; no publishing has occurred.
