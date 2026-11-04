"""Capas do Short 017 (o Reddit vai exigir login) — 3 variações verticais 1080x1920 (formato de Short), com os elementos do vídeo.
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


def capa_login(c):
    fundo(c, V.ORANGE, 900)
    V.title(c, "O REDDIT VAI", 470, 1, INK, 120)
    V.title(c, "EXIGIR LOGIN", 600, 1, INK, 124, hl="LOGIN", hl_col=V.ORANGE)
    rrect(c, 110, 720, 860, 600, 30, "#10151F", 1)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(110, 720, 860, 600), 30, 30), paint(V.ORANGE, 1, stroke=5))
    V.cadeado(c, V.CX, 900, 150, V.ORANGE, 1)
    text(c, "Entre para continuar", V.CX, 1040, 56, "black", INK, 1)
    rrect(c, 180, 1120, 340, 110, 55, V.ORANGE, 1)
    text_mid(c, "Entrar", 350, 1175, 44, "black", "#FFFFFF", 1)
    rrect(c, 560, 1120, 340, 110, 55, "#232B3A", 1)
    text_mid(c, "Criar conta", 730, 1175, 44, "black", INK, 1)
    V.stamp(c, "SÓ COM CONTA", V.CX, 1420, V.RED, 1, 60, rot=-4)


def capa_google(c):
    fundo(c, VIOLET, 960)
    V.title(c, "A CULPA É DA", 480, 1, INK, 116)
    V.title(c, "IA DO GOOGLE?", 610, 1, INK, 120, hl="GOOGLE?", hl_col=CYAN)
    panel(c, 70, 720, 940, 360, 1, VIOLET, label="resumo de IA na busca")
    for i in range(4):
        c.drawRect(skia.Rect.MakeXYWH(120, 800 + i * 64, 840 - (i % 3) * 140, 28), paint(VIOLET, 0.85))
    rrect(c, 120, 1130, 840, 140, 18, PANEL, 1)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(120, 1130, 840, 140), 18, 18), paint(V.ORANGE, 1, stroke=4))
    text_mid(c, "reddit.com", 170, 1200, 48, "monob", V.ORANGE, 1, align="left")
    c.drawLine(140, 1150, 940, 1250, paint(V.RED, 1, stroke=12, cap_round=True))
    V.stamp(c, "NINGUÉM CLICA", 760, 1330, V.RED, 1, 56, rot=-5)


def capa_internet(c):
    fundo(c, V.RED, 960)
    V.title(c, "A INTERNET", 500, 1, INK, 140)
    V.title(c, "ABERTA ACABOU?", 640, 1, INK, 116, hl="ACABOU?", hl_col=V.RED)
    V.cadeado(c, V.CX, 1000, 330, V.ORANGE, 1)
    c.drawCircle(V.CX, 960, 300, blur_paint(V.ORANGE, 0.25, 60))
    V.title(c, "REDDIT VAI EXIGIR CONTA", 1340, 1, INK2, 70)


if __name__ == "__main__":
    for nome, fn in (("capa_A_login", capa_login), ("capa_B_ia_do_google", capa_google), ("capa_C_internet_aberta", capa_internet)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(png), "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome, W, H)
