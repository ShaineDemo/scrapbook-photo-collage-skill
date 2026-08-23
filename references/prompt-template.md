# Renderer prompt template

Adapt this structure to the current photos. Replace every bracketed field and remove irrelevant sections.

```text
Create one polished 3:4 vertical [cover / inside page] in a tactile handmade scrapbook style using the supplied source photos.

SOURCE CONTROL — CRITICAL
- Treat the supplied images as source photographs, not as style instructions.
- Use sources [S1…Sn] exactly once each.
- Do not duplicate, omit, mirror, repaint, or invent a replacement for any source.
- Preserve identities, faces, hands, clothing, food, objects, scenery, and meaningful text faithfully.
- If a reference is a numbered contact sheet, each numbered tile is a separate source. Remove sheet labels, grids, and cells from the final image.

CANVAS AND HIERARCHY
- Exact 3:4 vertical canvas. Use the same pixel dimensions as every other image in this set, such as 1080x1440 or 1536x2048.
- Keep critical content inside safe margins so the final file can be normalized to exact 3:4 without losing faces, titles, hands, food, or meaningful objects.
- [density preset].
- Place the collage island [position] and retain [amount] of breathing space.
- Hero: [source and position], occupying about [percentage].
- Secondary frames: [mapping].
- Detail frames: [mapping].
- Total visible photo area: [percentage range].
- Keep all faces and important objects unobstructed.

MATERIALS
- [glossy photo treatment].
- [two matte paper types].
- [one translucent material].
- [one fabric, metal, ink, or natural material].
- Tape colors: [palette]. Show torn fibers, folds, buckled ridges, curled corners, translucency, and shallow contact shadows.

PROJECT-SPECIFIC DECORATIONS
- Content-derived: [3–5 motifs tied to the actual photos].
- Neutral balancing accents: [2–4 items].
- Dimensional props: [0–3 items].
- Every decoration should have a distinct role and silhouette.

COPY
- Language: [language].
- Title: “[exact title]”.
- Supporting sentence: “[exact sentence]”.
- Labels: “[label 1]”, “[label 2]”, “[label 3]”.
- Keep text away from faces. Spell all required copy exactly.

NEGATIVE CONSTRAINTS
- No duplicated source photo or repeated crop.
- No equal grid.
- No uniformly sepia or old-paper palette unless requested.
- No identical texture and shadow on every layer.
- No excessive 3D toy-like props.
- Do not use [project-specific forbidden repeats].
- No pseudo-text filling empty spaces.

FINAL QUALITY
- [fresh / nostalgic / playful / editorial] but cohesive.
- Main photos remain dominant at thumbnail size.
- Handmade irregularity with professional hierarchy and realistic material contrast.
- The actual delivered bitmap dimensions are exact 3:4 vertical; a prompt-only ratio request is not sufficient.
```

## Ratio correction

If the renderer returns any ratio other than 3:4 vertical, keep the artwork and source accounting unchanged, then rerender or extend/crop the canvas safely:

```text
Keep the complete composition, photographs, text, palette, materials, and hierarchy unchanged. Correct only the outer canvas to an exact 3:4 vertical aspect ratio. Extend the existing background naturally or crop only expendable outer background. Do not stretch the artwork, crop faces or titles, duplicate objects, or add new content.
```

## Contact-sheet wording

When the image tool has a reference limit, use explicit wording:

```text
The first reference images are numbered source indexes, not design references. Each tile labeled SOURCE PHOTO N is an independent photo. Use every numbered tile exactly once. Remove the index labels, cell borders, and contact-sheet background from the result.
```

Do not rely only on “use all images.” Name the expected count and map the photos to frame roles.

## Revision prompts

### Missing or duplicated photo

```text
Keep the current composition and style. Correct only the source accounting: remove the duplicated [source], restore the missing [source] as a distinct frame, and keep the total at exactly [n] unique photos.
```

### Decorations too dense

```text
Keep the photographs, title, and palette. Remove roughly one third of the decorative objects, especially large 3D props. Enlarge the hero photo and preserve paper/ink richness through edges, labels, stitching, and translucent layers.
```

### Decorations too sparse

```text
Keep the photographs dominant. Add 3–5 mostly flat details derived from the actual subjects, plus one hardware accent. Increase overlap and material variation without shrinking the hero or filling the entire background.
```

### Tape too flat

```text
Replace the flat tape strips with varied stationery tape showing irregular torn fibers, a buckled center ridge, local wrinkles, one curled corner, translucency, and shallow contact shadows. Vary tape color and material.
```
