"""Capas — Frações, Decimais e Dízimas, Episódio 8: Revisão geral (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep8", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34, maxw=1000):
    while text_w(s, "black", size) + pad * 2 > maxw:
        size -= 4
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 8", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pegadinhas(c):
    background(c); selo(c); painel(c)
    K.expr(c, "1/2 + 1/3 = 2/5", 1470, 300, 80, 1.0)
    w = K.expr_w("1/2 + 1/3 = 2/5", 80)
    V.strike(c, 1470 - w / 2 - 10, 305, 1470 + w / 2 + 10, 305, 1, RED, 1)
    K.chip(c, "FALSO", 1470, 470, RED, 1, 64)
    K.fmid(c, "0,999… = 1", 1470, 640, 78, "black", INK)
    K.chip(c, "VERDADEIRO", 1470, 790, GREEN, 1, 54)
    big(c, "9 PEGADINHAS", 340)
    big(c, "DE FRAÇÃO:", 470)
    boxed(c, "QUANTAS VOCÊ ACERTA?", 70, 520, 110, AMBER)
    text(c, "revisão final de frações, decimais e dízimas", 90, 860, 46, "extrabold", INK2, align="left")


def capa_questoes(c):
    background(c); selo(c); painel(c)
    for k, (L, s, ok) in enumerate((("A", "800 L", False), ("B", "1.600 L", True), ("C", "2.000 L", False),
                                    ("D", "3.200 L", False), ("E", "4.800 L", False))):
        y = 260 + k * 130
        if ok:
            rrect(c, 1180, y - 50, 580, 100, 18, GREEN, 0.15)
        badge_num(c, L, 1240, y, 1, 34, bg=GREEN if ok else INK)
        text_mid(c, s, 1300, y, 56, "black", INK, align="left")
    big(c, "5 QUESTÕES", 340)
    big(c, "ESTILO ENEM", 470)
    boxed(c, "RESOLVIDAS", 70, 520, 140, GREEN)
    text(c, "cada alternativa errada explicada", 90, 860, 46, "extrabold", INK2, align="left")


def capa_revisao(c):
    background(c); selo(c); painel(c)
    for k in range(7):
        x = 1300 + (k % 2) * 340 if k < 6 else 1470
        y = 250 + (k // 2) * 210
        V.icone(c, k, x, y, 1.0, 1.0)
    big(c, "FRAÇÕES EM", 340)
    big(c, "1 REVISÃO", 470)
    boxed(c, "ANTES DO ENEM", 70, 520, 130, BLUE)
    text(c, "os 7 episódios, as pegadinhas e o checklist", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_9_pegadinhas", capa_pegadinhas), ("capa_B_5_questoes", capa_questoes),
                     ("capa_C_revisao", capa_revisao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
