"""Check README paper tables and the review HTML follow CONTRIBUTING.md rules.

Run: python scripts/check_format.py
Exits non-zero and prints every problem found.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
# Header cells are padded with non-breaking spaces so every category table has the same column widths on GitHub.
PADDING = [("Paper", 17), ("Venue", 3), ("Method", 19), ("Result", 10), ("Team", 3)]
PAPER_CELL = re.compile(
    r"\*\*[^*]+\*\*: [^<\[\]]+<br>"
    r"\\\[\[Paper\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5})\)\\\]"
    r"( \\\[\[Code\]\(https://github\.com/[^)]+\)\\\])?"
    r"( \\\[\[Website\]\(https?://[^)]+\)\\\])?")
WIDTHS = PADDING
HEADER = "| " + " | ".join("&nbsp;" * k + n + "&nbsp;" * k for n, k in PADDING) + " |"
# Vague wording not allowed in Method / Result: use concrete names and exact numbers instead.
VAGUE = ("约", "大约", "左右", "等", "多个", "一些", "若干", "大幅", "显著", "明显", "很多", "更好", "较好")
SEPARATOR = "|" + ":---:|" * len(WIDTHS)

errors = []
readme = (ROOT / "README.md").read_text(encoding="utf-8")
review = (ROOT / "review" / "论文审阅表.html").read_text(encoding="utf-8")

for heading in ("当前主线", "Contents"):
    if not re.search(rf"^## (?:\S+ )?{heading}", readme, re.M):
        errors.append(f"README 缺少「## {heading}」一节")

lines = readme.splitlines()
paper_rows = 0
for i, line in enumerate(lines):
    if re.match(r"\| (&nbsp;)*Paper", line) and line != HEADER:
        errors.append(f"README 第 {i + 1} 行表头和标准表头不一致（表头里的 &nbsp; 用来固定列宽，要和标准表头完全一致）")
    if line != HEADER:
        continue
    if not lines[i - 2].startswith("## "):
        errors.append(f"README 第 {i + 1} 行的表格上方要有「## 类别名」标题")
    if lines[i + 1].strip() != SEPARATOR:
        errors.append(f"README 第 {i + 2} 行分隔行必须是 {len(WIDTHS)} 列居中：" + SEPARATOR)
    for n, row in enumerate(lines[i + 2:], start=i + 3):
        if not row.startswith("|"):
            break
        paper_rows += 1
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) != len(WIDTHS):
            errors.append(f"README 第 {n} 行应有 {len(WIDTHS)} 列，实际 {len(cells)} 列")
            continue
        paper, venue, method, result, team = cells
        pm = PAPER_CELL.fullmatch(paper)
        if not pm:
            errors.append(f"README 第 {n} 行 Paper 应为 **简称**: 标题<br>\\[[Paper](arXiv)\\] \\[[Code](GitHub)\\] \\[[Website](主页)\\]，"
                          "顺序固定，没有的 Code / Website 省略")
            continue
        for label, val in (("Venue", venue), ("Method", method), ("Result", result), ("Team", team)):
            if not val:
                errors.append(f"README 第 {n} 行 {label} 不能为空")
        if not re.search(r"[一-鿿]", method):
            errors.append(f"README 第 {n} 行 Method 要用中文")
        for label, val, limit in (("Method", method, 55), ("Result", result, 35)):
            if len(re.sub(r"[ -~]", "", val)) + len(re.findall(r"[ -~]", val)) / 2 > limit:
                errors.append(f"README 第 {n} 行 {label} 太长，压到约 {limit} 个汉字以内")
        for label, val in (("Method", method), ("Result", result)):
            vague = [v for v in VAGUE if v in val]
            if vague:
                errors.append(f"README 第 {n} 行 {label} 有模糊说法 {vague}，改成具体的名称或数字")
        if not re.search(r"\d", result) or "<br>" in result:
            errors.append(f"README 第 {n} 行 Result 要浓缩成一句含关键数字的话，不要换行")
        if "<br>" in method:
            errors.append(f"README 第 {n} 行 Method 要浓缩成一句话，不要换行")
        if "/" in team:
            errors.append(f"README 第 {n} 行 Team 不要用 /，多个单位用 <br> 分行")
        if not re.search(r"(arXiv|\d{4})", venue):
            errors.append(f"README 第 {n} 行 Venue 应写会议和年份，如 ICML 2026 / arXiv 2026.09")
        if pm.group(1) not in review:
            errors.append(f"README 第 {n} 行论文 {pm.group(1)} 不在审阅表里，必须先进审阅表")

stats = re.search(r"<sub>(\d+) Papers? · (\d+) Meetings? · Updated \d{4}\.\d{2}\.\d{2}</sub>", readme)
meetings = len(list((ROOT / "meetings").glob("*.md")))
if not stats:
    errors.append("README 标题下缺少统计行：<sub>N Papers · M Meetings · Updated YYYY.MM.DD</sub>")
else:
    if int(stats.group(1)) != paper_rows:
        errors.append(f"README 统计行的论文数应为 {paper_rows}（表格里实际的论文数）")
    if int(stats.group(2)) != meetings:
        errors.append(f"README 统计行的会议数应为 {meetings}（meetings/ 里的纪要数）")

CARD_ROWS = ("模块", "Year / Venue", "Paper", "Code", "Website", "Team")
CARD_SECTIONS = ("一句话", "问题", "方法", "真机结果")
for card in sorted((ROOT / "papers").glob("*.md")):
    text = card.read_text(encoding="utf-8")
    for row in CARD_ROWS:
        m = re.search(rf"^\| {re.escape(row)} \| (.*?) \|$", text, re.M)
        if not m or not m.group(1).strip():
            errors.append(f"{card.name} 缺少「{row}」或为空（没有的写 -）")
    for sec in CARD_SECTIONS + ("仿真结果|实验结果",):
        m = re.search(rf"^## (?:{sec})[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        if not m or not m.group(1).strip():
            errors.append(f"{card.name} 缺少「{sec.split('|')[0]}」一节或内容为空")

if errors:
    print("格式检查未通过：")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("格式检查通过")
