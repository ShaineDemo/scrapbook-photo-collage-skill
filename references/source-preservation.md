# Source preservation and fidelity recovery

Use this workflow whenever the renderer may redraw, omit, merge, replace, or crop important source content. It preserves the integrated look whenever possible and keeps the background-only compositor as the last visual fallback.

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

1. **Integrated full-composition reference edit:** Prefer one reference-guided render that builds the source photo, card, mat, tape, clips, foreground crossings, contact shadow, lettering, and surrounding materials together. Never generate empty photo slots first on this path.
2. **Geometry-preserving source recovery:** If the layout and attachment geometry are successful but the source pixels changed, restore the untouched original inside the already-rendered card geometry while keeping the generated mat, tape, clips, foreground crossings, and contact shadow.
3. **Background-only locked-photo fallback:** Only if the first two paths are unavailable, generate lower layers and place untouched originals with `scripts/compose_locked_photos.py`.
4. **Brief-only fallback:** If neither reference editing nor deterministic compositing is available, deliver the prompt, frame map, and source ledger. Do not present a source-altering render as final.

After one failed fidelity inspection, stop asking the same generative renderer to reconstruct deleted people or objects. Restore the original into the successful generated card geometry first; switch to the background-only fallback only if that recovery is impossible.

## Generate a lower background with card footprints

The background prompt must use coordinate footprints as a placement map, not as visible holes:

```text
Generate only the lower layers of a 3:4 vertical composition: a clearly visible outer stage, one bounded scrapbook island, layered stationery, English title and captions, stitching, and project-specific decorations beneath or beside the future photo cards. Use [N] rectangular card footprints at [positions, exact sizes, and optional small rotations] as a placement map.

Do not paint a placeholder, fake photo, colored mat, empty aperture, blurred subject, or prebuilt frame inside a footprint. Continue the ordinary lower paper construction beneath it. The compositor will render the exact card, mat, source photo, shadow, and optional rotation, so no mismatched placeholder edge can remain visible.
```

Use rectangular cards in the background-only fallback. Avoid irregular source masks, perspective distortion, or curled source pixels because these make pixel-locked placement unreliable. The complete rectangular card may rotate shallowly. Lower materials may continue beneath it, and a separately generated transparent foreground overlay may touch only the outer mat perimeter after placement.

Require at least two perimeter contacts per card—such as tape plus a clip, a paper overlap plus thread, or a corner tab plus a foreground leaf—and a shallow contact shadow following the whole card edge. Composite at 4× working resolution when practical, downsample with LANCZOS, and inspect at 200% for jagged edges, halos, light seams, or mismatched placeholder borders.

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

Coordinates are `X Y WIDTH HEIGHT` in pixels and describe the unrotated outer photo card. `--rotate SOURCE_ID DEGREES` rotates the complete card by at most ±6 degrees and never changes its internal crop. `--overlay` accepts an optional same-size transparent PNG that is composited last. The script rejects non-3:4 backgrounds, duplicate source IDs, missing files, rotated cards that leave the canvas, wrong-size overlays, more than 18% blank mat inside a frame, and a one-photo page outside the 20–46% hard visible-photo range. The normal single-page design target is 26–40%; the wider limits only reject obviously tiny or photo-dominated layouts. Multiple placements are rejected unless `--summary-layout` is present.

Always pass `--summary-layout` for the final combined page. It rejects summaries without a hero at least 1.4× the next-largest visible photo, outside the 36–64% hard summed visible-photo range, or using aligned grid/contact-sheet placement. The normal summary target is 44–58%. Arrange one connected asymmetric photo island: every card overlaps, touches, or connects through shared backing, thread, or a clip spine. Keep the title above or outside this island and never use a central vertical text spine to divide disconnected photo columns. When the script rejects a layout, redesign the complete card footprints and rerun it. Do not increase `--max-mat-fraction` or widen the photo-area limits merely to force a weak composition through validation.

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

If any check fails, do not deliver the image. Restore the untouched original into successful generated card geometry when available; otherwise recompose from the original source using the background-only locked-photo fallback.

## Working-file discipline

Lower-layer backgrounds, numbered contact sheets, manifests, and layout notes are intermediate production files. Keep them in a temporary work directory and exclude them from the final gallery and final ZIP unless the user requests editable production assets.

Use the bundled compositing script rather than creating per-run scripts in the user's project. The generated background should contain its decorative English title and labels once. Do not add a second title pass, and do not run the final locked-photo composite back through image generation. If using a foreground overlay, generate and inspect it separately, keep it transparent outside its small attachment elements, and apply it only through the deterministic compositor.
