"""Capas — Operações e Conjuntos Numéricos, Episódio 3: Intervalos reais (tema claro). 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = V.ftext_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    V.fmid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA BÁSICA · EPISÓDIO 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def bolas_grandes(c, x, y, cheia, col=V.FAIXA, r=70):
    c.drawCircle(x, y, r, paint("#FFFFFF"))
    c.drawCircle(x, y, r, paint(col, 1, stroke=14))
    if cheia:
        c.drawCircle(x, y, r, paint(col))


def capa_bolinha(c):
    background(c)
    selo(c)
    painel(c)
    bolas_grandes(c, 1300, 360, True)
    text(c, "entra", 1300, 500, 48, "black", GREEN)
    bolas_grandes(c, 1640, 360, False)
    text(c, "fica fora", 1640, 500, 48, "black", RED)
    r = V.RetaI(1200, 1700, 720, 0, 6, [(v, str(v)) for v in range(0, 7, 2)])
    r.base(c, 1); r.faixa(c, 2, 5, 1); r.bola(c, 2, 1, 1, r=22); r.bola(c, 5, 0, 1, r=22)
    text(c, "BOLINHA", 80, 340, 140, "black", INK, align="left")
    text(c, "CHEIA OU", 80, 470, 140, "black", INK, align="left")
    boxed(c, "VAZIA?", 70, 520, 160, V.FAIXA)
    text(c, "intervalos reais do zero", 90, 860, 56, "extrabold", INK2, align="left")


def capa_infinito(c):
    background(c)
    selo(c)
    painel(c)
    V.fmid(c, "[−∞, 5]", 1470, 330, 110, "black", RED)
    check_icon(c, 1470, 460, 40, 1, RED, "x")
    line(c, 1200, 540, 1740, 540, LINE, 1, 4)
    V.fmid(c, "]−∞, 5]", 1470, 680, 110, "black", GREEN)
    check_icon(c, 1470, 810, 40, 1, GREEN)
    text(c, "O INFINITO", 80, 340, 140, "black", INK, align="left")
    text(c, "É SEMPRE", 80, 470, 140, "black", INK, align="left")
    boxed(c, "ABERTO", 70, 520, 160, PURPLE)
    text(c, "o erro de colchete no ENEM", 90, 860, 56, "extrabold", INK2, align="left")


def capa_acima(c):
    background(c)
    selo(c)
    painel(c)
    V.fmid(c, "\"acima de 100\"", 1470, 250, 56, "black", BLUE)
    r = V.RetaI(1230, 1700, 380, 80, 140, [(100, "100")])
    r.base(c, 1); r.faixa(c, 100, "+inf", 1); r.bola(c, 100, 0, 1, r=24)
    V.fmid(c, "x > 100", 1470, 470, 60, "black", PURPLE)
    line(c, 1200, 560, 1740, 560, LINE, 1, 4)
    V.fmid(c, "\"a partir de 18\"", 1470, 630, 56, "black", BLUE)
    r2 = V.RetaI(1230, 1700, 760, 0, 60, [(18, "18")])
    r2.base(c, 1); r2.faixa(c, 18, "+inf", 1); r2.bola(c, 18, 1, 1, r=24)
    V.fmid(c, "x ≥ 18", 1470, 860, 60, "black", PURPLE)
    text(c, "ACIMA DE", 80, 340, 140, "black", INK, align="left")
    text(c, "NÃO É", 80, 470, 140, "black", INK, align="left")
    boxed(c, "A PARTIR DE", 70, 520, 130, AMBER, INK)
    text(c, "a pegadinha dos intervalos", 90, 860, 56, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_bolinha_cheia_ou_vazia", capa_bolinha), ("capa_B_infinito_aberto", capa_infinito),
                     ("capa_C_acima_de", capa_acima)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
