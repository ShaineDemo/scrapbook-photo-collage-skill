#!/usr/bin/env python3
"""Place original photos into a 3:4 scrapbook background without generative edits."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageColor, ImageFilter, ImageOps
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


@dataclass
class PlannedPlacement:
    source_id: str
    path: Path
    frame: tuple[int, int, int, int]
    fitted: Image.Image
    photo_offset: tuple[int, int]
    rotation: float
    mat_fraction: float
    canvas_photo_fraction: float


def cluster_count(values: list[float], tolerance: float) -> int:
    """Count near-aligned coordinates without requiring pixel-perfect equality."""
    clusters: list[float] = []
    for value in sorted(values):
        for index, center in enumerate(clusters):
            if abs(value - center) <= tolerance:
                clusters[index] = (center + value) / 2
                break
        else:
            clusters.append(value)
    return len(clusters)


def channel_sum(channel: Image.Image) -> int:
    """Return the sum of an 8-bit channel without deprecated pixel iterators."""
    return sum(value * count for value, count in enumerate(channel.histogram()))


def validate_summary_layout(
    plans: list[PlannedPlacement],
    canvas_width: int,
    canvas_height: int,
    min_photo_fraction: float,
    max_photo_fraction: float,
) -> None:
    if len(plans) < 2:
        raise SystemExit("--summary-layout requires at least two source placements")

    areas = sorted(
        (plan.fitted.width * plan.fitted.height for plan in plans), reverse=True
    )
    hero_ratio = areas[0] / areas[1]
    if hero_ratio < 1.4:
        raise SystemExit(
            "Summary hierarchy is too even: the largest visible photo must be at least "
            f"1.4x the next-largest (received {hero_ratio:.2f}x). Enlarge one hero card."
        )

    total_photo_fraction = sum(plan.canvas_photo_fraction for plan in plans)
    if total_photo_fraction < min_photo_fraction:
        raise SystemExit(
            f"Summary photos cover only {total_photo_fraction:.1%} of the canvas; hard "
            f"minimum is {min_photo_fraction:.1%} and the design target is 42–56%. "
            "Enlarge the hero and supporting photo cards."
        )
    if total_photo_fraction > max_photo_fraction:
        raise SystemExit(
            f"Summary photos cover {total_photo_fraction:.1%} of the canvas; hard maximum "
            f"is {max_photo_fraction:.1%} and the design target is 42–56%. Reduce the "
            "supporting photo cards and leave room for one coherent story-and-object cluster."
        )

    if len(plans) >= 4:
        x_centers = [plan.frame[0] + plan.frame[2] / 2 for plan in plans]
        y_centers = [plan.frame[1] + plan.frame[3] / 2 for plan in plans]
        x_clusters = cluster_count(x_centers, canvas_width * 0.055)
        y_clusters = cluster_count(y_centers, canvas_height * 0.055)
        if x_clusters * y_clusters == len(plans) and x_clusters > 1 and y_clusters > 1:
            raise SystemExit(
                "Summary placement reads as an aligned grid/contact sheet. Stagger frame "
                "centers, overlap paper layers, and rerun with one clearly dominant hero."
            )


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
    parser.add_argument(
        "--rotate",
        action="append",
        nargs=2,
        default=[],
        metavar=("SOURCE_ID", "DEGREES"),
        help=(
            "Optionally rotate the complete photo-card assembly. Repeat per source; "
            "absolute values above 6 degrees are rejected."
        ),
    )
    parser.add_argument(
        "--overlay",
        type=Path,
        help=(
            "Optional transparent full-canvas PNG placed after the locked photos. "
            "Use only for small clips, tape ends, corner tabs, thread, or leaves."
        ),
    )
    parser.add_argument(
        "--max-mat-fraction",
        type=float,
        default=0.18,
        help=(
            "Maximum blank mat inside any photo card after contain fitting. "
            "Default: 0.18."
        ),
    )
    parser.add_argument(
        "--min-single-photo-fraction",
        type=float,
        default=0.14,
        help=(
            "Hard minimum visible source-photo area for a one-photo page, as a fraction "
            "of the canvas. The design target is 0.18–0.30. Default: 0.14."
        ),
    )
    parser.add_argument(
        "--max-single-photo-fraction",
        type=float,
        default=0.40,
        help=(
            "Hard maximum visible source-photo area for a one-photo page, as a fraction "
            "of the canvas. This preserves room for the story cluster. Default: 0.40."
        ),
    )
    parser.add_argument(
        "--summary-layout",
        action="store_true",
        help="Validate hero hierarchy and reject aligned grid/contact-sheet summaries.",
    )
    parser.add_argument(
        "--min-summary-photo-fraction",
        type=float,
        default=0.34,
        help=(
            "Hard minimum summed visible photo area for a summary page. "
            "The design target is 0.42–0.56. Default: 0.34."
        ),
    )
    parser.add_argument(
        "--max-summary-photo-fraction",
        type=float,
        default=0.62,
        help=(
            "Hard maximum summed visible photo area for a summary page. "
            "The design target is 0.42–0.56. Default: 0.62."
        ),
    )
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()

    if not args.background.is_file():
        raise SystemExit(f"Missing background: {args.background}")
    if args.border < 0 or args.shadow < 0:
        raise SystemExit("--border and --shadow must be zero or greater")
    if not 0 <= args.max_mat_fraction < 1:
        raise SystemExit("--max-mat-fraction must be at least 0 and less than 1")
    if not 0 < args.min_single_photo_fraction < 1:
        raise SystemExit("--min-single-photo-fraction must be greater than 0 and less than 1")
    if not 0 < args.max_single_photo_fraction < 1:
        raise SystemExit("--max-single-photo-fraction must be greater than 0 and less than 1")
    if args.min_single_photo_fraction >= args.max_single_photo_fraction:
        raise SystemExit("single-photo minimum must be smaller than its maximum")
    if not 0 < args.min_summary_photo_fraction < 1:
        raise SystemExit("--min-summary-photo-fraction must be greater than 0 and less than 1")
    if not 0 < args.max_summary_photo_fraction < 1:
        raise SystemExit("--max-summary-photo-fraction must be greater than 0 and less than 1")
    if args.min_summary_photo_fraction >= args.max_summary_photo_fraction:
        raise SystemExit("summary-photo minimum must be smaller than its maximum")

    placements = [parse_placement(values) for values in args.place]
    source_ids = [source_id for source_id, _, _ in placements]
    if len(source_ids) != len(set(source_ids)):
        raise SystemExit("Every SOURCE_ID must be unique; duplicate source IDs are not allowed")
    if len(placements) > 1 and not args.summary_layout:
        raise SystemExit(
            "Multiple photo placements require --summary-layout so hierarchy, density, "
            "and anti-grid checks cannot be skipped."
        )

    rotations: dict[str, float] = {}
    for source_id, degrees_text in args.rotate:
        if source_id in rotations:
            raise SystemExit(f"Rotation for {source_id} was provided more than once")
        if source_id not in source_ids:
            raise SystemExit(f"Rotation references unknown SOURCE_ID: {source_id}")
        try:
            degrees = float(degrees_text)
        except ValueError as exc:
            raise SystemExit(f"Rotation for {source_id} must be a number") from exc
        if abs(degrees) > 6:
            raise SystemExit(
                f"Rotation for {source_id} is {degrees:g} degrees; maximum is ±6 degrees"
            )
        rotations[source_id] = degrees

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
        "layout": "summary" if args.summary_layout else "single",
        "validation": {
            "max_mat_fraction": args.max_mat_fraction,
            "min_single_photo_fraction": args.min_single_photo_fraction,
            "max_single_photo_fraction": args.max_single_photo_fraction,
            "min_summary_photo_fraction": args.min_summary_photo_fraction,
            "max_summary_photo_fraction": args.max_summary_photo_fraction,
            "summary_hierarchy": "largest visible photo >= 1.4x next-largest"
            if args.summary_layout
            else None,
        },
        "sources": [],
    }

    plans: list[PlannedPlacement] = []
    for source_id, path, (x, y, width, height) in placements:
        if not path.is_file():
            raise SystemExit(f"Missing source image for {source_id}: {path}")
        if width <= args.border * 2 or height <= args.border * 2:
            raise SystemExit(f"Frame for {source_id} is too small for the selected border")
        if x < 0 or y < 0 or x + width > canvas_width or y + height > canvas_height:
            raise SystemExit(f"Frame for {source_id} is outside the canvas")

        inner_width = width - args.border * 2
        inner_height = height - args.border * 2

        with Image.open(path) as source_file:
            source = ImageOps.exif_transpose(source_file).convert("RGBA")
        fitted = ImageOps.contain(
            source,
            (inner_width, inner_height),
            Image.Resampling.LANCZOS,
        )
        photo_x = args.border + (inner_width - fitted.width) // 2
        photo_y = args.border + (inner_height - fitted.height) // 2
        fitted_area = fitted.width * fitted.height
        mat_fraction = 1 - fitted_area / (inner_width * inner_height)
        canvas_photo_fraction = fitted_area / (canvas_width * canvas_height)

        if mat_fraction > args.max_mat_fraction:
            source_ratio = source.width / source.height
            raise SystemExit(
                f"Frame for {source_id} leaves {mat_fraction:.1%} blank mat; maximum is "
                f"{args.max_mat_fraction:.1%}. Regenerate or resize that photo card closer to "
                f"the source aspect ratio {source_ratio:.3f}."
            )

        plans.append(
            PlannedPlacement(
                source_id=source_id,
                path=path,
                frame=(x, y, width, height),
                fitted=fitted,
                photo_offset=(photo_x, photo_y),
                rotation=rotations.get(source_id, 0.0),
                mat_fraction=mat_fraction,
                canvas_photo_fraction=canvas_photo_fraction,
            )
        )

    if len(plans) == 1:
        photo_fraction = plans[0].canvas_photo_fraction
        if photo_fraction < args.min_single_photo_fraction:
            raise SystemExit(
                f"Single-page photo covers only {photo_fraction:.1%} of the canvas; hard "
                f"minimum is {args.min_single_photo_fraction:.1%} and the design target is "
                "18–30%. Enlarge the complete photo card without changing its aspect ratio."
            )
        if photo_fraction > args.max_single_photo_fraction:
            raise SystemExit(
                f"Single-page photo covers {photo_fraction:.1%} of the canvas; hard maximum "
                f"is {args.max_single_photo_fraction:.1%} and the design target is 18–30%. "
                "Reduce the complete photo card and use the recovered space for the title, journal "
                "copy, layered materials, and a compact decoration cluster."
            )
    if args.summary_layout:
        validate_summary_layout(
            plans,
            canvas_width,
            canvas_height,
            args.min_summary_photo_fraction,
            args.max_summary_photo_fraction,
        )

    locked_photo_mask = Image.new("L", canvas.size, 0)
    for plan in plans:
        source_id = plan.source_id
        path = plan.path
        x, y, width, height = plan.frame
        photo_x, photo_y = plan.photo_offset

        card = Image.new("RGBA", (width, height), frame_color)
        inner_width = width - args.border * 2
        inner_height = height - args.border * 2
        mat = Image.new("RGBA", (inner_width, inner_height), mat_color)
        card.paste(mat, (args.border, args.border))
        card.alpha_composite(plan.fitted, (photo_x, photo_y))

        card_photo_mask = Image.new("L", (width, height), 0)
        card_photo_mask.paste(plan.fitted.getchannel("A"), (photo_x, photo_y))

        if plan.rotation:
            rendered_card = card.rotate(
                plan.rotation,
                resample=Image.Resampling.BICUBIC,
                expand=True,
            )
            rendered_photo_mask = card_photo_mask.rotate(
                plan.rotation,
                resample=Image.Resampling.BICUBIC,
                expand=True,
            )
        else:
            rendered_card = card
            rendered_photo_mask = card_photo_mask

        center_x = x + width / 2
        center_y = y + height / 2
        rendered_x = round(center_x - rendered_card.width / 2)
        rendered_y = round(center_y - rendered_card.height / 2)
        if (
            rendered_x < 0
            or rendered_y < 0
            or rendered_x + rendered_card.width > canvas_width
            or rendered_y + rendered_card.height > canvas_height
        ):
            raise SystemExit(
                f"Rotated card for {source_id} extends outside the canvas; move its "
                "unrotated frame inward or reduce --rotate"
            )

        if args.shadow:
            shadow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
            shadow_plate = Image.new("RGBA", rendered_card.size, (0, 0, 0, 0))
            shadow_alpha = rendered_card.getchannel("A").point(lambda value: value * 92 // 255)
            shadow_plate.putalpha(shadow_alpha)
            shadow_layer.alpha_composite(
                shadow_plate,
                (rendered_x + args.shadow // 2, rendered_y + args.shadow // 2),
            )
            shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(args.shadow))
            canvas = Image.alpha_composite(canvas, shadow_layer)

        canvas.alpha_composite(rendered_card, (rendered_x, rendered_y))
        source_mask_canvas = Image.new("L", canvas.size, 0)
        source_mask_canvas.paste(rendered_photo_mask, (rendered_x, rendered_y))
        locked_photo_mask = ImageChops.lighter(locked_photo_mask, source_mask_canvas)

        allowed_changes = ["EXIF orientation", "uniform resize", "contain placement"]
        if plan.rotation:
            allowed_changes.append("shallow whole-card rotation")

        manifest["sources"].append(
            {
                "id": source_id,
                "path": str(path.resolve()),
                "frame": [x, y, width, height],
                "rotation_degrees": plan.rotation,
                "rendered_card_bbox": [
                    rendered_x,
                    rendered_y,
                    rendered_card.width,
                    rendered_card.height,
                ],
                "unrotated_photo_box": [
                    x + photo_x,
                    y + photo_y,
                    plan.fitted.width,
                    plan.fitted.height,
                ],
                "mat_fraction": round(plan.mat_fraction, 6),
                "canvas_photo_fraction": round(plan.canvas_photo_fraction, 6),
                "allowed_changes": allowed_changes,
            }
        )

    if args.overlay:
        if not args.overlay.is_file():
            raise SystemExit(f"Missing transparent foreground overlay: {args.overlay}")
        with Image.open(args.overlay) as overlay_source:
            if "A" not in overlay_source.getbands():
                raise SystemExit("--overlay must contain an alpha channel")
            overlay = ImageOps.exif_transpose(overlay_source).convert("RGBA")
        if overlay.size != canvas.size:
            raise SystemExit(
                f"Overlay must match the canvas exactly; received {overlay.width}x"
                f"{overlay.height}, expected {canvas_width}x{canvas_height}"
            )
        overlay_alpha = overlay.getchannel("A")
        alpha_sum = channel_sum(overlay_alpha)
        overlay_fraction = alpha_sum / (255 * canvas_width * canvas_height)
        if overlay_fraction > 0.35:
            raise SystemExit(
                f"Overlay covers {overlay_fraction:.1%} of the canvas; maximum is 35%. "
                "Use it only for small foreground clips, tape ends, tabs, thread, or leaves."
            )
        photo_alpha_sum = channel_sum(locked_photo_mask)
        overlap = ImageChops.multiply(overlay_alpha, locked_photo_mask)
        overlap_fraction = (
            channel_sum(overlap) / photo_alpha_sum if photo_alpha_sum else 0.0
        )
        if overlap_fraction > 0.02:
            raise SystemExit(
                f"Foreground overlay covers {overlap_fraction:.1%} of locked photo pixels; "
                "maximum is 2%. Move attachments to the outer card perimeter."
            )
        canvas = Image.alpha_composite(canvas, overlay)
        manifest["foreground_overlay"] = {
            "path": str(args.overlay.resolve()),
            "canvas_alpha_fraction": round(overlay_fraction, 6),
            "locked_photo_overlap_fraction": round(overlap_fraction, 6),
        }

    save_image(canvas, args.output)
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()
