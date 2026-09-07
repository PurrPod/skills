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
| **`dispatching-parallel-agents`** | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`executing-plans`** | Use when you have a written implementation plan to execute in a separate session with review checkpoints | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`finishing-a-development-branch`** | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`guizang-ppt-skill`** | 生成横向翻页网页 PPT（单 HTML 文件），含 WebGL 背景、演讲者视图、观众屏同步、讲稿备注、章节幕封、数据大字报、图片网格等模板。提供两种风格：① “电子杂志 × 电子墨水”（衬线 + 流体背景 + 暖色） ② “瑞士国际主义”（无衬线 + 网格点阵 + IKB/柠檬黄/柠檬绿/安全橙高亮）。当用户需要制作分享 / 演讲 / 发布会风格的网页 PPT，或提到“杂志风 PPT”、“瑞士风 PPT”、“Swiss Style”、“horizontal swipe deck”时使用。 | 歸藏 | [链接](https://github.com/op7418/guizang-ppt-skill) |
| **`receiving-code-review`** | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`requesting-code-review`** | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`subagent-driven-development`** | Use when executing implementation plans with independent tasks in the current session | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`systematic-debugging`** | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`test-driven-development`** | Use when implementing any feature or bugfix, before writing implementation code | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`using-git-worktrees`** | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`using-superpowers`** | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
| **`verification-before-completion`** | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always | Jesse Vincent (obra) | [链接](https://github.com/obra/superpowers) |
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
