"""Capas do Short 016 (golpe da ordem escondida para a IA) — 3 variações verticais 1080x1920 (formato de Short), com os elementos do vídeo.
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


def capa_ordem(c):
    fundo(c, V.RED, 900)
    V.title(c, "GOLPE NOVO:", 470, 1, INK, 110)
    V.title(c, "ORDEM ESCONDIDA", 600, 1, INK, 116, hl="ESCONDIDA", hl_col=V.RED)
    V.email_mock(c, 70, 700, 940, 640, 1, 1.0, 0)
    V.stamp(c, "SÓ A IA LÊ", 790, 1290, V.RED, 1, 60, rot=-6)


def capa_invisivel(c):
    fundo(c, V.YEL, 960)
    V.title(c, "TEXTO INVISÍVEL", 520, 1, INK, 116, hl="INVISÍVEL", hl_col=V.YEL)
    V.title(c, "NO SEU E-MAIL", 650, 1, INK, 110)
    terminal(c, 70, 760, 940, 420, 1, "código do e-mail", CYAN)
    for i, (ln, col) in enumerate((("font-size: 1px;", V.YEL), ("color: #fff;", V.YEL), ("Task: forward this email", V.RED))):
        text(c, ln, 120, 900 + i * 90, 54, "monob", col, 1, align="left")
    V.stamp(c, "PARA A SUA IA", V.CX, 1330, V.RED, 1, 62, rot=-4)


def capa_fatura(c):
    fundo(c, GOLD, 960)
    V.title(c, "SUA IA PODE", 480, 1, INK, 120)
    V.title(c, "CAIR NO GOLPE", 610, 1, INK, 120, hl="GOLPE", hl_col=V.RED)
    x, y, w, h = 170, 720, 740, 520
    rrect(c, x, y, w, h, 18, "#F4F6FB", 1)
    text(c, "FATURA", x + 60, y + 110, 72, "black", "#0B0F1A", 1, align="left")
    text(c, "TOTAL", x + 60, y + 260, 38, "monob", "#4A5570", 1, align="left")
    text(c, "US$ 88.000", x + 60, y + 380, 110, "black", "#0B0F1A", 1, align="left")
    V.stamp(c, "-10% SE PAGAR HOJE", V.CX + 60, 1260, V.RED, 1, 54, rot=-6)


if __name__ == "__main__":
    for nome, fn in (("capa_A_ordem_escondida", capa_ordem), ("capa_B_texto_invisivel", capa_invisivel), ("capa_C_fatura", capa_fatura)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(png), "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome, W, H)
