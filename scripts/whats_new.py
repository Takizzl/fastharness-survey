"""Print recorded review-table content and meetings without summarizing.

The text comes straight from review/论文审阅表.html (the human-curated source)
and meetings/*.md. Nothing is summarized or rewritten.

Usage:
  python scripts/whats_new.py                          # the latest CHANGELOG entry
  python scripts/whats_new.py --last 3                 # the last 3 CHANGELOG entries
  python scripts/whats_new.py --all                    # every paper in the review table
  python scripts/whats_new.py --module "VLM1 + VLM2"   # only one category
  python scripts/whats_new.py --paper Spotter          # only one paper
  (--module / --paper can be combined with --last or --all)
"""
import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
FIELDS = ["问题", "方法", "仿真结果", "真机结果", "团队"]
NOTICE = "> 以下内容取自审阅表与会议记录；逐项显示审核状态，待审核内容不代表人工确认。"


def source_key(url):
    match = re.search(r"arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})", url)
    return match.group(1) if match else url.rstrip("/")


class ReviewTable(HTMLParser):
    """Collect each paper row of the review table as plain text lines per cell."""

    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell = [], None, None
        self.module = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "tr":
            self.row = {"cells": [], "href": None}
        elif tag == "td" and self.row is not None:
            self.cell = {"cls": a.get("class", ""), "lines": [""]}
        elif self.cell is None:
            return
        elif tag == "a" and self.cell["cls"] == "p" and a.get("href", "").startswith("https://") and self.row["href"] is None:
            self.row["href"] = a["href"]
        elif tag in ("br", "p"):
            self.cell["lines"].append("")
        elif tag == "li":
            self.cell["lines"].append("- ")

    def handle_endtag(self, tag):
        if tag == "td" and self.cell is not None:
            lines = [re.sub(r"^- +", "- ", ln.strip()) for ln in self.cell["lines"]]
            lines = [ln for ln in lines if ln and ln != "-"]
            if self.cell["cls"] == "m":
                self.module = " ".join(lines)
            else:
                self.row["cells"].append(lines)
            self.cell = None
        elif tag == "tr" and self.row is not None:
            if self.row["href"] and len(self.row["cells"]) == 6:
                self.rows.append({"module": self.module, "href": self.row["href"],
                                  "paper": self.row["cells"][0],
                                  **dict(zip(FIELDS, self.row["cells"][1:]))})
            self.row = None

    def handle_data(self, data):
        if self.cell is not None:
            self.cell["lines"][-1] += re.sub(r"\s+", " ", data)


def load_review():
    parser = ReviewTable()
    parser.feed((ROOT / "review" / "论文审阅表.html").read_text(encoding="utf-8"))
    return {source_key(r["href"]): r for r in parser.rows}


def changelog_entries(n):
    text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    parts = re.split(r"^## ", text, flags=re.M)[1:]
    return [("## " + p).strip() for p in parts[:n]]


def card_source(card):
    text = (ROOT / card).read_text(encoding="utf-8")
    for field in ("Paper", "Website"):
        match = re.search(rf"^\| {field} \| (https://[^\s|]+)", text, re.M)
        if match:
            return source_key(match.group(1))
    return None


def card_info(href):
    """Match the explicit metadata source, never incidental citation text."""
    key = source_key(href)
    for card in (ROOT / "papers").glob("*.md"):
        text = card.read_text(encoding="utf-8")
        if card_source(card) == key:
            title = text.splitlines()[0].lstrip("# ").strip()
            get = lambda k: (re.search(rf"^\| {k} \| (https://[^\s（|]+)", text, re.M) or [None, "-"])[1]
            return title, get("Code"), get("Website")
    return None, "-", "-"


def print_paper(r):
    title, code, web = card_info(r["href"])
    print(f"### {title or r['paper'][0]}（{r['module']}）")
    label = "Paper" if "arxiv.org/" in r["href"] else "Source"
    links = [f"[{label}]({r['href']})"] + [f"[{k}]({u})" for k, u in (("Code", code), ("Website", web)) if u != "-"]
    print("- " + " ".join(links))
    for extra in r["paper"][1:]:
        label = "状态" if extra in ("已入库", "待审核") else "备注"
        print(f"- {label}：{extra.strip('（）')}")
    for f in FIELDS:
        lines = r.get(f) or ["-"]
        if len(lines) == 1:
            print(f"- {f}：{lines[0]}")
            continue
        print(f"- {f}：")
        for ln in lines:
            # "- item" lines nest under the preceding heading line; other lines are headings
            print(f"        {ln}" if ln.startswith("- ") else f"    - {ln}")
    print()


def matches(r, module, paper):
    if module and module.lower() not in r["module"].lower():
        return False
    if paper and paper.lower() not in r["paper"][0].lower():
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--last", type=int, default=1, help="最近 N 次更新")
    ap.add_argument("--all", action="store_true", help="审阅表里的全部论文")
    ap.add_argument("--module", help='只看某个类别，如 "VLM1 + VLM2"')
    ap.add_argument("--paper", help="只看某篇论文，如 Spotter")
    args = ap.parse_args()
    if args.last < 1:
        ap.error("--last 必须大于 0")
    review = load_review()
    filtered = bool(args.module or args.paper)
    scope = "（筛选：" + " ".join(x for x in (args.module, args.paper) if x) + "）" if filtered else ""
    categories = "；".join(sorted({r["module"] for r in review.values()}))

    print(NOTICE + "\n")
    if args.all:
        hits = [r for r in review.values() if matches(r, args.module, args.paper)]
        print(f"## 审阅表全部论文{scope}：共 {len(hits)} 篇\n")
        for r in hits:
            print_paper(r)
        if not hits:
            print("没有找到匹配的论文。现有类别：" + categories)
        return

    for entry in changelog_entries(args.last):
        cards = list(dict.fromkeys(re.findall(r"\((papers/[^)]+\.md)\)", entry)))
        hits = [review[a] for a in map(card_source, cards) if a in review]
        shown = [r for r in hits if matches(r, args.module, args.paper)]
        print(entry.splitlines()[0].replace("## ", "## 更新：", 1) + "\n")
        print(f"本次共新增 / 修改 {len(hits)} 篇论文，下面列出 {len(shown)} 篇{scope}。\n")
        if not filtered:
            for meeting in dict.fromkeys(re.findall(r"\((meetings/[^)]+\.md)\)", entry)):
                print(f"### 会议纪要：{meeting}\n")
                print((ROOT / meeting).read_text(encoding="utf-8").strip() + "\n")
        for r in shown:
            print_paper(r)
        if filtered and not shown:
            print("这次更新里没有匹配的论文，可加 --all 查看全部。现有类别：" + categories + "\n")
        for c in cards:
            if card_source(c) not in review:
                print(f"### {c}\n- 审阅表里没有对应来源（{card_source(c)}），请人工确认。\n")


if __name__ == "__main__":
    main()
