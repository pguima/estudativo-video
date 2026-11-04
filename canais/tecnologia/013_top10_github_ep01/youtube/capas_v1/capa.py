"""Capas do vídeo Tecnologia 013 — Top 10 projetos do GitHub, ep. 1 (tema 'tech'). 3 variações em 1280x720.
Só motion graphics: nomes dos projetos como texto, sem logos de terceiros."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
sys.path.insert(0, str(HERE.parent / "roteiro"))
import skia
import tech
from motor import *  # noqa
from tech import *  # noqa
import visual as V  # também troca a fonte mono para DejaVu Sans Mono


def base(c, col=CYAN, tag="TOP 10 · GITHUB · OUTUBRO 2026"):
    tech.background(c, 3.0)
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        tech._bracket(c, x, y, dx, dy, col, 0.7)
    chip(c, tag, 84, 110, col, 1, size=34, filled=True)


def big(c, l1, l2, word, col, y0=330):
    for s, y in ((l1, y0), (l2, y0 + 130)):
        if s:
            size = min(120, 120 * 1000 / text_w(s, "black", 120))
            glow_text(c, s, 80, y, size, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, y0 + 180, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, y0 + 267, size, "black", "#03050B")


def rodape(c, s, size=40):
    size = min(size, size * 990 / text_w(s, "monob", size))
    text(c, s, 90, 930, size, "monob", INK2, align="left")


def lista(c, x=1140, y=150, w=680, h=800, esconde_1=False, hi_agentes=False):
    panel(c, x, y, w, h, 1, CYAN, label="github.com/trending · mês")
    for i, (sid, p) in enumerate(V.RANK):
        yy = y + 95 + i * 73
        ag = p["nome"] in V.AGENTES
        col = (CYAN if ag else DIM) if hi_agentes else p["col"]
        text(c, f"#{p['pos']}", x + 50, yy, 38, "black", col, 1, align="left")
        if esconde_1 and p["pos"] == 1:
            for k in range(7):
                c.drawRect(skia.Rect.MakeXYWH(x + 150 + k * 44, yy - 30, 34, 30), blur_paint(INK2, 0.5, 6))
            text(c, "?", x + 480, yy, 44, "black", GOLD, 1, align="left")
        else:
            nm = p["nome"]
            text(c, nm, x + 150, yy, min(34, 34 * 330 / text_w(nm, "extrabold", 34)), "extrabold",
                 INK if (ag or not hi_agentes) else INK2, 1, align="left")
        text(c, "+" + V.fmt(p["ganho"]), x + w - 40, yy, 28, "monob", INK2, 1, align="right")


def capa_estrelas(c):
    base(c, CYAN)
    glow_text(c, "53 MIL", 80, 380, 200, "black", INK, 1, align="left", glow=0.2)
    text(c, "ESTRELAS EM 1 MÊS", 90, 470, 56, "monob", CYAN, align="left")
    big(c, None, "", "TOP 10", CYAN, y0=380)
    rodape(c, "os projetos que mais cresceram no GitHub")
    lista(c)


def capa_misterio(c):
    base(c, GOLD)
    big(c, "QUAL PROJETO", "GANHOU 53 MIL", "ESTRELAS?", GOLD)
    rodape(c, "o Top 10 do GitHub em outubro de 2026")
    lista(c, esconde_1=True)


def capa_agentes(c):
    base(c, VIOLET)
    big(c, "7 DE 10", "SÃO PARA", "AGENTES", VIOLET)
    rodape(c, "o que está em alta no GitHub agora")
    lista(c, hi_agentes=True)


if __name__ == "__main__":
    for nome, fn in (("capa_A_53_mil", capa_estrelas), ("capa_B_qual_projeto", capa_misterio),
                     ("capa_C_7_de_10_agentes", capa_agentes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
