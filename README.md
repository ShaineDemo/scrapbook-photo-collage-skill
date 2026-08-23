# Scrapbook Photo Collage Skill

[简体中文](README.zh-CN.md)

A portable, open-source Agent Skill for turning 1–8 user photos into tactile scrapbook covers, travel diaries, memory boards, and social-media collages.

It captures the design decisions that usually separate a convincing scrapbook from a generic template:

- every supplied photo receives one individual design and appears exactly once in the combined summary;
- one clear hero and asymmetric supporting frames;
- generated lettering for expressive short titles, with a deterministic option for exact copy;
- varied paper, vellum, fabric, metal, tape, and natural textures;
- tape with real folds, buckling, torn fibers, and curled corners;
- decorations derived from the current photo content instead of a fixed camera/seal/stamp bundle;
- a controlled density range that keeps the photos dominant.

The default is a complete balanced, medium-density scrapbook set. One uploaded photo produces one single-photo collage. Two to eight uploaded photos produce one single-photo collage per source plus one combined summary collage. Six photos therefore produce seven final images: six individual designs followed by one six-photo summary. Extra style variants or alternate ratios are generated only when requested.

## Example: six photos become a complete scrapbook set

The same six source photos produce six individually art-directed pages plus one combined summary. The Skill keeps the photographs recognizable while changing the palette, materials, lettering, and decorations to match each subject.

<p align="center">
  <img src="examples/after/07-life-lately-summary.webp" alt="Combined scrapbook summary using all six source photos" width="720">
</p>

<p align="center"><strong>Final combined summary — all six originals, each used exactly once</strong></p>

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

Python 3 and [Pillow](https://python-pillow.org/) are optional and used only when more source photos must be packed into numbered contact sheets.

## Install

Clone the repository and run one of:

```bash
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target claude
python3 scripts/install_skill.py --target kimi
python3 scripts/install_skill.py --target deepcode
python3 scripts/install_skill.py --target qoder
python3 scripts/install_skill.py --target qoderwork
python3 scripts/install_skill.py --target codebuddy
```

For TRAE and 豆包, see [cross-agent compatibility](references/compatibility.md). A generic standalone prompt is available at [adapters/portable-agent-prompt.md](adapters/portable-agent-prompt.md).

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
references/compatibility.md      Product-specific installation guidance
scripts/build_contact_sheet.py   Numbered source-index generator
scripts/install_skill.py         Portable installer
adapters/                        TRAE and generic chat fallbacks
```

## Privacy

The repository includes only the project author's authorized demonstration images under `examples/`. The Skill does not upload images by itself. Your chosen agent and image provider determine where attached photos are processed.

## License

[MIT](LICENSE)
