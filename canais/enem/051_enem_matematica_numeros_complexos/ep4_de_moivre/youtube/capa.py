"""Capas — Números Complexos, Episódio 4: forma trigonométrica e De Moivre (tema claro). 3 variações em 1280x720.
A = a tela do radar com a seta e "(1 + i)⁸ EM UMA LINHA?";
B = "MULTIPLICAR É GIRAR": a seta curta, a seta longa girada e o arco entre elas;
C = o ponto −1 + i no plano com "45° OU 135°?" (as duas opções em cores neutras).
Nenhuma mostra gabarito (o 16 da Questão 7 e o 60° da Questão 6 não aparecem)."""
import importlib.util, math, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · NÚMEROS COMPLEXOS · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_radar(c):
    background(c); selo_topo(c)
    cx, cy, R = 470, 600, 360
    V.radar_tela(c, cx, cy, R, 1.2, 1)
    for j in range(1, 8):
        V.seta(c, cx, cy, 45 * j, 60 + 28 * j, "#3FD69A", 0.45, 5, False)
    V.seta(c, cx, cy, 45, 120, "#FFD166", 1, 10)
    V.arco(c, cx, cy, 80, 0, 45, "#FFD166", 1, 8)
    V.expr(c, "(1+i)^8", 1390, 420, 190, 1, cores={0: PURPLE})
    s = "EM UMA LINHA?"
    text(c, s, 1390, 680, fit(s, 130, 900), "black", INK)
    pill(c, "sem 8 multiplicações", 1390, 820, GREEN, size=46, anchor="center", bounds=(0, 1920))


def capa_girar(c):
    background(c); selo_topo(c, W / 2)
    s = "MULTIPLICAR"
    text(c, s, W / 2, 280, fit(s, 150, 1500), "black", INK)
    s2 = "É GIRAR"
    text(c, s2, W / 2, 440, fit(s2, 160, 1500), "black", PURPLE)
    cx, cy = 760, 940
    line(c, cx - 420, cy, cx + 720, cy, INK2, 1, 5)
    V.seta(c, cx, cy, 15, 300, BLUE, 1, 12)
    V.seta(c, cx, cy, 70, 430, PURPLE, 1, 12)
    V.arco(c, cx, cy, 220, 15, 70, AMBER, 1, 10)
    pill(c, "× módulos", 1330, 690, BLUE, size=50, anchor="center", bounds=(0, 1920))
    pill(c, "+ ângulos", 1330, 820, AMBER, size=50, anchor="center", bounds=(0, 1920))


def capa_quadrante(c):
    background(c); selo_topo(c)
    cx, cy, u = 520, 640, 230
    X, Y = V.plano(c, cx, cy, 340, u, 1, rotulos=False, ticks=((-1, "−1", "x"), (1, "1", "y")))
    V.seta(c, cx, cy, 135, math.sqrt(2) * u, PURPLE, 1, 12)
    V.expr(c, "−1 + i", X(-1) - 10, Y(1) - 70, 70, 1, cores={0: PURPLE})
    text(c, "θ = ?", 1400, 360, 120, "black", INK)
    for k, s_ in enumerate(("45°", "135°")):
        x = 1220 + k * 380
        rrect(c, x - 160, 470, 320, 180, 30, "#FFFFFF", 1, shadow=True)
        text_mid(c, s_, x, 560, 110, "black", INK, 1)
    text_mid(c, "OU", 1410, 560, 60, "black", INK2, 1)
    V.selo(c, 1410, 800, 1.0, "O QUADRANTE DECIDE", AMBER, -4, 52)


if __name__ == "__main__":
    for nome, fn in (("capa_A_radar_em_uma_linha", capa_radar), ("capa_B_multiplicar_e_girar", capa_girar),
                     ("capa_C_45_ou_135", capa_quadrante)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
