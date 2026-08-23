#!/usr/bin/env python3
"""Install this Skill into a supported agent's user-level skills directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_NAME = "scrapbook-photo-collage"
DEFAULT_ROOTS = {
    "codex": Path.home() / ".codex" / "skills",
    "workbuddy": Path.home() / ".workbuddy" / "skills",
    "claude": Path.home() / ".claude" / "skills",
    "kimi": Path.home() / ".kimi-code" / "skills",
    "deepcode": Path.home() / ".agents" / "skills",
    "qoder": Path.home() / ".qoder" / "skills",
    "qoderwork": Path.home() / ".qoderwork" / "skills",
    "grok": Path.home() / ".grok" / "skills",
    "generic": Path.home() / ".agents" / "skills",
}
INCLUDE = ("SKILL.md", "LICENSE", "agents", "references", "scripts", "adapters")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=DEFAULT_ROOTS, default="generic")
    parser.add_argument("--dest", type=Path, help="Override the target skills root directory")
    parser.add_argument("--force", action="store_true", help="Replace an existing installation")
    args = parser.parse_args()

    source = Path(__file__).resolve().parents[1]
    root = (args.dest or DEFAULT_ROOTS[args.target]).expanduser().resolve()
    destination = root / SKILL_NAME

    if destination.exists():
        if not args.force:
            raise SystemExit(f"Already exists: {destination}\nRe-run with --force to replace it.")
        shutil.rmtree(destination)

    destination.mkdir(parents=True)
    for name in INCLUDE:
        item = source / name
        if not item.exists():
            continue
        target = destination / name
        if item.is_dir():
            shutil.copytree(item, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        else:
            shutil.copy2(item, target)

    print(destination)


if __name__ == "__main__":
    main()
