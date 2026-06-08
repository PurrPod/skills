# 📦 SkillPod for PurrCat

欢迎来到 **SkillPod** —— 专为 [PurrCat](https://github.com/PurrPod/purrcat) 打造的官方与社区扩展技能（Skill）合集！当然，所有 Skill 均符合 Anthoropic 官方技能规范，亦可用于其它 Agent。

在这里，你可以发现、分享并安装各种强大的 Skill，让你的 Agent 拥有处理各种垂直领域任务的能力。

---

## 🚀 如何安装 Skill （对于 PurrCat 来说）

在安装任何技能之前，请确保你已经成功安装了最新版本的 `purrcat` CLI。

你可以通过以下命令，直接从本仓库的 URL 安装你想要的单个 Skill：

```bash
purrcat install skill <url-to-the-single-skill-dir>

```

其它 Agent 只需运行各自的命令将技能文件夹下载到正确的位置即可。

### 💡 安装示例

```bash
purrcat install skill https://github.com/your-username/skillpod/tree/main/official/stem-note-skill

```

---

## 📂 仓库结构

本仓库将 Skill 划分为两大类，方便大家按需检索：

```text
SkillPod/
├── 📁 official/         # 官方维护的 Skill（由 PurrCat 核心团队提供）
│   ├── stem-note-skill/   
│   └── ...
├── 📁 community/        # 社区贡献的 Skill（由开源社区开发者提供）
│   ├── web-scraper/     
│   └── ...
└── README.md

```

---

## 🤝 如何贡献你的 Skill？

我们非常欢迎大家将自己编写的优秀 Skill 贡献到 `community/` 目录下！

### 贡献要求：

1. **Fork** 本仓库并创建分支。
2. 在 `community/` 目录下创建一个独立的文件夹（例如：`community/my-awesome-skill/`）。
3. **【关键】明确声明你的开源协议**：
* 请在你的 Skill 文件夹内放置属于该 Skill 的 `LICENSE` 文件。
* 推荐在你的 `SKILL.md` 的 `description` 或前置元数据中加入 `license: MIT/GPL-3.0` 等标识。


4. 提交 **Pull Request (PR)**。

---

## 📄 开源协议说明 (License)

* **仓库基础设施**：本仓库的目录结构、构建脚本及相关说明文档采用 MIT 协议。
* **独立的 Skill 协议**：**本仓库中收录的每个 Skill 均独立拥有其自身的开源协议。** 请在安装和使用特定的 Skill 前，查阅该 Skill 目录下的 `LICENSE` 文件或说明。若该 Skill 未包含独立的协议声明，默认继承主仓库的 MIT 协议。