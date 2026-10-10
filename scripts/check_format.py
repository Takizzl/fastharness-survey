"""Check README paper table and review HTML follow CONTRIBUTING.md rules.

Run: python scripts/check_format.py
Exits non-zero and prints every problem found.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
WIDTHS = [("Year", 50), ("Venue", 130), ("Paper Title", 440), ("Repository", 110),
          ("Method", 230), ("Result", 160), ("Team", 120), ("Website", 70)]
HEADER = "| " + " | ".join(
    f'{n}<br><img src="assets/spacer.png" width="{w}" height="1">' for n, w in WIDTHS) + " |"
SEPARATOR = "|" + ":---:|" * 8

errors = []
readme = (ROOT / "README.md").read_text(encoding="utf-8")
review = (ROOT / "review" / "论文审阅表.html").read_text(encoding="utf-8")

for heading in ("Current Focus", "Contents"):
    if not re.search(rf"^## \S* ?{heading}$", readme, re.M):
        errors.append(f"README 缺少「{heading}」一节")
paper_rows = len(re.findall(r"^\| \d{4} \|", readme, re.M))
badge = re.search(r"badge/Papers-(\d+)-", readme)
if not badge or int(badge.group(1)) != paper_rows:
    errors.append(f"README 顶部 Papers 徽章应为 {paper_rows}（表格里实际的论文数）")
meetings = len(list((ROOT / "meetings").glob("*.md")))
mbadge = re.search(r"badge/Meetings-(\d+)-", readme)
if not mbadge or int(mbadge.group(1)) != meetings:
    errors.append(f"README 顶部 Meetings 徽章应为 {meetings}（meetings/ 里的纪要数）")

lines = readme.splitlines()
if "## 论文" in readme:
    errors.append("README 不要「## 论文」总表，每个类别单独一张表")
if HEADER not in lines:
    errors.append("README 没有找到标准表头，见 CONTRIBUTING.md")
for i, line in enumerate(lines):
    if line.startswith("| Year") and line != HEADER:
        errors.append(f"README 第 {i + 1} 行表头和标准表头不一致（列宽占位图也要一致）")
    if line != HEADER:
        continue
    if not lines[i - 2].startswith("## "):
        errors.append(f"README 第 {i + 1} 行的表格上方要有「## 类别名」标题")
    if lines[i + 1].strip() != SEPARATOR:
        errors.append(f"README 第 {i + 2} 行分隔行必须是 8 列居中：" + SEPARATOR)
    for n, row in enumerate(lines[i + 2:], start=i + 3):
        if not row.startswith("|"):
            break
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) != 8:
            errors.append(f"README 第 {n} 行应有 8 列，实际 {len(cells)} 列")
            continue
        year, _, title, repo, method, result, team, website = cells
        m = re.match(r"\[(.+)\]\((https://arxiv\.org/[^)]+)\)", title)
        if not m:
            errors.append(f"README 第 {n} 行 Paper Title 必须是 [完整标题](arXiv 链接)")
            continue
        text = m.group(1)
        plain = text.replace("&nbsp;", " ").replace("<br>", " ")
        if len(plain) > 40 and text.count("<br>") != 1:
            errors.append(f"README 第 {n} 行标题超过 40 字符，需用一个 <br> 断成两行")
        if " " in text:
            errors.append(f"README 第 {n} 行标题内的空格要写成 &nbsp;")
        if not re.fullmatch(r"\d{4}", year):
            errors.append(f"README 第 {n} 行 Year 应为四位年份")
        if repo != "---" and "img.shields.io/github/stars/" not in repo:
            errors.append(f"README 第 {n} 行 Repository 应为星数徽章或 ---")
        if website != "---" and not website.startswith("[website]("):
            errors.append(f"README 第 {n} 行 Website 应为 [website](链接) 或 ---")
        for name, val in (("Method", method), ("Result", result), ("Team", team)):
            if not val:
                errors.append(f"README 第 {n} 行 {name} 不能为空")
        arxiv_id = re.search(r"(\d{4}\.\d{4,5})", m.group(2))
        if arxiv_id and arxiv_id.group(1) not in review:
            errors.append(f"README 第 {n} 行论文 {arxiv_id.group(1)} 不在审阅表里，必须先进审阅表")

if errors:
    print("格式检查未通过：")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("格式检查通过")
