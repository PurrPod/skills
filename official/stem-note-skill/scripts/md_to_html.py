#!/usr/bin/env python3
import os
import sys
import json
import re

def print_help_and_exit(error_msg=None):
    print("=" * 60)
    if error_msg:
        print(f"❌ 错误: {error_msg}\n")
    else:
        print("💡 沉浸式复习工作台生成器 - 帮助说明\n")
        
    print("【重大升级】")
    print("现在你需要传入【根目录】（如 信号与系统_速成复习库）。")
    print("脚本会自动扫描内部的所有章节，并生成一个总的 index.html 目录页。\n")
    
    print("【正确命令格式】")
    print("python scripts/md_to_html.py <根目录路径>\n")
    print("=" * 60)
    sys.exit(1)

def parse_markdown_quiz(md_text):
    lines = md_text.split('\n')
    title = "章节自测题"
    questions = []
    current_category = "综合题"
    current_question = None
    in_analysis = False  # 新增状态锁：进入解析区后锁定，直到遇到新题号
    
    for line in lines:
        stripped = line.strip()
        if not stripped: continue
            
        if stripped.startswith('# '):
            title = stripped[2:].strip()
            continue
        if stripped.startswith('## '):
            current_category = stripped[3:].strip()
            continue
            
        # 匹配大题号（题目开始）- 解析锁开启时忽略
        match_q = re.match(r'^(\d+)\.\s*(.*)', line)
        if match_q:
            if current_question: questions.append(current_question)
            
            q_type = 'choice'
            if '判断' in current_category: q_type = 'judgement'
            elif '填空' in current_category: q_type = 'blank'
            elif '计算' in current_category or '简答' in current_category: q_type = 'qa'
                
            current_question = {'category': current_category, 'question': match_q.group(2), 'type': q_type, 'options': [], 'answer': '', 'analysis': '', '_is_parsing_analysis': False}
            in_analysis = False
            continue

        # 紧凑型判断题匹配 - 解析锁开启时忽略
        match_tf = re.match(r'^\s*-\s*\[([ xX])\]\s*(\d+)\.\s*(.*)', line)
        if match_tf and '判断' in current_category:
            if current_question: questions.append(current_question)
            is_true = match_tf.group(1).lower() == 'x'
            current_question = {'category': current_category, 'question': match_tf.group(3), 'type': 'judgement', 'options': [{'text': '正确'}, {'text': '错误'}], 'answer': '正确' if is_true else '错误', 'analysis': '', '_is_parsing_analysis': False}
            in_analysis = False
            continue
            
        if current_question:
            # 进入解析区后，开启状态锁
            if stripped.startswith('>') or stripped.startswith('解析') or stripped.startswith('**解'):
                in_analysis = True
                current_question['_is_parsing_analysis'] = True
                content = stripped.lstrip('>').replace('解析：', '').replace('解析:', '').strip()
                if content: current_question['analysis'] += content + '<br>'
                continue
                
            # 如果解析锁开了，把后续所有行都追加到 analysis 中，无论它是不是数字
            if in_analysis:
                current_question['analysis'] += stripped + '<br>'
                continue
            
            # 选项匹配
            match_opt = re.match(r'^\s*-\s*\[([ xX])\]\s*(.*)', line)
            if match_opt:
                is_correct = match_opt.group(1).lower() == 'x'
                opt_text = match_opt.group(2).strip()
                current_question['options'].append({'text': opt_text})
                if is_correct:
                    letter_match = re.match(r'^([A-Za-z])\s*\.\s*', opt_text)
                    current_question['answer'] = letter_match.group(1) if letter_match else opt_text
                continue
                
            if stripped.startswith('答案：') or stripped.startswith('答案:'):
                current_question['answer'] = stripped[3:].strip()
                current_question['type'] = 'blank'
                continue
                
            if current_question.get('_is_parsing_analysis'):
                current_question['analysis'] += stripped + '<br>'
                continue

    if current_question:
        questions.append(current_question)
        
    for q in questions:
        if '_is_parsing_analysis' in q: del q['_is_parsing_analysis']
        if not q['analysis']: q['analysis'] = '暂无解析'
            
    return title, questions

def generate_root_index(root_dir, course_name, chapters):
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{course_name} - 期末速成复习库</title>
    <style>
        :root {{ --bg: #f8fafc; --card: #ffffff; --text: #1e293b; --primary: #4f46e5; --hover: #f1f5f9; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, sans-serif; }}
        body {{ background: var(--bg); color: var(--text); padding: 40px 20px; }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        .header {{ text-align: center; margin-bottom: 50px; }}
        .header h1 {{ font-size: 28pt; color: var(--primary); margin-bottom: 10px; }}
        .header p {{ color: #64748b; font-size: 12pt; }}
        .chapter-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 20px; }}
        .chapter-card {{ background: var(--card); border-radius: 16px; padding: 25px; text-decoration: none; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); transition: all 0.3s; display: flex; flex-direction: column; justify-content: space-between; }}
        .chapter-card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 15px -3px rgba(79,70,229,0.1); border-color: #c7d2fe; }}
        .ch-title {{ font-size: 14pt; font-weight: bold; color: #334155; margin-bottom: 15px; line-height: 1.4; }}
        .ch-meta {{ display: flex; justify-content: space-between; align-items: center; color: #64748b; font-size: 10.5pt; border-top: 1px dashed #cbd5e1; padding-top: 15px; }}
        .btn-enter {{ background: #eef2ff; color: var(--primary); padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 10pt; transition: 0.2s; }}
        .chapter-card:hover .btn-enter {{ background: var(--primary); color: white; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 {course_name}</h1>
            <p>沉浸式交互期末复习库</p>
        </div>
        <div class="chapter-grid">
"""
    for ch in chapters:
        html += f"""
            <a href="{ch['path']}" class="chapter-card">
                <div class="ch-title">{ch['name']}</div>
                <div class="ch-meta">
                    <span>包含 {ch['q_count']} 道测试题</span>
                    <span class="btn-enter">进入学习 →</span>
                </div>
            </a>
        """
    
    html += """
        </div>
    </div>
</body>
</html>
"""
    index_path = os.path.join(root_dir, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return index_path

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ['-h', '--help']:
        print_help_and_exit()

    root_dir = sys.argv[1]
    if not os.path.exists(root_dir) or not os.path.isdir(root_dir):
        print_help_and_exit(f"找不到指定的根目录: '{root_dir}'")

    # 提取课程名 (如从 "信号与系统_速成复习库" 中提取 "信号与系统")
    course_name = os.path.basename(os.path.normpath(root_dir)).replace('_速成复习库', '')
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "..", "templates", "test_html_templates.html")
    if not os.path.exists(template_path):
        print_help_and_exit(f"缺失 HTML 模板文件: {template_path}")
        
    with open(template_path, 'r', encoding='utf-8') as f:
        html_template = f.read()

    processed_chapters = []

    # 遍历根目录下的子文件夹
    for item in sorted(os.listdir(root_dir)):
        chap_path = os.path.join(root_dir, item)
        # 只处理非隐藏的文件夹
        if os.path.isdir(chap_path) and not item.startswith('.'):
            quiz_md_path = os.path.join(chap_path, "章节自测题.md")
            notes_md_path = os.path.join(chap_path, "核心概念与公式.md")
            
            # 如果有题库，则处理
            if os.path.exists(quiz_md_path):
                print(f"正在编译章节: {item} ...")
                
                with open(quiz_md_path, 'r', encoding='utf-8') as f:
                    quiz_text = f.read()
                    
                notes_text = "> **⚠️ 未找到核心笔记**\n\n未找到 `核心概念与公式.md`。"
                if os.path.exists(notes_md_path):
                    with open(notes_md_path, 'r', encoding='utf-8') as f:
                        notes_text = f.read()

                title, questions = parse_markdown_quiz(quiz_text)
                questions_json = json.dumps(questions, ensure_ascii=False, indent=2)
                safe_notes_text = notes_text.replace("</script>", "<\\/script>")

                # 注入变量 (新增了 COURSE_NAME 和 CHAPTER_NAME)
                final_html = html_template.replace("{{COURSE_NAME}}", course_name)\
                                          .replace("{{CHAPTER_NAME}}", item)\
                                          .replace("{{QUESTIONS_JSON}}", questions_json)\
                                          .replace("{{NOTES_MARKDOWN}}", safe_notes_text)

                output_html = os.path.join(chap_path, "复习工作台.html")
                with open(output_html, 'w', encoding='utf-8') as f:
                    f.write(final_html)
                    
                processed_chapters.append({
                    'name': item,
                    'path': f"{item}/复习工作台.html",
                    'q_count': len(questions)
                })

    # 生成总目录 index.html
    if processed_chapters:
        index_html_path = generate_root_index(root_dir, course_name, processed_chapters)
        print("=" * 50)
        print("✅ 全书编译成功！")
        print(f"共生成了 {len(processed_chapters)} 个章节工作台。")
        print(f"🏠 请用浏览器打开主页总目录开始复习: \n---> {index_html_path}")
    else:
        print("⚠️ 未在目录下找到任何包含 '章节自测题.md' 的子文件夹。")

if __name__ == '__main__':
    main()