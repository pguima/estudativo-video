"""Capas — Função Exponencial, Episódio 1: multiplicar em vez de somar e o gráfico (tema claro). 3 variações em 1280x720.
A = a mesada: barras verdes que explodem, "R$ 1 → R$ 1 MILHÃO?" e o selo "só dobrando";
B = as duas escadas (+2 × ×2) em diagonal, com "SOMAR OU MULTIPLICAR?";
C = as curvas 2ˣ e (1/2)ˣ cruzando em (0, 1) e a parede tracejada, com "A CURVA ENCOSTA?".
Nenhuma mostra gabarito (a Q9 e o 25 °C não aparecem)."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO EXPONENCIAL · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_mesada(c):
    background(c); selo_topo(c)
    x0, base = 1000, 960
    for k in range(11):
        h = max(8, 800 * 2 ** k / 1024)
        rrect(c, x0 + k * 82 + 6, base - h, 68, h, 10, mix("#FFFFFF", GREEN, 0.25 + 0.065 * k))
    line(c, x0 - 10, base, x0 + 11 * 82, base, INK2, 1.0, 6)
    s1, s2, s3 = "R$ 1", "VIRA", "R$ 1 MILHÃO?"
    text(c, s1, 110, 380, 170, "black", GREEN, align="left")
    text(c, s2, 110, 540, 130, "black", INK, align="left")
    text(c, s3, 110, 720, fit(s3, 150, 860), "black", PURPLE, align="left")
    V.selo(c, 400, 880, 1.0, "SÓ DOBRANDO", AMBER, -5, 54)


def capa_escadas(c):
    background(c); selo_topo(c, W / 2)
    s = "SOMAR OU MULTIPLICAR?"
    text(c, s, W / 2, 270, fit(s, 130, 1780), "black", INK)
    base, esc, larg = 1000, 22, 110
    for x0, vals, col in ((120, [1 + 2 * k for k in range(7)], BLUE), (1000, [2 ** k for k in range(8)], PURPLE)):
        line(c, x0 - 10, base, x0 + len(vals) * larg + 10, base, INK2, 1.0, 6)
        for k, v in enumerate(vals):
            h = v * esc
            top = max(base - h, 340)
            rrect(c, x0 + k * larg + 5, top, larg - 10, base - top, 12, mix("#FFFFFF", col, 0.35 + 0.06 * k))
            if base - h > 380:
                text(c, str(v), x0 + k * larg + larg / 2, top - 16, 40, "black", col)
    pill(c, "+2 +2 +2", 120, 420, BLUE, size=46, bounds=(0, 1920))
    pill(c, "×2 ×2 ×2", 1000, 420, PURPLE, size=46, bounds=(0, 1920))


def capa_parede(c):
    background(c); selo_topo(c)
    P = V.Plano(160, 260, 900, 680, (-3, 3.2), (-0.6, 8.5))
    P.eixos(c, 1.0, xt=range(-3, 4), yt=range(2, 9, 2), size=30)
    V.parede(c, P, 0, 1.0, None)
    P.curva(c, 1.0, lambda x: 2 ** x, BLUE, width=14)
    P.curva(c, 1.0, lambda x: 0.5 ** x, PURPLE, width=14)
    P.ponto(c, 0, 1, GREEN, 1.0, None, r=16)
    c.drawCircle(P.px(2.6), P.py(0.17), 60, paint(AMBER, 1.0, stroke=8))
    for k, (s_, col) in enumerate((("A CURVA", INK), ("ENCOSTA", AMBER), ("NO ZERO?", INK))):
        text(c, s_, 1480, 420 + k * 180, fit(s_, 150, 760), "black", col)
    V.mx(c, "2^x", 1290, 930, 80, 1.0, BLUE)
    V.mx(c, "(1/2)^x", 1600, 930, 80, 1.0, PURPLE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_um_real_um_milhao", capa_mesada), ("capa_B_somar_ou_multiplicar", capa_escadas),
                     ("capa_C_a_curva_encosta", capa_parede)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
