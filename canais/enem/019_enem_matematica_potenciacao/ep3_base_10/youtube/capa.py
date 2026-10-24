"""Capas — Potenciação e Radiciação, Episódio 3: Potências de base 10 (tema claro). 3 variações em 1280x720."""
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


def capa_milhao(c):
    background(c); selo(c); painel(c)
    K.expr(c, "1 000 000", 1470, 250, 96, 1)
    K.fmid(c, "× 0,001", 1470, 380, 96, "black", INK)
    K.expr(c, "10^6 · 10^{-3}", 1470, 540, 90, 1, cores={0: BLUE, 2: PURPLE})
    K.expr(c, "= 10^3 = 1 000", 1470, 760, 84, 1, cores={1: GREEN, 3: GREEN, 4: GREEN})
    big(c, "1 MILHÃO × 0,001", 340)
    big(c, "DE CABEÇA EM", 470)
    boxed(c, "3 SEGUNDOS", 70, 520, 150, GREEN)
    text(c, "potências de 10: é só somar os expoentes", 90, 860, 46, "extrabold", INK2, align="left")


def capa_zeros(c):
    background(c); selo(c); painel(c)
    K.expr(c, "10^6", 1470, 300, 200, 1, cores={0: INK})
    V.numeral(c, 1470, 560, 100, 6, 1)
    text(c, "6 zeros", 1470, 700, 50, "black", PURPLE)
    K.expr(c, "10^{-3} = 0,001", 1470, 840, 70, 1, cores={2: BLUE})
    big(c, "O EXPOENTE DO 10", 340)
    big(c, "É UM CONTADOR", 470)
    boxed(c, "DE ZEROS", 70, 520, 150, BLUE)
    text(c, "ler potências de 10 sem errar um zero", 90, 860, 46, "extrabold", INK2, align="left")


def capa_habitante(c):
    background(c); selo(c); painel(c)
    K.expr(c, "{7,2·10^9}/{1,2·10^6}", 1470, 360, 90, 1)
    K.expr(c, "= 6·10^3", 1470, 600, 110, 1, cores={1: GREEN})
    K.fmid(c, "dividir, não multiplicar", 1470, 800, 46, "black", AMBER)
    big(c, "“POR HABITANTE”", 340)
    big(c, "É DIVIDIR,", 470)
    boxed(c, "NÃO MULTIPLICAR", 70, 520, 130, AMBER)
    text(c, "a armadilha das potências de 10 no ENEM", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_milhao_de_cabeca", capa_milhao), ("capa_B_contador_de_zeros", capa_zeros),
                     ("capa_C_por_habitante", capa_habitante)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
