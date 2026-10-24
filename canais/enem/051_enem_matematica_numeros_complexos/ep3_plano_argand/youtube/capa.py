"""Capas — Números Complexos, Episódio 3: o plano de Argand-Gauss (tema claro). 3 variações em 1280x720.
A = o galpão quadriculado com o robô de 1 + 2i a 4 + 6i, catetos 3 e 4 e a linha reta com "?": "ANDOU 7 METROS?";
B = a manivela girando (4, 1) com o arco de 90° e o ponto de chegada em "?": "VEZES i GIRA?";
C = "|3 + 4i| = 7 ?" gigante com o selo "VOCÊ CAI NESSA?".
Nenhuma mostra gabarito (o 5 da Q4 e o −2 + 3i da Q5 não aparecem)."""
import importlib.util, math, subprocess, sys
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · NÚMEROS COMPLEXOS · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_robo(c):
    background(c); selo_topo(c)
    pl = V.Plano(190, 960, 100, 0, 5, 0, 7)
    pl.draw(c, 1, rotulos=False, numeros=False)
    V.tri(c, pl, (1, 2), (4, 6), 1, ah=0, cat=("3 m", "4 m"), size=40)
    (x0, y0), (x1, y1) = pl.P(1, 2), pl.P(4, 6)
    line(c, x0, y0, x1, y1, PURPLE, 1, 6, dash=[18, 12])
    pill(c, "?", (x0 + x1) / 2 - 40, (y0 + y1) / 2 - 20, PURPLE, size=56, anchor="center", bounds=(0, 1920))
    V.ponto(c, pl, 1, 2, "", BLUE, 1, r=16)
    V.ponto(c, pl, 4, 6, "", BLUE, 1, r=16)
    V.robo(c, x0, y0 - 46, 1, 1.6)
    s = "ANDOU 7 METROS?"
    text(c, s, 1330, 420, fit(s, 140, 1000), "black", INK)
    text(c, "1 + 2i  →  4 + 6i", 1330, 560, 70, "black", BLUE)
    V.selo(c, 1330, 780, 1.0, "O PLANO DOS COMPLEXOS", PURPLE, -5, 60)


def capa_manivela(c):
    background(c); selo_topo(c, W / 2)
    s = "VEZES i GIRA O PONTO?"
    text(c, s, W / 2, 290, fit(s, 140, 1780), "black", INK)
    pl = V.Plano(700, 960, 92, -3, 5, 0, 5)
    pl.draw(c, 1, rotulos=False, numeros=False)
    V.ponto(c, pl, 4, 1, "(4, 1)", BLUE, 1, dx=20, dy=50, size=48, r=16)
    V.manivela(c, pl, V.ANG41, V.ANG41 + 90, V.R17, 0.7, PURPLE, 1, rot_arco="")
    X, Y = pl.P(-1, 4)
    c.drawCircle(X, Y, 40, paint(mix("#FFFFFF", AMBER, 0.3), 1))
    text_mid(c, "?", X, Y, 64, "black", AMBER)
    pill(c, "90°", 1560, 560, AMBER, size=64, anchor="center", bounds=(0, 1920))
    pill(c, "sem mudar a distância", 1560, 720, GREEN, size=40, anchor="center", bounds=(0, 1920))


def capa_armadilha(c):
    background(c); selo_topo(c, W / 2)
    rrect(c, 260, 330, 1400, 360, 40, "#FFFFFF", 1, shadow=True)
    s = "|3 + 4i| = 7 ?"
    text(c, s, W / 2, 580, fit(s, 210, 1300), "black", RED)
    V.selo(c, 1480, 760, 1.0, "VOCÊ CAI NESSA?", AMBER, -8, 72)
    rrect(c, 0, 900, W, 180, 0, PURPLE)
    text_mid(c, "módulo, distância e o giro de 90°", W / 2, 990, 70, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_andou_7_metros", capa_robo), ("capa_B_vezes_i_gira", capa_manivela),
                     ("capa_C_modulo_7", capa_armadilha)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
