---
name: image-to-bouquet
description: Translate a reference image such as an album cover, artwork, poster, or photo into a physically buildable bouquet, then generate one realistic first-person handheld smartphone photo. Analyze palette, tone, structure, and texture; choose feasible flowers and wrapping with quantities and substitutes; save the design specification, exact prompt, and generated image. Use for image-to-floral reinterpretation, not ordinary flower identification or generic bouquet advice.
---

# Image to Bouquet

Turn one source image into one florist-buildable bouquet and one believable left-hand-forward smartphone photograph. This skill is self-contained: do not require or invoke another prompt, photography, or realism skill to complete the task.

The output mode is fixed. Do not ask the user to choose a style and do not create a bouquet-only product/effect image.

## Required input

Require one source image. Treat it as a **visual reference**, not an edit target. If several images are supplied, distinguish the image to translate from example results; ask which image drives the bouquet only when labels and context cannot resolve the role.

## Workflow

1. Inspect the actual source pixels. If a local image is not already visible, load it with the available image-viewing tool.
2. Analyze dominant, secondary, highlight, accent, and dark-anchor colors; temperature, saturation, contrast, value distribution, texture, negative space, direction, density, and focal hierarchy. Approximate hex values are design aids, not colorimetric claims.
3. If useful and Pillow is available, run `scripts/extract_palette.py` for measured candidates. Visually correct its output because borders, typography, skin, shadows, transparency, and compression can distort frequency.
4. Read [references/floral-translation.md](references/floral-translation.md). Translate the image's **relationships** into real flower roles, silhouette, stem direction, paper layers, and tie. Do not map every sampled color to a different flower.
5. Pass the florist-buildability gate before prompting: every flower/material has a common purchasable name, natural/dyed/painted status, quantity, visual job, sourcing risk, and feasible substitute; stems converge at a real binding point; the bouquet fits one-hand carrying; wrapping layers can fold around the stem bundle. Revise the design if it needs fictional species, unsupported flower heads, impossible colors, or structure that cannot be tied.
6. Read [references/handheld-realism.md](references/handheld-realism.md). Build the photograph from visible causes—first-person geometry, phone-lens behavior, a real location, motivated available light, natural falloff, physical contact, and small imperfections—not from generic words such as `cinematic`, `8k`, or `masterpiece`.
7. Write the bouquet specification and exact final prompt before generation. Follow [references/deliverables.md](references/deliverables.md). A normal run has exactly three final files.
8. Use the built-in image generation tool by default. Include the source image as a palette/visual-system reference. State that it must not reproduce the source's title, typography, people, logos, or literal artwork.
9. Inspect the generated image itself. Check source resemblance, botanical identity, real stem support and binding, paper construction, hand anatomy and contact pressure, first-person perspective, phone-camera texture, motivated light, and forbidden content. If one critical invariant fails, make one targeted regeneration that repeats all invariants; then re-check. Do not retry indefinitely.
10. Save final files in the user-named destination or, by default, `outputs/image-to-bouquet/<source-slug>/`. Never overwrite an existing run; append `-v2`, `-v3`, and so on.

## Non-negotiable image contract

- Default vertical 9:16 smartphone frame.
- Bouquet is the first visual focus and is held straight forward at chest height.
- A single left forearm enters naturally from the lower-left or lower-center; exactly one plausible left hand grips the tied stem bundle. Finger configuration, wrist angle, scale, skin texture, and grip pressure must be credible.
- The unseen right hand takes the photograph. No visible phone, face, selfie pose, second person, second hand, or detached arm.
- Use an ordinary lived-in location whose colors and mood support the source without literally recreating it. Background evidence stays subordinate.
- Use one believable available-light setup with natural shadow falloff. Preserve realistic skin color even when the source palette is strongly colored.
- Ask for recent-smartphone main-camera behavior: roughly 24–28 mm equivalent, modest dynamic range, mild computational sharpening, coherent depth, and small exposure/framing imperfections. Avoid fake telephoto bokeh and studio polish.
- Every visible bloom connects to a plausible stem or branch; stems converge into one bindable bundle; paper compresses around the stems; the hand visibly carries the bouquet's weight.
- Prefer natural flower colors. Exact unnatural colors may use real florist dye, spray, or preserved material only when disclosed in the specification; use paper for large impossible color fields.
- Unless requested: no caption, album cover, printed artwork, title, logo, watermark, vase, gift box, decorative text, fictional flower, or background person.

## Completion contract

A run is complete only when these three checked files exist:

1. `<source-slug>-bouquet-spec.md`
2. `<source-slug>-image-prompt.md`
3. `<source-slug>-handheld.png` (or the actual generated raster extension)

Return clickable paths, show the final image, summarize the decisive flower-and-paper mapping in one sentence, state that built-in image generation was used, and identify any disclosed dye/seasonality constraint. Do not claim the bouquet was physically built or florist-validated.
