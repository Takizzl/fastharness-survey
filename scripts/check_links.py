"""Check that every Paper / Code / Website link in README.md and papers/*.md opens.

Run: python scripts/check_links.py
Exits non-zero and lists each link that does not return HTTP 2xx/3xx.
"""
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
URL = re.compile(r"https?://[^\s)（）|<>\"']+")


def collect():
    files = [ROOT / "README.md", *sorted((ROOT / "papers").glob("*.md"))]
    urls = {}
    for f in files:
        for u in URL.findall(f.read_text(encoding="utf-8")):
            u = u.rstrip(".,;，。；")
            if "img.shields.io" not in u:
                urls.setdefault(u, f.name)
    return urls


def status(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 fastharness-link-check"})
    for method in ("HEAD", "GET"):
        req.method = method
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if method == "GET":
                return e.code
        except Exception as e:  # network error, timeout
            if method == "GET":
                return type(e).__name__
    return "unknown"


def main():
    urls = collect()
    with ThreadPoolExecutor(8) as pool:
        results = dict(zip(urls, pool.map(status, urls)))
    bad = {u: s for u, s in results.items() if not (isinstance(s, int) and 200 <= s < 400)}
    for u, s in sorted(results.items()):
        print(f"{s}  {u}")
    if bad:
        print(f"\n链接检查未通过：{len(bad)} 个链接打不开")
        for u, s in bad.items():
            print(f" - {s}  {u}（出现在 {urls[u]}）")
        sys.exit(1)
    print(f"\n链接检查通过：{len(results)} 个链接都能打开")


if __name__ == "__main__":
    main()
