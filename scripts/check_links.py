"""Check that every Paper / Code / Website link in README.md and papers/*.md opens.

Run: python scripts/check_links.py
Fails on definite HTTP errors. Network failures and access restrictions are
reported as unverified warnings, never counted as verified links.
"""
import re
import sys
import urllib.request
import urllib.error
import socket
import time
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
    for attempt in range(2):
        if attempt:
            time.sleep(1)
        req.method = "GET"
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.status, ""
        except urllib.error.HTTPError as e:
            result = e.code, str(e.reason)
            if e.code not in (403, 408, 425, 429) and e.code < 500:
                return result
        except urllib.error.URLError as e:
            result = None, f"{type(e.reason).__name__}: {e.reason}"
        except (TimeoutError, ConnectionError, socket.gaierror) as e:
            result = None, f"{type(e).__name__}: {e}"
    return result


def outcome(code):
    if code is None or code in (403, 408, 425, 429) or code >= 500:
        return "unverified"
    return "verified" if 200 <= code < 400 else "broken"


def main():
    urls = collect()
    with ThreadPoolExecutor(8) as pool:
        results = dict(zip(urls, pool.map(status, urls)))
    bad = {u: s for u, s in results.items() if outcome(s[0]) == "broken"}
    uncertain = {u: s for u, s in results.items() if outcome(s[0]) == "unverified"}
    for u, (code, reason) in sorted(results.items()):
        state = outcome(code)
        print(f"{state}: {code if code is not None else 'network'}  {u}  {reason}")
        if state != "verified":
            level = "error" if state == "broken" else "warning"
            message = f"{u} ({urls[u]}): {code} {reason}"
            message = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
            print(f"::{level}::{message}")
    print(f"\n已验证 {len(results)-len(bad)-len(uncertain)}；明确失效 {len(bad)}；访问未核实 {len(uncertain)}")
    if bad:
        print(f"\n链接检查未通过：{len(bad)} 个链接打不开")
        for u, s in bad.items():
            print(f" - {s}  {u}（出现在 {urls[u]}）")
        sys.exit(1)
    if uncertain:
        print("存在外部访问警告；这些链接没有被计为验证通过，请查看具体原因。")
    else:
        print(f"\n链接检查通过：{len(results)} 个链接都能打开")


if __name__ == "__main__":
    main()
