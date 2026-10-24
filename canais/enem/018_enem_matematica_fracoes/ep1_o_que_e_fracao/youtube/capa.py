"""Capas — Frações, Decimais e Dízimas, Episódio 1: O que é uma fração (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_quatro(c):
    background(c); selo(c); painel(c)
    K.pizza(c, 1470, 400, 220, 4, 3, 1.0, pull=0.6)
    K.fr(c, "3", "4", 1470, 740, 110, INK)
    big(c, "3/4 TEM 4", 340)
    big(c, "SIGNIFICADOS", 470)
    boxed(c, "DIFERENTES", 70, 520, 140, BLUE)
    text(c, "o que é uma fração, do zero e com pizza", 90, 860, 46, "extrabold", INK2, align="left")


def capa_de(c):
    background(c); selo(c); painel(c)
    K.expr(c, "3/4 de 200", 1470, 330, 84, 1.0, cores={1: AMBER})
    K.fmid(c, "↓", 1470, 470, 90, "black", PURPLE)
    K.expr(c, "3/4 × 200", 1470, 610, 84, 1.0, cores={1: PURPLE})
    K.fmid(c, "= 150", 1470, 800, 100, "black", GREEN)
    big(c, "A PALAVRA “DE”", 340)
    big(c, "É UM SINAL DE", 470)
    boxed(c, "VEZES", 70, 520, 160, PURPLE)
    text(c, "o atalho que resolve metade das questões", 90, 860, 46, "extrabold", INK2, align="left")


def capa_simplificar(c):
    background(c); selo(c); painel(c)
    K.fr(c, "84", "120", 1470, 300, 120, INK)
    K.fmid(c, "÷ 12", 1470, 520, 70, "black", GREEN)
    K.fr(c, "7", "10", 1470, 690, 130, BLUE)
    big(c, "SIMPLIFIQUE", 340)
    big(c, "QUALQUER FRAÇÃO", 470)
    boxed(c, "DE UMA VEZ SÓ", 70, 520, 140, GREEN)
    text(c, "frações equivalentes e o atalho do MDC", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quatro_significados", capa_quatro), ("capa_B_de_e_vezes", capa_de),
                     ("capa_C_de_uma_vez", capa_simplificar)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
