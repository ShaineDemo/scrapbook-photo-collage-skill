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

Choose each window from the original source aspect ratio. The fallback uses uncropped `contain`, so a badly mismatched window creates large empty mats and weakens photo dominance. Redesign the reservation window instead of accepting a large blank area.

## Place the originals deterministically

Example for one portrait source around a 0.56 aspect ratio on a 900×1200 background:

```bash
python3 scripts/compose_locked_photos.py \
  --background scrapbook-background.png \
  --output final.png \
  --place S1 original-portrait.jpg 174 100 552 958 \
  --manifest final.sources.json
```

Illustrative combined-page example using square sources; replace every window with dimensions derived from the actual source ledger:

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

Coordinates are `X Y WIDTH HEIGHT` in pixels and describe the outer photo frame. The script rejects non-3:4 backgrounds, duplicate source IDs, missing files, out-of-canvas frames, more than 18% blank mat inside a frame, and a one-photo page below 38% visible photo area. The normal single-page design target remains 42–58%; the lower value is only a hard rejection floor. Multiple placements are rejected unless `--summary-layout` is present.

Always pass `--summary-layout` for the final combined page. It rejects summaries without a hero at least 1.4× the next-largest visible photo, below a 42% summed visible-photo floor, or using aligned grid/contact-sheet placement. The normal summary target remains 50–65%. When the script rejects a layout, redesign the generated empty windows and rerun it. Do not increase `--max-mat-fraction` or decrease either photo-area minimum merely to force a weak composition through validation.

The manifest records each placed photo's `mat_fraction` and `canvas_photo_fraction`, making it possible to audit whether the final page actually meets the intended dominance rather than trusting the visual prompt.

## Fidelity inspection

Before delivery, compare each placed frame with its original and verify:

- the same number of people and animals;
- the same faces, clothing, gestures, hands, food, objects, landmarks, and visible text;
- no source was replaced with a newly invented group photo or similar-looking scene;
- every stable source ID appears once in the summary;
- no decoration covers or visually merges with the photo window;
- all outputs remain exact 3:4.

If any check fails, do not deliver the image. Recompose from the original source using the locked-photo fallback.

## Working-file discipline

Empty-window backgrounds, numbered contact sheets, manifests, and layout notes are intermediate production files. Keep them in a temporary work directory and exclude them from the final gallery and final ZIP unless the user requests editable production assets.

Use the bundled compositing script rather than creating per-run scripts in the user's project. The generated background should contain its decorative title and labels once. Do not add a second title pass, and do not run the final locked-photo composite back through image generation.
