# Renderer prompt template

Adapt this structure to the current photos. Replace every bracketed field and remove irrelevant sections.

Use this direct-editing prompt only when the renderer can keep source-photo regions locked. Otherwise skip to **Background-only hybrid prompt** below and composite the originals deterministically.

```text
Create one polished 3:4 vertical [cover / inside page] in a tactile handmade scrapbook style using the supplied source photos.

SOURCE CONTROL — CRITICAL
- Treat the supplied images as source photographs, not as style instructions.
- Use sources [S1…Sn] exactly once each.
- Do not duplicate, omit, mirror, repaint, or invent a replacement for any source.
- Preserve identities, faces, hands, clothing, food, objects, scenery, and meaningful text faithfully.
- Preserve the original number of people and animals. Do not remove, add, merge, or substitute subjects.
- If a reference is a numbered contact sheet, each numbered tile is a separate source. Remove sheet labels, grids, and cells from the final image.

CANVAS AND HIERARCHY
- Exact 3:4 vertical canvas. Use the same pixel dimensions as every other image in this set, such as 1080x1440 or 1536x2048.
- Keep critical content inside safe margins so the final file can be normalized to exact 3:4 without losing faces, titles, hands, food, or meaningful objects.
- [density preset].
- Place the collage island [position] and retain [amount] of breathing space.
- Hero: [source and position], occupying about [percentage].
- On a combined page, the hero frame is at least 1.4 times the visible area of the next-largest frame.
- Secondary frames: [mapping].
- Detail frames: [mapping].
- Total visible photo area: [percentage range].
- Keep all faces and important objects unobstructed.
- Match each photo window to its source orientation and aspect ratio; avoid large letterbox voids.
- Break row and column alignment. The composition must not read as a 2×2 grid or contact sheet.

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

## Background-only hybrid prompt

Use this safer prompt when reference fidelity is uncertain:

```text
Create only the handmade scrapbook surround for one exact 3:4 vertical page. Generate the background paper, layered stationery, title, captions, tape, stitching, and project-specific decorations.

This background is an intermediate production asset. It must already contain the final decorative title and non-critical labels exactly once, so no second title pass is needed later.

Reserve exactly [N] clean rectangular photo windows:
- S1 window: [X, Y, width, height or clear position and size]
- [remaining windows]

Keep all decorations outside the photo windows and do not cross their edges. Fill each window with one plain matte placeholder color only.

Match every window closely to the aspect ratio of its assigned source. For a combined page, make one hero window at least 1.4 times the area of the next-largest window, stagger edges, and avoid equal rows or columns.

CRITICAL: do not generate photographs, people, faces, bodies, hands, pets, food, scenery, landmarks, or fake source-image content inside any photo window. Do not invent a group photo. The untouched original photos will be placed later by deterministic compositing.

[materials, decorations, exact copy, and quality direction]
```

After generation, use `scripts/compose_locked_photos.py` as described in [source-preservation.md](source-preservation.md). Do not run the finished composite through another generative edit.

Keep the empty-window background, manifest, and any contact sheet in a temporary work directory. Deliver only the final composite. Do not write an ad-hoc helper script into the user's project to add titles, borders, or labels.

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

Discard the altered render. Keep its art direction only, regenerate a background with empty windows, and use the hybrid locked-photo fallback. A missing, duplicated, substituted, or repainted source is a fidelity failure, not a cosmetic revision.

### Person, pet, object, or scene removed or changed

Discard the altered render immediately. Do not ask the model to reconstruct the missing subject. Generate only the surround and empty rectangular windows, then place the original source files with `scripts/compose_locked_photos.py`.

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
