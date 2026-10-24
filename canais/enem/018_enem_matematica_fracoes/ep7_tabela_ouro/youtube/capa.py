"""Capas — Frações, Decimais e Dízimas, Episódio 7: A tabela que vale ouro (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep7", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 7", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_ouro(c):
    background(c); selo(c); painel(c)
    for k, (n_, d_, p) in enumerate((("1", "2", "50%"), ("3", "8", "37,5%"), ("1", "5", "20%"))):
        y = 290 + k * 230
        K.fr(c, n_, d_, 1300, y - 30, 80, INK)
        K.fmid(c, "=", 1430, y, 70, "black", LIGHT)
        K.fmid(c, p, 1610, y, 80, "black", GREEN)
    big(c, "A ÚNICA TABELA", 340)
    big(c, "QUE VALE A PENA", 470)
    boxed(c, "DECORAR", 70, 520, 160, AMBER)
    text(c, "fração, decimal e porcentagem de cabeça", 90, 860, 46, "extrabold", INK2, align="left")


def capa_tres_oitavos(c):
    background(c); selo(c); painel(c)
    K.fr(c, "3", "8", 1470, 250, 120, INK)
    K.fmid(c, "3,8%   38%", 1470, 500, 70, "black", RED)
    V.strike(c, 1250, 500, 1690, 500, 1, RED, 1)
    K.fmid(c, "= 37,5%", 1470, 700, 100, "black", GREEN)
    text(c, "3 × 12,5%", 1470, 830, 44, "black", INK2)
    big(c, "3/8 NÃO É 3,8%", 340)
    big(c, "NEM 38%. É...", 470)
    boxed(c, "37,5%", 70, 520, 160, GREEN)
    text(c, "o atalho dos oitavos, sem dividir", 90, 860, 46, "extrabold", INK2, align="left")


def capa_padroes(c):
    background(c); selo(c); painel(c)
    K.pizza(c, 1300, 360, 140, 5, 1, 1.0, pull=0.6)
    K.fmid(c, "20%", 1640, 360, 80, "black", PURPLE)
    K.pizza(c, 1300, 720, 140, 8, 1, 1.0, pull=0.6)
    K.fmid(c, "12,5%", 1640, 720, 72, "black", GREEN)
    big(c, "CADA QUINTO: 20%", 340)
    big(c, "CADA OITAVO:", 470)
    boxed(c, "12,5%", 70, 520, 160, GREEN)
    text(c, "padrões para não decorar a tabela inteira", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_tabela_que_vale_ouro", capa_ouro), ("capa_B_tres_oitavos", capa_tres_oitavos),
                     ("capa_C_cada_quinto_cada_oitavo", capa_padroes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
