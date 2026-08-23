# Source-preservation fallback

Use this fallback whenever the renderer may redraw, omit, merge, replace, or crop important source content. It is the default safety path for renderers that cannot lock reference-image pixels reliably.

## Immutable source contract

Inside every delivered photo frame, the original photo may undergo only:

- EXIF orientation correction;
- uniform resizing;
- uncropped `contain` placement inside a rectangular frame.

Do not use generative fill, face restoration, beauty retouching, background replacement, relighting, object removal, subject insertion, mirroring, semantic crop, or text rewriting inside the photo bounds. Preserve the original subject count. A person, pet, meal, landmark, sign, or found object present in the source must remain present in the placed photo.

Cropping is outside this safety path. Use it only when the user explicitly requests it or after a reliable visual audit proves that no person, hand, face, pet, food, landmark, or meaningful text will be removed.

## Choose the rendering path

1. **Locked reference editing:** Use direct image editing only when the tool can preserve each supplied photo as a locked image region.
2. **Hybrid locked-photo fallback:** If preservation is uncertain, generate only the background, papers, lettering, tape, and decorations. Then place the untouched originals with `scripts/compose_locked_photos.py`.
3. **Brief-only fallback:** If neither locked editing nor deterministic compositing is available, deliver the background prompt, frame map, and source ledger. Do not present a source-altering render as final.

After one failed fidelity inspection, stop asking the same generative renderer to “restore” deleted people or objects. Discard that render and switch to the hybrid fallback.

## Generate a background with reserved frames

The background prompt must request clean rectangular reservation zones:

```text
Generate only the 3:4 vertical scrapbook surround: background paper, layered stationery, title, captions, tape, stitching, and project-specific decorations. Reserve [N] clean rectangular photo windows at [positions and approximate sizes]. Keep decorations outside those windows and do not cross their edges.

The windows must contain plain matte placeholder color only. Do not generate photographs, people, faces, bodies, pets, food, scenery, landmarks, or fake source-image content inside them. Do not draw photo-like content that could remain visible after the original photos are placed.
```

Use rectangular windows in the fallback path. Avoid irregular masks, perspective distortion, curled photographs, or objects overlapping a photo window because these make pixel-locked placement unreliable.

## Place the originals deterministically

Example for one 900×1200 background:

```bash
python3 scripts/compose_locked_photos.py \
  --background scrapbook-background.png \
  --output final.png \
  --place S1 original.jpg 110 120 680 650 \
  --manifest final.sources.json
```

Example for a combined page:

```bash
python3 scripts/compose_locked_photos.py \
  --background summary-background.png \
  --output summary.png \
  --place S1 photo-1.jpg 70 100 470 390 \
  --place S2 photo-2.jpg 570 120 250 300 \
  --place S3 photo-3.jpg 90 540 310 300 \
  --place S4 photo-4.jpg 440 500 380 340 \
  --manifest summary.sources.json
```

Coordinates are `X Y WIDTH HEIGHT` in pixels and describe the outer photo frame. The script rejects non-3:4 backgrounds, duplicate source IDs, missing files, and out-of-canvas frames. It always uses uncropped `contain` placement and records the source-to-frame mapping when `--manifest` is supplied.

## Fidelity inspection

Before delivery, compare each placed frame with its original and verify:

- the same number of people and animals;
- the same faces, clothing, gestures, hands, food, objects, landmarks, and visible text;
- no source was replaced with a newly invented group photo or similar-looking scene;
- every stable source ID appears once in the summary;
- no decoration covers or visually merges with the photo window;
- all outputs remain exact 3:4.

If any check fails, do not deliver the image. Recompose from the original source using the locked-photo fallback.
