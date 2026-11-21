"""Does every chart in the built page render exactly as it does alone? usage: chart_iso_check.py REPO OUTDIR
For each chart and each colour scheme: screenshot the chart inside the full page (all 10 charts inlined, CSS scoped by
build.py) and the same chart alone on a page with the same head (raw, unscoped SVG). Any pixel difference is a style
leaking between charts or a scoping mistake. Reduced motion is on, so every chart is in its final state."""
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
worst = 0.0
with sync_playwright() as pw:
    br = pw.chromium.launch()
    for scheme in ('light', 'dark'):
        ctx = br.new_context(viewport={'width': 1100, 'height': 1400}, color_scheme=scheme, reduced_motion='reduce', device_scale_factor=1)
        pg = ctx.new_page(); pg.goto(full.as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
        for n in names:
            # show only this figure, so it sits at the same coordinates as on the page where it is alone
            # (the other charts stay in the document, so their styles still apply: a leak would still show)
            pg.evaluate('''(n) => { for (const el of document.querySelectorAll("main > *")) el.style.display = (el.matches('figure[data-visual="' + n + '"]')) ? "" : "none"; window.scrollTo(0, 0); }''', n)
            a = pg.locator(f'figure[data-visual="{n}"] svg').screenshot()
            raw = (docs / 'visuals' / f'{n}.svg').read_text()
            raw = re.sub(r'<\?xml[^>]*\?>', '', raw).strip()
            raw = re.sub(r'<!-- wilson\.md brand -->.*?<!-- /wilson\.md brand -->\n?', '', raw, flags=re.S)
            alone = out / f'_alone_{n}.html'
            alone.write_text(f'<!doctype html><html lang="en"><head>{base}{head}</head><body><main><figure data-visual="{n}">{raw}</figure></main></body></html>')
            p2 = ctx.new_page(); p2.goto(alone.as_uri()); p2.wait_for_load_state('networkidle'); p2.evaluate('document.fonts.ready')
            b = p2.locator(f'figure[data-visual="{n}"] svg').screenshot(); p2.close()
            A = Image.open(io.BytesIO(a)).convert('RGB'); B = Image.open(io.BytesIO(b)).convert('RGB')
            A.save(out / f'{n}_{scheme}_page.png'); B.save(out / f'{n}_{scheme}_alone.png')
            assert A.size == B.size, (n, scheme, A.size, B.size)
            d = np.abs(np.asarray(A, dtype=float) - np.asarray(B, dtype=float)).max(axis=2)
            frac = float((d > 24).mean()) * 100
            worst = max(worst, frac)
            print(f'{scheme:5s} {n:12s} size {A.size[0]}x{A.size[1]}  pixels differing {frac:.3f}%  mean diff {d.mean():.3f}')
        ctx.close()
    br.close()
print('worst', round(worst, 3), '%', 'PASS' if worst < 0.05 else 'FAIL')
sys.exit(0 if worst < 0.05 else 1)
