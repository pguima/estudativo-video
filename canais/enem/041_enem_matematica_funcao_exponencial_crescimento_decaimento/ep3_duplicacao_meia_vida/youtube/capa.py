"""Capas — Função Exponencial, Episódio 3: duplicação e meia-vida (tema claro). 3 variações em 1280x720, sem gabarito.
Formatos: A = pizza gigante à direita cortada, título empilhado à esquerda ("ACABOU?"); B = relógio no centro com o
"×12?" riscado em cima; C = barras da meia-vida ocupando a largura, com a última barra em "?"."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · EXPONENCIAL · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_pizza(c):
    background(c); selo_topo(c)
    text(c, "PERDE METADE", 90, 330, fit("PERDE METADE", 120, 1000), "black", INK, align="left")
    text(c, "A CADA 30 ANOS.", 90, 470, fit("A CADA 30 ANOS.", 120, 1000), "black", INK, align="left")
    w = text_w("ACABOU?", "black", 170) + 90
    shadow_rrect(c, 80, 540, w, 230, 30, 1, 1.4)
    rrect(c, 80, 540, w, 230, 30, RED)
    text_mid(c, "ACABOU?", 80 + w / 2, 655, 170, "black", "#FFFFFF")
    text(c, "depois de 60 anos?", 90, 880, 56, "extrabold", PURPLE, align="left")
    V.pizza(c, 1480, 560, 330, 1.0, 1.0)
    V.selo(c, 1480, 960, 1.0, "QUANTO SOBRA?", AMBER, -4, 48)


def capa_relogio(c):
    background(c); selo_topo(c, W / 2)
    s = "DOBROU 6 VEZES."
    text(c, s, W / 2, 280, fit(s, 140, 1700), "black", INK)
    V.relogio(c, 560, 650, 230, 1.0, 6.12, col=PURPLE, rot_=None)
    text_mid(c, "× 12 ?", 1340, 600, 230, "black", RED)
    strike(c, 1020, 600, 1660, 600, 1.0, RED)
    V.selo(c, 1340, 840, 1.0, "ENTÃO É × QUANTO?", GREEN, -4, 52)


def capa_barras(c):
    background(c); selo_topo(c, W / 2)
    s = "MEIA-VIDA SEM DECORAR"
    text(c, s, W / 2, 270, fit(s, 130, 1760), "black", INK)
    base, x0, w, gap, hmax = 960, 170, 300, 110, 560
    line(c, x0 - 30, base, x0 + 4 * (w + gap) - gap + 30, base, INK2, 1.0, 6)
    for k in range(4):
        xx = x0 + k * (w + gap)
        h = hmax / 2 ** k
        if k < 3:
            rrect(c, xx, base - h, w, h, 18, mix("#FFFFFF", PURPLE, 0.6 - 0.1 * k))
            text(c, f"{100 / 2 ** k:g}%".replace(".", ","), xx + w / 2, base - h - 26, 64, "black", PURPLE)
        else:
            rrect(c, xx, base - 200, w, 200, 18, "#FFFFFF")
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(xx, base - 200, w, 200), 18, 18),
                        paint(AMBER, 1.0, stroke=8))
            text_mid(c, "?", xx + w / 2, base - 100, 150, "black", AMBER)
        if k > 0:
            text(c, "÷2", xx - gap / 2, base - hmax / 2 ** k - 110, 44, "black", GRAY)


if __name__ == "__main__":
    for nome, fn in (("capa_A_acabou_pizza", capa_pizza), ("capa_B_dobrou_6_vezes", capa_relogio),
                     ("capa_C_barras_meia_vida", capa_barras)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
