"""Capas — Notação Científica e Ordem de Grandeza, Episódio 1: a forma exata (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

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


def capa_escrita(c):
    background(c); selo(c); painel(c)
    K.expr(c, "25 · 10^3", 1470, 270, 100, 1, cores=V.mono("25 · 10^3", RED))
    strike(c, 1290, 270, 1650, 270, 1, RED, 1)
    K.expr(c, "2,5 · 10^4", 1470, 420, 100, 1, cores=V.mono("2,5 · 10^4", GREEN))
    check_icon(c, 1740, 410, 34, 1, GREEN)
    line(c, 1200, 520, 1740, 520, "#E6E6E2", 1, 3)
    K.expr(c, "0,5 · 10^4", 1470, 620, 100, 1, cores=V.mono("0,5 · 10^4", RED))
    strike(c, 1270, 620, 1670, 620, 1, RED, 1)
    K.expr(c, "5 · 10^3", 1470, 770, 100, 1, cores=V.mono("5 · 10^3", GREEN))
    check_icon(c, 1700, 760, 34, 1, GREEN)
    big(c, "VALOR CERTO,", 340)
    big(c, "ESCRITA", 470)
    boxed(c, "ERRADA", 70, 520, 160, RED)
    text(c, "a forma exata da notação científica", 90, 860, 46, "extrabold", INK2, align="left")


def capa_converta(c):
    background(c); selo(c); painel(c)
    text(c, "Terra → Lua, em metros", 1470, 250, 34, "black", GRAY)
    x0, cw = V.digitos(c, "384400000", 1470, 380, 96, 1, virg=1, cores={0: GREEN})
    V.pulos(c, x0, cw, 380, 96, 9, 8, -1, 1)
    K.contador(c, 1470, 620, 8, 1, "casas ←", PURPLE, 120)
    K.expr(c, "3,844 · 10^8", 1470, 860, 90, 1, cores={0: GREEN})
    big(c, "CONVERTA", 340)
    big(c, "QUALQUER", 470)
    boxed(c, "NÚMERO", 70, 520, 160, BLUE)
    text(c, "é só contar as casas da vírgula", 90, 860, 46, "extrabold", INK2, align="left")


def capa_negativo(c):
    background(c); selo(c); painel(c)
    K.expr(c, "10^{-3}", 1470, 330, 170, 1)
    K.fmid(c, "≠ negativo", 1470, 560, 80, "black", RED)
    K.expr(c, "= 0,001", 1470, 780, 130, 1, cores={0: GREEN, 1: GREEN})
    big(c, "10⁻³ É UM", 340)
    big(c, "NÚMERO", 470)
    boxed(c, "NEGATIVO?", 70, 520, 160, AMBER)
    text(c, "não: o expoente diz o lado da vírgula", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_valor_certo_escrita_errada", capa_escrita), ("capa_B_converta_qualquer_numero", capa_converta),
                     ("capa_C_expoente_negativo", capa_negativo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
