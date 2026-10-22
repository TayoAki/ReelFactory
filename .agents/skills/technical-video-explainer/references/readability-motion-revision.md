# Graphics refinement: original vs previous vs revised

The revision covers the same 46-second, 12-scene passage. The original was examined through existing dense tilt samples, new matched frames, projected-text checks and 6fps caption observations. No claim of pixel-exact reproduction is made.

| Problem in the previous render | What changed | Why it matters |
|---|---|---|
| Tool icon disappeared under global fill/stroke CSS | Separate rules for stroked tool and filled database icons; check final rendered endpoint | An existing SVG element is not evidence of a visible icon |
| Connection routes lacked arrowheads | Explicit native SVG markers | The graphic now reproduces the source's connection notation |
| Whole-family transform moved things together | Separate SVG groups for backplates, front card and peers | Persistent objects retain the source's distinct motion roles |
| Font-size changes and doubled italics distorted card text | Normal serif type with fixed metrics inside explicit plane matrices | Letterforms remain coherent throughout the tilt |
| Peer cards drifted/faded in | Cards emerge from underneath the front card into their final positions | Motion now explains membership in the family |
| Small low-contrast role text | Darker role text with fixed design-space size and projected-text checks | Foreground/background separation improves without adding labels |
| Thin hollow captions, rough ASR phrasing | Filled bold font, stronger outline, 33 source-derived phrase blocks | Captions are easier to read and closer to the original phrase rhythm |
| Domain annotation wrapped across lines | Single-line annotation near its source location | The secondary label reads as one annotation, not a new paragraph |

Role-text design-color contrast against gradient endpoints: previous minimum **4.03:1**, revised minimum **7.40:1**. This calculation does not certify real-world readability. The rendered glyph size, overlap, reading duration and actual player scale also matter.

Caption phrase timing was interpreted from source samples at 6fps, with normalized wording. Orange-highlight positions inform emphasis where measurable; presenter-only shots use approximate stepping. This is an improvement over the earlier ASR grouping, not word-perfect synchronization.

Remaining differences: static fictional presenter, approximate Genie vector and fonts, surface texture, source easing and some reveal timing. The review lets the viewer switch between previous and revised versions while the original remains on the left.
