#!/usr/bin/env python3
"""
stem-note-tutor 阶段管理器
用法: python3 scripts/stage_manager.py --stage=<1|2|3|4> [--workdir=<工作目录>]

--stage:   阶段编号 1-4
--workdir: 工作目录（存放 stageN.md 的位置），默认为当前目录
"""

import argparse
import os
import sys


def check_prereq(stage: int, workdir: str):
    """检查前置 stageN.md 文件是否存在"""
    required_file = os.path.join(workdir, f"stage{stage}.md")
    if not os.path.isfile(required_file):
        print(f"❌ 前置任务未完成：在 {workdir} 下未找到 stage{stage}.md")
        print(f"请先完成第 {stage} 阶段，生成 stage{stage}.md 后再继续。")
        sys.exit(1)


PROMPTS = {
    1: """你觉得这一部分最重要的是什么，与后续章节最核心关联的思想是什么？我要如何感性地感受？""",

    2: """好的，那现在给我讲解这份课件吧，尽量以感性的视角带我掌握每一份知识点，涵盖每一个重要知识点""",

    3: """你讲得很好，但只能相当于带我入了门，而实际的理论或公式遇上了我也不会，如果能穿插一些对具体理论和公式的实际感受就好了，这样我还能参加期末考""",

    4: """前面三阶段你都讲过了，现在我对课件中抽象的概念、公式的物理含义、以及容易混淆的对比点还有一些疑问。

请根据课件的实际内容，**站在我（一个正在学习的学生）的角度**，找出课件中 3 个最容易让人困惑的难点，用追问的形式提出来，然后由你来逐一深入解答。

这 3 个追问应当覆盖不同方面，例如：
- 某个抽象概念的直觉理解
- 某个公式中各个参数的物理/实际意义
- 不同概念之间的对比与区别
- 容易犯错的典型误区
请直接输出追问和对应的深入解答，不要问我"哪些地方不懂"。

完成后，请思考前面及当前所有阶段是否做到：
1. 输出内容方便渲染（如数学公式用`$`包裹，代码块用反引号包裹等）
2. 是否在各阶段的产物中直接或间接地涵盖了所有关键且重要的知识点"""
}


def main():
    parser = argparse.ArgumentParser(description="stem-note-tutor 阶段管理器")
    parser.add_argument("--stage", type=int, required=True, choices=[1, 2, 3, 4],
                        help="阶段编号 1-4")
    parser.add_argument("--workdir", type=str, default=".",
                        help="工作目录（存放 stageN.md 的位置），默认当前目录")
    args = parser.parse_args()

    workdir = args.workdir
    stage = args.stage

    # 前置检查
    if stage >= 2:
        check_prereq(stage - 1, workdir)

    # 输出对应阶段的 prompt
    print(PROMPTS[stage].strip())


if __name__ == "__main__":
    main()
