"""Capas — Notação Científica, Episódio 2: multiplicar, dividir, elevar e tirar raiz (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def big(c, s, y, maxw=1000, size=140):
    while K.ftext_w(s, "black", size) > maxw:
        size -= 4
    K.ftext(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34, maxw=1000):
    while K.ftext_w(s, "black", size) + pad * 2 > maxw:
        size -= 4
    w = K.ftext_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    K.fmid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · NOTAÇÃO CIENTÍFICA · EP. 2", 84, 90, BLUE, size=36, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_gangorra(c):
    background(c); selo(c); painel(c)
    K.expr(c, "40·10^6", 1470, 260, 96, 1.0, cores={0: RED})
    check_icon(c, 1720, 230, 36, 1.0, RED, "x")
    V.gangorra(c, 1470, 560, 8, "4", "10^7", 1.0, larg=520, size=64)
    K.expr(c, "= 4·10^7", 1470, 820, 90, 1.0, cores={1: GREEN})
    big(c, "VALOR CERTO,", 340)
    big(c, "RESPOSTA", 470)
    boxed(c, "ERRADA", 70, 520, 160, RED)
    text(c, "o passo que quase todo mundo esquece", 90, 860, 46, "extrabold", INK2, align="left")


def capa_sinal(c):
    background(c); selo(c); painel(c)
    K.fmid(c, "−2 − (−5)", 1470, 330, 100, "black", AMBER)
    K.fmid(c, "↓", 1470, 470, 80, "black", INK2)
    K.fmid(c, "−2 + 5 = +3", 1470, 610, 90, "black", GREEN)
    K.expr(c, "0,4·10^3 → 4·10^2", 1470, 790, 64, 1.0, cores={2: GREEN})
    big(c, "DIVIDIR EM", 340)
    big(c, "NOTAÇÃO CIENTÍFICA", 470)
    boxed(c, "SEM ERRAR O SINAL", 70, 520, 120, AMBER)
    text(c, "multiplicar, dividir, elevar e tirar raiz", 90, 860, 46, "extrabold", INK2, align="left")


def capa_raiz(c):
    background(c); selo(c); painel(c)
    K.expr(c, "√{1,6·10^{-5}}", 1470, 280, 90, 1.0)
    V.gangorra(c, 1470, 560, -8, "16", "10^{-6}", 1.0, larg=520, size=60)
    K.expr(c, "= 4·10^{-3}", 1470, 820, 86, 1.0, cores={1: GREEN})
    big(c, "RAIZ COM EXPOENTE", 340)
    big(c, "ÍMPAR? USE A", 470)
    boxed(c, "GANGORRA", 70, 520, 160, PURPLE)
    text(c, "o truque que deixa o expoente par", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_valor_certo_resposta_errada", capa_gangorra), ("capa_B_sinal", capa_sinal),
                     ("capa_C_raiz_gangorra", capa_raiz)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
