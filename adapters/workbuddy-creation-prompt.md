# Tencent WorkBuddy creation prompt

Create a custom Tencent WorkBuddy Skill named `scrapbook-photo-collage` from this repository.

Use `SKILL.md` as the canonical workflow. Include the files in `references/` as on-demand guidance, and retain `scripts/build_contact_sheet.py` as an optional helper. When WorkBuddy requires its own YAML metadata or implementation wrapper, generate the smallest valid wrapper and keep the procedure in `SKILL.md` instead of copying it into several files.

The Skill should activate when a user supplies 1–8 photos and asks for a scrapbook, journal, travel-diary, memory-board, or collage cover. If the active WorkBuddy toolset includes reference-image generation or editing, render the result. Otherwise return the complete layout brief and image-renderer prompt. Never claim that a bitmap was rendered without an image tool.

After creating the package, validate that the Skill can account for every source photo exactly once and that it can read the linked reference files.
