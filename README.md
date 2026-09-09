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
| **`brainstorming`** | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation. | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`brandkit`** | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist, cinematic, editorial, dark-tech, luxury, cultural, security, gaming, developer-tool, and consumer-app brand systems. Optimized for intentional logo concepting, refined composition, sparse typography, strong symbolic meaning, premium mockups, art-directed imagery, and flexible grid layouts. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`design-taste-frontend`** | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`design-taste-frontend-v1`** | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which is a substantial rewrite. Use this v1 install name only if you need exact backward compatibility. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`dispatching-parallel-agents`** | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`embedded-captions`** | Add captions or subtitles to an existing single-subject talking-head video without editing the footage. Use for plain verbatim captions, cinematic captions embedded behind the subject, VFX captions, “炸/特效/酷炫字幕,” or a named identity from the 35-style catalog. Route by visual identity, not by backend engine. The quiet `anchor` rail is the default; embed every word only when the user explicitly wants a fully cinematic treatment. The workflow runs locally end to end, including transcription and subject matting; split multi-shot footage before applying it. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`executing-plans`** | Use when you have a written implementation plan to execute in a separate session with review checkpoints | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`faceless-explainer`** | Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site or footage to capture, so the visuals are invented per scene (typography, abstract graphics, diagrams, data-viz). Use for topic explainers, concept breakdowns, how-tos, listicles. Not a video built from a website (/product-launch-video — promo or tour). Unclear → /hyperframes. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`figma`** | Import Figma content into a HyperFrames composition — rendered assets, brand tokens, components, storyboard sections → reconstructed motion (frames read as states, not slides) (REST/CLI), connector-assisted motion when available, and shaders from a connector or native export. Use when the user pastes a figma.com link or asks to bring a Figma design, frame, logo, brand, or animation into a video/composition. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`finishing-a-development-branch`** | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`full-output-enforcement`** | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`general-video`** | Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion. Use for longer or multi-scene pieces, brand and sizzle reels, montages, static loops, static title cards, footage remixes, and freeform builds. Use motion-graphics instead for a short unnarrated motion-first unit, including an animated title. Route fresh creation through hyperframes before using this skill. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`gpt-taste`** | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typography (bans 6-line wraps), gapless bento grids, strict GSAP ScrollTriggers (pinning, stacking, scrubbing), inline micro-images, and massive section spacing. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`guizang-ppt-skill`** | 生成横向翻页网页 PPT（单 HTML 文件），含 WebGL 背景、演讲者视图、观众屏同步、讲稿备注、章节幕封、数据大字报、图片网格等模板。提供两种风格：① “电子杂志 × 电子墨水”（衬线 + 流体背景 + 暖色） ② “瑞士国际主义”（无衬线 + 网格点阵 + IKB/柠檬黄/柠檬绿/安全橙高亮）。当用户需要制作分享 / 演讲 / 发布会风格的网页 PPT，或提到“杂志风 PPT”、“瑞士风 PPT”、“Swiss Style”、“horizontal swipe deck”时使用。 | 歸藏 | [链接](https://github.com/op7418/guizang-ppt-skill) |
| **`high-end-visual-design`** | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the common defaults that make AI designs look cheap or generic. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`hyperframes`** | Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, including a promo, explainer, captioned clip, title card, overlay, slideshow or interactive deck, Remotion port, or any HyperFrames HTML composition. Also use it to inspect, diagnose, validate, preview, publish, or batch-render an existing HyperFrames project. Inputs may be a website URL, GitHub PR, Figma design or URL, text or brief, existing footage, or music. It resumes project state, captures intent when applicable, selects and installs the owning workflow, and routes domain capabilities. HyperFrames is the default output framework unless the user explicitly chooses another framework for the deliverable or asks only to record a browser session. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-animation`** | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (GSAP default, plus Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, TypeGPU). Use for any motion or animation task: pick 2-4 rules and compose, or load a blueprint, or look up runtime-specific API (e.g. GSAP eases / Lottie player / Three.js mixer). Also covers auditing an existing composition's choreography (animation map) and 24 named text-animation effects. HyperFrames-native: single paused timeline, seek-safe, deterministic. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-audio`** | Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume automation, ducking, a music bed that fights a voiceover (voiceover carve), effects on a track (EQ, compressor, limiter, gate, saturation, delay, reverb, chorus, phaser, bitcrush), automation envelopes drawn on a track's volume or any effect parameter, or one submix bus carrying a chain, a fader and an automation clock for several tracks at once (`<hf-audio-group>`). Don't use for sourcing or generating audio — finding BGM, SFX, or making a voiceover is `/media-use`. Don't use for clip timing or track layout, which is `/hyperframes-core`. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-cli`** | Use the HyperFrames CLI development loop: init, add, catalog, capture, lint, check, snapshot, compare, grade-compare, preview, play, present, beats, keyframes, single or batch render, publish, cloud, cloudrun, feedback, lambda, doctor, browser, info, upgrade, skills, compositions, docs, benchmark, telemetry, transcribe, auth, tts, and remove-background. Also use when diagnosing build or render failures. validate, inspect, and layout are deprecated aliases; use check. Covers local, HeyGen-hosted cloud, AWS Lambda, and Google Cloud Run rendering. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-core`** | The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation. Also covers Tailwind projects and the STORYBOARD.md / SCRIPT.md plan formats. Read before writing composition HTML. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-creative`** | Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand / style decisions. For atomic motion patterns and scene blueprints, use `hyperframes-animation`. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-keyframes`** | Use when a HyperFrames composition needs a punch-in, punch-out, zoom, reframe, Ken Burns treatment, camera move, visual match/whip handoff, or other seek-safe 2D/3D keyframes; also for GSAP, CSS keyframes, Anime.js, WAAPI, FLIP, paths, masks, SVG morph/draw, text trails, 3D depth, or `hyperframes keyframes` diagnostics. Don't use for broad scene strategy, brand design, media sourcing, captions, or general video planning. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`hyperframes-registry`** | Install, discover, and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add or hyperframes catalog, installing one item or every block matching a tag, wiring an installed item into index.html, or working with hyperframes.json. Covers discovery, install locations, block sub-composition wiring, component snippet merging, and authoring a new block or component to contribute upstream (idea → scaffold → validate → PR). | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`image-to-code`** | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website to match them as closely as possible. In Codex, it must prefer large, readable, section-specific images instead of tiny compressed boards, generate fresh standalone images for sections or detail views instead of cropping old ones, avoid lazy under-generation, avoid cards-inside-cards-inside-cards UI, and keep the hero clean, spacious, readable, and visible on a small laptop. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`imagegen-frontend-mobile`** | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. Prioritizes clean hierarchy, comfortably readable text, strong multi-screen consistency, controlled color palettes, non-generic creative direction, textured surfaces, image-led composition, tasteful custom iconography, and clean phone mockup framing. By default, screens should be shown inside a subtle premium iPhone or similar phone mockup with a visible frame, while the main focus stays on the app content itself. This skill generates images only. It does not write code. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`imagegen-frontend-web`** | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section. A landing page with 8 sections produces 8 images. Never compress multiple sections into one image. Enforces composition variety (not always left-text / right-image), background-image freedom, varied CTAs, varied hero scales (giant / mid / mini minimalist), narrative concept spine, second-read moments, and a single consistent palette across all images. Optimized for landing pages, marketing sites, and product comps that developers or coding models can accurately recreate. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`industrial-brutalist-ui`** | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. For data-heavy dashboards, portfolios, or editorial sites that need to feel like declassified blueprints. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`media-use`** | Agent Media OS, the single skill for every media need in a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local file or paste-ready block + ledger record (one verb, `resolve`); generate via TTS / music / image models when the catalog misses; produce voiceover, transcription, captions, and background removal through one shared audio engine; operate on media (cut / reframe / transform); and reuse assets across projects. Also use for vague feedback that real footage looks dark, flat, boring, should feel retro/camcorder/print/ASCII, needs privacy, or needs a media reveal. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`minimalist-ui`** | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`motion-graphics`** | A short, design-led motion graphic where motion is the message — kinetic typography, stat count-up, chart/data-viz hit, logo sting / brand lockup, lower-third / callout / social overlay, animated map (highlight regions, connect places, zoom to a location), animated tweet / news-article / headline, webpage / UI animation (scroll, cursor, callouts), or fusing a real image's geometry into a chart. Usually under 10s (up to ~30s), no narration or live-action subject; renders to MP4 or transparent overlay. Longer / narrated / multi-scene → /general-video. Unclear → /hyperframes. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`music-to-video`** | Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a beat-synced video — lyric video, slideshow, or kinetic promo. The music drives all pacing; any user-supplied images/videos are cut onto the same beat grid, and a complete video needs zero assets. Narrated pieces → the input-matched workflow (see /hyperframes). Unclear → /hyperframes. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`pr-to-video`** | Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video — changelog, feature reveal, fix, or refactor walkthrough built from the diff, commits, and files: the input is a code change, not a website. Not a product promo (/product-launch-video) or a no-PR topic explainer (/faceless-explainer). Unclear → /hyperframes. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`product-launch-video`** | Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, app and company launches. Use when the user wants to market, launch, promote, or reveal a product; the default for any commercial URL. Site tours / showcases of a website route here too — the brief carries the show-it-as-is intent. Unclear → /hyperframes. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`receiving-code-review`** | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`redesign-existing-projects`** | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`remotion-to-hyperframes`** | Port an existing Remotion (React) composition's source to HyperFrames HTML. Use ONLY on an explicit ask to port/convert/migrate/translate a Remotion source — one-way, Remotion-only. A passing Remotion mention, reference-only code, or "make something like my Remotion video" is a fresh build (/general-video). Unclear → /hyperframes. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`requesting-code-review`** | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`slideshow`** | Author a HyperFrames slideshow — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and built-in presenter mode with speaker notes; also converts an existing page into a deck. Output is a navigable deck, not a rendered MP4. If the user didn't explicitly ask for a slideshow, confirm before authoring. Unclear → /hyperframes. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
| **`stitch-design-taste`** | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion, and hardware-accelerated performance. | Leonxlnx | [链接](https://github.com/Leonxlnx/taste-skill) |
| **`subagent-driven-development`** | Use when executing implementation plans with independent tasks in the current session | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`systematic-debugging`** | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`talking-head-recut`** | Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data callouts, quotes, side panels, picture-in-picture — synced to the transcript, on a 16:9 / 9:16 / 4:5 canvas of your choice; the clip plays untouched underneath. Trigger on "graphic overlays", "on-screen graphics", "package / dress up my video". Not plain subtitles (/embedded-captions). Unclear → /hyperframes. | HeyGen | [链接](https://github.com/heygen-com/hyperframes) |
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
