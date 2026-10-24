"""Capas — Unidades e conversões, Episódio 3: o tempo não é decimal e as unidades compostas (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · UNIDADES · EP. 3", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_relogio(c):
    background(c); selo(c); painel(c)
    V.relogio(c, 1470, 450, 230, 45, 1.0, GREEN, 4)
    V.linha(c, [("0,75 h = ", INK), ("45 min", GREEN)], 1470, 830, 64, 1.0)
    big(c, "O RELÓGIO", 330)
    big(c, "NÃO É", 470)
    boxed(c, "DECIMAL", 70, 520, 170, AMBER)
    text(c, "horas quebradas sem errar, do zero", 90, 860, 44, "extrabold", INK2, align="left")


def capa_velocidade(c):
    background(c); selo(c); painel(c)
    V.velocimetro(c, 1470, 380, 190, 90, 160, 1.0)
    V.painel(c, 1470, 760, "25", 1.0)
    big(c, "km/h PARA m/s:", 330)
    big(c, "DIVIDE OU", 470)
    boxed(c, "MULTIPLICA?", 70, 520, 160, PURPLE)
    text(c, "o 3,6 explicado, sem decorar", 90, 860, 44, "extrabold", INK2, align="left")


def capa_andares(c):
    background(c); selo(c); painel(c)
    V.andares(c, 1470, 320, "km", "h", 1.0, 100)
    arrow(c, 1470, 450, 1470, 600, PURPLE, 1.0, 7, 22)
    text(c, "em cima × 1 000", 1500, 505, 32, "black", BLUE, align="left")
    text(c, "embaixo × 3 600", 1500, 565, 32, "black", AMBER, align="left")
    V.andares(c, 1470, 740, "m", "s", 1.0, 100, GREEN)
    big(c, "UNIDADE COMPOSTA:", 330)
    big(c, "CONVERTA OS", 470)
    boxed(c, "DOIS ANDARES", 70, 520, 160, BLUE)
    text(c, "velocidade, densidade e vazão sem erro", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_relogio_nao_decimal", capa_relogio), ("capa_B_divide_ou_multiplica", capa_velocidade),
                     ("capa_C_dois_andares", capa_andares)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
