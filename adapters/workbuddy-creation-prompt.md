# Tencent WorkBuddy installation prompt

Install the `scrapbook-photo-collage` Skill from this GitHub repository:

`https://github.com/ShaineDemo/scrapbook-photo-collage-skill`

Install it as a user-level Skill available across projects. Use `SKILL.md` as the canonical workflow, keep the files in `references/` as on-demand guidance, retain `examples/after/` including `08-open-sky-stage.png` as the primary execution-time background anchor for both single pages and summaries, and retain `requirements.txt` plus both `scripts/build_contact_sheet.py` and `scripts/compose_locked_photos.py` as optional helpers. Add any WorkBuddy-specific frontmatter or wrapper required by the current product without duplicating the canonical instructions.

The Skill should activate when a user supplies 1–8 photos and asks for a scrapbook, journal, travel-diary, memory-board, or collage cover. One source should produce one single-photo collage. Two to eight sources should automatically produce one single-photo collage per source plus one combined summary collage, so six sources produce seven final images without the user having to request separate outputs. Every rendered result must be exact 3:4 vertical, and all results in a set must share the same pixel dimensions; verify the actual file dimensions rather than trusting the prompt alone. If the active WorkBuddy toolset includes reference-image generation or editing, render the complete set. Otherwise return the complete set of layout briefs and image-renderer prompts. Never claim that a bitmap was rendered without an image tool.

After creating the package, validate that every source receives a single-photo output, that the final summary accounts for every original source exactly once, that no person or important source content is removed or repainted, and that the Skill can read the linked reference files.
