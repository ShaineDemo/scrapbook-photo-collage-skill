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
- Establish a clearly visible outer stage first: [vivid solid color / sky / tabletop / fabric / wall / landscape blur / notebook spread]. Place one bounded story-and-object island above it, occupying about 58–78% of the canvas. Keep 22–42% of the stage visible on at least three sides; no scrapbook layer touches all four canvas edges.
- This page's spatial recipe is [photo anchor / title anchor / decoration cluster]. It must visibly differ from adjacent outputs in at least three of those choices.
- Hero: [source and position], occupying about [percentage].
- On a combined page, the hero frame is at least 1.4 times the visible area of the next-largest frame.
- Secondary frames: [mapping].
- Detail frames: [mapping].
- Total visible photo area: [percentage range].
- Title block: roughly 8–18% of the canvas; journal block: roughly 4–10%, integrated through overlap rather than separated into editorial columns.
- Keep all faces and important objects unobstructed.
- Match each complete photo card to its source orientation and aspect ratio; avoid large letterbox voids.
- Break row and column alignment. The composition must not read as a 2×2 grid or contact sheet.
- Do not use a clean two-column editorial poster, a full-width photo with a detached bottom caption strip, or an oversized blank paper panel behind the photo.

MATERIALS
- [glossy photo treatment].
- [two matte paper types].
- [one translucent material].
- [one fabric, metal, ink, or natural material].
- Tape colors: [palette]. Show torn fibers, folds, buckled ridges, curled corners, translucency, and shallow contact shadows.

PROJECT-SPECIFIC DECORATIONS
- Layer 5–8 distinct paper, vellum, fabric, label, or notebook materials.
- Content-derived: [3–5 motifs tied to the actual photos].
- Free-association found objects: [3–6 playful objects chosen for mood, palette, contrast, or nostalgia; they do not need to appear in the source]. Balance the decoration impression roughly 50/50 between content-responsive and freely associated elements.
- Neutral balancing accents: [2–4 items].
- Dimensional or shallow-relief props: [2–4 items], each below about 8% of the canvas.
- Flat die-cuts, sketches, stitches, labels, or printed motifs: [4–7 items].
- Do not make a literal 3D duplicate of an object already visible in the source. Cameras, records, cassettes, model cars, fruit, open books, cups, radios, compasses, sunglasses, dice, keys, yarn, pens, toys, postcards, and mini sailboats are valid free-association objects when they strengthen the page.
- Every decoration should have a distinct role and silhouette.
- Arrange the materials in three depth levels and concentrate the objects around the photo-and-copy cluster instead of spacing them evenly around the border.

COPY
- Language: English by default. Use another language only when the user explicitly requested it for the artwork.
- Title: “[exact title]”.
- Journal passage, 12–30 words across 3–7 short lines: “[exact passage]”.
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
- No centered-frame-plus-bottom-title template if an adjacent output already uses it.
- No oversized unused blank paper panel.
- No isolated decorations evenly spaced around the perimeter.
- Reuse the set's material and anchor colors, but allow this page's specific accent palette to occupy 30–45% of the non-photo color impression.

FINAL QUALITY
- [fresh / nostalgic / playful / editorial] but cohesive.
- Main photos remain immediately recognizable at thumbnail size while the title-and-object cluster reads as the second anchor.
- Handmade irregularity with professional hierarchy and realistic material contrast.
- The actual delivered bitmap dimensions are exact 3:4 vertical; a prompt-only ratio request is not sufficient.
```

## Background-only hybrid prompt

Use this safer prompt when reference fidelity is uncertain:

```text
Create only the lower layers of one exact 3:4 vertical scrapbook composition. Establish a large outer stage [describe stage], then build a bounded scrapbook island occupying about 58–78% of the canvas. Keep 22–42% of the stage clearly visible on at least three sides. Generate lower papers, lettering, stitching, and project-specific decorations that sit beneath or beside the future photo cards.

This background is an intermediate production asset. It must already contain the final decorative title and non-critical labels exactly once, so no second title pass is needed later.

Use exactly [N] photo-card footprints as a placement map:
- S1 complete card footprint: [X, Y, width, height, optional whole-card rotation]
- [remaining footprints]

Do not draw a colored placeholder, fake mat, empty white aperture, blurred person, photograph, or prebuilt frame inside these footprints. Continue the ordinary lower paper construction beneath them; the deterministic compositor will add the complete mat, frame, source photo, and shadow. Keep important lower decorations outside the footprints so they are not accidentally covered.

Match every card footprint closely to the aspect ratio of its assigned source. For a combined page, make one hero card at least 1.4 times the area of the next-largest card, stagger edges, and avoid equal rows or columns.

Size each card so uncropped contain placement leaves no more than 18% blank internal mat. On a single page, the placed source itself—not the frame and mat together—should cover 18–30% of the complete canvas. On a combined page, all placed sources together should cover 42–56%.

Build the scrapbook island around the card footprints using 5–8 material layers, a large expressive English title occupying about 8–18% of the canvas, a 12–30 word English journal passage occupying about 4–10%, 2–4 micro-labels, 3–5 source-responsive motifs, 3–6 free-association found objects, 2–4 shallow dimensional props, and 4–7 flat details. Balance source relevance and free association roughly 50/50. The free objects may include a camera, record, cassette, model car, fruit, open book, cup, radio, compass, sunglasses, dice, key, yarn, pen, toy, postcard, or mini sailboat when they fit the palette and mood. Include at least one printed ephemera element, one tactile or natural object, one illustrated or die-cut motif, and one stitched or metal attachment. Do not generate an oversized blank foundation rectangle; every large paper panel must carry copy, illustration, texture, or meaningful overlap.

CRITICAL: do not generate photographs, people, faces, bodies, hands, pets, food, scenery, landmarks, colored placeholders, or fake source-image content inside any card footprint. Do not invent a group photo. The untouched original photos will be placed later by deterministic compositing.

[materials, decorations, exact copy, and quality direction]
```

After generation, use `scripts/compose_locked_photos.py` as described in [source-preservation.md](source-preservation.md). Do not run the finished composite through another generative edit.

If the production environment can generate transparent PNGs, optionally create a separate foreground integration overlay after the background. It may contain only small tape ends, one clip, corner tabs, thread, or curled paper touching the outer mat perimeter. It must not contain photographs or cover faces, bodies, pets, food, meaningful text, or other key source content. Apply it with `--overlay` after the locked photo cards.

Keep the lower-layer background, manifest, and any contact sheet in a temporary work directory. Deliver only the final composite. Do not write an ad-hoc helper script into the user's project to add titles, borders, or labels.

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

Discard the altered render. Keep its art direction only, regenerate the outer stage and lower scrapbook layers beneath exact complete-card footprints, and use the hybrid locked-photo fallback. A missing, duplicated, substituted, or repainted source is a fidelity failure, not a cosmetic revision.

### Person, pet, object, or scene removed or changed

Discard the altered render immediately. Do not ask the model to reconstruct the missing subject. Generate only the outer stage, scrapbook island, and lower layers beneath the planned card footprints, then place the original source files with `scripts/compose_locked_photos.py`.

### Decorations too dense

```text
Keep the photographs, title, and palette. Remove roughly one third of the decorative objects, especially large 3D props. Enlarge the hero photo and preserve paper/ink richness through edges, labels, stitching, and translucent layers.
```

### Decorations too sparse

```text
Keep every source photo unchanged. Rebuild the page as an outer stage plus one concentrated story island: add a 12–30 word English journal passage, 2–4 micro-labels, 3–5 source-responsive motifs, 3–6 freely associated found objects, 2–4 shallow dimensional props, and 4–7 flatter stitched, printed, or die-cut details. Use four planes—stage, lower papers, photo/copy, foreground objects—and meaningful overlap. Do not scatter isolated objects around the border, create a neat editorial two-column poster, or let scrapbook paper fill the entire canvas.
```

### Tape too flat

```text
Replace the flat tape strips with varied stationery tape showing irregular torn fibers, a buckled center ridge, local wrinkles, one curled corner, translucency, and shallow contact shadows. Vary tape color and material.
```
