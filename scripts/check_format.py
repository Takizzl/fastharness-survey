"""Check README paper tables and the review HTML follow CONTRIBUTING.md rules.

Run: python scripts/check_format.py
Exits non-zero and prints every problem found.
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from whats_new import load_review, source_key, card_source

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
# Header cells are padded with non-breaking spaces so every category table has the same column widths on GitHub.
PADDING = [("Paper", 17), ("Venue", 3), ("Method", 19), ("Result", 10), ("Team", 3)]
PAPER_CELL = re.compile(
    r"\*\*[^*]+\*\*: [^<\[\]]+<br>"
    r"\\\[\[Paper\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5})\)\\\]"
    r" \\\[\[Code\]\(https://github\.com/[^)]+\)\\\]"
    r" \\\[\[Website\]\(https?://[^)]+\)\\\]")
WIDTHS = PADDING
HEADER = "| " + " | ".join("&nbsp;" * k + n + "&nbsp;" * k for n, k in PADDING) + " |"
# Vague wording not allowed in Method / Result: use concrete names and exact numbers instead.
VAGUE = ("约", "大约", "左右", "等", "多个", "一些", "若干", "大幅", "显著", "明显", "很多", "更好", "较好")
SEPARATOR = "|" + ":---:|" * len(WIDTHS)

errors = []
review_rows = load_review()
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
        if "[待审核](review/论文审阅表.html)" in paper:
            pending_links = re.findall(r"\]\((https://[^)]+)\)", paper)
            matches = [review_rows[key] for key in dict.fromkeys(map(source_key, pending_links)) if key in review_rows]
            if len(matches) != 1 or "待审核" not in matches[0]["paper"]:
                errors.append(f"README 第 {n} 行待审核条目必须有来源链接并已进入审阅表")
            if not all(cells) or method in ("-", "—"):
                errors.append(f"README 第 {n} 行待审核论文需要方法，缺失字段写 —")
            if not re.search(r"[一-鿿]", method) or "<br>" in method:
                errors.append(f"README 第 {n} 行待审核方法必须为中文单段")
            if len(method) > 100 or len(result) > 100:
                errors.append(f"README 第 {n} 行待审核方法或结果过长，应精简为一句话")
            continue
        pm = PAPER_CELL.fullmatch(paper)
        if not pm:
            errors.append(f"README 第 {n} 行 Paper 应为 **简称**: 标题<br>\\[[Paper](arXiv)\\] \\[[Code](GitHub)\\] \\[[Website](主页)\\]，"
                          "三个链接都必须有，顺序固定")
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

CARD_ROWS = ("模块", "Year / Venue", "Paper", "Code", "Website", "Team")
CARD_SECTIONS = ("一句话", "问题", "方法", "真机结果")
for card in sorted((ROOT / "papers").glob("*.md")):
    text = card.read_text(encoding="utf-8")
    key = card_source(card.relative_to(ROOT))
    record = review_rows.get(key)
    if record is None:
        errors.append(f"{card.name} 的元数据来源没有对应审阅表条目")
    else:
        module = re.search(r"^\| 模块 \| (.*?) \|$", text, re.M)
        if module and module.group(1).split("（", 1)[0] != record["module"]:
            errors.append(f"{card.name} 模块与审阅表不一致")
        state = "已入库" if "已入库" in record["paper"] else "待审核"
        review_field = re.search(r"^\| Review \| (.*?) \|$", text, re.M)
        if not review_field or state not in review_field.group(1).replace("待人工审核", "待审核"):
            errors.append(f"{card.name} 审核状态与审阅表不一致")
    for row in CARD_ROWS:
        m = re.search(rf"^\| {re.escape(row)} \| (.*?) \|$", text, re.M)
        if not m or not m.group(1).strip():
            errors.append(f"{card.name} 缺少「{row}」或为空（没有的写 -）")
    for sec in CARD_SECTIONS + ("仿真结果|实验结果",):
        m = re.search(rf"^## (?:{sec})[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        if not m or not m.group(1).strip():
            errors.append(f"{card.name} 缺少「{sec.split('|')[0]}」一节或内容为空")

if paper_rows != len(review_rows):
    errors.append(f"README 条目数 {paper_rows} 与审阅表 {len(review_rows)} 不一致")

# Check maintained local destinations; source archives are immutable evidence.
documents = [*ROOT.glob("*.md"), *ROOT.glob("papers/*.md"), *ROOT.glob("ideas/*.md"),
             *ROOT.glob("meetings/*.md"), ROOT / "review" / "论文审阅表.html"]
for document in documents:
    text = document.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```|`[^`\n]*`", "", text, flags=re.S)
    links = re.findall(r"\]\(([^)]+)\)", text) + re.findall(r'(?:href|src)="([^"]+)"', text)
    for link in links:
        parts = urlsplit(link)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        target = (document.parent / unquote(parts.path)).resolve()
        if not target.exists():
            errors.append(f"{document.relative_to(ROOT)} 的站内目标不存在：{link}")

if errors:
    print("格式检查未通过：")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("格式检查通过")
