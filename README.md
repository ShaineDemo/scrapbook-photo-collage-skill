# Scrapbook Photo Collage Skill

[简体中文](README.zh-CN.md)

> Turn everyday photos into tactile scrapbook pages worth keeping.

A portable, open-source Agent Skill that turns 1–8 everyday photos into tactile scrapbook stories with atmosphere, personality, and a sense of occasion. Travel days, dinners, friendships, pets, quiet weekends, and small favorite moments can all become a polished set worth keeping and sharing.

> **Early-stage release:** this Skill has currently been tested only in **Codex**. Codex with ImageGen is the recommended environment while the workflow continues to mature.

## Why try it?

- **Give casual photos a finished look** — bring together color, lettering, and mood without learning complex layout tools.
- **Let each moment inspire the page** — people, places, weather, food, and emotion guide part of the creative direction, while playful keepsakes add surprise and personality.
- **Keep the memory real while making it playful** — photographs stay clear and recognizable while paper, notes, maps, tickets, cameras, records, books, fruit, coffee, tiny models, and other found details enrich the story.
- **Turn a photo group into a complete series** — receive individual pages for posting as well as a combined cover or recap.
- **Share it anywhere** — the consistent 3:4 vertical format works beautifully for Xiaohongshu/RedNote, Instagram, blogs, and personal albums.

Upload your photos and the Skill creates a story-rich medium-density set. By default, every single page and combined summary places a concentrated handmade collage island in front of an expansive photographic sky, soft clouds, warm horizon light and low distant treetops. Paper and fabric belong to the foreground island, not a flat canvas-filling background. Real photographs, expressive English lettering, a short journal note and playful objects come together as one tactile composition. One photo becomes one finished scrapbook page; two to eight photos become individual pages for each moment plus one recap. Every result shares the same **3:4 vertical ratio**. The outer scene is decorative atmosphere; the source photographs keep their own setting and light.

Version 1.9 bundles `examples/after/08-open-sky-stage.png` as its primary visual anchor for both single and summary pages. It is a style reference, not an additional source photo. A fresh installation carries the same baseline without needing reference images from a previous conversation. The older examples below illustrate material construction; their flat backgrounds are not the current default.

## The style: tactile photo scrapbook

This project calls the style **tactile photo scrapbook**: photography is combined with torn paper, translucent vellum, fabric, folded tape, handwritten titles, tickets, maps, notes, and small found details to create a page that feels assembled by hand.

The Skill draws part of its inspiration from the subjects, colors, setting, weather, activity, and mood of the current photos, then gives itself room to collect delightful objects that do not have to be literally present in the picture. A coastal scene may grow into tide notes and a folded chart, then gain a tiny camera, fruit slice, compass, radio, or toy sailboat for rhythm and character. A quiet indoor moment might combine fabric and window light with an open book, coffee cup, record, model car, or other charming keepsake. This roughly half-related, half-free approach keeps each page imaginative instead of mechanically literal.

Decorative titles and journal fragments are written in **English by default**, giving the set a compact editorial feel. Another language is used only when you explicitly ask for it.

The style can feel fresh, quiet, playful, romantic, editorial, or nostalgic without forcing every story into aged beige paper. Photographs remain recognizable and emotionally central, while titles, journal fragments, tactile materials, and small found objects turn the whole page into a miniature story world.

## What can you make with it?

- **Travel and city walks** — trip covers, destination diaries, road-trip pages, weekend recaps, and multi-stop memory boards.
- **Cafes, restaurants, and food** — favorite-dish pages, date-night records, cafe journals, menus, and food-trip summaries.
- **Friends, couples, and family** — birthdays, anniversaries, friendship memories, family albums, and monthly photo dumps.
- **Pets** — keepsake portraits, adoption-day pages, birthdays, everyday moments, and memorial pages.
- **Museums, exhibitions, books, and films** — exhibition notes, reading journals, cultural-day recaps, and personal collections.
- **Milestones and seasons** — graduation, moving, a new job, holidays, yearly reviews, and “life lately” summaries.
- **Social posts** — covers and carousel sets for Xiaohongshu/RedNote, Instagram, blogs, newsletters, or personal portfolios.

## Example: six photos become a complete scrapbook set

The same six source photos produce six individually art-directed pages plus one combined summary. The Skill keeps the photographs recognizable while changing the palette, materials, lettering, and decorations to match each subject.

<p align="center">
  <img src="examples/after/07-life-lately-summary.webp" alt="Combined scrapbook summary using all six source photos" width="720">
</p>

<p align="center"><strong>Six moments brought together as one “Life, Lately” story</strong></p>

<table>
  <thead>
    <tr>
      <th width="50%">Original photo</th>
      <th width="50%">Single-photo scrapbook result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="examples/before/01-dinner.webp" alt="Original evening dinner photo" width="420"></td>
      <td><img src="examples/after/01-dinner-after-blue-hour.webp" alt="Dinner After Blue Hour scrapbook result" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/02-museum.webp" alt="Original museum statue photo" width="420"></td>
      <td><img src="examples/after/02-quiet-wonders.webp" alt="Quiet Wonders museum scrapbook result" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/03-dog.webp" alt="Original dog photo" width="420"></td>
      <td><img src="examples/after/03-good-dog-days.webp" alt="Good Dog Days scrapbook result" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/04-cafe-solo.webp" alt="Original solo cafe portrait" width="420"></td>
      <td><img src="examples/after/04-a-quiet-cup.webp" alt="A Quiet Cup scrapbook result" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/05-cafe-couple.webp" alt="Original cafe couple photo" width="420"></td>
      <td><img src="examples/after/05-stay-a-little-longer.webp" alt="Stay a Little Longer scrapbook result" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/06-coast.webp" alt="Original coastal landscape photo" width="420"></td>
      <td><img src="examples/after/06-coastal-air.webp" alt="Coastal Air scrapbook result" width="420"></td>
    </tr>
  </tbody>
</table>

## Requirements

This is an early-stage Skill and has currently been tested only in **Codex**. We recommend using Codex on a surface that provides ImageGen. A finished bitmap requires reference-image generation or editing; without an available image tool, Codex can still produce the art direction and renderer prompt but cannot render the final scrapbook images.

Python 3 and [Pillow](https://python-pillow.org/) are optional. Besides building numbered contact sheets, they enable a safer fallback that creates the handmade surround separately and places the untouched original photos afterward, preventing a weak renderer from deleting or repainting people and scenes.

## Install

Clone the repository and install it for Codex:

```bash
python3 scripts/install_skill.py --target codex
```

The installer copies the Skill to `~/.codex/skills/scrapbook-photo-collage/`. Start a new Codex task after installation so the latest version is discovered cleanly.

## Use

Invoke the installed Skill explicitly or ask naturally:

> Use the scrapbook photo collage skill to turn these eight travel photos into a cohesive 3:4 scrapbook set. Create one English-copy design for each photo and finish with a combined summary collage. Keep the people recognizable, leave a visible atmospheric background around each scrapbook island, and mix photo-inspired details with playful found keepsakes.

## Contact sheets

When an image tool accepts fewer references than the number of source photos:

```bash
python3 -m pip install Pillow
python3 scripts/build_contact_sheet.py photo1.jpg photo2.jpg photo3.jpg photo4.jpg photo5.jpg \
  --output-dir ./contact-sheets --per-sheet 4
```

The generated indexes do not crop the source photos and label each tile with a stable source number.

## Repository layout

```text
SKILL.md                         Canonical Skill instructions
agents/openai.yaml               Codex UI metadata
references/visual-system.md      Density, materials, and decoration logic
references/prompt-template.md    Renderer prompt structure and revision prompts
references/source-preservation.md Locked-photo fallback and fidelity checks
scripts/build_contact_sheet.py   Numbered source-index generator
scripts/compose_locked_photos.py Deterministic original-photo compositor
scripts/install_skill.py         Codex installer entry point
```

## Privacy

The repository includes only the project author's authorized demonstration images under `examples/`. The Skill does not upload images by itself. Your chosen agent and image provider determine where attached photos are processed.

## License

[MIT](LICENSE)
