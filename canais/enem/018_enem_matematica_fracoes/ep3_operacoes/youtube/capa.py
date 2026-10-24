"""Capas — Frações, Decimais e Dízimas, Episódio 3: As quatro operações com frações (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_soma(c):
    background(c); selo(c); painel(c)
    K.expr(c, "1/2 + 1/3", 1470, 300, 100, 1.0)
    K.fmid(c, "≠", 1300, 470, 110, "black", RED)
    K.fr(c, "2", "5", 1430, 450, 90, RED)
    V.strike(c, 1370, 520, 1500, 400, 1, RED)
    K.pizza(c, 1450, 760, 140, 6, 5, 1.0, sel_col=GREEN)
    K.expr(c, "= 5/6", 1680, 760, 70, 1.0, cores={1: GREEN})
    big(c, "1/2 + 1/3 = 2/5?", 340)
    big(c, "PARECE CERTO...", 470)
    boxed(c, "ESTÁ ERRADO", 70, 520, 150, RED)
    text(c, "as quatro operações com frações, do zero", 90, 860, 46, "extrabold", INK2, align="left")


def capa_divisao(c):
    background(c); selo(c); painel(c)
    K.expr(c, "3/4 ÷ 2/5", 1470, 320, 96, 1.0, cores={2: AMBER})
    K.fmid(c, "↓", 1470, 470, 80, "black", PURPLE)
    K.expr(c, "3/4 · 5/2", 1470, 620, 96, 1.0, cores={2: AMBER})
    K.expr(c, "= 15/8", 1470, 830, 96, 1.0, cores={1: GREEN})
    big(c, "DIVIDIR FRAÇÃO:", 340)
    big(c, "CONSERVA E", 470)
    boxed(c, "INVERTE A 2ª", 70, 520, 150, PURPLE)
    text(c, "as quatro operações sem calculadora", 90, 860, 46, "extrabold", INK2, align="left")


def capa_cruz(c):
    background(c); selo(c); painel(c)
    V.cfrac(c, "4", "9", 1330, 420, 150, 1.0, cut_n=1, cut_d=1, new_n="1", new_d="3")
    K.fmid(c, "·", 1470, 440, 100, "black", INK)
    V.cfrac(c, "3", "8", 1610, 420, 150, 1.0, cut_n=1, cut_d=1, new_n="1", new_d="2")
    K.expr(c, "= 1/6", 1470, 790, 110, 1.0, cores={1: GREEN})
    big(c, "CORTE EM CRUZ", 340)
    big(c, "E A CONTA", 470)
    boxed(c, "ENCOLHE", 70, 520, 160, GREEN)
    text(c, "o atalho que evita números enormes", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_parece_certo", capa_soma), ("capa_B_conserva_inverte", capa_divisao),
                     ("capa_C_corte_em_cruz", capa_cruz)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
