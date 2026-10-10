"""Check README paper table and review HTML follow CONTRIBUTING.md rules.

Run: python scripts/check_format.py
Exits non-zero and prints every problem found.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
HEADER = "| Module | Year | Venue | Paper Title | Repository | Method | Result | Team | Website |"
SEPARATOR = "|" + ":---:|" * 9

errors = []
readme = (ROOT / "README.md").read_text(encoding="utf-8")
review = (ROOT / "review" / "论文审阅表.html").read_text(encoding="utf-8")

if "## 当前主线" not in readme:
    errors.append("README 缺少「## 当前主线」")

lines = readme.splitlines()
if HEADER not in lines:
    errors.append("README 论文表头不对，应为：" + HEADER)
else:
    i = lines.index(HEADER)
    if lines[i + 1].strip() != SEPARATOR:
        errors.append("README 表格分隔行必须是 9 列居中：" + SEPARATOR)
    if readme.count(HEADER) > 1:
        errors.append("README 只能有一张论文表")
    for n, row in enumerate(lines[i + 2:], start=i + 3):
        if not row.startswith("|"):
            break
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) != 9:
            errors.append(f"README 第 {n} 行应有 9 列，实际 {len(cells)} 列")
            continue
        _, year, _, title, repo, method, result, team, website = cells
        if title == "待补":
            continue
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
