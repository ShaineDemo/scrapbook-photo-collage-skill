# Source-preservation fallback

Use this fallback whenever the renderer may redraw, omit, merge, replace, or crop important source content. It is the default safety path for renderers that cannot lock reference-image pixels reliably.

## Immutable source contract

Inside every delivered photo frame, the original photo may undergo only:

- EXIF orientation correction;
- uniform resizing;
- uncropped `contain` placement inside a rectangular frame;
- optional shallow rotation of the **complete photo-card assembly** by no more than 6 degrees.

Whole-card rotation changes the physical orientation of the card on the page; it must not crop, warp, repaint, or perspective-transform the source inside the card.

Do not use generative fill, face restoration, beauty retouching, background replacement, relighting, object removal, subject insertion, mirroring, semantic crop, or text rewriting inside the photo bounds. Preserve the original subject count. A person, pet, meal, landmark, sign, or found object present in the source must remain present in the placed photo.

Cropping is outside this safety path. Use it only when the user explicitly requests it or after a reliable visual audit proves that no person, hand, face, pet, food, landmark, or meaningful text will be removed.

## Choose the rendering path

1. **Locked reference editing:** Use direct image editing only when the tool can preserve each supplied photo as a locked image region.
2. **Hybrid locked-photo fallback:** If preservation is uncertain, generate only the background, papers, lettering, tape, and decorations. Then place the untouched originals with `scripts/compose_locked_photos.py`.
3. **Brief-only fallback:** If neither locked editing nor deterministic compositing is available, deliver the background prompt, frame map, and source ledger. Do not present a source-altering render as final.

After one failed fidelity inspection, stop asking the same generative renderer to “restore” deleted people or objects. Discard that render and switch to the hybrid fallback.

## Generate a lower background with card footprints

The background prompt must use coordinate footprints as a placement map, not as visible holes:

```text
Generate only the lower layers of a 3:4 vertical composition: a clearly visible outer stage, one bounded scrapbook island, layered stationery, English title and captions, stitching, and project-specific decorations beneath or beside the future photo cards. Use [N] rectangular card footprints at [positions, exact sizes, and optional small rotations] as a placement map.

Do not paint a placeholder, fake photo, colored mat, empty aperture, blurred subject, or prebuilt frame inside a footprint. Continue the ordinary lower paper construction beneath it. The compositor will render the exact card, mat, source photo, shadow, and optional rotation, so no mismatched placeholder edge can remain visible.
```

Use rectangular cards in the fallback path. Avoid irregular source masks, perspective distortion, or curled source pixels because these make pixel-locked placement unreliable. The complete rectangular card may rotate shallowly. Lower materials may continue beneath it, and a separately generated transparent foreground overlay may touch only the outer mat perimeter after placement.

Choose each complete card footprint from the original source aspect ratio. The fallback uses uncropped `contain`, so a badly mismatched card creates large empty mats and weakens the intended hierarchy. Redesign the card footprint instead of accepting a large blank area.

## Place the originals deterministically

Example for one portrait source around a 0.56 aspect ratio on a 900×1200 background. This card footprint places the original at about 28% of the canvas, leaving room for a story-rich title, journal passage, materials, and objects:

```bash
python3 scripts/compose_locked_photos.py \
  --background scrapbook-background.png \
  --output final.png \
  --place S1 original-portrait.jpg 230 180 440 763 \
  --rotate S1 -3 \
  --overlay scrapbook-foreground.png \
  --manifest final.sources.json
```

Illustrative combined-page example using square sources; replace every card footprint with dimensions derived from the actual source ledger:

```bash
python3 scripts/compose_locked_photos.py \
  --background summary-background.png \
  --output summary.png \
  --summary-layout \
  --place S1 photo-square-1.jpg 30 70 500 500 \
  --place S2 photo-square-2.jpg 550 180 350 350 \
  --place S3 photo-square-3.jpg 30 680 330 330 \
  --place S4 photo-square-4.jpg 420 800 310 310 \
  --manifest summary.sources.json
```

Coordinates are `X Y WIDTH HEIGHT` in pixels and describe the unrotated outer photo card. `--rotate SOURCE_ID DEGREES` rotates the complete card by at most ±6 degrees and never changes its internal crop. `--overlay` accepts an optional same-size transparent PNG that is composited last. The script rejects non-3:4 backgrounds, duplicate source IDs, missing files, rotated cards that leave the canvas, wrong-size overlays, more than 18% blank mat inside a frame, and a one-photo page outside the 14–40% hard visible-photo range. The normal single-page design target is 18–30%; the wider limits only reject obviously tiny or photo-dominated layouts. Multiple placements are rejected unless `--summary-layout` is present.

Always pass `--summary-layout` for the final combined page. It rejects summaries without a hero at least 1.4× the next-largest visible photo, outside the 34–62% hard summed visible-photo range, or using aligned grid/contact-sheet placement. The normal summary target is 42–56%. When the script rejects a layout, redesign the complete card footprints and rerun it. Do not increase `--max-mat-fraction` or widen the photo-area limits merely to force a weak composition through validation.

The manifest records each placed photo's `mat_fraction` and `canvas_photo_fraction`, making it possible to audit whether the final page actually meets the intended dominance rather than trusting the visual prompt.

## Fidelity inspection

Before delivery, compare each placed frame with its original and verify:

- the same number of people and animals;
- the same faces, clothing, gestures, hands, food, objects, landmarks, and visible text;
- no source was replaced with a newly invented group photo or similar-looking scene;
- every stable source ID appears once in the summary;
- no foreground attachment covers a face, body, pet, food, meaningful text, or other key source content;
- no exposed placeholder, mismatched mat, or double frame makes the original look pasted over a generated hole;
- all outputs remain exact 3:4.

If any check fails, do not deliver the image. Recompose from the original source using the locked-photo fallback.

## Working-file discipline

Lower-layer backgrounds, numbered contact sheets, manifests, and layout notes are intermediate production files. Keep them in a temporary work directory and exclude them from the final gallery and final ZIP unless the user requests editable production assets.

Use the bundled compositing script rather than creating per-run scripts in the user's project. The generated background should contain its decorative English title and labels once. Do not add a second title pass, and do not run the final locked-photo composite back through image generation. If using a foreground overlay, generate and inspect it separately, keep it transparent outside its small attachment elements, and apply it only through the deterministic compositor.
