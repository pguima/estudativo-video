"""Capas do Short 015 (IPO da Anthropic) — 3 variações verticais 1080x1920 (formato de Short), com os elementos do vídeo.
Inglês: VIDEO_FORMATO=vertical python _ferramentas/idioma.py capa <proj>  (textos em roteiro/textos_en.py → youtube_en/).
Texto importante no miolo (y 400–1500): a grade do canal e o feed cortam as bordas."""
import os, subprocess, sys
from pathlib import Path
os.environ.setdefault("VIDEO_FORMATO", "vertical")  # antes do import motor
HERE = Path(__file__).parent
PROJ = next(d for d in HERE.parents if (d / "roteiro").is_dir()) if not (HERE.parent / "roteiro").is_dir() else HERE.parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
sys.path.insert(0, str(PROJ / "roteiro"))
import skia
import visual as V
from motor import *  # noqa
from tech import *  # noqa


def fundo(c, glow, gy=900):
    V.BACKGROUND(c, 20.0)
    c.drawCircle(V.CX, gy, 640, blur_paint(glow, 0.16, 170))
    chip(c, "TECNATIVO", V.CX, 230, CYAN, 1, anchor="center", size=30, filled=True)


def capa_prejuizo(c):
    fundo(c, V.RED, 760)
    chip(c, "EMPRESA DO CLAUDE", V.CX, 470, V.CLAUDE, 1, anchor="center", size=40, filled=True)
    V.money(c, "-US$ 80 BI", 720, V.RED, 1, 210, 0.4)
    V.title(c, "EM 6 MESES", 900, 1, INK, 110, hl="6 MESES", hl_col=V.RED)
    V.chart_up(c, 140, 1000, 800, 330, 1, LIME, 1)
    V.stamp(c, "E VAI PARA A BOLSA", V.CX, 1440, GOLD, 1, 62, rot=-4)


def capa_recorde(c):
    fundo(c, LIME, 960)
    V.title(c, "MAIOR IPO", 520, 1, INK, 140)
    V.title(c, "DA HISTÓRIA?", 680, 1, INK, 130, hl="HISTÓRIA?", hl_col=GOLD)
    bw, bh = 900, 360
    bx, by = V.CX - bw / 2, 820
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, by, bw, bh), 30, 30), blur_paint(LIME, 0.45, 40))
    rrect(c, bx, by, bw, bh, 30, "#050A0C", 1)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, by, bw, bh), 30, 30), paint(LIME, 1, stroke=5))
    text(c, "NASDAQ", V.CX, by + 100, 54, "monob", INK2, 1)
    glow_text(c, "ANT", V.CX, by + 290, 190, "black", LIME, 1, glow=0.45)
    V.title(c, "A EMPRESA DO CLAUDE", 1340, 1, V.CLAUDE, 74)
    V.stamp(c, "~US$ 100 BI?", V.CX, 1480, GOLD, 1, 60, rot=-4)


def capa_bolha(c):
    fundo(c, MAGENTA, 980)
    V.title(c, "É BOLHA?", 520, 1, INK, 140, hl="BOLHA?", hl_col=MAGENTA)
    V.bolha(c, V.CX, 950, 360, 1, 0.5)
    text_mid(c, "IA", V.CX, 950, 170, "black", INK, 1)
    V.stamp(c, "-US$ 80 BI", V.CX - 190, 1330, V.RED, 1, 58, rot=-6)
    V.stamp(c, "+1.300%", V.CX + 220, 1400, LIME, 1, 58, rot=5)
    V.title(c, "A EMPRESA DO CLAUDE NA BOLSA", 1560, 1, INK2, 60)


if __name__ == "__main__":
    for nome, fn in (("capa_A_prejuizo", capa_prejuizo), ("capa_B_maior_ipo", capa_recorde), ("capa_C_bolha", capa_bolha)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(png), "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome, W, H)
