"""Check every quote in facts files or article against its anchor text. Usage: python3 -I quote_check.py <s1.txt> <facts.json|article.md>"""
import json, re, sys, unicodedata
def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('—','-').replace('–','-')
    return re.sub(r'\s+', ' ', s).strip().lower()
anchor = norm(open(sys.argv[1], encoding='utf-8').read())
src = sys.argv[2]
quotes = []
if src.endswith('.json'):
    for f in json.load(open(src)):
        if str(f.get('source','')).startswith('S-1') and f.get('quote'): quotes.append((f['source'], f['quote']))
else:
    txt = open(src, encoding='utf-8').read()
    for m in re.finditer(r'^>\s*"(.+?)"\s*\(S-1[^)]*\)', txt, re.M): quotes.append(('article', m.group(1)))
    for m in re.finditer(r'"([^"]{25,400})"\s*\((?:\[)?S-1', txt): quotes.append(('article-inline', m.group(1)))
bad = 0
for where, q in quotes:
    qn = norm(q).strip('". ')
    parts = [p.strip() for p in re.split(r'\.\.\.|…|\[[^\]]*\]', qn) if len(p.strip()) > 8]
    ok = all(p in anchor for p in parts) if parts else qn in anchor
    if not ok: bad += 1; print(f'MISS {where}: {q[:120]}')
print(f'checked {len(quotes)} quotes, {bad} misses')
sys.exit(1 if bad else 0)
