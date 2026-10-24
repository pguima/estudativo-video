"""Capas — Expressões Algébricas, Episódio 3: fatoração e frações algébricas (tema claro). 3 variações em 1280x720.
A = a fração (x + 3)/3 gigante com a tesoura e "VOCÊ CORTARIA?"; B = o L virando retângulo (geometria ocupando a capa);
C = faixa com os 5 casos em fichas e o título embaixo."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · ÁLGEBRA · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_corta(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 110, 190, 900, 800, 40, 1, 1.4)
    rrect(c, 110, 190, 900, 800, 40, "#FFFFFF")
    K.expr(c, "{x+3}/3", 560, 590, 260)
    V.tesoura(c, 880, 420, 280, 1.0, 0.8, RED)
    s1 = "VOCÊ"
    text(c, s1, 1520, 400, 150, "black", INK)
    text(c, "CORTARIA", 1520, 560, fit("CORTARIA", 150, 820), "black", INK)
    w = text_w("ESSE 3?", "black", 150) + 80
    shadow_rrect(c, 1520 - w / 2, 610, w, 190, 30, 1, 1.4)
    rrect(c, 1520 - w / 2, 610, w, 190, 30, RED)
    text_mid(c, "ESSE 3?", 1520, 705, 150, "black", "#FFFFFF")
    text(c, "fator × termo", 1520, 900, 60, "extrabold", PURPLE)


def capa_l(c):
    background(c); selo_topo(c, W / 2)
    A, B = 560.0, 220.0
    x0, y0 = 130.0, 330.0
    V._ret(c, x0, y0, A - B, A, BLUE, 1.0)
    V._ret(c, x0 + A - B, y0 + B, B, A - B, AMBER, 1.0)
    rrect(c, x0 + A - B, y0, B, B, 6, None, 1.0, stroke=5, stroke_color=RED)
    text_mid(c, "−", x0 + A - B / 2, y0 + B / 2, 120, "black", RED)
    arrow(c, 760, 610, 860, 610, GREEN, 1.0, 10, 30)
    V._ret(c, 900, 250, A - B, A + B - 40, BLUE, 1.0)
    V._ret(c, 900, 250, A - B, B - 20, AMBER, 1.0)
    text(c, "O L QUE VIRA", 1580, 520, 84, "black", INK)
    text(c, "RETÂNGULO", 1580, 625, 84, "black", PURPLE)
    K.expr(c, "a^2-b^2 = (a+b)(a-b)", 1580, 800, 64, cores={1: GREEN})


def capa_casos(c):
    background(c); selo_topo(c, W / 2)
    casos = [("FATOR COMUM", "3x(2x+3)"), ("AGRUPAMENTO", "(a+2)(x+3)"), ("DIF. DE QUADRADOS", "(x+5)(x-5)"),
             ("QUADRADO PERFEITO", "(x-3)^2"), ("SOMA E PRODUTO", "(x+2)(x+3)")]
    for k, (tit, e) in enumerate(casos):
        x = 70 + k * 362
        shadow_rrect(c, x, 210, 336, 380, 30, 1, 1.4)
        rrect(c, x, 210, 336, 380, 30, "#FFFFFF")
        badge_num(c, k + 1, x + 168, 280, 1.0, 40, bg=PURPLE)
        text(c, tit, x + 168, 390, fit(tit, 34, 300), "black", PURPLE)
        K.expr(c, e, x + 168, 490, 52 if len(e) < 9 else 44, cores={0: INK})
    s = "OS 5 CASOS DE FATORAÇÃO"
    text(c, s, W / 2, 790, fit(s, 130, 1780), "black", INK)
    text(c, "e a fração que você NÃO pode cortar", W / 2, 920, 64, "extrabold", RED)


if __name__ == "__main__":
    for nome, fn in (("capa_A_voce_cortaria", capa_corta), ("capa_B_L_vira_retangulo", capa_l),
                     ("capa_C_cinco_casos", capa_casos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
