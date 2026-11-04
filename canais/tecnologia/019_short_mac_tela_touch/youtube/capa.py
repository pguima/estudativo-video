"""Capas do Short 019 (o primeiro Mac com tela touch) — 3 variações verticais 1080x1920 (formato de Short), com os elementos do vídeo.
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


def capa_jobs(c):
    fundo(c, V.RED, 950)
    chip(c, "STEVE JOBS · 2010", V.CX, 360, GOLD, 1, anchor="center", size=40, filled=True)
    V.title(c, "\"NÃO FUNCIONA\"", 490, 1, INK, 104, hl="NÃO FUNCIONA", hl_col=V.RED)
    V.notebook(c, V.CX, 940, 860, 1, 3.0, liga=1.0, toque=(0.55, 0.45, 1.0))
    V.title(c, "1º MAC TOUCH", 1380, 1, INK, 110, hl="TOUCH", hl_col=CYAN)


def capa_preco(c):
    fundo(c, GOLD, 960)
    V.title(c, "MAC COM TELA TOUCH", 470, 1, INK, 96, hl="TOUCH", hl_col=CYAN)
    V.money(c, "US$ 2.899", 660, GOLD, 1, 200)
    V.notebook(c, V.CX, 1040, 760, 1, 3.0, liga=1.0, toque=(0.5, 0.5, 1.0))
    V.stamp(c, "R$ 34.999" if V.PT else "+$400 FOR TOUCH", V.CX, 1420, V.RED, 1, 64, rot=-4)


def capa_braco(c):
    fundo(c, CYAN, 960)
    V.title(c, "O BRAÇO", 470, 1, INK, 120)
    V.title(c, "VAI CAIR?", 610, 1, INK, 130, hl="CAIR?", hl_col=V.RED)
    V.notebook(c, 520, 980, 640, 1, 3.0, liga=1.0)
    V.braco(c, 1060, 1500, 620, 980, 1, 0.55)
    V.title(c, "O 1º MAC TOUCH", 1420, 1, INK2, 64)


if __name__ == "__main__":
    for nome, fn in (("capa_A_jobs", capa_jobs), ("capa_B_preco", capa_preco), ("capa_C_braco", capa_braco)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(png), "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome, W, H)
