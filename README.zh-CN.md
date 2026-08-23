# Scrapbook Photo Collage Skill

> 把普通照片，变成值得收藏的纸感手账。

这是一个可移植的开源 Agent Skill，可以把 1–8 张日常照片变成有氛围、有细节、也更有故事感的纸感手账。旅行、聚会、约会、美食、宠物或某个普通周末，都可以被整理成值得收藏和分享的一组作品。

## 为什么值得试试？

- **让随手拍更有作品感**：普通照片也能拥有完整的配色、标题和画面氛围。
- **让照片讲出自己的故事**：人物、地点、天气、食物和情绪都会成为设计灵感。
- **保留真实又增加趣味**：照片仍然清晰自然，周围加入纸张、手写字、票据、地图和小物件，让画面更丰富。
- **一组照片自动变成完整系列**：既有适合单独发布的页面，也有适合作为封面或回顾的合辑。
- **适合直接分享**：统一的 3:4 竖版画面可用于小红书、Instagram、博客和个人相册。

上传照片后，Skill 默认会制作一套丰富但不过度拥挤的“中密度”作品。1 张照片会变成 1 张完整手账；2–8 张照片会得到每个瞬间的独立页面，以及 1 张串联全部回忆的合辑。比如上传 6 张照片，就会收获 6 张单图作品和 1 张总结封面。所有成品统一为 **3:4 竖版比例**，可以直接组成风格连贯的发布系列。

## 风格名称：纸感照片手账

我们把这种风格称为 **纸感照片手账**：以真实照片为主体，结合撕边纸张、半透明硫酸纸、布料、带褶皱的胶带、手写标题、票据、地图、便签和少量纪念物，形成像亲手剪贴出来的故事页面。

Skill 会从照片中的人物、地点、颜色、天气、活动与情绪寻找灵感，再为这一刻选择合适的配色和细节。海滨照片可以延伸出潮汐卡、浪花硫酸纸和海岸地图；博物馆照片可以搭配藏品票据、宣纸、墨迹与建筑线稿；温暖的室内时光也可以发展成布料、便签和窗边光影组成的安静页面。

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

<p align="center"><strong>六个生活片段，汇成一页完整的「最近生活」</strong></p>

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

“能安装 Skill”不等于“能完成出图”。Codex 在提供 ImageGen 的产品界面中可以直接渲染；WorkBuddy 支持自定义 Skill，并可在当前账号、模型和工具集提供参考图生成或编辑能力时完成本工作流；Grok Build 可原生安装 Skill，并可在接入 Grok Imagine 工具或 API 后进行参考图编辑。Qoder 目前官方只明确提供文生图。Claude Code、Kimi Code、Deep Code 与 QoderWork 要完成这种保留原照片的拼贴，需要另外连接生图/改图模型、插件、API 或 MCP。安装前可查看[已核实的能力矩阵](references/compatibility.md#verified-rendering-capabilities)。

Python 3 与 Pillow 仅用于在参考图数量超过模型上限时生成带编号的无裁切素材索引图，不是必须依赖。

## 安装

克隆仓库后运行对应命令：

```bash
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target workbuddy
python3 scripts/install_skill.py --target claude
python3 scripts/install_skill.py --target kimi
python3 scripts/install_skill.py --target deepcode
python3 scripts/install_skill.py --target qoder
python3 scripts/install_skill.py --target qoderwork
python3 scripts/install_skill.py --target grok
```

- Codex、WorkBuddy、Claude Code、Kimi Code、Deep Code、Qoder、QoderWork、Grok Build：支持原生、项目级或产品自定义 Skill。
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
