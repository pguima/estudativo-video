"""Capas do Short 018 (a tela do iPhone dobrável está rachando) — 3 variações verticais 1080x1920 (formato de Short), com os elementos do vídeo.
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


def capa_racha(c):
    fundo(c, V.RED, 950)
    V.title(c, "IPHONE DOBRÁVEL", 470, 1, INK, 110)
    V.title(c, "RACHANDO", 600, 1, INK, 130, hl="RACHANDO", hl_col=V.RED)
    V.celular(c, V.CX, 1010, 600, 1.0, 1, crack=1.0, linha=1.0)
    V.stamp(c, "EM POUCAS HORAS", V.CX, 1400, V.RED, 1, 58, rot=-4)


def capa_conserto(c):
    fundo(c, GOLD, 960)
    V.title(c, "CONSERTO DA TELA", 470, 1, INK, 100)
    V.money(c, "US$ 999", 680, V.RED, 1, 230)
    x, w = 120, 840
    text(c, "iPhone Duo · US$ 1.999", x, 860, 44, "extrabold", INK, 1, align="left")
    rrect(c, x, 890, w, 76, 16, CYAN, 1)
    text(c, "tela interna · US$ 999", x, 1060, 44, "extrabold", INK, 1, align="left")
    rrect(c, x, 1090, w * 0.5, 76, 16, V.RED, 1)
    V.stamp(c, "METADE DO PREÇO", V.CX, 1330, V.RED, 1, 60, rot=-4)


def capa_areia(c):
    fundo(c, V.SAND, 960)
    V.title(c, "UM GRÃO DE AREIA", 470, 1, INK, 104, hl="AREIA", hl_col=V.SAND)
    V.title(c, "QUEBRA A TELA?", 600, 1, INK, 116, hl="TELA?", hl_col=V.RED)
    V.celular(c, V.CX, 1030, 560, 1.0, 1, crack=1.0)
    hx = V.CX
    c.drawCircle(hx, 1030 - 560 * 0.12, 40, blur_paint(V.SAND, 0.7, 18))
    c.drawCircle(hx, 1030 - 560 * 0.12, 22, paint(V.SAND, 1))
    V.title(c, "O PROBLEMA DO IPHONE DUO", 1420, 1, INK2, 62)


if __name__ == "__main__":
    for nome, fn in (("capa_A_racha", capa_racha), ("capa_B_conserto", capa_conserto), ("capa_C_areia", capa_areia)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(png), "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome, W, H)
