"""Check every quote in facts files or the article against the filing it cites.
Usage: python3 -I scripts/quote_check.py <target: facts.json | article.md>   (paths resolve from the repo root)
Citation -> anchor:
  (S-1, ...)               anchors/s1.txt            original S-1, Oct 26, 2026
  (Prospectus, ...)        anchors/424b4.txt         final prospectus (424B4) dated Nov 18, 2026
  (Pricing term sheet...)  anchors/fwp-pricing.txt   free writing prospectus, Nov 18, 2026
Backward compatible: `quote_check.py anchors/s1.txt article.md` still works (a .txt first argument is ignored)."""
import json, re, sys, unicodedata, pathlib

def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()

root = pathlib.Path(__file__).resolve().parent.parent
args = [a for a in sys.argv[1:] if not a.endswith('.txt')]
src = args[-1]
ANCHORS = {'S-1': 'anchors/s1.txt', 'Prospectus': 'anchors/424b4.txt', 'Pricing term sheet': 'anchors/fwp-pricing.txt'}
text = {k: norm((root / v).read_text(encoding='utf-8')) for k, v in ANCHORS.items() if (root / v).exists()}
CITE = r'(S-1|Prospectus|Pricing term sheet)'
quotes = []
if src.endswith('.json'):
    for f in json.load(open(src)):
        s = str(f.get('source', ''))
        kind = next((k for k in ANCHORS if s.startswith(k)), None)
        if kind and f.get('quote'): quotes.append((kind, s, f['quote']))
else:
    txt = open(src, encoding='utf-8').read()
    seen = set()
    for m in re.finditer(r'^>\s*"(.+?)"\s*\((?:\[)?' + CITE, txt, re.M):
        quotes.append((m.group(2), 'article-block', m.group(1))); seen.add(m.start(1))
    for m in re.finditer(r'"([^"]{25,400})"\s*\((?:\[)?' + CITE, txt):
        if m.start(1) not in seen: quotes.append((m.group(2), 'article-inline', m.group(1)))
bad, counts = 0, {}
for kind, where, q in quotes:
    counts[kind] = counts.get(kind, 0) + 1
    anchor = text.get(kind)
    if anchor is None:
        bad += 1; print(f'MISS {where}: no anchor file for {kind}: {q[:100]}'); continue
    qn = norm(q).strip('". ')
    parts = [p.strip() for p in re.split(r'\.\.\.|…|\[[^\]]*\]', qn) if len(p.strip()) > 8]
    ok = all(p in anchor for p in parts) if parts else qn in anchor
    if not ok: bad += 1; print(f'MISS {where} ({kind}): {q[:120]}')
print(f'checked {len(quotes)} quotes ({", ".join(f"{k} {v}" for k, v in counts.items()) or "none"}), {bad} misses')
sys.exit(1 if bad else 0)
