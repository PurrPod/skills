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
| `desc` | 技能描述（必须与 SKILL.md 中的 `description` 一致） |
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
| **`paper-reading-mentor`** | Use this skill when the user provides a research paper (PDF or text) and wants to go through a complete deep study. Triggers on: deep paper analysis, paper explanation, research reconstruction, paper code walkthrough, paper experiment replication. Do NOT trigger on: reading a paper for a quick summary only, looking up a specific formula or definition, writing a paper review/survey. | PurrPod | [链接](https://github.com/PurrPod/skills) |
| **`stem-note-tutor`** | Use this skill only when the user provides a STEM course PDF or slide material and wants a step-by-step, gradually deepening tutoring experience. The skill delivers prompts in 4 sequential stages — from big-picture intuition to exam-ready formula mastery. | PurrPod | [链接](https://github.com/PurrPod/skills) |

<!-- END_OFFICIAL_TABLE -->

### External (外部收录)

<!-- BEGIN_EXTERNAL_TABLE -->
| 技能名 (Install ID) | 描述 | 作者 | 仓库 |
| :--- | :--- | :--- | :--- |
| **`brainstorming`** | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation. | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`brandkit`** | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist, cinematic, editorial, dark-tech, luxury, cultural, security, gaming, developer-tool, and consumer-app brand systems. Optimized for intentional logo concepting, refined composition, sparse typography, strong symbolic meaning, premium mockups, art-directed imagery, and flexible grid layouts. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`design-taste-frontend`** | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`design-taste-frontend-v1`** | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which is a substantial rewrite. Use this v1 install name only if you need exact backward compatibility. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`dispatching-parallel-agents`** | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`embedded-captions`** | 给现有单主体出镜视频加字幕/烧录字幕而不改原片：逐字 verbatim、人物背后电影感 embed、VFX 特效字幕、35 种风格目录按视觉身份路由（非按引擎）。转写+主体抠像全流程本地端到端，多镜头素材先拆分再用。用户要"加字幕/炸字幕/特效字幕/指定风格字幕"时使用。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`executing-plans`** | Use when you have a written implementation plan to execute in a separate session with review checkpoints | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`faceless-explainer`** | 把任意文本（文章/笔记/主题/brief）做成无出镜讲解视频：无站点可截，画面按场景现造（typography/抽象图形/图解/数据可视化）。适用主题讲解、概念拆解、How-to、清单体。不是网站转 promo（那走 product-launch-video），不确定先走 hyperframes 入口。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`figma`** | 把 Figma 内容导入 HyperFrames 合成：渲染资产、品牌 token、组件、分镜段落重建为动态（帧=状态非幻灯片），支持 REST/CLI 与 connector 辅助动效。用户粘贴 figma.com 链接，或要把 Figma 设计/框架/logo/品牌/动画带入视频或合成时使用。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`finishing-a-development-branch`** | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`full-output-enforcement`** | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`general-video`** | 无专项工作流匹配时（或 BRIEF flow: companion）自由创作/编辑自定义 HyperFrames 合成：较长多场景片、品牌与 sizzle reel、蒙太奇、静态循环/标题卡、素材混剪、自由构建。短促无旁白动效优先走 motion-graphics；新创作先经 hyperframes 入口路由。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`gpt-taste`** | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typography (bans 6-line wraps), gapless bento grids, strict GSAP ScrollTriggers (pinning, stacking, scrubbing), inline micro-images, and massive section spacing. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`guizang-ppt-skill`** | 生成横向翻页网页 PPT（单 HTML 文件），含 WebGL 背景、演讲者视图、观众屏同步、讲稿备注、章节幕封、数据大字报、图片网格等模板。提供两种风格：① “电子杂志 × 电子墨水”（衬线 + 流体背景 + 暖色） ② “瑞士国际主义”（无衬线 + 网格点阵 + IKB/柠檬黄/柠檬绿/安全橙高亮）。当用户需要制作分享 / 演讲 / 发布会风格的网页 PPT，或提到“杂志风 PPT”、“瑞士风 PPT”、“Swiss Style”、“horizontal swipe deck”时使用。 | 歸藏 | [链接](https://github.com/op7418/guizang-ppt-skill) |
| **`high-end-visual-design`** | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the common defaults that make AI designs look cheap or generic. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`hyperframes`** | HyperFrames 总入口（强制先读）：任何做/改/编/渲视频、动画、动效（promo/讲解/字幕/标题卡/浮层/幻灯片/Remotion 移植）都先走这里；也用于检查/诊断/校验/预览/发布/批量渲染既有 HyperFrames 项目。输入支持 URL、GitHub PR、Figma、文本 brief、素材、音乐；负责恢复项目状态、捕获意图、安装负责工作流并路由领域能力。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-animation`** | HyperFrames 动画知识全集：原子动效规则、多阶段场景蓝图、转场与动效设计技法，含 7 个运行时适配器（GSAP 默认 + Lottie/Three.js/Anime.js/CSS keyframes/Web Animations API/TypeGPU）与 24 种命名文字动效。HyperFrames 原生：单条 paused 时间线、seek-safe、确定性渲染；也用于审计既有合成的 choreography。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-audio`** | HyperFrames 合成内已放音轨的混音：淡入淡出/交叉淡化、轨增益与音量自动化、ducking（音乐压人声时 voiceover carve）、单轨效果链（EQ/压缩/限幅/门限/饱和/delay/reverb/chorus/phaser/bitcrush）、子混音总线组。找 BGM/SFX 或生成人声请走 media-use，剪接与轨布局另有其责。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-cli`** | HyperFrames CLI 开发闭环全命令：init/add/catalog/capture/lint/check/snapshot/compare/preview/play/present/render(单批与批量)/publish/cloud/cloudrun/lambda/doctor/browser/info/upgrade 等；构建或渲染失败诊断也用。覆盖本地、HeyGen 云、AWS Lambda 与 Google Cloud Run 渲染。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-core`** | HyperFrames 合成契约（写 composition HTML 前必读）：data-* 时间轴属性、clip 窗口、轨道/子合成/变量、框架媒体播放、确定性渲染规则与校验；也覆盖 Tailwind 工程与 STORYBOARD.md/SCRIPT.md 计划格式。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-creative`** | HyperFrames 的非动画创意指导：设计 spec（frame.md/design.md）、配色、字体排版、旁白、节拍规划、音频响应视觉、构图模式与品牌/风格决策。原子动效规则与场景蓝图请走 hyperframes-animation。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-keyframes`** | HyperFrames 合成需要关键帧镜头时用：punch-in/out、变焦、reframe、Ken Burns、运镜、视觉匹配与 whip 交接；含 GSAP/CSS keyframes/Anime.js/WAAPI/FLIP、路径/遮罩/SVG morph/文字拖尾/3D 景深与 hyperframes keyframes 诊断。宽泛场景策略/品牌设计/媒体/字幕/整体规划不归它管。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-registry`** | HyperFrames registry 块与组件的安装/发现/接线：hyperframes add/catalog、按 tag 整批安装、接线进 index.html、编辑 hyperframes.json；亦覆盖自建块/组件贡献上游（idea→scaffold→validate→PR）。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`image-to-code`** | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website to match them as closely as possible. In Codex, it must prefer large, readable, section-specific images instead of tiny compressed boards, generate fresh standalone images for sections or detail views instead of cropping old ones, avoid lazy under-generation, avoid cards-inside-cards-inside-cards UI, and keep the hero clean, spacious, readable, and visible on a small laptop. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`imagegen-frontend-mobile`** | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. Prioritizes clean hierarchy, comfortably readable text, strong multi-screen consistency, controlled color palettes, non-generic creative direction, textured surfaces, image-led composition, tasteful custom iconography, and clean phone mockup framing. By default, screens should be shown inside a subtle premium iPhone or similar phone mockup with a visible frame, while the main focus stays on the app content itself. This skill generates images only. It does not write code. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`imagegen-frontend-web`** | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section. A landing page with 8 sections produces 8 images. Never compress multiple sections into one image. Enforces composition variety (not always left-text / right-image), background-image freedom, varied CTAs, varied hero scales (giant / mid / mini minimalist), narrative concept spine, second-read moments, and a single consistent palette across all images. Optimized for landing pages, marketing sites, and product comps that developers or coding models can accurately recreate. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`industrial-brutalist-ui`** | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. For data-heavy dashboards, portfolios, or editorial sites that need to feel like declassified blueprints. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`media-use`** | HyperFrames 项目的统一媒体入口（Media OS）：BGM/SFX/图/图标/logo/人声/调色/LUT 一律 resolve 为冻结本地文件或即贴块+台账记录；目录缺失时经 TTS/音乐/生图模型生成；共享音频引擎覆盖人声、转写、字幕与去背景；可裁切/重构图/变换并跨项目复用资产。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`minimalist-ui`** | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`motion-graphics`** | 短促设计主导动效片（动效即信息，通常 <10s 上限 ~30s）：kinetic 文字、数字 count-up、图表 data-viz、logo sting、lower-third/呼出/社媒浮层、动图地图、推文/标题动画、网页 UI 运镜。无旁白无真人主体，出 MP4 或透明叠加层。更长/带旁白/多场景走 general-video。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`music-to-video`** | 把音乐轨（音频文件/抽音轨的视频/按情绪 brief 生成的曲）变成卡点视频：歌词视频、幻灯片或 kinetic promo。音乐主导全部节奏，用户供图/片也切进同一拍点网格，无任何素材也能零资产成片；带旁白内容走输入匹配工作流。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`pr-to-video`** | 把 GitHub PR（URL/owner#N 或检出仓库里的"这个 PR"）变成代码变更讲解视频：changelog、feature reveal、修复或重构走读，素材来自 diff/commits/files。输入是代码变更而非网站；非产品 promo 也非无 PR 主题讲解。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`product-launch-video`** | 把产品/营销 URL、粘贴脚本或 brief 做成产品发布/宣传视频：SaaS promo、功能揭幕、产品 demo、App 与公司发布。用户要营销/发布/推广/揭示产品时使用；任何商业 URL 的默认工作流，网站导览/秀场也路由于此。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`receiving-code-review`** | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`redesign-existing-projects`** | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`remotion-to-hyperframes`** | 把现成 Remotion(React) 合成源码移植为 HyperFrames HTML。仅在用户明确要求 port/convert/migrate/translate 时用（单向、只收 Remotion）；顺带提及/仅参考代码/"仿我的 Remotion 视频"属新创作，走 general-video。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`requesting-code-review`** | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`slideshow`** | 创作 HyperFrames 幻灯片——演示/Pitch/可交互 deck：独立 slide、片段渐显、分支跳转、热点导航、内置演讲者模式（含讲稿备注）；也可把现有页面转 deck。产物是可导航 deck 而非渲染 MP4；用户没明确要 slideshow 先确认。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`stitch-design-taste`** | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion, and hardware-accelerated performance. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`subagent-driven-development`** | Use when executing implementation plans with independent tasks in the current session | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`systematic-debugging`** | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`talking-head-recut`** | 给现成出镜/访谈/播客视频叠加定时设计的图形浮层卡（原片不动）：kinetic 标题、lower-thirds、数据 callout、引言、侧栏、画中画，按转写稿同步，画布 16:9/9:16/4:5。用户要"图形浮层/包装/打扮我的视频"时用；纯字幕走 embedded-captions。 | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`test-driven-development`** | Use when implementing any feature or bugfix, before writing implementation code | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`using-git-worktrees`** | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`using-superpowers`** | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`verification-before-completion`** | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`video-shotcraft`** | Create cinematic product videos from shot recipe cards, a validated template, and code/audio assets (Remotion + real page screenshots + 2.5D camera moves + beat-synced cuts + sound design). Use when the user asks to turn a frontend project or webpage into a product video, says "use video-shotcraft to make a video/promo", names the Ink Press template or asks to reproduce its effect, or wants a single shot card's motion. 用镜头配方卡 + 已验收模板 + 代码/音频资产制作电影感产品视频（Remotion + 真实页面截图 + 2.5D 运镜 + 节奏卡点 + 声音设计）。当用户要求"用 video-shotcraft 做视频/宣传片"、把前端项目/网页做成产品视频、点名 Ink Press 模板或要求复刻模板片效果，或要用镜头卡做单个动效镜头时使用。 | Vincentwei1021 | [链接](https://github.com/Vincentwei1021/video-shotcraft) |
| **`writing-plans`** | Use when you have a spec or requirements for a multi-step task, before touching code | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`writing-skills`** | Use when creating new skills, editing existing skills, or verifying skills work before deployment | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |

<!-- END_EXTERNAL_TABLE -->

---

## 4. 贡献指南

### 官方技能

`skills/` 目录下的技能由 PurrCat 核心团队**直接在本仓库中维护**，不接收外部 PR。如有问题反馈或改进建议，请提交 Issue。

官方技能的 `SKILL.md` 仅需包含 `name` 与 `description` 两个 frontmatter 字段，且 `name` 必须与技能文件夹名称严格一致：

```yaml
---
name: data-analyzer
description: 提供结构化数据清洗与分析能力。
---
```

### 外部技能（通过 JSON 收录）

若技能代码已托管于独立的外部仓库，可将其以索引的形式收录至本市集：

1. 在 `external/` 目录下创建一个 JSON 文件，**文件名必须与技能的 `name` 一致**（例如：`external/data-analyzer.json`）。
2. 填写全部必填字段：

```json
{
  "name": "data-analyzer",
  "desc": "提供结构化数据清洗与分析能力。",
  "author": "DeveloperName",
  "icon-link": "https://example.com/icon.png",
  "skill-single-link": "https://github.com/DeveloperName/my-skills/tree/main/data-analyzer",
  "repo": "https://github.com/DeveloperName/my-skills"
}
```

3. 提交 Pull Request。CI 会自动校验：
   * JSON 可解析且包含全部 6 个必填字段；
   * 文件名与 `name` 字段严格一致；
   * `desc` / `name` 需与外部技能 SKILL.md 中的内容保持一致（人工保证）。

PR 审核通过并合并后，流水线将自动把所有官方技能与外部索引合并为全局注册表 `registry.json`，并重写本文档的技能清单。

---

## 5. 开源协议 (License)

* **仓库基础设施**：本仓库的目录结构、构建脚本及相关说明文档均遵循 MIT 协议。
* **独立技能协议**：**本仓库中收录的各级技能均独立适用其自身的开源协议。** 在安装或使用特定技能前，请务必查阅该技能目录下的 `LICENSE` 文件或 `SKILL.md` 中的授权说明。若未提供独立的协议声明，则默认继承本仓库的 MIT 协议。
