# Deliverables and prompt scaffold

## Output directory and names

Use the user's destination if supplied. Otherwise use:

```text
outputs/image-to-bouquet/<source-slug>/
├── <source-slug>-bouquet-spec.md
├── <source-slug>-image-prompt.md
└── <source-slug>-handheld.png
```

Use a short filesystem-safe source slug. Create a sibling version rather than overwriting an existing run. Do not create a bouquet-only effect image or a second style variant.

## Bouquet specification template

```markdown
# <Source name> → Handheld bouquet specification

## Run
- Source image: <path, attachment label, or user description>
- Output: first-person left-hand-forward smartphone photo
- Intended aspect ratio: 9:16 unless requested otherwise
- Interpretation: <one-sentence design thesis>

## Visual analysis
- Dominant / secondary / highlight / accent / dark anchor: <color name + approximate hex + role>
- Tone: <temperature, key, saturation, contrast>
- Structure: <direction, focal placement, density, negative space>
- Texture and mood: <surface cues and emotional register>
- Ignore as noise: <border, typography, skin, compression, etc.>

## Florist-buildable recipe
| Material | Common market name | Color/treatment | Count | Visual job | Sourcing | Feasible substitute |
|---|---|---|---:|---|---|---|
| ... | ... | natural/dyed/etc. | ... | ... | ordinary/seasonal/special-order | ... |

## Wrapping and construction
| Layer | Material | Color/finish/opacity | Fold and physical purpose |
|---|---|---|---|
| Protective | ... | ... | ... |
| Inner | ... | ... | ... |
| Backing/outer | ... | ... | ... |
| Tie | ... | ... | ... |

- Silhouette and mechanics: <shape, center of mass, stem direction, binding point, exposed grip area>
- Buildability verdict: <why a florist can source and assemble it>
- Disclosed constraints: <seasonality, dye, spray, preservation, safety>
- Preserve from source: <3–6 decisive relationships>
- Avoid: <specific design and generation failures>

## Handheld capture plan
- Location and real-life evidence: <ordinary location + 2–4 subordinate details>
- Camera geometry: <phone main camera, height, distance, framing>
- Light source and falloff: <one motivated source + optional justified fill>
- Phone imperfections: <crop, tilt, exposure, grain/sharpening appropriate to light>
- Hand and grip: <left forearm entry, sleeve, pressure, bouquet weight>
```

## Exact prompt file

Save the exact prompt sent to built-in image generation, not a summary:

```markdown
# Final handheld image-generation prompt

- Input image role: Visual reference for palette hierarchy, tonal relationships, texture, negative space, and compositional rhythm; not an edit target or literal content source.

## Prompt sent to image generation

<exact prompt>
```

## Final prompt scaffold

Customize every placeholder from the completed specification. Keep the capture causal and concrete.

```text
Use case: photorealistic-natural
Asset type: candid first-person smartphone bouquet photograph
Input image: Image 1 is a visual reference for palette hierarchy, tonal structure, texture, negative space, and mood only; it is not an edit target. Do not reproduce its person, title, typography, logo, artwork, or literal scene.
Primary request: translate Image 1's visual system into one physically buildable bouquet held forward in an everyday first-person phone snapshot. Preserve <dominant/secondary/highlight/anchor relationships, skeleton, focal placement, and negative space>.

Subject hierarchy: the bouquet is the first visual focus. The binding point, supporting stems, and hand are secondary evidence. The background proves a real place but remains subordinate.
Florist-buildable recipe: <common flower/material names, natural/dyed status, exact or approximate stem counts, and each visual job>. Every flower head connects to its own plausible stem or branch; heavy heads are structurally supported; all stems converge into one real binding point; no invented flowers.
Wrapping construction: <protective, inner, backing, outer, and tie layers in order; real materials, color, finish, opacity, fold direction>. Paper wraps and compresses around the stem bundle with natural wrinkles; no disconnected floating paper planes.
Silhouette and mechanics: <source-derived shape, center of mass, negative space, binding height, exposed tied stems>. The complete bundle fits one adult hand and visibly obeys gravity.

Composition/framing: first-person vertical 9:16 smartphone photo. A single left forearm enters from the lower-left or lower-center; exactly one anatomically plausible left hand grips the tied stem bundle and holds the bouquet straight forward at chest height. Natural thumb/finger opposition, continuous wrist, realistic scale, skin creases, and visible grip pressure. The unseen right hand takes the photograph. No visible phone, right hand, face, selfie pose, mirror, second person, or detached arm.
Scene/backdrop: <ordinary lived-in location> with only <2–4 real-use details>. Its incidental colors support the source palette without recreating Image 1. Background details remain less sharp, bright, and saturated than the bouquet.
Camera: recent smartphone main camera, approximately 24–28 mm equivalent, camera at chest-to-eye height, bouquet at arm's length, autofocus/exposure on bouquet, coherent perspective and moderate depth, modest dynamic range, mild computational sharpening, slight handheld tilt or imperfect crop. No telephoto compression, macro/full-view contradiction, or fake creamy bokeh.
Lighting: <one believable available light source> shapes hand, petals, stems, paper, and background consistently, with natural falloff, controlled highlights, and detailed shadows. <Optional secondary source only if justified>. Preserve believable skin color even under the source palette; no studio softbox, unmotivated rim light, HDR, or generic glow.
Color: <source-derived palette and proportional roles>. Keep large impossible colors in paper; disclose limited florist dye/spray where used. Protect neutral materials and skin from uniform color casting.
Real texture: species-correct petals and leaves, stem nodes, small asymmetry, minor petal curl or bruising, cut stems, paper fibers, cellophane reflections, ribbon tension, sleeve friction, skin pores, and environment wear appropriate to the scene.
Constraints: recognizable purchasable flowers, accurate botanical structure, plausible sourcing and assembly, exactly one visible left hand, one bindable stem bundle, no album cover, no copied artwork, no title, no typography, no logo, no watermark, no vase, no gift box, no background person.
Avoid: AI-looking, CGI, 3D render, plastic petals, waxy skin, beauty filter, HDR, over-sharpened, fake bokeh, impossible reflections, inconsistent shadows, unmotivated light, perfect symmetry, generic luxury background, distorted hand, extra fingers, fused fingers, duplicated hand, broken wrist, detached arm, object merging, floating flower heads, unsupported stems, impossible binding, rigid floating paper, visible phone, selfie, face, illustration, anime, sketch, storyboard texture, garbled text.
```

## Final inspection checklist

- Palette hierarchy, skeleton, focal placement, negative space, texture, and mood still evoke the hidden source.
- Every named flower is recognizable and matches the written color/treatment and approximate quantity.
- Flower heads have plausible stems; stems converge; binding and paper compression are visible; scale and gravity work.
- Exactly one plausible left hand/forearm appears with credible contact pressure; phone, face, other hand, and people are absent.
- Camera behaves like one 24–28 mm-equivalent phone capture; depth, scale, crop, and perspective agree.
- Light has one explainable source and consistent falloff; skin remains believable.
- Location has real but subordinate evidence; image is not a polished fashion or luxury campaign.
- No source artwork, caption, title, logo, watermark, vase, box, fictional species, or impossible material.

Allow one targeted regeneration for a critical failure. Do not call an unchecked or still-failing result complete.
