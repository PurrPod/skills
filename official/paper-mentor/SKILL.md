---
name: paper-mentor
description: Use this skill when the user provides a research paper (PDF or text) and wants to go through a complete 4-stage deep study — from prerequisites to code architecture to live experiment observation. The skill produces 4 markdown files in a progressive, self-contained reconstruction notebook style.
---

# Paper Mentor — 4-Stage Research Reconstruction

## 核心规则

1. **严格顺序执行**：必须从 Stage 1 开始，依次推进到 Stage 4。不可跳级。
2. **脚本获取提示词**：每个阶段开始前，运行 `python3 scripts/stage_manager.py --stage=N --workdir=<工作目录>` 获取该阶段的提示词。如果前置阶段未完成，脚本会报错阻止继续。
3. **自行回答**：获取 prompt 后，**由你根据论文内容自行写出完整的讲解文档**。所有交互环节（选择题、追问等）采用自问自答形式——文档里自己提问、自己解答，行云流水。
4. **交付产物**：每个阶段完成后，将内容保存为 `stage1.md` ~ `stage4.md`，存放在 `--workdir` 指定的目录下。
5. **统一输出目录**：所有文件放入 `/path/to/your/workdir/`（由你创建）。
6. **静默推进**：每个阶段完成后直接进入下一阶段，不要在中间告知用户文件已生成。全部 4 个阶段都完成后，再统一告知用户。
7. **内容完备性**：各阶段的产物必须覆盖论文所有关键知识点。

## 详细步骤

### Stage 1 — Prerequisites（前置知识清单）

1. 创建工作目录 `/path/to/workdir/`。
2. 运行 `python3 scripts/stage_manager.py --stage=1 --workdir=/path/to/your/workdir/` 获取 prompt。
3. 根据 prompt 和论文内容，从最基础的依赖知识开始，逐层构建前置知识树，写为自包含讲解。
4. 保存为 `/path/to/your/workdir/stage1.md`。
5. 直接进入 Stage 2。

### Stage 2 — Research Reconstruction（发明者思维复盘）

1. 运行 `python3 scripts/stage_manager.py --stage=2 --workdir=/path/to/your/workdir/` 获取 prompt。
2. 根据 prompt 和论文内容，以"站在作者视角重新发明论文"的方式写出复盘文档。自问自答，给出选择题并自行解答。
3. 保存为 `/path/to/your/workdir/stage2.md`。
4. 直接进入 Stage 3。

### Stage 3 — Code Architecture Reconstruction（代码架构重建）

1. 运行 `python3 scripts/stage_manager.py --stage=3 --workdir=/path/to/your/workdir/` 获取 prompt。
2. 根据 prompt 和论文内容，从系统建模→架构推导→公式设计→代码映射的顺序，输出完整的架构重建文档。
3. 保存为 `/path/to/your/workdir/stage3.md`。
4. 直接进入 Stage 4。

### Stage 4 — Bring the Paper to Life（让论文活起来）

1. 运行 `python3 scripts/stage_manager.py --stage=4 --workdir=/path/to/your/workdir/` 获取 prompt。
2. 根据 prompt 和论文代码仓库（如果代码可用），输出 Live Paper 模式的实验讲解文档。
3. 保存为 `/path/to/your/workdir/stage4.md`。
4. 告知用户全部 4 个阶段已完成。

## 输出格式要求

- Markdown 格式，短句分行、大量留空行制造节奏感
- 使用 `$` 包裹数学公式
- 使用 ``` 包裹代码块
- 使用 ASCII 箭头（↓ →）和视觉化图表
- 每个文件末尾注明"内容基于论文阅读与经验整合而成"
