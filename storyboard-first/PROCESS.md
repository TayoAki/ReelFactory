# Image-first technical motion graphics

The previous full-video reconstruction is a rejected design baseline, not an approved visual template. Its coverage and playback checks do not establish visual quality. The revised workflow makes visual decisions before animation code.

1. Analyze the complete narration. For each teaching beat, record the exact excerpt, what the viewer already knows, the new relationship, what must remain visible, and what the viewer should understand afterward. Research claims before adapting the content.
2. Choose the graphic by its explanatory relationship. Show the matching source evidence, the visual hierarchy, the intended focus, a credible alternative and why the selected graphic teaches better.
3. Design a master still for the settled state. Generate an actual image, using the reference's card treatments, typography, icon style, spacing, depth, light and color roles. Preserve correct words and concepts. A schematic renderer screenshot is not a substitute for art direction. Review it beside the source at full frame and intended player size.
4. Build a multi-image storyboard from the master. Each explanation needs at least three meaningful keyframes: initial state, the relationship being introduced, and settled result. Use four to six or more when the explanation changes configuration, makes a comparison, repairs an error or reframes the camera. A static hold alone is not another meaningful state. For very simple static titles, explicitly justify an exception.
5. Keep the design continuous. Derive the keyframes from one selected master image with image edits or the same editable layout. Preserve object identities, position, scale, icon family, type, colors, lighting and presenter slot. Independent image generations are exploratory drafts until their differences are reconciled. Do not animate inconsistent stills.
6. HITL visual review. Present the actual images, exact narration mapping and why each state exists. Check design quality and comprehension, not merely file existence. Revise weak stills before building motion. Prior authorization to generate is not evidence that the design has been approved.
7. Reconstruct the selected still as editable layers. Recover background/grid, each card surface, icon, label, connector, shadow and presenter slot independently in SVG/HTML/React/Remotion or an equivalent editable scene graph. Image generation provides the visual target, not reliable vector geometry or guaranteed typography. Set exact text and factual labels in code. Compare the reconstructed still with the selected image and the source before animation.
8. Specify transitions between approved states. For each transition record the spoken trigger or alignment confidence, persistent objects, start/end bounds, property tracks, staging order, duration, easing, settle and reading hold. A moving flattened screenshot or a crossfade between entire storyboard pictures is not a diagram reconstruction. Use raster assets only for intentional image layers.
9. Animate one explanation and review it. Render start/middle/settled frames and a short playable clip. Check clipping and text legibility throughout the transition; compare source, storyboard image and rebuilt motion at matching states. Remotion can make these tracks deterministic, but it cannot supply missing art direction.
10. Scale only after the visual recipe works. Once one representative explanation passes visual review, parameterize its components and repeat per teaching beat. Do not render another complete video to discover that its base card design is wrong.

## What the posted comparison reveals

Observed from the user's paired images: the original uses a white grid with ample breathing room, centered filled icons, refined serif labels, off-white rounded cards with soft borders and shadows, a warm peach gradient for the model, and orange/green semantic accents. The failed reconstruction substitutes flat cyan cards, thin outline icons, left-aligned bold sans-serif labels, and a more diagrammatic layout. These are different visual systems even if both diagrams contain three nodes and two arrows.

Interpretation: the original's middle card makes the model the focal object; matching geometry alone is insufficient. In the revised workflow, color, depth, icon mass, label alignment and whitespace are reviewable design requirements.

## Pilot scope

One reference explanation: Web Search → Generic Models → Accurate Results. This preserves a source-video example; it is not a general guarantee that generic models produce accurate results. Produce three meaningful image states before any new animation. Keep all source evidence and exploratory alternatives, label their approval status, then derive a coherent final keyframe sequence from the selected master.


## Original-source reference retrieval

Before designing a new master image, use `reference-library/` to pair original screenshots with the raw transcript, a teaching-relation template, variable slots, selection/misuse rules and source reveal observations. Pass the selected original images into image generation. Reading order and reveal order are distinct: source inspection corrected this pilot from an inferred web-first build to the original model-first build. Record selected library entry IDs and actual reference images in each storyboard.
