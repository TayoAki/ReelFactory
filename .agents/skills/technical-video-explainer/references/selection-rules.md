# Choose a graphic by explanatory purpose

The evidence IDs below refer to `catalog.json`. These rules are editorial generalizations, not statistically validated learning-science claims.

| Teaching need | Graphic | Preserve / animate | Evidence | Use a different graphic when |
|---|---|---|---|---|
| Introduce one named concept | Definition card | Stable name; reveal role/audience | 02 | The audience already knows it; go straight to mechanism |
| Explain an actual connection | Compact mechanism diagram | Known hub; reveal endpoints then labelled routes | 02, 12 | Only membership matters; use a list/group |
| Make a capability concrete | Worked question → evidence → result | Same question and sample data | 02, 14–17 | The exact UI is the lesson; use authentic UI footage |
| Show insight leading to action | Result-to-action continuation | Keep result; add action and its status | 02, 19, 23 | No execution evidence exists; show a suggestion, not completion |
| Add a constraint | Boundary / permissioned route | Existing mechanism inside a labelled constraint | 02, 19 | The audience needs the permission model; show allowed/denied access explicitly |
| Distinguish related products | Product family / sibling cards | Known product; introduce peers and role annotations | 03 | Relationships are delegation or ownership; use hierarchy |
| Explain a failure | Counterexample with consequence | Question → specific mistake → visible result | 04–05 | No causal example exists; do not invent a red cross as evidence |
| Show why a fix matters | Context repair | Same source/model; add context and compare consequence | 06 | The process changes completely; use side-by-side before/after |
| Explain part of a larger system | Master/detail architecture focus | Fixed viewport; camera transforms nodes, edges and labels together | 07, 10, 21 | No master layout exists yet; establish it or use a clean section cut |
| Explain category/ownership | Hierarchy build | Parent persists; children and enclosures appear | 08, 21 | The items are merely peers; use equal cards |
| Ground an abstract category | Changing examples in fixed context | Category remains while examples change | 09 | The mechanism needs depth; choose one worked example |
| Compare measured outcomes | Chart with selective focus | Axes, units and baselines remain fixed | 11 | Numbers are unsourced or incomparable; use a qualified qualitative comparison |
| Show a feature in practice | Heading + evidence panel | Heading/points stay fixed; evidence changes with active point | 13, 18, 22 | A feature list would duplicate narration; use only the evidence |
| Verify provenance | UI evidence inspection | Answer → citation → source detail | 15–16, 24 | The citation alone answers the question; avoid unnecessary zoom |
| Introduce a new chapter | Brief chapter plate | Change topic, then orient the next content view | 18, 25 | No real section change exists |
| Enumerate peer concerns | Aligned category cards | Shared heading/baseline; one entry at a time | 20 | Tasks must happen in order; use timeline |
| Explain ordered rollout | Persistent timeline | Prior steps dim in place; active detail changes below | 25–26 | Recommendations are unordered; use fixed list |
| Summarize recommendations | Fixed emphasis list | All positions persist; active item changes | 27 | Each item needs a long example; split into separate scenes |

## Motion rules grounded in observations

- The card-to-family change has two jobs: plane change, then layer expansion. Do not replace it with an unrelated pile appearing. Source interval about 55.167–56.300s.
- Source architecture camera change is about 234.367–236.100s. Its measured estimate applies to that move, not every future zoom.
- Governance cards relocate their heading before an edge-on-to-front turn. Preserve the category while making room. Source about 1429–1432s.
- Best-practice list emphasis switches between adjacent frames around 1989.733s; do not assume every focus change fades.
- Speaker/captions stay outside inner diagram transforms. Child edges and labels share their nodes' coordinate system.
- A settled hold is a valid state. Motion is a semantic event, not an obligation on every sentence.

## What this reference cannot establish

One video does not prove these patterns are universally optimal or universally recognized. Source appearance does not prove a product capability. Reuse the teaching relationship and validate the new content separately.

## Failure cases observed during this generation pass

- Opening definition card appeared before the source introduced it. Inspecting 39.2–41.5s frames revealed a blank-stage interval followed by card growth. Rule: align a visual event to decoded frames, not solely the ASR word onset.
- Applying perspective/scale to a whole card shrank the text. Increasing all labels equally then caused an overlapping peer card to cover the technical-audience subtitle. Rule: check optical size and the visible content area of each overlapping card; one font size does not fit every role label.
- A generated green boundary used a diamond marker despite a shield being called for. Rule: validate the symbol’s meaning against the asset plan, not only its location. The final reconstruction uses the sourced shield-lock symbol.
- Source-style icon-only connections omitted the storyboard’s proposed Data/Tools labels. Rule: compare output to both the source and the approved plan; a reference match can still be a plan deviation. This omission is explicitly reported instead of silently called compliant.

## Motion and legibility revision — observed failure cases

- **Observed:** applying both italic typography and a sheared card plane doubled the slant, flattening small text. **Rule:** use normal serif text for a plane already supplying the slant; inspect the projected glyphs at delivery size.
- **Observed:** animated font-size compensation made letters grow during the card tilt. **Rule:** fix design-space text metrics and animate an explicit card plane; treat any readability adaptation as a deliberate layout choice.
- **Observed:** transforming the whole family moved the backplates with the front card. **Rule:** give the stack, front card and sibling cards separate persistent identities. In this reference the front card moves away from a stationary stack and siblings emerge from beneath it.
- **Observed:** a global `fill`/`stroke` rule erased the crossed-tool glyph. **Rule:** distinguish filled icons from stroked icons and inspect the final rendered endpoint, not just whether its SVG element exists.
- **Measured/estimated:** OCR and orange-highlight locations sampled from the source at 6fps reveal phrase boundaries earlier than the previous ASR grouping. **Rule:** for reconstruction use source-caption evidence; for new narration use newly aligned words. Sampled timing is not frame-perfect alignment.
- **Design check:** evaluate text/background contrast and fixed projected font sizes, then inspect text occlusion against overlapping peers. Bounds checks alone do not prove a label can be read.
