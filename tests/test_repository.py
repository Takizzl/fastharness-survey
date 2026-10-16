import contextlib
import io
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import whats_new
import check_links


class RepositoryTests(unittest.TestCase):
    def test_all_review_entries_are_queryable(self):
        records = whats_new.load_review()
        self.assertTrue(records)
        for name in ('LoopROS', 'PhysicalRSI', 'Robota-Embed', 'GPT-as-Policy',
                     'JitRL', 'COAP', 'PhysMem', 'GroundingPI'):
            self.assertEqual(sum(name in r['paper'][0] for r in records.values()), 1)
        for card in (whats_new.ROOT / 'papers').glob('*.md'):
            self.assertIn(whats_new.card_source(card.relative_to(whats_new.ROOT)), records)

    def test_source_metadata_not_incidental_citations(self):
        self.assertEqual(whats_new.card_source('papers/loopros.md'), 'https://loopmaster.ai/loopros')
        title, code, web = whats_new.card_info('https://arxiv.org/abs/2610.19495v1')
        self.assertIn('Robota-Embed', title)
        self.assertEqual(code, '-')
        self.assertEqual(whats_new.source_key('https://arxiv.org/abs/2610.19495v2'), '2610.19495')

    def test_readme_category_counts(self):
        import re
        text = (whats_new.ROOT / 'README.md').read_text(encoding='utf-8')
        records = list(whats_new.load_review().values())
        rows = re.findall(r'^\| \[(\d+\. [^\]]+)\]\(#[^)]+\) \| [^|]+ \| ([^|]+) \|$', text, re.M)
        self.assertTrue(rows)
        category_ids = [category.split('.', 1)[0] for category, _ in rows]
        self.assertEqual(len(category_ids), len(set(category_ids)))
        self.assertEqual(set(category_ids), {r['module'].split('.', 1)[0] for r in records})
        for category, count in rows:
            entries = [r for r in records if r['module'].split('.', 1)[0] == category.split('.', 1)[0]]
            numbers = [int(n) for n in re.findall(r'\d+', count)]
            self.assertEqual(sum(numbers), len(entries), category)
            if '已入库' in count:
                self.assertEqual(numbers[0], sum('已入库' in r['paper'] for r in entries))

    def test_link_classification(self):
        for code in (200, 301):
            self.assertEqual(check_links.outcome(code), 'verified')
        for code in (404, 410, 401):
            self.assertEqual(check_links.outcome(code), 'broken')
        for code in (None, 403, 408, 429, 503):
            self.assertEqual(check_links.outcome(code), 'unverified')

    def test_markdown_escaped_url_is_normalized(self):
        urls = check_links.collect()
        self.assertIn('https://arxiv.org/pdf/2610.02204', urls)
        self.assertFalse(any('\\.' in url or '&amp;' in url for url in urls))

    def test_network_diagnostic_and_retry(self):
        error = urllib.error.URLError(TimeoutError('test timeout'))
        with patch.object(check_links.urllib.request, 'urlopen', side_effect=error) as request, patch.object(check_links.time, 'sleep'):
            code, reason = check_links.status('https://example.com')
        self.assertIsNone(code)
        self.assertIn('test timeout', reason)
        self.assertEqual(request.call_count, 2)

    def test_broken_link_fails_but_unverified_is_not_claimed_passed(self):
        for code in (404, None, 200):
            output = io.StringIO()
            with patch.object(check_links, 'collect', return_value={'https://example.com': 'test.md'}), patch.object(check_links, 'status', return_value=(code, 'test')), contextlib.redirect_stdout(output):
                if code == 404:
                    with self.assertRaises(SystemExit) as result:
                        check_links.main()
                    self.assertEqual(result.exception.code, 1)
                else:
                    check_links.main()
            if code is None:
                self.assertIn('访问未核实 1', output.getvalue())
                self.assertNotIn('链接检查通过', output.getvalue())

    def test_review_table_rowspans(self):
        # A seven-column table must account for carried module cells on each row.
        from html.parser import HTMLParser
        class Grid(HTMLParser):
            def __init__(self):
                super().__init__(); self.remaining = 0; self.widths = []; self.width = 0
            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if tag == 'tr':
                    self.width = int(self.remaining > 0)
                    self.remaining = max(0, self.remaining - 1)
                elif tag in ('td', 'th'):
                    self.width += 1
                    if 'rowspan' in attrs:
                        self.remaining = int(attrs['rowspan']) - 1
            def handle_endtag(self, tag):
                if tag == 'tr': self.widths.append(self.width)
        grid = Grid()
        grid.feed((whats_new.ROOT / 'review/论文审阅表.html').read_text(encoding='utf-8'))
        self.assertTrue(grid.widths)
        self.assertEqual(set(grid.widths), {7})


if __name__ == '__main__':
    unittest.main()
