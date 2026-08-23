# Scrapbook Photo Collage Skill

这是一个可移植的开源 Agent Skill，用于把 1–8 张用户照片制作成具有真实纸张、胶带、手写字与内容化装饰的手账拼贴、旅行日记、回忆板或社交媒体封面。

它重点解决以下问题：

- 多图中每张原图只出现一次，不漏图、不重复；
- 主图明确，其他照片采用非对称层级，而不是平均网格；
- 照片、纸张、硫酸纸、布料、金属与胶带具有不同质感；
- 胶带具有真实撕边、褶皱、折脊、翘角与轻微阴影；
- 装饰物根据本次照片内容动态选择，不再固定复用相机、印章、唱片或咖啡；
- 控制装饰密度和 3D 物体数量，让照片始终是主体。

默认输出一张“中密度”成品。例如用户上传 6 张照片时，Skill 会生成 1 张包含 6 个不同照片画面的多图拼贴；只有用户明确要求逐张制作、多个版本或轮播组图时，才输出多张图片。

## 能力要求

Skill 本身是模型无关的工作流说明，不会凭空给 Agent 增加生图能力。要输出最终图片，宿主 Agent 仍需提供支持参考图的生图/改图模型、API、插件或 MCP 工具。纯文本 Agent 会输出完整构图方案和可交付给生图模型的 Prompt。

Python 3 与 Pillow 仅用于在参考图数量超过模型上限时生成带编号的无裁切素材索引图，不是必须依赖。

## 安装

克隆仓库后运行对应命令：

```bash
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target claude
python3 scripts/install_skill.py --target kimi
python3 scripts/install_skill.py --target deepcode
python3 scripts/install_skill.py --target qoder
python3 scripts/install_skill.py --target qoderwork
python3 scripts/install_skill.py --target codebuddy
```

- Codex、Claude Code、Kimi Code、Deep Code、Qoder、QoderWork、CodeBuddy：原生或项目级 `SKILL.md`。
- TRAE：使用 [TRAE 项目规则适配文件](adapters/trae-project_rules.md)。
- 豆包及不支持文件型 Skill 的聊天产品：将 [通用智能体提示词](adapters/portable-agent-prompt.md) 放入自定义智能体设定或知识库。
- WorkBuddy 自定义 Skill 页面：把 [WorkBuddy 创建指令](adapters/workbuddy-creation-prompt.md) 交给 WorkBuddy，让其生成所需的本地包装文件。

更完整的安装目录和能力限制见 [兼容性说明](references/compatibility.md)。

## 使用示例

> 使用 scrapbook-photo-collage Skill，把我上传的八张旅行照片做成一张 3:4 手账封面。每张图只出现一次，人物保持一致，装饰物根据照片中的地点、食物和纪念物生成。

## 隐私

仓库不包含任何用户照片，也不会自行上传图片。图片由你选择的 Agent 与生图服务处理。

## 许可证

[MIT](LICENSE)
