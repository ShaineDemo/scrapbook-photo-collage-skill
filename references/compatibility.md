# Compatibility and installation

The canonical package follows the open Agent Skills directory format: a folder with `SKILL.md` plus optional `scripts/` and `references/`. Rendering still depends on the host agent exposing an image-generation or image-editing tool.

## Native `SKILL.md` hosts

| Product | Suggested user-level location | Notes |
| --- | --- | --- |
| OpenAI Codex | `~/.codex/skills/scrapbook-photo-collage/` | Restart or begin a new task after installation. |
| Claude Code | `~/.claude/skills/scrapbook-photo-collage/` | Project skills can also live under `.claude/skills/`. |
| Kimi Code CLI | `~/.kimi-code/skills/scrapbook-photo-collage/` | Also discovers `~/.agents/skills/`; invoke with `/skill:scrapbook-photo-collage`. |
| DeepSeek Deep Code | `~/.agents/skills/scrapbook-photo-collage/` | Project scope: `.deepcode/skills/scrapbook-photo-collage/`. |
| Qoder IDE/CLI | `~/.qoder/skills/scrapbook-photo-collage/` | Project scope: `.qoder/skills/scrapbook-photo-collage/`. |
| QoderWork | `~/.qoderwork/skills/scrapbook-photo-collage/` | It can also install from a pasted GitHub repository URL. |
| Tencent CodeBuddy | `~/.codebuddy/skills/scrapbook-photo-collage/` or project `.codebuddy/skills/` | Availability depends on the CodeBuddy/WorkBuddy surface in use. |

Run the portable installer:

```bash
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target claude
python3 scripts/install_skill.py --target kimi
python3 scripts/install_skill.py --target deepcode
python3 scripts/install_skill.py --target qoder
python3 scripts/install_skill.py --target qoderwork
python3 scripts/install_skill.py --target codebuddy
```

Use `--dest /custom/skills/root` for an unlisted host or a custom data directory.

## TRAE

TRAE supports project and user rules. Copy `adapters/trae-project_rules.md` to `.trae/project_rules.md` in the target project and keep this repository accessible to the agent. The adapter tells TRAE to load the canonical `SKILL.md` only for relevant collage tasks.

## 豆包 / chat products without file-based Skills

At the time this package was published, 豆包 exposes custom agents but not a documented filesystem `SKILL.md` installer. Paste `adapters/portable-agent-prompt.md` into the custom agent's role/background instructions or upload it as knowledge. Attach the source photos in the conversation.

The same fallback works for a plain DeepSeek chat, Kimi chat, or any agent that can read a Markdown prompt but cannot discover Skill folders.

## Tencent WorkBuddy custom-skill surface

Some WorkBuddy surfaces generate a custom Skill package rather than scanning an Agent Skills folder. Start a new WorkBuddy task and paste [the WorkBuddy creation prompt](../adapters/workbuddy-creation-prompt.md). It tells WorkBuddy to use the canonical `SKILL.md`, references, and portable fallback as the implementation source.

## Capability limitation

An instruction Skill can choose a composition, build prompts, and run available tools; it cannot add an image model to a host that has none. In a text-only host, expect the complete set of layout briefs and renderer prompts. Connect an image model through the host's native image tool, API, plugin, or MCP integration to render the final bitmaps.

For two to eight input photos, the default workflow makes `N + 1` image-rendering calls or equivalent batch jobs: one single-photo collage per source plus one combined summary. Hosts with generation quotas or per-task output limits must not silently replace that set with only the summary image; they should preserve all planned outputs and clearly report the rendering limitation.

## Primary references

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code skills](https://code.claude.com/docs/en/slash-commands)
- [Kimi Code Agent Skills](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html)
- [DeepSeek Deep Code integration](https://api-docs.deepseek.com/quick_start/agent_integrations/deepcode)
- [Qoder skills](https://docs.qoder.com/extensions/skills)
- [QoderWork skills](https://docs.qoder.com/qoderwork/skills)
- [CodeBuddy skills in large repositories](https://www.workbuddy.ai/docs/cli/large-codebases)
- [TRAE rules overview](https://www.trae.ai/ide/)
- [豆包 feature introduction](https://www.doubao.com/legal/feature_intro)
