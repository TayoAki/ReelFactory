# All storyboard graphics — comparison and reusable rules

**Coverage:** all 12 scenes of the current 46-second storyboard. The full reference is catalogued in 27 source sequences; the other source sequences have not been newly reconstructed in this pass.

A fresh render reuses and adjusts the editable V1/GSAP reconstruction. This is not a Remotion migration or pixel-exact recreation. Static fictional presenter images are intentional placeholders. The source sample numbers and chat are illustrative.

## Scene 01 — presenter-to-product

**Spoken excerpt:** So I come from the Genie One world.

**Teaching purpose:** Identify the product the guest is discussing.

**Why selected:** Presenter establishes context; the single card creates a stable referent for the next sentence.

**Better alternative / tradeoff:** Open on a full-screen product UI. That is useful for an original explainer, but starts at a detail level the reference has not introduced.

**Original:** The source changes from speaker to white stage, then grows the card.

**Generated:** Opening card growth was retimed after inspecting 39.2–41.5s source samples; presenter remains a static placeholder.

**Remaining difference:** Transition timing is still approximate; the card mark, font and caption grouping differ.

**Reusable rule:** Establish the stage before introducing the referent. Align visible events from frames, not just the product-name timestamp.

[Three-state comparison and motion](generated/scene-01/comparison.mp4) · [Graphic keyframe](generated/scene-01/graphic.png)

## Scene 02 — product-definition

**Spoken excerpt:** Genie One is our AI co-worker for business users.

**Teaching purpose:** Know the intended audience and basic role.

**Why selected:** This sentence defines an audience. A stable labelled card supports that distinction without implying a mechanism.

**Better alternative / tradeoff:** A business-person icon beside a chat window makes the role more concrete; reserve that for an approved adaptation because the reference uses the product card.

**Original:** One named product and a short audience subtitle establish the role.

**Generated:** The generated scene uses the same single-card hierarchy.

**Remaining difference:** The subtitle is present on the card rather than following a separately certified source reveal; typography remains approximate.

**Reusable rule:** Definition needs one stable referent and one meaningful qualifier, not an early architecture diagram.

[Three-state comparison and motion](generated/scene-02/comparison.mp4) · [Graphic keyframe](generated/scene-02/graphic.png)

## Scene 03 — data-tools-connections

**Spoken excerpt:** It connects to your data and tools.

**Teaching purpose:** Understand that the product can use data and connected tools.

**Why selected:** Keeping the product preserves continuity while the two new endpoints explain the added relationship.

**Better alternative / tradeoff:** Show real connector settings. More concrete, but too much UI detail for this approximately 2.4-second sentence.

**Original:** The source shrinks the card and adds database/tool symbols with bidirectional arrowheads.

**Generated:** The revised scene retains the product, restores the tool glyph and adds arrowheads at both ends of the source-style connections.

**Remaining difference:** Generic database/tool silhouettes and exact endpoint positions still differ. Proposed Data/Tools text labels are not shown in the reference-style render.

**Reusable rule:** Connection, flow and dependency are different meanings. Record connector semantics and flag plan/render label omissions.

[Three-state comparison and motion](generated/scene-03/comparison.mp4) · [Graphic keyframe](generated/scene-03/graphic.png)

## Scene 04 — question-to-answer

**Spoken excerpt:** It answers questions about your business.

**Teaching purpose:** See what a business question and a useful answer look like.

**Why selected:** A question and answer demonstrate the capability more clearly than abstract boxes labelled “Question” and “Answer.”

**Better alternative / tradeoff:** An official UI capture is more authentic for a product tutorial, but a different capture would change this reconstruction and require an appropriate matching example.

**Original:** The source replaces the diagram with a large illustrative chat and returned product totals.

**Generated:** The revised chat preserves the question and illustration values; results reach readable opacity sooner, and the action is revealed without moving its baseline.

**Remaining difference:** Query typing, answer reveal timing, bubbles and glyphs are approximate; results can still be entering at the end of this short beat.

**Reusable rule:** When a capability needs proof by example, preserve the same question, evidence and output rather than generic answer boxes.

[Three-state comparison and motion](generated/scene-04/comparison.mp4) · [Graphic keyframe](generated/scene-04/graphic.png)

## Scene 05 — answer-to-action

**Spoken excerpt:** It acts on the answers that it gives you

**Teaching purpose:** Recognize an action that builds on the returned insight.

**Why selected:** Retaining the answer makes the consequence clear: the action uses the result instead of starting an unrelated task.

**Better alternative / tradeoff:** Show a completed campaign or tool execution. Reject for this scene: it would claim a result the reference illustration does not establish.

**Original:** An action suggestion appears under the retained answer.

**Generated:** The generated action stays attached to the product totals.

**Remaining difference:** The source action reveal and caption phrase timing are not frame-exact; no actual campaign execution is depicted.

**Reusable rule:** Show action status explicitly. A suggestion, request, confirmation and completed operation are distinct visual states.

[Three-state comparison and motion](generated/scene-05/comparison.mp4) · [Graphic keyframe](generated/scene-05/graphic.png)

## Scene 06 — governance-enclosure

**Spoken excerpt:** all within the governance framework that you already have.

**Teaching purpose:** Understand that existing access controls still apply.

**Why selected:** The boundary adds one constraint to a mechanism the viewer already understands. It preserves visual continuity.

**Better alternative / tradeoff:** Show two users with different permissions and allowed/denied records. This explains governance better in a standalone tutorial, but needs a separate beat and should not be squeezed into this reconstruction.

**Original:** The same chat shrinks into a green governance enclosure with a shield.

**Generated:** The generated enclosure retains the chat and now uses a sourced shield-lock icon.

**Remaining difference:** Boundary position/radius, shield design and exact shrink/draw timing differ; this is a shorthand for governance.

**Reusable rule:** Add a constraint to the mechanism already understood. Use a separate permission example if the access model itself is the lesson.

[Three-state comparison and motion](generated/scene-06/comparison.mp4) · [Graphic keyframe](generated/scene-06/graphic.png)

## Scene 07 — card-to-family

**Spoken excerpt:** But Genie One sits in a larger stack of AI co-workers and other AI tools on Databricks. So, for example,

**Teaching purpose:** Place the known product within a broader product family.

**Why selected:** The known object changes into a family metaphor. This matches the reference and prepares the comparison.

**Better alternative / tradeoff:** Flat product-family header with three equal cards. It is less likely to imply a technical stack, but departs from the reference and reveals products ahead of the narration.

**Original:** The known product tilts, layers extrude, then the graphic holds.

**Generated:** The revised scene uses explicit SVG plane matrices: a 110px flat card tilts, five backplates expand, then the front card separates from the stationary stack.

**Remaining difference:** Geometry is estimated from decoded source samples. Texture, tiny spacing and exact source easing remain approximate; text no longer animates its font size during the tilt.

**Reusable rule:** Treat plane change, extrusion and hold as distinct states. Check readability after transforms, not only in flat assets.

[Three-state comparison and motion](generated/scene-07/comparison.mp4) · [Graphic keyframe](generated/scene-07/graphic.png)

## Scene 08 — audience-annotation

**Spoken excerpt:** if Genie One is our agent for business users,

**Teaching purpose:** Recall the first role before contrasting it with another.

**Why selected:** The annotation makes the comparison criterion explicit before the next product is introduced.

**Better alternative / tradeoff:** Use a two-column audience table. Good for a summary, but premature before the second role is named.

**Original:** A curved annotation identifies the business audience above the central card.

**Generated:** The generated label anchors to the known product without replacing the family.

**Remaining difference:** Leader shape, endpoint and label spacing differ from source.

**Reusable rule:** Annotate the comparison criterion before introducing the contrasting role. A leader is not a data-flow arrow.

[Three-state comparison and motion](generated/scene-08/comparison.mp4) · [Graphic keyframe](generated/scene-08/graphic.png)

## Scene 09 — technical-role

**Spoken excerpt:** Genie Code is our agent for technical users. It helps them write code and do other work within the lakehouse.

**Teaching purpose:** Distinguish a technical-work product by audience and activity.

**Why selected:** Sibling position communicates product-family membership; the words explain the meaningful distinction.

**Better alternative / tradeoff:** Show a notebook or code-editing demo. Better for demonstrating the workflow, but a new demo would interrupt the family comparison; propose it for a later dedicated beat.

**Original:** Genie Code appears left of the central Genie One card with a technical-work note below.

**Generated:** The revised peer cards emerge from beneath the front card, with fixed serif text metrics and darker role labels. Their hierarchy follows the source.

**Remaining difference:** Card shapes, overlap and source font are approximate; no notebook demo is inserted into this family beat.

**Reusable rule:** Use position for sibling status and text for role differences. Equal category is not delegation or ownership.

[Three-state comparison and motion](generated/scene-09/comparison.mp4) · [Graphic keyframe](generated/scene-09/graphic.png)

## Scene 10 — shared-access

**Spoken excerpt:** We also have Genie Agents, which can be accessed by both types of users.

**Teaching purpose:** Introduce the domain specialist and distinguish access from role.

**Why selected:** This completes the family without resetting the scene. Shared access is stated separately from specialization.

**Better alternative / tradeoff:** Draw two audience lanes converging on Agents. It makes access clearer, but introduces another diagram in the middle of the reference family layout.

**Original:** Genie Agents completes the family on the right, with both audiences identified.

**Generated:** The generated third card preserves the central anchor and left/right role arrangement.

**Remaining difference:** Card subtitle wrapping, exact reveal and perspective are approximate.

**Reusable rule:** Distinguish shared audience from specialist function; do not invent call routes among peer products.

[Three-state comparison and motion](generated/scene-10/comparison.mp4) · [Graphic keyframe](generated/scene-10/graphic.png)

## Scene 11 — domain-specialization

**Spoken excerpt:** And they're really focused on domain-specific work. They're essentially domain experts.

**Teaching purpose:** Understand specialization as curated business context.

**Why selected:** The additional label explains the third product’s distinction while the first two remain visible for comparison.

**Better alternative / tradeoff:** Zoom into a Sales agent with curated tables, definitions and example questions. More concrete and educational, but needs extra screen time and a separately approved scene.

**Original:** The third product receives a curved domain-specific-work annotation.

**Generated:** The generated annotation adds the specialist role while retaining all products.

**Remaining difference:** The revised annotation stays on one line as in the source. Its exact position, curve and reveal remain approximate.

**Reusable rule:** The role should be named. A robot or brain would add imagery without explaining the domain constraint.

[Three-state comparison and motion](generated/scene-11/comparison.mp4) · [Graphic keyframe](generated/scene-11/graphic.png)

## Scene 12 — speaker-return

**Spoken excerpt:** And I can actually cover that in more depth if we want to.

**Teaching purpose:** Recognize a conversational handoff rather than a new concept.

**Why selected:** The speaker is offering elaboration. A new diagram would introduce information the narration does not teach.

**Better alternative / tradeoff:** Hold the family diagram. It is economical but misses the reference’s conversational cut.

**Original:** The source cuts back to the speaker rather than introducing another concept.

**Generated:** The generated scene uses the requested full-frame static fictional presenter.

**Remaining difference:** Person, background and natural movement intentionally differ; cut/caption timing is approximate.

**Reusable rule:** A no-new-graphic beat is part of the template library. Do not force a diagram onto conversational handoffs.

[Three-state comparison and motion](generated/scene-12/comparison.mp4) · [Graphic keyframe](generated/scene-12/graphic.png)

