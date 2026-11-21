"""Convert an EDGAR HTML filing to the plain-text anchor format used by quote_check.py,
then print a section map (line numbers of the main all-caps headings).
Usage: python -I scripts/filing_to_text.py anchors/424b4.htm anchors/424b4.txt"""
import re, sys
from bs4 import BeautifulSoup

src, dst = sys.argv[1], sys.argv[2]
html = open(src, encoding='utf-8', errors='ignore').read()
soup = BeautifulSoup(html, 'html.parser')
for t in soup(['script', 'style']):
    t.decompose()
lines = [l for l in soup.get_text('\n').split('\n')]
out, blank = [], False
for l in lines:
    s = ' ' + re.sub(r'[ \t ]+', ' ', l).strip() + ' '
    if s.strip() == '':
        continue
    out.append(s)
open(dst, 'w', encoding='utf-8').write('\n'.join(out) + '\n')

HEADS = ['PROSPECTUS SUMMARY', 'THE OFFERING', 'SUMMARY CONSOLIDATED FINANCIAL', 'RISK FACTORS',
         'USE OF PROCEEDS', 'DIVIDEND POLICY', 'CAPITALIZATION', 'DILUTION',
         "MANAGEMENT’S DISCUSSION AND ANALYSIS", "MANAGEMENT'S DISCUSSION AND ANALYSIS", 'BUSINESS',
         'MANAGEMENT', 'EXECUTIVE COMPENSATION', 'CERTAIN RELATIONSHIPS', 'PRINCIPAL AND SELLING STOCKHOLDERS',
         'PRINCIPAL STOCKHOLDERS', 'DESCRIPTION OF CAPITAL STOCK', 'SHARES ELIGIBLE FOR FUTURE SALE',
         'UNDERWRITING', 'CONCURRENT PRIVATE PLACEMENT', 'LEGAL MATTERS', 'INDEX TO CONSOLIDATED FINANCIAL STATEMENTS',
         'NOTES TO CONSOLIDATED FINANCIAL STATEMENTS', 'NOTES TO UNAUDITED', 'LETTER FROM OUR FOUNDERS', 'OUR FOUNDERS']
print(f'{dst}: {len(out)} lines')
seen = {}
for i, s in enumerate(out, 1):
    t = s.strip()
    if t.isupper() and 3 < len(t) < 70:
        for h in HEADS:
            if t.startswith(h):
                seen.setdefault(t, []).append(i)
for t, ls in seen.items():
    print(f'  {t[:60]:60s} {ls[:12]}')
