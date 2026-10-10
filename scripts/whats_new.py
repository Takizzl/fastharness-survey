"""Print the human-reviewed content of recently added papers and meetings, verbatim.

The text comes straight from review/论文审阅表.html (the human-curated source)
and meetings/*.md. Nothing is summarized or rewritten.

Usage:
  python scripts/whats_new.py            # the latest CHANGELOG entry
  python scripts/whats_new.py --last 3   # the last 3 CHANGELOG entries
  python scripts/whats_new.py --all      # every paper in the review table
"""
import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
FIELDS = ["问题", "方法", "仿真结果", "真机结果", "团队"]


class ReviewTable(HTMLParser):
    """Collect each paper row of the review table as plain text lines per cell."""

    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell = [], None, None
        self.module = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "tr":
            self.row = {"cells": [], "module": None, "href": None}
        elif tag == "td" and self.row is not None:
            self.cell = {"cls": a.get("class", ""), "lines": [""], "in_li": False}
        elif self.cell is None:
            return
        elif tag == "a" and "arxiv.org" in a.get("href", "") and self.row["href"] is None:
            self.row["href"] = a["href"]
        elif tag == "br":
            self.cell["lines"].append("")
        elif tag == "li":
            self.cell["lines"].append("- ")
        elif tag == "p":
            self.cell["lines"].append("")

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
    return {re.search(r"(\d{4}\.\d{4,5})", r["href"]).group(1): r for r in parser.rows}


def changelog_entries(n):
    text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    parts = re.split(r"^## ", text, flags=re.M)[1:]
    return [("## " + p).strip() for p in parts[:n]]


def arxiv_of(card):
    m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", (ROOT / card).read_text(encoding="utf-8"))
    return m.group(1) if m else None


def print_paper(r):
    print(f"### {r['paper'][0]}（{r['module']}）")
    print(f"- 论文链接：{r['href']}")
    for extra in r["paper"][1:]:
        label = "状态" if extra in ("已入库", "待审核") else "发表"
        print(f"- {label}：{extra.strip('（）')}")
    for f in FIELDS:
        lines = r.get(f) or ["-"]
        if len(lines) == 1:
            print(f"- {f}：{lines[0]}")
        else:
            print(f"- {f}：")
            for ln in lines:
                print(f"    {ln}")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--last", type=int, default=1)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    review = load_review()

    print("> 以下内容逐字取自人工审核的审阅表和会议纪要，未经 AI 改写。\n")
    if args.all:
        for r in review.values():
            print_paper(r)
        return
    for entry in changelog_entries(args.last):
        print(entry.splitlines()[0].replace("## ", "## 更新：", 1))
        print()
        for meeting in dict.fromkeys(re.findall(r"\((meetings/[^)]+\.md)\)", entry)):
            print(f"### 会议纪要：{meeting}\n")
            print((ROOT / meeting).read_text(encoding="utf-8").strip())
            print()
        for card in dict.fromkeys(re.findall(r"\((papers/[^)]+\.md)\)", entry)):
            aid = arxiv_of(card)
            if aid in review:
                print_paper(review[aid])
            else:
                print(f"### {card}\n- 审阅表里没有这篇论文（arXiv {aid}），请人工确认。\n")


if __name__ == "__main__":
    main()
