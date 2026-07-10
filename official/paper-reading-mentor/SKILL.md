---
name: paper-reading-mentor
description: Use this skill when the user provides a research paper (PDF or text) and wants to go through a complete deep study. Triggers on: deep paper analysis, paper explanation, research reconstruction, paper code walkthrough, paper experiment replication. Do NOT trigger on: reading a paper for a quick summary only, looking up a specific formula or definition, writing a paper review/survey.
---

# Paper Reading Mentor — 4+1 Stage Research Reconstruction

## 核心规则

1. **严格顺序执行**：必须从 Stage 1 开始，依次推进到 Stage 4。Stage 5 可选，仅在用户明确要求时触发。不可跳级。
2. **脚本获取提示词**：每个阶段开始前，运行 `python3 scripts/stage_manager.py --stage=N --workdir=<工作目录>` 获取该阶段的提示词。如果前置阶段未完成，脚本会报错阻止继续。
3. **自行回答，不等待用户**：获取 prompt 后，**由你根据论文内容自行写出完整的讲解文档**。所有交互环节（选择题、追问等）采用自问自答形式——文档里自己提问、自己解答，行云流水。**绝对不要停下来等用户回答再继续**。
4. **交付产物**：每个阶段完成后，将内容保存为对应名称的文件，存放在 `--workdir` 指定的目录下：
   - Stage 1 → `PreKnowledgeTree.md`
   - Stage 2 → `PaperRebirth.md`
   - Stage 3 → `ArchitectureBlueprint.md`
   - Stage 4 → `ExecutionCompanion.md`
   - Stage 5（可选）→ `ResearchEvolution.md`
5. **独立工作目录**：每次讲解建一个新的独立工作目录（如 `mkdir -p /agent_vm/paper-reading-<论文关键词>/`），不要复用固定路径，避免覆盖历史产出。
6. **静默推进**：每个阶段完成后直接进入下一阶段，不要在中间告知用户文件已生成。全部阶段都完成后，再统一告知用户。
7. **跨阶段链接**：每个阶段文件的末尾，必须包含指向**前一个文件**和**下一个文件**的 Markdown 链接（`[← 回顾：xxx](PreKnowledgeTree.md)` / `[继续：xxx →](PaperRebirth.md)`），形成自然的阅读导航链。Stage 1 没有前驱，Stage 4/5 看情况。
8. **内容完备性**：各阶段的产物必须覆盖论文所有关键知识点。
9. **大文件写入用 Bash**：如果文件内容超过 50 行，使用 Bash 的 `cat >>` 分批写入，避免 FileSystem 截断。
10. **后阶段 Prerequisite 自检**：每个阶段（Stage 2~5）完成后，自动问自己一句"有没有发现新的前置知识？"。如果有，**立即追加更新 `PreKnowledgeTree.md`**，在末尾新增章节。保证知识树的完整性随阶段推进而生长。

## Gotchas（避坑指南）

- **PDF 读取分段**：读取论文 PDF 时，使用 FileSystem read 每次 limit ≤ 50 行，否则会被截断。读完一段后立即在下轮继续读取下一段。
- **纯理论论文处理**：如果论文没有公开代码仓库（理论证明类论文），Stage 3 应从第一性原理推导验证性实现的代码架构，Stage 4 应实际写出并运行这段验证代码，让证明在 CPU 上执行。
`ExecutionCompanion.md`, `ResearchEvolution.md`。
- **材料不可用时的免责声明**：如果论文代码仓库打不开/GitHub 404、PDF 乱码或不可读、Supplementary 找不到、仓库只有 README 没有实际代码——在产物文件开头用显眼 `⚠️` 标注：哪些内容忠实于原文、哪些内容是基于片段/描述推断的、哪些是自行构造的示例。不要假装读到了你没读到的东西。

## Failure Mode（常见失败场景与处理）

以下是执行此 Skill 时可能遇到的典型故障，必须按规则处理：

| 故障场景 | 处理方式 |
|----------|----------|
| 论文没有公开代码仓库 | Stage 3/4 已内置处理：从第一性原理推导验证代码，实际写出并运行 |
| GitHub/代码链接打不开（404/超时） | 在 `ExecutionCompanion.md` 开头注明"代码仓库不可访问"，然后按"无代码"模式处理 |
| 代码仓库只有 README，没有实际源码 | 同上，注明后按无代码模式处理 |
| PDF 无法读取/乱码 | 尝试换一种读取方式（如先 copy 到沙盒再读）。如果仍然失败，告知用户 PDF 不可读，请提供可读版本 |
| Supplementary 材料找不到 | 在对应产物中注明"Supplementary 未获取，以下分析基于主论文" |
| 论文引用了你没读过的前置论文 | 记录到 `PreKnowledgeTree.md` 的"延伸阅读"章节，不要假装读过 |
| 论文格式异常（如扫描版） | 使用 `Bash` 工具 + `pdftotext` 或 `ocrmypdf` 尝试转换。若转换后乱码，按"PDF 不可读"处理 |

## 详细步骤

### Stage 1 — 前置知识树（PreKnowledgeTree）

1. 创建工作目录（建议 `/agent_vm/paper-reading-output/`）。
2. 运行 `python3 scripts/stage_manager.py --stage=1 --workdir=/path/to/workdir/` 获取 prompt。
3. 根据 prompt 和论文内容，从最基础的依赖知识开始，逐层构建前置知识树，写为自包含讲解。
4. 保存为 `PreKnowledgeTree.md`，末尾加导航链接指向 `PaperRebirth.md`。
5. 直接进入 Stage 2。

### Stage 2 — 论文重生（PaperRebirth）

1. 运行 `python3 scripts/stage_manager.py --stage=2 --workdir=/path/to/workdir/` 获取 prompt。
2. 根据 prompt 和论文内容，以"站在作者视角重新发明论文"的方式写出复盘文档。自问自答，给出选择题并自行解答。
3. 保存为 `PaperRebirth.md`，开头链接回 `PreKnowledgeTree.md`，末尾链接指向 `ArchitectureBlueprint.md`。
4. 直接进入 Stage 3。

### Stage 3 — 架构蓝图（ArchitectureBlueprint）

1. 运行 `python3 scripts/stage_manager.py --stage=3 --workdir=/path/to/workdir/` 获取 prompt。
2. 根据 prompt 和论文内容，从系统建模→架构推导→公式设计→代码映射的顺序，输出完整的架构重建文档。
3. **对于纯理论论文（无代码仓库）**：从第一性原理推导验证性实现，包含完整的数据流图、文件结构设计和伪代码。
4. 保存为 `ArchitectureBlueprint.md`，开头链接回 `PaperRebirth.md`，末尾链接指向 `ExecutionCompanion.md`。
5. 反思 stage1 里的交付产物是否有需要更新的新的前置知识。
6. 直接进入 Stage 4。

### Stage 4 — 执行伴侣（ExecutionCompanion）

1. 运行 `python3 scripts/stage_manager.py --stage=4 --workdir=/path/to/workdir/` 获取 prompt。
2. 按 prompt 中的**分层递进策略**执行：Tier 1 CPU 最小 Demo → Tier 2 缩小版 Demo → Tier 3 官方实验介绍。
3. **纯理论论文**：跳过 Tier 3，专注于写验证代码并运行。
4. 保存为 `ExecutionCompanion.md`，开头链接回 `ArchitectureBlueprint.md`。
5. 在文件末尾追加 **Verification Checklist（验证清单）**：列出未来读者复现/运行此论文时需要检查的关键节点，包括预期输出、常见错误标志、调试建议。让读者知道"哪里没成功"而不仅仅是"结束了"。
6. 如果用户没有要求 Stage 5，告知用户全部 4 个阶段已完成。**如果用户明确要求深入分析/审稿视角**，则进入 Stage 5。

### Stage 5（可选）— 研究进化（ResearchEvolution）

> ⚠️ **仅当用户明确要求审稿视角/深入分析时触发**，默认不执行。

1. 运行 `python3 scripts/stage_manager.py --stage=5 --workdir=/path/to/workdir/` 获取 prompt。
2. 根据 prompt，以 Reviewer 的视角对论文进行证据导向的批判性分析。**观点要具体、有证据支撑。**
3. 保存为 `ResearchEvolution.md`，开头链接回 `ExecutionCompanion.md`（如果生成了 Stage 4）或 `ArchitectureBlueprint.md`（如果跳过了 Stage 4）。
4. 告知用户全部阶段已完成。

## 输出格式要求

- Markdown 格式，短句分行、大量留空行制造节奏感
- 使用 `$` 包裹数学公式
- 使用 ``` 包裹代码块
- 使用 ASCII 箭头（↓ →）和视觉化图表
- 每个文件末尾注明"内容基于论文阅读与经验整合而成"
- **每个文件头部和尾部必须有导航链接**，链向相邻阶段的文档，像读书一样自然翻页
