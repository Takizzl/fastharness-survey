"""Check README paper tables and the review HTML follow CONTRIBUTING.md rules.

Run: python scripts/check_format.py
Exits non-zero and prints every problem found.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
WIDTHS = [("Name", 90), ("Paper", 250), ("Venue", 95), ("Method", 250),
          ("Result", 130), ("Team", 100), ("Links", 115)]
HEADER = "| " + " | ".join(
    f'{n}<br><img src="assets/spacer.png" width="{w}" height="1">' for n, w in WIDTHS) + " |"
SEPARATOR = "|" + ":---:|" * len(WIDTHS)

errors = []
readme = (ROOT / "README.md").read_text(encoding="utf-8")
review = (ROOT / "review" / "论文审阅表.html").read_text(encoding="utf-8")

for heading in ("当前主线", "Contents"):
    if not re.search(rf"^## {heading}", readme, re.M):
        errors.append(f"README 缺少「## {heading}」一节")

lines = readme.splitlines()
paper_rows = 0
for i, line in enumerate(lines):
    if line.startswith("| Name") and line != HEADER:
        errors.append(f"README 第 {i + 1} 行表头和标准表头不一致（列宽占位图也要一致）")
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
        name, title, venue, method, result, team, links = cells
        if not re.fullmatch(r"\*\*[^*]+\*\*", name):
            errors.append(f"README 第 {n} 行 Name 应为加粗简称，如 **Spotter**")
        for label, val in (("Paper", title), ("Venue", venue), ("Method", method),
                           ("Result", result), ("Team", team)):
            if not val:
                errors.append(f"README 第 {n} 行 {label} 不能为空")
        if not re.search(r"(arXiv|\d{4})", venue):
            errors.append(f"README 第 {n} 行 Venue 应写会议和年份，如 ICML 2026 / arXiv 2026.09")
        m = re.match(r"\[Paper\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5})\)", links)
        if not m:
            errors.append(f"README 第 {n} 行 Links 必须以 [Paper](https://arxiv.org/abs/<id>) 开头")
            continue
        for part in links.split(" · ")[1:]:
            if not re.fullmatch(r"\[(Code|Website)\]\(https?://[^)]+\)", part):
                errors.append(f"README 第 {n} 行 Links 只能是 [Paper] · [Code] · [Website]，用 · 分隔")
        if m.group(1) not in review:
            errors.append(f"README 第 {n} 行论文 {m.group(1)} 不在审阅表里，必须先进审阅表")

badge = re.search(r"badge/Papers-(\d+)-", readme)
if not badge or int(badge.group(1)) != paper_rows:
    errors.append(f"README 顶部 Papers 徽章应为 {paper_rows}（表格里实际的论文数）")
meetings = len(list((ROOT / "meetings").glob("*.md")))
mbadge = re.search(r"badge/Meetings-(\d+)-", readme)
if not mbadge or int(mbadge.group(1)) != meetings:
    errors.append(f"README 顶部 Meetings 徽章应为 {meetings}（meetings/ 里的纪要数）")

if errors:
    print("格式检查未通过：")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("格式检查通过")
