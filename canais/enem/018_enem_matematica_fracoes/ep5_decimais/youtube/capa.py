"""Capas — Frações, Decimais e Dízimas, Episódio 5: Operações com decimais sem calculadora (tema claro). 3 variações em 1280x720.
A (recomendada) = o resultado que cresce · B = o erro do 0,12 · C = a conta armada."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_cresce(c):
    background(c); selo(c); painel(c)
    K.fmid(c, "4,8 ÷ 0,12", 1470, 230, 84, "black", INK)
    K.fmid(c, "= 40", 1470, 350, 110, "black", GREEN)
    for i in range(40):
        s_, l_ = divmod(i, 10)
        V.moeda_lado(c, 1260 + s_ * 140, 860 - l_ * 30, 1.0, V.PRATA, rx=56, ry=14)
    V.moeda(c, 1700, 470, 56, "12", 1.0, V.PRATA, "centavos")
    big(c, "DIVIDIU E", 340)
    big(c, "FICOU MAIOR?", 470)
    boxed(c, "ESTÁ CERTO", 70, 520, 140, GREEN)
    text(c, "somar, multiplicar e dividir, do zero", 90, 860, 40, "extrabold", INK2, align="left")


def capa_casas(c):
    background(c); selo(c); painel(c)
    K.fmid(c, "0,3 × 0,04", 1470, 260, 96, "black", INK)
    K.fmid(c, "0,12", 1470, 430, 100, "black", RED)
    line(c, 1330, 450, 1610, 410, RED, 1.0, 12)
    K.fmid(c, "= 0,012", 1470, 640, 116, "black", GREEN)
    pill(c, "1 + 2 = 3 casas", 1470, 820, PURPLE, size=46, anchor="center", bounds=(0, 1920))
    big(c, "0,3 × 0,04", 320, size=118)
    big(c, "NÃO É 0,12", 470, size=118)
    boxed(c, "CONTE AS CASAS", 70, 520, 140, PURPLE)
    text(c, "o erro mais comum com decimais", 90, 860, 44, "extrabold", INK2, align="left")


def capa_conta(c):
    background(c); selo(c); painel(c)
    xv = 1500
    K.boxed(c, xv - 26, 200, 52, 470, PURPLE, 1.0, 0.10, r=26, sw=3)
    V.numcol(c, "2,50", xv, 270, 130, INK, 1.0, cols={3: AMBER}, comma=1.0)
    V.numcol(c, "0,75", xv, 430, 130, INK, 1.0, comma=1.0)
    text(c, "+", xv - 290, 430 + 47, 130, "black", INK2)
    line(c, xv - 320, 530, xv + 250, 530, INK, 1.0, 8)
    V.numcol(c, "3,25", xv, 610, 130, GREEN, 1.0, comma=1.0)
    pill(c, "vírgula embaixo de vírgula", 1470, 820, PURPLE, size=40, anchor="center", bounds=(0, 1920))
    big(c, "DECIMAIS", 340)
    big(c, "SEM CALCULADORA", 470)
    boxed(c, "E SEM MEDO", 70, 520, 140, BLUE)
    text(c, "cada passo explicado, do zero", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_dividiu_e_cresceu", capa_cresce), ("capa_B_nao_e_0_12", capa_casas),
                     ("capa_C_conta_armada", capa_conta)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
