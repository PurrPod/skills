<h1 align="center">SkillPod for PurrCat</h1>

<p align="center">
    专为 <a href="https://github.com/PurrPod/purrcat">PurrCat</a> 打造的官方与社区扩展技能（Skill）合集。<br>
    所有 Skill 均符合 Anthropic 官方技能规范，亦可扩展用于其它 Agent 生态。
</p>

<p align="center">
    通过 SkillPod，你可以发现、分享并安装各种垂直领域的专业技能，扩展 Agent 的任务处理边界。
</p>

---

## 如何安装 Skill（以 PurrCat 为例）

在安装任何技能之前，请确保本地已成功配置最新版本的 `purrcat` 命令行工具（CLI）。

你可以通过指定本仓库中单个 Skill 的目录 URL 直接进行在线安装：

```bash
purrcat install skill <url-to-the-single-skill-dir>

```

对于其它兼容 Anthropic 规范的 Agent，只需运行其各自的集成命令，或将对应的技能文件夹克隆至指定的工作目录下即可。

### 安装示例

```bash
purrcat install skill https://github.com/PurrPod/skillpod/tree/main/official/stem-note-skill

```

---

## 仓库结构

本仓库将 Skill 划分为官方与社区两大类，以便于用户检索与维护：

```text
SkillPod/
├── official/            # 官方维护的 Skill（由 PurrCat 核心团队提供，保证长期稳定）
│   ├── stem-note-skill/   
│   └── ...
├── community/           # 社区贡献的 Skill（由开源社区开发者提供，功能多样）
│   ├── web-scraper/     
│   └── ...
└── README.md

```

---

## 如何贡献你的 Skill

我们非常欢迎并鼓励开发者将自己编写的优秀 Skill 提交至 `community/` 目录下。

### 贡献要求

1. **Fork 仓库**：Fork 本仓库并基于最新代码创建你的特性分支。
2. **创建独立目录**：在 `community/` 目录下创建一个具有辨识度的独立文件夹（例如：`community/my-awesome-skill/`）。
3. **明确声明开源协议**：
* 请在你的 Skill 文件夹内放置独立的 `LICENSE` 文件。
* 推荐在 `SKILL.md` 的前置元数据（Metadata）中显式加入 `license: MIT/GPL-3.0` 等声明标识。


4. **提交申请**：提交 Pull Request (PR) 并简要说明该 Skill 的应用场景。

---

## 开源协议说明 (License)

* **仓库基础设施**：本仓库的目录结构、构建脚本及相关说明文档采用 MIT 协议。
* **独立的 Skill 协议**：**本仓库中收录的每个 Skill 均独立拥有其自身的开源协议。** 请在安装和使用特定的 Skill 前，务必查阅该 Skill 目录下的 `LICENSE` 文件或说明。若该 Skill 未包含独立的协议声明，默认继承主仓库的 MIT 协议。
