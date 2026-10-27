"""Assemble article/article.md + site/visuals/*.svg + site/motion.js into
site/index.html (GitHub Pages) and README.md (static, SVGs as <img>)."""
import re, pathlib, markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "docs"
md = (ROOT / "article/article.md").read_text()
MARK = re.compile(r"^<!--\s*visual:([a-z-]+)\s*-->\s*$", re.M)

title = re.search(r"^#\s+(.+)$", md, re.M).group(1).strip()

# README: static images, relative to repo root
readme = MARK.sub(lambda m: f'<p align="center"><img src="docs/visuals/{m.group(1)}.svg" alt="{m.group(1)} diagram" width="760"></p>', md)
readme = readme.replace("](research/", "](research/")
banner = "> **Animated version:** https://wilsonwu-ai.github.io/anthropic-ipo-explained/\n\n"
readme = re.sub(r"^(#\s+.+\n)", lambda m: m.group(1) + "\n" + banner, readme, count=1, flags=re.M)
(ROOT / "README.md").write_text(readme)

# Page: inline SVGs inside figures so motion.js can reach them
def figure(m):
    name = m.group(1)
    svg = (SITE / "visuals" / f"{name}.svg").read_text()
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg).strip()
    return f'\n<figure data-visual="{name}">{svg}</figure>\n'

body_md = MARK.sub(figure, md)
body_md = re.sub(r"\]\(facts/", "](https://github.com/wilsonwu-ai/anthropic-ipo-explained/blob/main/facts/", body_md)
html_body = markdown.markdown(body_md, extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])
html_body = html_body.replace("<a href=\"http", "<a target=\"_blank\" rel=\"noopener\" href=\"http")

page = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="What the Anthropic S-1 reveals about how the AI industry makes money, what it costs, and why AI software runs on hardware.">
<style>
:root{{--bg:#fbfaf7;--ink:#1f2330;--muted:#5b6070;--rule:#e4e1d8;--accent:#eb6c36;--card:#ffffff;--quote:#f3efe6}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#14161c;--ink:#eceae4;--muted:#a3a6b0;--rule:#2b2f3a;--accent:#f08a5d;--card:#1c1f27;--quote:#20242e}}}}
:root[data-theme=dark]{{--bg:#14161c;--ink:#eceae4;--muted:#a3a6b0;--rule:#2b2f3a;--accent:#f08a5d;--card:#1c1f27;--quote:#20242e}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:18px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,sans-serif}}
main{{max-width:760px;margin:0 auto;padding:48px 16px 96px}}
h1{{font-size:clamp(30px,6vw,46px);line-height:1.1;letter-spacing:-.02em;margin:0 0 12px}}
h2{{font-size:clamp(22px,4.2vw,30px);line-height:1.2;margin:64px 0 12px;padding-top:16px;border-top:1px solid var(--rule)}}
h3{{font-size:19px;margin:28px 0 6px}}
a{{color:var(--accent);text-underline-offset:2px}}
blockquote{{margin:20px 0;padding:14px 18px;background:var(--quote);border-left:4px solid var(--accent);border-radius:6px}}
blockquote p{{margin:.3em 0}}
figure{{margin:28px -8px;padding:8px;background:var(--card);border:1px solid var(--rule);border-radius:12px}}
figure svg{{display:block;width:100%;height:auto;border-radius:8px}}
@media (max-width:640px){{figure{{overflow-x:auto;-webkit-overflow-scrolling:touch}}figure svg{{width:700px;max-width:none}}figure::after{{content:"swipe to see the whole picture";display:block;font-size:13px;color:var(--muted);padding:6px 4px 0;position:sticky;left:0}}}}
table{{border-collapse:collapse;width:100%;font-size:16px;display:block;overflow-x:auto}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--rule);vertical-align:top}}
code{{font-size:.9em}}
hr{{border:0;border-top:1px solid var(--rule);margin:40px 0}}
</style></head>
<body><main>
{html_body}
</main>
<script src="motion.js"></script>
</body></html>
"""
(SITE / "index.html").write_text(page)
print("built", len(md.split()), "words;", len(MARK.findall(md)), "visuals")
