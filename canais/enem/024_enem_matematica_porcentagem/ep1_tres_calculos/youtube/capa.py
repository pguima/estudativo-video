"""Capas — Porcentagem, Episódio 1: os três cálculos básicos e a conta de cabeça (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · PORCENTAGEM · EP. 1", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_tres(c):
    background(c); selo(c); painel(c)
    V.triangulo(c, 1470, 440, 520, 1.0, "total", 1.0)
    for k, (s, col) in enumerate((("a PARTE?", PURPLE), ("a TAXA?", PURPLE), ("o TOTAL?", AMBER))):
        text(c, s, 1250 + k * 220, 830, 40, "black", col)
    big(c, "PORCENTAGEM:", 330)
    big(c, "SÓ EXISTEM", 470)
    boxed(c, "3 PERGUNTAS", 70, 520, 160, PURPLE)
    text(c, "descubra qual a questão faz e a conta sai", 90, 860, 44, "extrabold", INK2, align="left")


def capa_cabeca(c):
    background(c); selo(c); painel(c)
    text(c, "de 240", 1470, 220, 40, "bold", GRAY)
    rows = [("10%", "24", INK), ("5%", "12", BLUE), ("15%", "36", GREEN), ("1%", "2,4", PURPLE)]
    for k, (p, r, col) in enumerate(rows):
        y = 330 + k * 150
        text(c, p, 1300, y + 20, 72, "black", col)
        text(c, "→", 1470, y + 20, 64, "black", GRAY)
        text(c, r, 1640, y + 20, 72, "black", col)
    big(c, "10%, 5% E 15%", 330)
    big(c, "DE CABEÇA,", 470)
    boxed(c, "SEM CALCULADORA", 70, 520, 140, GREEN)
    text(c, "a vírgula faz o trabalho por você", 90, 860, 44, "extrabold", INK2, align="left")


def capa_base(c):
    background(c); selo(c); painel(c)
    V.seta_var(c, 1290, 1650, 360, 40, 50, 1.0, GREEN, 1.0, "+25%", 1.0, size=80)
    V.seta_var(c, 1290, 1650, 660, 50, 40, 1.0, RED, 1.0, "?", 1.0, size=80)
    text(c, "mesma diferença: 10", 1470, 880, 38, "black", AMBER)
    big(c, "DE 40 PARA 50 É +25%.", 330)
    big(c, "E DE 50 PARA 40?", 470)
    boxed(c, "NÃO É −25%", 70, 520, 160, RED)
    text(c, "o erro do denominador, explicado do zero", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_tres_perguntas", capa_tres), ("capa_B_de_cabeca", capa_cabeca),
                     ("capa_C_a_base", capa_base)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
