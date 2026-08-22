#!/usr/bin/env python3
"""Build numbered, uncropped contact sheets for image-reference tools."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError as exc:
    raise SystemExit("Pillow is required: python3 -m pip install Pillow") from exc


def font(size: int):
    candidates = (
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    )
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def build_sheet(paths: list[Path], output: Path, start: int, width: int, cell_height: int) -> None:
    columns = 2
    margin, gap, label_height = 32, 24, 54
    rows = math.ceil(len(paths) / columns)
    cell_width = (width - margin * 2 - gap) // columns
    height = margin * 2 + rows * cell_height + (rows - 1) * gap
    sheet = Image.new("RGB", (width, height), "#eef2f4")
    draw = ImageDraw.Draw(sheet)
    label_font = font(30)

    for offset, path in enumerate(paths):
        row, column = divmod(offset, columns)
        x = margin + column * (cell_width + gap)
        y = margin + row * (cell_height + gap)
        draw.rounded_rectangle(
            (x, y, x + cell_width, y + cell_height),
            radius=16,
            fill="#ffffff",
            outline="#25313b",
            width=4,
        )
        draw.text((x + 16, y + 10), f"SOURCE PHOTO {start + offset}", font=label_font, fill="#111820")
        frame_width = cell_width - 28
        frame_height = cell_height - label_height - 14
        with Image.open(path) as source:
            image = ImageOps.exif_transpose(source).convert("RGB")
            fitted = ImageOps.contain(image, (frame_width, frame_height), Image.Resampling.LANCZOS)
        paste_x = x + 14 + (frame_width - fitted.width) // 2
        paste_y = y + label_height + (frame_height - fitted.height) // 2
        sheet.paste(fitted, (paste_x, paste_y))

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=95)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("contact-sheets"))
    parser.add_argument("--per-sheet", type=int, default=4, choices=range(1, 9))
    parser.add_argument("--width", type=int, default=2048)
    parser.add_argument("--cell-height", type=int, default=800)
    args = parser.parse_args()

    missing = [str(path) for path in args.images if not path.is_file()]
    if missing:
        raise SystemExit("Missing image files:\n" + "\n".join(missing))

    for sheet_index, first in enumerate(range(0, len(args.images), args.per_sheet), start=1):
        batch = args.images[first : first + args.per_sheet]
        output = args.output_dir / f"source-index-{sheet_index}.jpg"
        build_sheet(batch, output, first + 1, args.width, args.cell_height)
        print(output)


if __name__ == "__main__":
    main()
