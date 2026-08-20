# Handheld smartphone realism

Use these rules for the skill's single output style: a believable first-person phone photo of the designed bouquet.

## 1. Lock the first-person geometry

- The photographer is behind the camera.
- One left forearm enters from the lower-left or lower-center. The left hand closes around the tied stem bundle and holds the bouquet straight forward at chest height.
- The unseen right hand operates the phone. Do not show the phone, right hand, face, torso, mirror reflection, selfie pose, or another person holding the bouquet.
- Ask for exactly one visible hand, a continuous wrist-to-forearm connection, plausible hand scale, natural thumb/finger opposition, and visible pressure where skin contacts ribbon, paper, and stems.
- Not all five fingers need to be fully visible in a grip, but the visible configuration must be anatomically possible. Reject extra, fused, duplicated, or disconnected fingers.
- A simple sleeve may enter with the forearm. Keep it subordinate and avoid adding a new dominant color unless the source supports it.

## 2. Simulate one real phone capture

Prompt as a physical capture, not as an idealized render:

- vertical 9:16 by default;
- recent smartphone main camera, approximately 24–28 mm full-frame equivalent;
- camera at chest-to-eye height, bouquet at arm's length;
- autofocus and exposure prioritize the bouquet; background stays readable rather than becoming creamy telephoto bokeh;
- slight wide-lens perspective, small handheld tilt or imperfect crop, modest dynamic range, mild computational sharpening;
- low light may add fine luminance/chroma noise and slight motion softness; daylight may preserve small clipped highlights or uneven exposure;
- keep hand, bouquet, and background perspective coherent. Do not combine macro flower detail, telephoto compression, and a full arm's-length view.

## 3. Establish subject hierarchy

1. First visual focus: the source-derived bouquet and its focal flowers.
2. Supporting focus: the hand, binding point, paper contact, and enough stems to prove construction.
3. Background: location evidence and mood, never equally sharp, bright, or saturated.

Use framing, brightness, local contrast, and focus to enforce this order. The hand is functional evidence, not a beauty-photo subject.

## 4. Choose a lived-in location

Select an ordinary location compatible with the source's light and palette: home doorway, apartment corridor, sidewalk, stairwell, small park path, studio corner, bus stop, balcony, or sunlit wall. Do not recreate the source image literally.

Add only two to four believable traces of use—uneven pavement, worn wall paint, doorway spill, dust, scuffed skirting, irregular plants, cables, condensation, or imperfect shadows. Keep them subordinate. Avoid an empty generic luxury interior or an implausibly beautiful anonymous backdrop.

## 5. Give light a source

Name one main available source: daylight, window, overcast sky, sunset, doorway spill, streetlight, shop light, or practical lamp. Optional fill or rim light must be explainable by a visible or plausible secondary source.

- Ask for natural falloff across hand, petals, and wrapping.
- Keep shadow detail and controlled highlights; avoid crushed pure black and glowing pure white.
- Preserve believable skin color under strong source palettes. A blue or green reference may tint shadows and surroundings, but must not turn the hand into uniformly colored plastic.
- Avoid studio softboxes, unmotivated rim light, generic glow, HDR contrast, and hard light boundaries.

## 6. Preserve real material texture

Request botanical and construction evidence: slight petal bruising or curl, different petal thicknesses, leaf veins, stem nodes, cut stems, natural asymmetry, paper fibers, cellophane reflections, ribbon tension, skin pores and creases, fabric friction, and small handling wrinkles. Use only details appropriate to the chosen flowers and location.

Avoid waxy skin, oily highlights, plastic petals, perfect symmetry, identical repeated flowers, fused petals, floating heads, fake condensation, or paper that behaves like rigid 3D geometry.

## 7. Prompt exclusions

Adapt this stable list rather than relying on vague `bad quality` language:

```text
AI-looking, CGI, 3D render, plastic petals, waxy skin, beauty filter, HDR, over-sharpened, fake bokeh, impossible reflections, inconsistent shadows, unmotivated light, hard light cutoff, perfect symmetry, generic luxury background, distorted hand, extra fingers, fused fingers, duplicated hand, broken wrist, detached arm, object merging, floating flower heads, unsupported stems, impossible binding, rigid floating paper, visible phone, selfie, face, background person, album cover, copied artwork, logo, watermark, garbled text, illustration, anime, sketch, storyboard texture
```

## 8. Inspection and one-retry rule

Inspect the actual result in this order:

1. **Hand geometry:** exactly one left hand and forearm; plausible grip, wrist, fingers, scale, and skin contact.
2. **Floristry mechanics:** recognizable flowers, supported heads, converging stems, visible binding, compressed paper, one-hand scale, believable gravity.
3. **Camera coherence:** first-person arm's-length view, 24–28 mm-like perspective, coherent focus and depth, phone absent.
4. **Light logic:** named source is consistent across hand, petals, paper, ground, and background; no unexplained glow.
5. **Source translation:** palette hierarchy, skeleton, negative space, focal placement, texture, and mood remain recognizable.
6. **Real-world texture:** ordinary location evidence, small imperfections, natural skin and plant texture, no luxury-ad polish.
7. **Forbidden content:** no source artwork, text, logo, watermark, face, extra person, vase, or gift box.

If one critical invariant fails, regenerate once with a targeted correction and repeat every non-negotiable invariant. If the second image still fails, deliver neither as validated; report the specific failure instead of claiming success.
