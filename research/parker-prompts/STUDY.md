# Parker Prompts → a better ReelFactory production method

Channel: https://www.youtube.com/@parkerprompts/videos

## What was actually studied

ScrapeCreators supplied the latest and popular upload pages, video metadata, and timestamped transcripts for four selected videos. These are bounded pages, not an exhaustive channel audit. View counts below are retrieval snapshots, not proof that a particular edit caused performance.

| Selected video | Retrieved views | Evidence available |
|---|---:|---|
| [How the Top 1% Make Cinematic AI Videos (FREE System)](https://www.youtube.com/watch?v=LIK6ZayNndU) | 17,052 | Full playable 15-minute reference obtained through Firecrawl's YouTube provider; manually inspected 16 opening samples, 30 full-video samples and 16 workflow-detail samples, plus timestamped transcript |
| [Claude Opus 5 + Higgsfield AI = EASY AI Motion Graphics](https://www.youtube.com/watch?v=8_pawKQCvpk) | 51,453 | Timestamped transcript and metadata; footage provider returned 502, so no visual claims attributed to this video |
| [FREE Claude Prompt That Creates AI Videos AUTOMATICALLY!](https://www.youtube.com/watch?v=7bE0PCee01Y) | 38,406 | Timestamped transcript and metadata; footage provider returned 502, so no visual claims attributed to this video |
| [How to Use Notebooklm Better than 99% of People](https://www.youtube.com/watch?v=SogSf-1p9t4) | 375,857 | Timestamped transcript and metadata; footage provider returned 502, so no visual claims attributed to this video |

Visual evidence: `LIK6ZayNndU/review/opening.jpg`  , `whole.jpg` and `workflow-detail.jpg`. Exact sampled times are shown on those sheets. Opening cut candidates were detected from reduced-resolution frames; score changes are not certified semantic cut boundaries. No exhaustive human frame-by-frame review, full audio-stem analysis, or precise presenter screen-share measurement is claimed.

## The important correction to our earlier drafts

The earlier drafts were valid sourced explainers, but repeated resized documentation cards with frequent camera resets. The image changed without the explanation progressing. Too much screen area stayed empty, evidence text was small, and the result did not establish a strong reason to keep watching.

The sampled Parker tutorial is more deliberate. It alternates a presenter, a short process graphic, finished creative output, working application views, highlighted prompt text, reference sheets, and an assessment of the result. A screen can remain on the same application while the meaningful detail changes. A constant one-second cut rule would miss this mechanism.

## Observed visual sequence: cinematic tutorial

Ranges are approximate semantic sections supported by samples and transcript, not frame-exact cut in/out points.

| Time / anchor | What is visible or said | Transferable mechanism |
|---|---|---|
| 0–5.5 s | Presenter at desk establishes the problem: fine-looking AI video that does not feel cinematic | Start with a recognizable failure and a specific promised improvement |
| ~5.5–13.8 s | Three purple step pills appear; an example is framed on the same purple ground | Compress the process into a visible mental model |
| ~14–44 s | A substantially uninterrupted finished anime-film preview, with multiple camera angles and dialogue | Demonstrate that the promised output exists before a long setup sequence |
| ~44–75 s | Presenter and recurring purple product/tool graphics introduce the two-tool workflow | Explain the system after the viewer has seen why it matters |
| ~75–140 s | Application/connector setup, with a small circular presenter inset; consistent purple framing | Let the actual application occupy most of the picture; preserve orientation |
| ~140–240 s | Prompt and template passages are enlarged or highlighted inside a consistent frame | Direct attention to the exact setting being explained, not an entire page at unreadable size |
| ~240–315 s | Character reference sheets and prompts; identity is established before film generation | Lock reusable visual references before expensive or complicated production |
| ~315–350 s | Timestamped shot prompt, with explicit framing and camera instructions | Give each shot a purpose, composition and action before rendering |
| ~350–400 s | Finished realistic-film excerpt | Return to the artifact immediately after the build sequence |
| ~400–460 s | Presenter interprets the result, then introduces the next style | Close the loop with evaluation rather than calling every result perfect |
| ~460–630 s | Anime reference sheets → prompt → generated film → commentary | Reuse the system; change one substantial variable at a time |
| ~630–790 s | Cartoon setup and character sheets → film → commentary | Escalate or vary the examples without reteaching the setup |
| ~790–899 s | Black-and-white character sheets and noir output | Stress-test the workflow with a more constrained visual style |

The consistent purple frame is an observed production choice. We borrow consistency, evidence hierarchy and attention control; we do not copy the creator's face, voice, exact brand treatment, proprietary prompt kit or creative films.

## Explicit methods from the transcripts

1. **A visual reference is a contract.** In the cinematic tutorial at ~3:18, reference-sheet templates establish character identity before scene generation. At ~4:57, the narrator asks for seven shots, each with camera movement, then specifies framing, field of view, motion and dialogue. For technical videos, the equivalent contract is a fixed dataset, color mapping, typography, value formatting, chart scale and recurring layout.
2. **Change one thing at a time.** The motion-graphics transcript at ~1:02 describes approving still images before animating them. At ~2:49–2:55, its prompt first locks everything that must stay fixed and only then names the one thing that changes. Our charts should change the filter, highlight, comparison or camera target deliberately; they should not randomly change grade and crop at every cut.
3. **Separate decisions from expensive generation.** The automatic-video transcript at ~1:29 describes eight stages. At ~3:07–3:09, it explains why an incorrect high-resolution render costs more. We can apply this by checking a shot plan and representative frames before a full local render. These are production checks, not a new user approval requirement for already-authorized reversible work.
4. **Plan continuity.** At ~4:13–4:15 in the automatic-video transcript, one generated part ends mid-action and the next begins with a match cut on that action. Our equivalent is carrying the same chart, colors and data identity through a filter change so the viewer does not need to reorient.
5. **Show validation as part of the workflow.** The NotebookLM transcript at ~0:49 recommends a focused topic; at ~3:16–3:35 it moves to source validation before topic questions. Our video should show what the data actually covers and retain a reproducible query, rather than implying that an attractive chart proves an unperformed Fabric run.

Creator statements about vendor models, pricing, limits and UI paths are source claims, not independently verified current product documentation. We do not need those services to implement the technical data-graphic pilot, and no Higgsfield connection or generation is claimed.

## The new production rules

| Earlier draft behavior | New rule | Acceptance check |
|---|---|---|
| Narration introduces the topic while a source card sits in the middle | Show the real result immediately | First scene contains an actual computed result, not only a title |
| The same screenshot flips between two crops | Every scene changes the information state | The shot list names the new finding, action or comparison |
| Most of the evidence is too small for a phone | Let data graphics use the frame | Primary number ≥100 px and labels ≥28 px at 1080 px wide |
| Repeated full-page quotations | Show one relevant value, query region or interaction | No long page is the primary visual for a whole explanation |
| A new image means a new orientation task | Preserve a single visual system | Fixed colors, spacing and chart positions across related scenes |
| More cuts are treated as improvement | Motion follows meaning and spoken timing | Cuts/markers follow a changed result or named value; no periodic crop swapping |
| Final render is the first real review | Inspect representative stills before rendering | Source, layout and narration checks are saved |

## Concrete pilot

`../../videos/10-nyc-parker-pilot/` is an original short vertical data story, adapting the long-form teaching mechanisms rather than copying the source's runtime or presenter layout.

The opening reveals the actual 3,963,898-request dataset and the 611,282 illegal-parking result. A continuous data-explorer treatment then carries the viewer through the date window, residential-noise hour distribution, Sunday comparison, heat seasonality and the one pigeon request. Charts are original SVG/HTML graphics driven by retained NYC Open Data responses. They are not invented product screenshots or an unperformed Fabric execution.

The V1 rendering and caption devices remain in use, with meaningful transitions replacing the earlier fixed crop cadence. Narration uses a local synthetic review voice. No copied reference footage, creator likeness, creator voice or unlicensed music is present in the pilot. The original nine drafts remain available for comparison.


## Closer Fabric revision

The user's follow-up requested closer reference treatment and Microsoft Fabric as the subject. `../../videos/11-fabric-data-agent/` is the resulting 84-second, 16:9 tutorial. It uses the observed purple framing, finished-result preview before setup, three numbered process cards, source application screens, a moving table-selection demonstration, enlarged prompts, and timed highlights while inspecting a generated query. It returns to Create → Choose → Verify at the end.

It teaches the documented Fabric data-agent workflow using Microsoft's own CC BY 4.0 screenshots and animated demonstration. It does not claim an authenticated Fabric session or copy Parker's presenter, voice or films. The review narration is synthetic. Full source, prerequisites and the distinction between Microsoft's AdventureWorks and GamingDataAgent examples are retained in the per-video PLAN.md.

A portable `../../fabric-review.html` embeds the final MP4 so that opening a downloaded copy requires no local server.
