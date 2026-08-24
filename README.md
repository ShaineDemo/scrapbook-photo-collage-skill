# Scrapbook Photo Collage Skill

[简体中文](README.zh-CN.md)

> Turn everyday photos into tactile scrapbook pages worth keeping.

A portable, open-source Agent Skill that turns 1–8 everyday photos into tactile scrapbook stories with atmosphere, personality, and a sense of occasion. Travel days, dinners, friendships, pets, quiet weekends, and small favorite moments can all become a polished set worth keeping and sharing.

## Why try it?

- **Give casual photos a finished look** — bring together color, lettering, and mood without learning complex layout tools.
- **Let each moment inspire the page** — people, places, weather, food, and emotion guide the creative direction.
- **Keep the memory real while making it playful** — photographs stay clear and recognizable while paper, notes, maps, tickets, and found details enrich the story.
- **Turn a photo group into a complete series** — receive individual pages for posting as well as a combined cover or recap.
- **Share it anywhere** — the consistent 3:4 vertical format works beautifully for Xiaohongshu/RedNote, Instagram, blogs, and personal albums.

Upload your photos and the Skill creates a story-rich medium-density set: each page gathers a real photograph, expressive lettering, a short journal note, layered paper and fabric, and a varied cluster of small objects into one tactile composition. One photo becomes one finished scrapbook page; two to eight photos become individual pages for each moment plus one recap that brings the whole story together. Upload six photos, for example, and you receive six individual designs and one summary cover. Every result shares the same **3:4 vertical ratio**, ready to publish as a cohesive series.

## The style: tactile photo scrapbook

This project calls the style **tactile photo scrapbook**: photography is combined with torn paper, translucent vellum, fabric, folded tape, handwritten titles, tickets, maps, notes, and small found details to create a page that feels assembled by hand.

The Skill draws inspiration from the subjects, colors, setting, weather, activity, and mood of the current photos, then builds a visual world around that moment. A coastal scene may grow into tide notes, wave vellum, and a folded chart; a museum visit may pair with catalog slips, rice paper, ink studies, and architectural lines; a quiet indoor moment may become a soft composition of fabric, notes, and window light.

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

The Skill is model-agnostic, but a finished bitmap requires the host agent to expose an image-generation or image-editing tool with reference-image support. A text-only agent can still produce the complete art direction and renderer prompt.

Host support is not the same as rendering support. Codex can render when ImageGen is available. WorkBuddy supports custom Skills and can complete this workflow when its active account, model, and toolset expose reference-image generation or editing. Grok Build installs the Skill natively and can use Grok Imagine, including reference-image editing when that tool or API is connected. Qoder currently documents text-to-image only. Claude Code, Kimi Code, DeepSeek Harness, and QoderWork require an external image model, plugin, API, or MCP tool for this photo-preserving workflow. See the [verified capability matrix](references/compatibility.md#verified-rendering-capabilities) before installation.

Python 3 and [Pillow](https://python-pillow.org/) are optional. Besides building numbered contact sheets, they enable a safer fallback that creates the handmade surround separately and places the untouched original photos afterward, preventing a weak renderer from deleting or repainting people and scenes.

## Install

Clone the repository and run one of:

```bash
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target workbuddy
python3 scripts/install_skill.py --target claude
python3 scripts/install_skill.py --target kimi
python3 scripts/install_skill.py --target deepseek-harness
python3 scripts/install_skill.py --target qoder
python3 scripts/install_skill.py --target qoderwork
python3 scripts/install_skill.py --target grok-build
```

These targets correspond to **Codex**, **WorkBuddy**, **Claude Code**, **Kimi Code CLI**, **DeepSeek Harness**, **Qoder IDE/CLI**, **QoderWork**, and **Grok Build**. Qoder and QoderWork are separate products with separate Skill directories, so each has its own target.

WorkBuddy can also install the Skill conversationally: start a new task, paste this repository URL, and ask it to install the Skill. The current desktop product places imported Skills under `~/.workbuddy-ai/skills/`; restart WorkBuddy or begin a new task after installation. See the [WorkBuddy installation prompt](adapters/workbuddy-creation-prompt.md) for a ready-to-paste request. For TRAE and 豆包, see [cross-agent compatibility](references/compatibility.md). A generic standalone prompt is available at [adapters/portable-agent-prompt.md](adapters/portable-agent-prompt.md).

## Use

Invoke the installed Skill explicitly or ask naturally:

> Use the scrapbook photo collage skill to turn these eight travel photos into a cohesive 3:4 scrapbook set. Create one design for each photo and finish with a combined summary collage. Keep the people recognizable and make the decorations respond to the places and objects in the photos.

For Kimi Code CLI:

```text
/skill:scrapbook-photo-collage Create a balanced 3:4 travel-diary cover from the attached photos.
```

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
SKILL.md                         Canonical cross-agent instructions
agents/openai.yaml               Codex UI metadata
references/visual-system.md      Density, materials, and decoration logic
references/prompt-template.md    Renderer prompt structure and revision prompts
references/source-preservation.md Locked-photo fallback and fidelity checks
references/compatibility.md      Product-specific installation guidance
scripts/build_contact_sheet.py   Numbered source-index generator
scripts/compose_locked_photos.py Deterministic original-photo compositor
scripts/install_skill.py         Portable installer
adapters/                        TRAE and generic chat fallbacks
```

## Privacy

The repository includes only the project author's authorized demonstration images under `examples/`. The Skill does not upload images by itself. Your chosen agent and image provider determine where attached photos are processed.

## License

[MIT](LICENSE)
