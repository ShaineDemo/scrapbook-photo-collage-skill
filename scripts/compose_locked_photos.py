#!/usr/bin/env python3
"""Place original photos into a 3:4 scrapbook background without generative edits."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from PIL import Image, ImageColor, ImageFilter, ImageOps
except ImportError as exc:
    raise SystemExit("Pillow is required: python3 -m pip install Pillow") from exc


def parse_placement(values: list[str]) -> tuple[str, Path, tuple[int, int, int, int]]:
    source_id, path_text, x, y, width, height = values
    try:
        box = tuple(int(value) for value in (x, y, width, height))
    except ValueError as exc:
        raise SystemExit("X, Y, WIDTH, and HEIGHT must be integers") from exc
    return source_id, Path(path_text), box


def save_image(image: Image.Image, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    suffix = output.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        flattened = Image.new("RGB", image.size, "white")
        flattened.paste(image, mask=image.getchannel("A"))
        flattened.save(output, quality=95, subsampling=0)
    else:
        image.save(output)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--place",
        action="append",
        nargs=6,
        required=True,
        metavar=("SOURCE_ID", "IMAGE", "X", "Y", "WIDTH", "HEIGHT"),
        help="Repeat once per source. Coordinates describe the outer photo frame in pixels.",
    )
    parser.add_argument("--border", type=int, default=14)
    parser.add_argument("--frame-color", default="#fffdf7")
    parser.add_argument("--mat-color", default="#f3f0e8")
    parser.add_argument("--shadow", type=int, default=10)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()

    if not args.background.is_file():
        raise SystemExit(f"Missing background: {args.background}")
    if args.border < 0 or args.shadow < 0:
        raise SystemExit("--border and --shadow must be zero or greater")

    placements = [parse_placement(values) for values in args.place]
    source_ids = [source_id for source_id, _, _ in placements]
    if len(source_ids) != len(set(source_ids)):
        raise SystemExit("Every SOURCE_ID must be unique; duplicate source IDs are not allowed")

    with Image.open(args.background) as background_source:
        canvas = ImageOps.exif_transpose(background_source).convert("RGBA")
    canvas_width, canvas_height = canvas.size
    if canvas_width * 4 != canvas_height * 3:
        raise SystemExit(
            f"Background must be exact 3:4 vertical; received {canvas_width}x{canvas_height}"
        )

    try:
        frame_color = ImageColor.getrgb(args.frame_color) + (255,)
        mat_color = ImageColor.getrgb(args.mat_color) + (255,)
    except ValueError as exc:
        raise SystemExit(f"Invalid color: {exc}") from exc
    manifest: dict[str, object] = {
        "canvas": [canvas_width, canvas_height],
        "fit": "contain",
        "sources": [],
    }

    for source_id, path, (x, y, width, height) in placements:
        if not path.is_file():
            raise SystemExit(f"Missing source image for {source_id}: {path}")
        if width <= args.border * 2 or height <= args.border * 2:
            raise SystemExit(f"Frame for {source_id} is too small for the selected border")
        if x < 0 or y < 0 or x + width > canvas_width or y + height > canvas_height:
            raise SystemExit(f"Frame for {source_id} is outside the canvas")

        if args.shadow:
            shadow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
            shadow_plate = Image.new("RGBA", (width, height), (0, 0, 0, 92))
            shadow_layer.paste(shadow_plate, (x + args.shadow // 2, y + args.shadow // 2))
            shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(args.shadow))
            canvas = Image.alpha_composite(canvas, shadow_layer)

        frame = Image.new("RGBA", (width, height), frame_color)
        inner_width = width - args.border * 2
        inner_height = height - args.border * 2
        mat = Image.new("RGBA", (inner_width, inner_height), mat_color)
        frame.paste(mat, (args.border, args.border))

        with Image.open(path) as source_file:
            source = ImageOps.exif_transpose(source_file).convert("RGBA")
        fitted = ImageOps.contain(
            source,
            (inner_width, inner_height),
            Image.Resampling.LANCZOS,
        )
        photo_x = args.border + (inner_width - fitted.width) // 2
        photo_y = args.border + (inner_height - fitted.height) // 2
        frame.alpha_composite(fitted, (photo_x, photo_y))
        canvas.alpha_composite(frame, (x, y))

        manifest["sources"].append(
            {
                "id": source_id,
                "path": str(path.resolve()),
                "frame": [x, y, width, height],
                "placed_photo": [x + photo_x, y + photo_y, fitted.width, fitted.height],
                "allowed_changes": ["EXIF orientation", "uniform resize", "contain placement"],
            }
        )

    save_image(canvas, args.output)
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
