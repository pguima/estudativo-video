"""Capas do Short 020 (a Microsoft oferece saída voluntária a 60 mil funcionários) — 3 variações verticais 1080x1920 (formato de Short), com os elementos do vídeo.
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


def capa_60mil(c):
    fundo(c, V.RED, 950)
    V.title(c, "MICROSOFT", 430, 1, INK, 110, hl="MICROSOFT", hl_col=CYAN)
    V.money(c, "60 MIL" if V.PT else "60,000", 590, V.RED, 1, 170)
    V.multidao(c, 1, 9.0, 0.0, 0.35, y0=720, dy=40)
    V.stamp(c, "PAGOS PARA SAIR", V.CX, 1430, V.RED, 1, 64, rot=-4)


def capa_ia(c):
    fundo(c, VIOLET, 960)
    V.title(c, "A CULPA É DA", 450, 1, INK, 100)
    V.title(c, "IA?", 590, 1, INK, 150, hl="IA?", hl_col=VIOLET)
    for i in range(4):
        V.rack(c, 110 + i * 220, 760, 190, 420, 1, 3.0, i)
    V.stamp(c, "60 MIL SAÍDAS" if V.PT else "60,000 BUYOUTS", V.CX, 1330, V.RED, 1, 62, rot=-4)


def capa_voce(c):
    fundo(c, GOLD, 960)
    V.title(c, "VOCÊ ACEITARIA", 450, 1, INK, 100)
    V.title(c, "SAIR?", 590, 1, INK, 150, hl="SAIR?", hl_col=V.RED)
    V.multidao(c, 1, 9.0, 0.0, 0.0, y0=760, dy=40)
    V.title(c, "A OFERTA DA MICROSOFT", 1420, 1, INK2, 64)


if __name__ == "__main__":
    for nome, fn in (("capa_A_60mil", capa_60mil), ("capa_B_ia", capa_ia), ("capa_C_voce", capa_voce)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(png), "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome, W, H)
