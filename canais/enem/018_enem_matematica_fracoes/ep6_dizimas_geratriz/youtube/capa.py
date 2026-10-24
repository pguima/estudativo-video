"""Capas — Frações, Decimais e Dízimas, Episódio 6: Decimal exato ou dízima? E a fração geratriz (tema claro).
3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep6", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 6", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_um(c):
    background(c); selo(c); painel(c)
    V.numero(c, "0,999…", 1470, 330, 120, {2: BLUE, 3: BLUE, 4: BLUE, 5: BLUE}, 1.0, align="center")
    K.fmid(c, "=", 1470, 500, 120, "black", INK2)
    K.fmid(c, "1", 1470, 680, 190, "black", GREEN)
    K.expr(c, "9/9 = 1", 1470, 860, 70, 1.0, cores={2: GREEN})
    big(c, "0,999… NÃO É", 340)
    big(c, "QUASE 1", 470)
    boxed(c, "É EXATAMENTE 1", 70, 520, 140, GREEN)
    text(c, "a prova e a fração geratriz, do zero", 90, 860, 46, "extrabold", INK2, align="left")


def capa_geratriz(c):
    background(c); selo(c); painel(c)
    V.numero(c, "0,8333…", 1470, 250, 90, {2: AMBER, 3: BLUE, 4: BLUE, 5: BLUE, 6: BLUE}, 1.0, align="center")
    K.fr(c, "5", "6", 1470, 470, 100, GREEN)
    V.numero(c, "1,2454545…", 1470, 660, 74, {2: AMBER, **{i: BLUE for i in range(3, 10)}}, 1.0, align="center")
    K.fr(c, "137", "110", 1470, 830, 76, GREEN)
    big(c, "QUALQUER DÍZIMA", 340)
    big(c, "VIRA FRAÇÃO", 470)
    boxed(c, "EM UM PASSO", 70, 520, 140, PURPLE)
    text(c, "a regra dos noves e dos zeros", 90, 860, 46, "extrabold", INK2, align="left")


def capa_antes(c):
    background(c); selo(c); painel(c)
    K.fr(c, "3", "8", 1270, 250, 90, INK)
    V.fatores(c, "8", [("2", 1), ("2", 1), ("2", 1)], 1380, 290, 50, 1.0)
    pill(c, "ACABA", 1470, 420, GREEN, size=44, anchor="center", bounds=(0, 1920))
    line(c, 1180, 520, 1760, 520, LINE, 1, 3)
    K.fr(c, "5", "12", 1270, 610, 90, INK)
    V.fatores(c, "12", [("2", 1), ("2", 1), ("3", 0)], 1380, 650, 50, 1.0)
    pill(c, "REPETE", 1470, 790, AMBER, size=44, anchor="center", bounds=(0, 1920))
    big(c, "VAI ACABAR OU", 340)
    big(c, "VAI REPETIR?", 470)
    boxed(c, "SAIBA ANTES", 70, 520, 140, AMBER)
    text(c, "o critério do 2 e do 5 no denominador", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_exatamente_1", capa_um), ("capa_B_qualquer_dizima", capa_geratriz),
                     ("capa_C_saiba_antes", capa_antes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
