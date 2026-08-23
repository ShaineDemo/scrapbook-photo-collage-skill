# Tencent WorkBuddy creation prompt

Create a custom Tencent WorkBuddy Skill named `scrapbook-photo-collage` from this repository.

Use `SKILL.md` as the canonical workflow. Include the files in `references/` as on-demand guidance, and retain `scripts/build_contact_sheet.py` as an optional helper. When WorkBuddy requires its own YAML metadata or implementation wrapper, generate the smallest valid wrapper and keep the procedure in `SKILL.md` instead of copying it into several files.

The Skill should activate when a user supplies 1–8 photos and asks for a scrapbook, journal, travel-diary, memory-board, or collage cover. One source should produce one single-photo collage. Two to eight sources should automatically produce one single-photo collage per source plus one combined summary collage, so six sources produce seven final images without the user having to request separate outputs. Every rendered result must be exact 3:4 vertical, and all results in a set must share the same pixel dimensions; verify the actual file dimensions rather than trusting the prompt alone. If the active WorkBuddy toolset includes reference-image generation or editing, render the complete set. Otherwise return the complete set of layout briefs and image-renderer prompts. Never claim that a bitmap was rendered without an image tool.

After creating the package, validate that every source receives a single-photo output, that the final summary accounts for every original source exactly once, and that the Skill can read the linked reference files.
