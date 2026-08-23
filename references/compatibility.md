# Compatibility and installation

The canonical package follows the open Agent Skills directory format: a folder with `SKILL.md` plus optional `scripts/` and `references/`. Rendering still depends on the host agent exposing an image-generation or image-editing tool.

## Supported hosts and staging locations

| Product | Suggested user-level location | Notes |
| --- | --- | --- |
| OpenAI Codex | `~/.codex/skills/scrapbook-photo-collage/` | Restart or begin a new task after installation. |
| Tencent WorkBuddy | `~/.workbuddy/skills/scrapbook-photo-collage/` | Stages the canonical package in WorkBuddy's configuration space; some versions require installation or conversion through the Skills UI. |
| Claude Code | `~/.claude/skills/scrapbook-photo-collage/` | Project skills can also live under `.claude/skills/`. |
| Kimi Code CLI | `~/.kimi-code/skills/scrapbook-photo-collage/` | Also discovers `~/.agents/skills/`; invoke with `/skill:scrapbook-photo-collage`. |
| DeepSeek Harness | `~/.dsh/skills/scrapbook-photo-collage/` | Project scope: `.dsh/skills/scrapbook-photo-collage/`; also discovers the shared `.agents/skills/` roots. |
| Qoder IDE/CLI | `~/.qoder/skills/scrapbook-photo-collage/` | Project scope: `.qoder/skills/scrapbook-photo-collage/`. |
| QoderWork | `~/.qoderwork/skills/scrapbook-photo-collage/` | It can also install from a pasted GitHub repository URL. |
| xAI Grok Build | `~/.grok/skills/scrapbook-photo-collage/` | Project scope: `.grok/skills/scrapbook-photo-collage/`; also discovers `~/.agents/skills/`. |

Run the portable installer:

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

## Verified rendering capabilities

Checked against official product documentation on 2026-08-23. “Native Skill” means the product can discover this package; it does not imply that the product can render the final bitmaps.

| Host surface | Native Skill | Built-in image capability relevant to this workflow | Practical status |
| --- | --- | --- | --- |
| OpenAI Codex | Yes | Image generation is available on Codex surfaces that expose ImageGen. | **Full when ImageGen is present.** Verify the active surface before starting. |
| Tencent WorkBuddy | Custom Skill | WorkBuddy documents custom Skills and models covering multimodal and image-processing scenarios; available models and tools vary by version, account, and service availability. | **Full only when the active WorkBuddy toolset exposes reference-image generation or editing.** Otherwise use the renderer-prompt fallback. |
| Claude Code | Yes | Claude does not natively generate photos or illustrations; Claude Code can connect tools through MCP. | **External image generation/editing tool required.** |
| Kimi Code CLI | Yes | Official built-ins document image/video input and inspection, but not image generation or editing. | **External image generation/editing tool required.** |
| DeepSeek Harness | Yes | The official harness supports Skills and composable tool plugins, but its product documentation does not establish a built-in reference-image generator/editor. | **External image generation/editing plugin or tool required.** |
| Qoder IDE/CLI | Yes | `/gen-image` provides text-to-image generation; official documentation does not establish reference-image editing. | **Partial.** External image-to-image support is required for faithful photo preservation. |
| QoderWork | Yes | Design creates code-based visual artifacts; the official documentation does not establish raster reference-image editing. | **External image generation/editing tool required for this Skill.** |
| xAI Grok Build | Yes | `/imagine` provides text-to-image. Grok Imagine APIs/tools support image generation and editing with up to three reference images per request. | **Full when the Imagine editing tool/API is connected; text-to-image alone is partial.** Use contact sheets when source count exceeds the reference limit. |

Consumer chat products are separate surfaces. Grok web/apps and 豆包 can generate images, but that does not prove that an installed file-based Skill can invoke their image renderer. Treat them as portable-prompt hosts unless their active agent surface exposes both Skill loading and a callable reference-image editing tool.

## Primary references

- [Agent Skills specification](https://agentskills.io/specification)
- [Codex image generation](https://learn.chatgpt.com/docs/image-generation)
- [Claude Code skills](https://code.claude.com/docs/en/slash-commands)
- [Claude image-generation limitation](https://support.claude.com/en/articles/9002504-can-claude-produce-images)
- [Kimi Code Agent Skills](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html)
- [Kimi Code built-in tools](https://www.kimi.com/code/docs/en/kimi-code-cli/reference/tools.html)
- [DeepSeek Harness overview](https://www.deepseek.com/harness/en/)
- [DeepSeek Harness Skill filesystem](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md)
- [Qoder skills](https://docs.qoder.com/extensions/skills)
- [Qoder image generation](https://docs.qoder.com/user-guide/chat/tools)
- [QoderWork skills](https://docs.qoder.com/qoderwork/skills)
- [QoderWork Design](https://docs.qoder.com/qoderwork/design)
- [WorkBuddy custom Skills](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills)
- [WorkBuddy model configuration](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model)
- [Grok Build skills](https://docs.x.ai/build/features/skills-plugins-marketplaces)
- [Grok Build image command](https://docs.x.ai/build/modes-and-commands)
- [Grok Imagine generation and editing](https://docs.x.ai/developers/model-capabilities/imagine)
- [TRAE rules overview](https://www.trae.ai/ide/)
- [豆包 feature introduction](https://www.doubao.com/legal/feature_intro)
