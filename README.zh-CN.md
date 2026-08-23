# Scrapbook Photo Collage Skill

> 把普通照片，变成值得收藏的纸感手账。

这是一个可移植的开源 Agent Skill，用于把 1–8 张用户照片制作成具有真实纸张、胶带、手写字与内容化装饰的手账拼贴、旅行日记、回忆板或社交媒体封面。

它重点解决以下问题：

- 每张原图都有一张独立成品，并在最终总结拼贴中各出现一次，不漏图、不重复；
- 主图明确，其他照片采用非对称层级，而不是平均网格；
- 照片、纸张、硫酸纸、布料、金属与胶带具有不同质感；
- 胶带具有真实撕边、褶皱、折脊、翘角与轻微阴影；
- 装饰物根据本次照片内容动态选择，不再固定复用相机、印章、唱片或咖啡；
- 控制装饰密度和 3D 物体数量，让照片始终是主体。

默认输出一套“中密度”成品，不需要用户额外要求逐张制作。上传 1 张照片时生成 1 张单图拼贴；上传 2–8 张照片时，先为每张原图分别生成 1 张单图拼贴，再生成 1 张包含全部原图的总结拼贴。因此上传 6 张照片时默认输出 7 张成品：6 张单图和 1 张六图合并图。只有额外风格版本或不同比例需要用户明确提出。

## 风格名称：纸感照片手账

我们把这种风格称为 **纸感照片手账**：以真实照片为主体，结合撕边纸张、半透明硫酸纸、布料、带褶皱的胶带、手写标题、票据、地图、便签和少量纪念物，形成像亲手剪贴出来的故事页面。

它不是给所有照片套同一套模板。Skill 会先观察照片中的人物、地点、颜色、天气、活动与情绪，再决定配色和装饰物。海滨照片可以延伸出潮汐卡、浪花硫酸纸和海岸地图；博物馆照片可以使用藏品票据、宣纸、墨迹与建筑线稿。相机、印章、火漆、唱片或咖啡杯不会成为每张图都重复出现的固定套餐。

这种风格既可以清新、安静、可爱和浪漫，也可以具有杂志感或怀旧感，不会把所有故事都强行做成泛黄旧纸。照片始终清晰、可辨、占据主体，纸张和装饰负责补充氛围、节奏与记忆感。

## 可以用在哪些场景？

- **旅行与城市漫步**：旅行封面、目的地日记、公路旅行、周末记录和多地点回忆板。
- **咖啡馆、美食与餐厅**：探店记录、约会晚餐、喜欢的菜、咖啡日记和美食旅行总结。
- **朋友、情侣与家人**：生日、纪念日、友情记录、家庭相册和月度照片回顾。
- **宠物生活**：宠物写真、领养纪念、生日、日常片段和纪念页面。
- **博物馆、展览、书籍与电影**：观展记录、阅读手账、文化一日游和个人收藏整理。
- **成长节点与四季记录**：毕业、搬家、新工作、节日、年度总结和“最近的生活”。
- **社交媒体内容**：小红书、Instagram、博客、Newsletter 或个人作品集的封面与多图轮播。

## 示例：六张照片生成一套完整手账

同一组 6 张原图会生成 6 张分别设计的单图作品，以及 1 张包含全部原图的总结拼贴。Skill 会保持照片主体清晰可辨，同时根据每张照片的题材改变配色、材质、手写字和装饰物。

<p align="center">
  <img src="examples/after/07-life-lately-summary.webp" alt="使用全部六张原图制作的合并手账拼贴" width="720">
</p>

<p align="center"><strong>最终合并图——六张原图各使用一次，不遗漏、不重复</strong></p>

<table>
  <thead>
    <tr>
      <th width="50%">原始照片</th>
      <th width="50%">单图手账成品</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="examples/before/01-dinner.webp" alt="晚餐原图" width="420"></td>
      <td><img src="examples/after/01-dinner-after-blue-hour.webp" alt="蓝调时刻晚餐手账" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/02-museum.webp" alt="博物馆雕像原图" width="420"></td>
      <td><img src="examples/after/02-quiet-wonders.webp" alt="博物馆主题手账" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/03-dog.webp" alt="狗狗原图" width="420"></td>
      <td><img src="examples/after/03-good-dog-days.webp" alt="狗狗主题手账" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/04-cafe-solo.webp" alt="单人咖啡馆原图" width="420"></td>
      <td><img src="examples/after/04-a-quiet-cup.webp" alt="安静咖啡时光手账" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/05-cafe-couple.webp" alt="双人咖啡馆原图" width="420"></td>
      <td><img src="examples/after/05-stay-a-little-longer.webp" alt="双人咖啡时光手账" width="420"></td>
    </tr>
    <tr>
      <td><img src="examples/before/06-coast.webp" alt="海岸风景原图" width="420"></td>
      <td><img src="examples/after/06-coastal-air.webp" alt="海滨旅行主题手账" width="420"></td>
    </tr>
  </tbody>
</table>

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

> 使用 scrapbook-photo-collage Skill，把我上传的八张旅行照片做成一套 3:4 手账作品：每张照片各生成一张，最后再生成一张八图总结拼贴。人物保持一致，装饰物根据照片中的地点、食物和纪念物生成。

## 隐私

仓库仅在 `examples/` 中包含项目作者授权用于展示的示例照片。Skill 本身不会自行上传图片，实际图片由你选择的 Agent 与生图服务处理。

## 许可证

[MIT](LICENSE)
