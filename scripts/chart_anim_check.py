"""After its animation has played, does each chart in the built page end in its final state? usage: chart_anim_check.py REPO OUTDIR
Plays every chart (adds the .play class as motion.js does), waits for the animation to finish, and compares the result
with the same chart alone and at rest. A keyframe name shared by two charts shows up here as a chart that never draws."""
import sys, re, pathlib, io
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

repo, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
docs = repo / 'docs'
page_html = (docs / 'index.html').read_text()
head = re.search(r'<head>(.*?)</head>', page_html, re.S).group(1)
names = re.findall(r'<figure data-visual="([a-z-]+)">', page_html)
base = f'<base href="{docs.as_uri()}/">'
full = out / '_full.html'; full.write_text(page_html.replace('<head>', '<head>' + base, 1))
worst, bad = 0.0, []
with sync_playwright() as pw:
    br = pw.chromium.launch()
    rest = br.new_context(viewport={'width': 1100, 'height': 1400}, color_scheme='dark', reduced_motion='reduce', device_scale_factor=1)
    move = br.new_context(viewport={'width': 1100, 'height': 1400}, color_scheme='dark', reduced_motion='no-preference', device_scale_factor=1)
    pg = move.new_page(); pg.goto(full.as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
    for n in names:
        pg.evaluate('''(n) => { for (const el of document.querySelectorAll("main > *")) el.style.display = (el.matches('figure[data-visual="' + n + '"]')) ? "" : "none"; window.scrollTo(0, 0);
                               const s = document.querySelector('figure[data-visual="' + n + '"] svg'); s.classList.remove('play'); void s.getBoundingClientRect(); s.classList.add('play'); }''', n)
        pg.wait_for_timeout(9000)
        a = pg.locator(f'figure[data-visual="{n}"] svg').screenshot()
        raw = (docs / 'visuals' / f'{n}.svg').read_text()
        raw = re.sub(r'<\?xml[^>]*\?>', '', raw).strip()
        raw = re.sub(r'<!-- wilson\.md brand -->.*?<!-- /wilson\.md brand -->\n?', '', raw, flags=re.S)
        alone = out / f'_alone_{n}.html'
        alone.write_text(f'<!doctype html><html lang="en"><head>{base}{head}</head><body><main><figure data-visual="{n}">{raw}</figure></main></body></html>')
        p2 = rest.new_page(); p2.goto(alone.as_uri()); p2.wait_for_load_state('networkidle'); p2.evaluate('document.fonts.ready')
        b = p2.locator(f'figure[data-visual="{n}"] svg').screenshot(); p2.close()
        A = Image.open(io.BytesIO(a)).convert('RGB'); B = Image.open(io.BytesIO(b)).convert('RGB')
        A.save(out / f'{n}_played.png')
        d = np.abs(np.asarray(A, dtype=float) - np.asarray(B, dtype=float)).max(axis=2)
        frac = float((d > 24).mean()) * 100; worst = max(worst, frac)
        if frac >= 1.0: bad.append(n)   # under 1% is edge anti-aliasing on layers that animated; a chart that fails to draw is 7% or more
        print(f'{n:12s} after playing vs at rest: pixels differing {frac:.3f}%')
    br.close()
print('worst', round(worst, 3), '%', 'PASS' if not bad else 'FAIL: ' + ', '.join(bad))
sys.exit(0 if not bad else 1)
