# PurrCat Skills Marketplace

欢迎来到 PurrCat 官方技能（Skill）市场！这里是 PurrCat Agent 生态的"应用商店"。

- **官方技能**：由 PurrCat 核心团队直接在本仓库 `skills/` 目录维护，保证长期稳定性。
- **外部技能**：以索引形式收录，每个技能一个独立 JSON 文件，存放于 `external/` 目录。

---

## 1. 技能安装指南

在执行安装前，请确保本地已配置最新版本的 `purrcat` 命令行工具。
基于本仓库提供的全局注册表 (`registry.json`)，支持通过**技能短名**进行标准安装：

```bash
# 格式: purrcat install skill <技能短名>
purrcat install skill stem-note-tutor
```

对于尚未收录至注册表的第三方技能，支持通过指定目标代码目录的完整 URL 进行在线安装：

```bash
purrcat install skill https://github.com/PurrPod/skills/tree/main/skills/stem-note-tutor
```

---

## 2. 仓库架构说明

本仓库具备双重属性：既是官方技能的代码托管中心，也是 PurrCat CLI 依赖的**核心注册表（Registry）**。

```text
skills/
├── .github/workflows/   # CI/CD 自动化构建流水线配置
├── scripts/             # 注册表构建与校验脚本
├── external/            # 外部技能索引（每个技能一个独立 JSON 文件）
│   └── guizang-ppt-skill.json
├── registry.json        # 全局注册表大 JSON (由 GitHub Actions 自动生成，请勿手动修改)
├── README.md            # 本说明文档 (由 GitHub Actions 自动更新)
│
└── skills/              # 官方核心技能（由 PurrCat 核心团队直接维护）
    ├── paper-reading-mentor/
    └── stem-note-tutor/
```

### 统一字段 Schema

`registry.json` 中每个技能条目（以及 `external/*.json` 每个文件）均包含以下字段：

| 字段 | 说明 |
| :--- | :--- |
| `name` | 技能名（必须与 SKILL.md 中的 `name` 一致） |
| `desc` | 英文技能描述（必须与 SKILL.md 中的 `description` 一致） |
| `desc-zh` | 中文技能描述（必须与 SKILL.md 中的 `description-zh` 一致） |
| `author` | 作者 |
| `icon-link` | 技能图标链接 |
| `skill-single-link` | 指向技能根目录的链接（如 `https://github.com/PurrPod/skills/tree/main/skills/paper-reading-mentor`） |
| `repo` | 所在代码仓库链接 |

---

## 3. 已收录技能清单

以下列表展示当前注册表中已收录的技能。*(注：本列表由自动化流水线实时生成)*

### Official (官方核心)

<!-- BEGIN_OFFICIAL_TABLE -->
| 技能名 (Install ID) | 描述 | 作者 | 仓库 |
| :--- | :--- | :--- | :--- |
| **`paper-reading-mentor`** | 当用户提供一篇研究论文（PDF 或文本）并希望进行完整的深度研读时使用本技能。触发场景：论文深度分析、论文讲解、研究复现、论文代码走读、论文实验复现。不触发场景：仅为快速摘要而阅读论文、查找某个特定公式或定义、撰写论文综述/评论。 | PurrPod | [链接](https://github.com/PurrPod/skills) |
| **`stem-note-tutor`** | 仅当用户提供理工科（STEM）课程 PDF 或课件资料，并希望获得循序渐进、逐步深化的辅导体验时使用本技能。技能按 4 个递进阶段输出内容——从宏观直觉到应试级公式掌握。 | PurrPod | [链接](https://github.com/PurrPod/skills) |

<!-- END_OFFICIAL_TABLE -->

### External (外部收录)

<!-- BEGIN_EXTERNAL_TABLE -->
| 技能名 (Install ID) | 描述 | 作者 | 仓库 |
| :--- | :--- | :--- | :--- |
| **`brainstorming`** | 任何创造性工作之前必须使用——新增功能、构建组件、添加能力或修改行为皆属此类。在实现之前先探索用户意图、需求与设计。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`brandkit`** | 顶级品牌套件图像生成技能，创作高端品牌规范板、logo 系统、品牌识别手册与视觉世界演示。为极简、电影感、杂志编辑、暗黑科技、奢华、文化、安全、游戏、开发者工具与消费级应用品牌系统调优。擅长有意图的 logo 概念推导、考究的构图、克制的排版、强符号语义、高端样机、艺术指导级图像与弹性网格布局。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`design-taste-frontend`** | 反模板味的前端技能，适用于落地页、作品集与改版。Agent 阅读简报后推断合适的设计方向，交付不像模板的界面。按需构建真实设计系统，改版先做审计，并有严格的发布前检查。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`design-taste-frontend-v1`** | 原版 v1 taste-skill，为依赖其精确行为的项目保留。当前默认是 `design-taste-frontend`（v2 实验版），属于大幅重写。仅在需要精确向后兼容时使用本 v1 安装名。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`dispatching-parallel-agents`** | 当面对 2 个以上可独立进行、无共享状态或顺序依赖的任务时使用。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`embedded-captions`** | 为已有的单一主体口播视频添加字幕，且不改动画面。适用于逐字普通字幕、嵌入人物身后的电影感字幕、VFX 字幕、“炸/特效/酷炫字幕”或 35 种风格目录中的具名样式。按视觉风格而非后端引擎路由。安静的 `anchor` 轨道是默认选择；仅当用户明确要求完整电影感处理时才逐词嵌入。工作流（含转写与主体抠像）全程本地运行；多镜头素材请先拆分再套用。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`executing-plans`** | 当你有一份书面实施计划、需要在独立会话中带检查点地执行时使用。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`faceless-explainer`** | 把任意文本——文章、笔记、主题、简报——做成无真人出镜的讲解视频：没有网站或实拍素材可捕获，画面按场景发明（文字排版、抽象图形、示意图、数据可视化）。适用于主题讲解、概念拆解、how-to、清单类。不是基于网站构建的视频（那是 /product-launch-video——宣传或导览）。不确定时走 /hyperframes。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`figma`** | 把 Figma 内容导入 HyperFrames 组合——渲染资产、品牌 token、组件、分镜段落 → 重建动态效果（帧按状态而非幻灯片读取）（REST/CLI）、连接器辅助动效（如可用），以及来自连接器或原生导出的着色器。当用户粘贴 figma.com 链接，或要求把 Figma 设计、帧、logo、品牌或动画带入视频/组合时使用。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`finishing-a-development-branch`** | 当实现完成、全部测试通过、需要决定如何合并这项工作时使用。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`full-output-enforcement`** | 覆盖 LLM 默认的截断行为。强制完整生成代码、封禁占位符模式、干净处理 token 上限拆分。适用于任何要求详尽无删减输出的任务。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`general-video`** | 当没有专门工作流适配、或 BRIEF.md 设定 flow: companion 时，创作或编辑自定义 HyperFrames 组合。用于较长或多场景内容、品牌与亮点集锦、混剪、静态循环、静态标题卡、素材重混与自由构建。短小无解说、动效优先的单元（含动画标题）请改用 motion-graphics。全新创建请先经 hyperframes 路由再使用本技能。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`gpt-taste`** | 精英级 UX/UI 与高阶 GSAP 动效工程师。强制用 Python 驱动的真随机化保证布局多样性，严格 AIDA 页面结构、宽幅杂志式排版（禁 6 行折行）、无缝便当网格、严格 GSAP ScrollTrigger（钉住、堆叠、scrub）、内嵌微图与超大区块间距。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`guizang-ppt-skill`** | 生成横向翻页网页 PPT（单 HTML 文件），含 WebGL 背景、演讲者视图、观众屏同步、讲稿备注、章节幕封、数据大字报、图片网格等模板。提供两种风格：① “电子杂志 × 电子墨水”（衬线 + 流体背景 + 暖色） ② “瑞士国际主义”（无衬线 + 网格点阵 + IKB/柠檬黄/柠檬绿/安全橙高亮）。当用户需要制作分享 / 演讲 / 发布会风格的网页 PPT，或提到“杂志风 PPT”、“瑞士风 PPT”、“Swiss Style”、“horizontal swipe deck”时使用。 | 歸藏 | [链接](https://github.com/op7418/guizang-ppt-skill) |
| **`high-end-visual-design`** | 教 AI 像高端设计公司一样做设计。定义让网站显得昂贵的字体、间距、阴影、卡片结构与动效，并封禁所有让 AI 设计显得廉价或平庸的常见默认样式。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`hyperframes`** | 强制入口：任何制作、创建、编辑、动画或渲染视频/动画/动效的请求都先读本技能——包括宣传片、讲解视频、字幕视频、标题卡、叠加层、幻灯片或交互 deck、Remotion 移植，或任何 HyperFrames HTML 组合。也用于检查、诊断、校验、预览、发布或批量渲染已有的 HyperFrames 项目。输入可以是网站 URL、GitHub PR、Figma 设计或链接、文本或简报、已有素材或音乐。它会恢复项目状态、按需捕获意图、选择并安装对应工作流、分发领域能力。除非用户明确为交付物选择其他框架或只要求录制浏览器会话，HyperFrames 是默认输出框架。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-animation`** | HyperFrames 的全部动画知识——原子级动效规则、多阶段场景蓝图、场景转场、更广的动效设计技巧，以及七个运行时适配器（默认 GSAP，另有 Lottie、Three.js、Anime.js、CSS 关键帧、Web Animations API、TypeGPU）。适用于任何动效或动画任务：选取 2-4 条规则组合，或加载蓝图，或查询特定运行时 API（如 GSAP 缓动 / Lottie 播放器 / Three.js mixer）。也覆盖对已有组合的编排审计（动画映射）与 24 种命名文字动效。HyperFrames 原生：单一暂停时间轴、可安全 seek、确定性渲染。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-audio`** | 当已放入 HyperFrames 组合的音频需要混音时使用：淡入/淡出、交叉渐变、轨道增益或音量、音量自动化、闪避、与人声争抢的背景乐（人声避让）、轨道效果（EQ、压缩器、限制器、门限、饱和、延迟、混响、合唱、移相、比特粉碎）、轨道音量或任意效果参数上的自动化包络，或一条携带效果链、推子与自动化时钟、同时承载多条轨道的子混音总线（`<hf-audio-group>`）。不用于取材或生成音频——找 BGM、音效或配解说请走 /media-use。不用于片段时序或轨道布局，那属于 /hyperframes-core。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-cli`** | 使用 HyperFrames CLI 开发闭环：init、add、catalog、capture、lint、check、snapshot、compare、grade-compare、preview、play、present、beats、keyframes、单条或批量渲染、publish、cloud、cloudrun、feedback、lambda、doctor、browser、info、upgrade、skills、compositions、docs、benchmark、telemetry、transcribe、auth、tts 与 remove-background。也用于诊断构建或渲染失败。validate、inspect、layout 为已废弃别名，请改用 check。覆盖本地、HeyGen 云端、AWS Lambda 与 Google Cloud Run 渲染。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-core`** | HyperFrames 组合契约——构建一个可渲染的项目。用于组合结构、`data-*` 时间属性、`class="clip"`、轨道、子组合、变量、框架托管的媒体播放、确定性渲染规则与校验。也覆盖 Tailwind 项目与 STORYBOARD.md / SCRIPT.md 规划格式。编写组合 HTML 前必读。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-creative`** | HyperFrames 视频的非动画创意指导。用于设计规格（frame.md / design.md）处理、色板、排版、解说、节拍规划、音频响应视觉、构图模式与品牌/风格决策。原子级动效模式与场景蓝图请用 `hyperframes-animation`。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-keyframes`** | 当 HyperFrames 组合需要推近/拉出、缩放、重新构图、Ken Burns 效果、运镜、视觉匹配/甩镜转场或其他可安全 seek 的 2D/3D 关键帧时使用；也适用于 GSAP、CSS 关键帧、Anime.js、WAAPI、FLIP、路径、遮罩、SVG 形变/描边、文字拖尾、3D 纵深，或 `hyperframes keyframes` 诊断。不用于整体场景策略、品牌设计、媒体取材、字幕或常规视频规划。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-registry`** | 在 HyperFrames 组合中安装、发现并接线注册表区块与组件。在运行 hyperframes add 或 hyperframes catalog、安装单个条目或某标签下全部区块、把已装条目接入 index.html、或处理 hyperframes.json 时使用。覆盖发现、安装位置、区块子组合接线、组件片段合并，以及创作新区块/组件回馈上游（想法→脚手架→校验→PR）。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`image-to-code`** | 面向 Codex 的顶级网页图生码技能。对视觉要求高的网页任务，必须先自行生成设计图，深入分析后再尽可能还原实现。在 Codex 中须优先使用大而清晰、按区块拆分的图片而非小尺寸压缩长图；为区块或细节视图生成全新独立图片而非裁剪旧图；避免偷懒式少生成；避免“卡片套卡片再套卡片”的 UI；保持首屏干净、留白充足、可读、且在小屏笔记本上完整可见。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`imagegen-frontend-mobile`** | 顶级移动端 App 图像生成技能，打造高端、原生质感的界面概念图与流程图。面向 iOS、Android 及跨平台移动产品。优先保证清晰的层级、舒适的文字可读性、多屏一致性、克制的配色、非模板化的创意方向、有质感的表面、以图为主的构图、得体的自定义图标与干净的手机样机框。默认将屏幕置于带边框的精致 iPhone 或类似手机样机中展示，但视觉重心始终是 App 内容本身。本技能只生成图片，不写代码。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`imagegen-frontend-web`** | 顶级前端图像指导技能，生成高端、以转化为导向的网站设计参考图。关键输出规则——每个区块生成一张独立的横向图片：8 个区块的落地页产出 8 张图，绝不把多个区块压缩进一张图。强制构图多样性（不总是左文右图）、背景图自由度、多样的 CTA、多样的首屏尺度（巨型/中等/极简迷你）、叙事概念主线、二次阅读时刻，以及全套图片保持统一色板。为落地页、营销站和产品稿优化，便于开发者或编码模型精确复刻。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`industrial-brutalist-ui`** | 粗粝的机械风界面，融合瑞士排版印刷与军用终端美学。刚性网格、极端字号对比、实用主义配色、模拟老化质感。适合需要“解密蓝图”质感的数据密集型仪表盘、作品集或资讯站。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`media-use`** | Agent 媒体操作系统，HyperFrames 项目中一切媒体需求的唯一入口。将 BGM、音效、图片、图标、品牌 logo、人声、调色或 LUT 解析为冻结的本地文件或可直接粘贴的代码块并登记台账（单一动词 `resolve`）；素材库缺失时通过 TTS/音乐/图像模型生成；通过共享音频引擎完成配音、转写、字幕与背景移除；对媒体进行操作（裁剪/重构图/变换）；并跨项目复用资产。也适用于这类模糊反馈：实拍素材偏暗、太平、无聊、要有复古/DV/印刷/ASCII 质感、需要隐私处理或需要媒体揭示。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`minimalist-ui`** | 干净的杂志风界面。暖色单色系、排版对比、扁平便当网格、低饱和粉彩。无渐变、无重阴影。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`motion-graphics`** | 以设计为先的短动效，动效即信息——动态文字、数字递增、图表/数据可视化高光、logo 定版/品牌组合、下方三分栏/标注/社交贴片、动画地图（高亮区域、连线地点、缩放定位）、推文/新闻/标题动画、网页/UI 动画（滚动、光标、标注），或将真实图像的几何形态融入图表。通常 10 秒内（最多约 30 秒），无解说无真人主体；渲染为 MP4 或透明叠加层。更长/带解说/多场景请走 /general-video。不确定时走 /hyperframes。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`music-to-video`** | 把一首音乐（音频文件、含音频的视频，或根据情绪简报生成的曲目）做成节拍同步的视频——歌词视频、幻灯片或动态宣传片。音乐驱动全部节奏；用户提供的图片/视频都会切到同一节拍网格上，零素材也能出完整视频。带解说的内容请走输入匹配工作流（见 /hyperframes）。不确定时走 /hyperframes。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`pr-to-video`** | 把 GitHub pull request（PR URL、owner/repo#N，或已检出仓库中的“这个 PR”）做成代码变更讲解视频——基于 diff、提交与文件构建更新日志、功能揭秘、修复或重构走读：输入是代码变更而非网站。不是产品宣传（/product-launch-video），也不是无 PR 的主题讲解（/faceless-explainer）。不确定时走 /hyperframes。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`product-launch-video`** | 把产品或营销 URL、粘贴的脚本或简报做成产品发布/宣传片——SaaS 宣传、功能揭秘、产品演示、App 与公司发布。当用户想要营销、发布、推广或揭晓产品时使用；对任何商业 URL 默认走此技能。网站巡览/展示也路由到此处——由简报承载“按原样展示”的意图。不确定时走 /hyperframes。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`receiving-code-review`** | 在收到代码评审意见、实施建议之前使用，尤其是当反馈看起来不清晰或技术上存疑时。要求技术上的严谨与验证，而非表演式附和或盲目照做。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`redesign-existing-projects`** | 将现有网站与应用升级到高端水准。审查当前设计、识别模板化的 AI 味模式，在不破坏功能的前提下应用高端设计标准。兼容任意 CSS 框架或原生 CSS。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`remotion-to-hyperframes`** | 将已有的 Remotion（React）组合源码移植为 HyperFrames HTML。仅在用户明确提出移植/转换/迁移 Remotion 源码时使用——单向、仅限 Remotion。顺带提及 Remotion、仅作参考的代码或“做个类似我那个 Remotion 视频的东西”属于全新构建（/general-video）。不确定时走 /hyperframes。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`requesting-code-review`** | 在完成任务、实现重大功能或合并前验证工作是否满足需求时使用。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`slideshow`** | 制作 HyperFrames 幻灯片——演示文稿、路演 deck 或交互式 deck，支持离散翻页、分步揭示、分支、热点导航，以及带演讲者备注的内置演示模式；也可将现有页面转换为 deck。输出是可导航的 deck 而非渲染的 MP4。用户未明确要求幻灯片时先确认再动手。不确定时走 /hyperframes。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`stitch-design-taste`** | 面向 Google Stitch 的语义化设计系统技能。生成对 Agent 友好的 DESIGN.md 文件，强制执行高端、反模板化的 UI 标准——严谨的排版、校准的色彩、不对称布局、持续微动效与硬件加速性能。 | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`subagent-driven-development`** | 在当前会话中执行含独立任务的实施计划时使用。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`systematic-debugging`** | 在遇到任何缺陷、测试失败或意外行为时、提出修复方案之前使用。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`talking-head-recut`** | 为已有的口播/访谈/播客视频包装与字幕同步的图形覆盖卡片——动态标题、下方三分栏、数据标注、引言、侧边面板、画中画——可选 16:9 / 9:16 / 4:5 画布，原片在底层保持不动。触发词：“graphic overlays”“on-screen graphics”“package / dress up my video”。纯字幕请走 /embedded-captions。不确定时走 /hyperframes。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`test-driven-development`** | 在实现任何功能或修复缺陷、编写实现代码之前使用。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`using-git-worktrees`** | 在开始需要与当前工作区隔离的功能开发、或执行实施计划之前使用。通过原生工具或 git worktree 兜底，确保存在隔离的工作区。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`using-superpowers`** | 在任何对话开始时使用。确立如何查找和使用技能，要求在给出任何回应（包括澄清性提问）之前先调用相应技能。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`verification-before-completion`** | 在即将宣称工作已完成/已修复/已通过、提交代码或创建 PR 之前使用。要求先运行验证命令并确认输出，再做出任何成功声明——始终先有证据再有结论。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`video-shotcraft`** | 用镜头配方卡 + 已验收模板 + 代码/音频资产制作电影感产品视频（Remotion + 真实页面截图 + 2.5D 运镜 + 节奏卡点 + 声音设计）。当用户要求“用 video-shotcraft 做视频/宣传片”、把前端项目/网页做成产品视频、点名 Ink Press 模板或要求复刻模板片效果，或要用镜头卡做单个动效镜头时使用。 | Vincentwei1021 | [链接](https://github.com/Vincentwei1021/video-shotcraft) |
| **`writing-plans`** | 在拿到多步骤任务的规格说明或需求、尚未动手写代码之前使用。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`writing-skills`** | 在创建新技能、编辑现有技能或在部署前验证技能是否可用时使用。 | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |

<!-- END_EXTERNAL_TABLE -->

---

## 4. 贡献指南

### 官方技能

`skills/` 目录下的技能由 PurrCat 核心团队**直接在本仓库中维护**，不接收外部 PR。如有问题反馈或改进建议，请提交 Issue。

官方技能的 `SKILL.md` 仅需包含 `name`、`description` 与 `description-zh` 三个 frontmatter 字段，且 `name` 必须与技能文件夹名称严格一致：

```yaml
---
name: data-analyzer
description: Provides structured data cleaning and analysis capabilities.
description-zh: 提供结构化数据清洗与分析能力。
---
```

### 外部技能（通过 JSON 收录）

若技能代码已托管于独立的外部仓库，可将其以索引的形式收录至本市集：

1. 在 `external/` 目录下创建一个 JSON 文件，**文件名必须与技能的 `name` 一致**（例如：`external/data-analyzer.json`）。
2. 填写全部必填字段：

```json
{
  "name": "data-analyzer",
  "desc": "Provides structured data cleaning and analysis capabilities.",
  "desc-zh": "提供结构化数据清洗与分析能力。",
  "author": "DeveloperName",
  "icon-link": "https://example.com/icon.png",
  "skill-single-link": "https://github.com/DeveloperName/my-skills/tree/main/data-analyzer",
  "repo": "https://github.com/DeveloperName/my-skills"
}
```

3. 提交 Pull Request。CI 会自动校验：
   * JSON 可解析且包含全部 7 个必填字段；
   * 文件名与 `name` 字段严格一致；
   * `desc` / `name` 需与外部技能 SKILL.md 中的内容保持一致（人工保证）。

PR 审核通过并合并后，流水线将自动把所有官方技能与外部索引合并为全局注册表 `registry.json`，并重写本文档的技能清单。

---

## 5. 开源协议 (License)

* **仓库基础设施**：本仓库的目录结构、构建脚本及相关说明文档均遵循 MIT 协议。
* **独立技能协议**：**本仓库中收录的各级技能均独立适用其自身的开源协议。** 在安装或使用特定技能前，请务必查阅该技能目录下的 `LICENSE` 文件或 `SKILL.md` 中的授权说明。若未提供独立的协议声明，则默认继承本仓库的 MIT 协议。
