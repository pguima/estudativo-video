"""Texto do material de estudo (HTML) com matemática legível: x^2, x^(−3), a^(m/n), √(50), √[3](54), (a/b).
Uso: extrair_material.py <arquivo.html> <saida.txt>"""
import re, sys, bs4
s = bs4.BeautifulSoup(open(sys.argv[1], encoding="utf-8").read(), "html.parser")
for x in s(["script", "style", "svg"]): x.decompose()
def idx(sup): return sup is not None and getattr(sup, "name", None) == "sup" and ".62em" in (sup.get("style") or "")
def dofrac(f):
    i = f.find_all("i", recursive=False)
    if len(i) == 2: f.replace_with(f"({i[0].get_text()}/{i[1].get_text()})")
for f in reversed(s.select("sup span.frac")): dofrac(f)
for sp in reversed(s.find_all("sup")):
    if idx(sp): continue
    t = sp.get_text(); sp.replace_with("^" + t if re.fullmatch(r"[0-9a-z]", t) else (f"^{t}" if t.startswith("(") else f"^({t})"))
for sb in reversed(s.find_all("sub")): sb.replace_with("_" + sb.get_text())
for r in reversed(s.select("span.rad")):
    nxt = r.next_sibling; n = ""
    if idx(nxt): n = nxt.get_text(); nxt.decompose()
    inner = r.get_text(); r.replace_with(f"√[{n}]({inner})" if n else f"√({inner})")
for f in reversed(s.select("span.frac")): dofrac(f)
for b in s.find_all(["p", "li", "tr", "h1", "h2", "h3", "div", "section", "summary", "dt", "dd", "br", "header", "td", "th"]):
    b.insert_before("\n" if b.name not in ("td", "th") else " | ")
txt = re.sub(r"[ \t\xa0]+", " ", s.get_text()); txt = re.sub(r"\n\s*\n+", "\n", txt).strip()
open(sys.argv[2], "w", encoding="utf-8").write(txt)
print(len(txt.split()), "palavras")
