"""Deterministic QA for the article. Run: python3 -I scripts/qa.py  (from repo root)
1. Every S-1 quote is verbatim in anchors/s1.txt.
2. Every number in the article appears in FACTS.md, s1.txt, the analysis files or the Sundai excerpts
   (derived numbers are printed as WARN for a human check, not failed).
3. No em-dashes, no ELI5 labels, all 7 visual markers present once, each SVG exists and parses."""
import re, sys, pathlib, subprocess, xml.dom.minidom
R = pathlib.Path(__file__).resolve().parent.parent
art = (R / 'article/article.md').read_text()
fails, warns = [], []

q = subprocess.run([sys.executable, '-I', str(R / 'scripts/quote_check.py'), str(R / 'anchors/s1.txt'), str(R / 'article/article.md')], capture_output=True, text=True)
print(q.stdout.strip().splitlines()[-1] if q.stdout.strip() else q.stderr)
if q.returncode: fails += [l for l in q.stdout.splitlines() if l.startswith('MISS')]

pool = '\n'.join(p.read_text() for p in [R/'facts/FACTS.md', R/'anchors/s1.txt', R/'analysis/equity.md', R/'analysis/mckinsey.md', R/'brief/sundai_questions.md', R/'brief/sundai_follow_the_money.md'] if p.exists())
pool_n = re.sub(r'(?<=\d),(?=\d{3})', '', pool)
body = re.sub(r'\(https?://[^)]+\)', '', art)
for m in sorted(set(re.findall(r'\$?\d[\d,]*\.?\d*\s?(?:%|x|bn|B|T|M|trn|billion|trillion|million)?', body))):
    n = re.sub(r'(?<=\d),(?=\d{3})', '', m).strip().rstrip('.')
    core = re.sub(r'[^\d.]', '', n).rstrip('.')
    if not core or len(core.replace('.', '')) < 2 or re.fullmatch(r'20[0-3]\d', core) or re.fullmatch(r'1?\d', core): continue
    if core not in pool_n: warns.append(f'number not in anchors (derived or unsupported?): {m.strip()}')

for bad, why in [('—', 'em-dash'), ('eli5', 'ELI5 label'), ("like you're 5", 'ELI5 label'), ('like i\'m 5', 'ELI5 label'), ('like i am five', 'ELI5 label')]:
    for p in [R/'article/article.md', *sorted((R/'docs/visuals').glob('*.svg'))]:
        if bad in p.read_text().lower(): fails.append(f'{why} in {p.name}')
for name in ['stack', 'revenue-mix', 'quarterly', 'loss-bridge', 'commitments', 'plans', 'valuation']:
    c = art.count(f'<!-- visual:{name} -->')
    if c != 1: fails.append(f'marker {name} appears {c}x')
    f = R / 'docs/visuals' / f'{name}.svg'
    if not f.exists(): fails.append(f'missing {f.name}'); continue
    try: xml.dom.minidom.parseString(f.read_text())
    except Exception as e: fails.append(f'{f.name} invalid XML: {e}')
print(f'words: {len(art.split())}')
for w in warns: print('WARN', w)
for f in fails: print('FAIL', f)
print(f'{len(fails)} fails, {len(warns)} warns')
sys.exit(1 if fails else 0)
