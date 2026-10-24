"""Capas — Determinantes e Sistemas Lineares, Episódio 4: uma, infinitas ou nenhuma (tema claro). 3 variações em 1280x720.
Formatos: A = o semáforo gigante no AMARELO com "D = 0 · IMPOSSÍVEL?" e as gêmeas × brigadas com "?" (sem dar a regra);
B = três mini-planos (cruzam, paralelas, coincidentes) numa faixa, com "1, ∞ OU NENHUMA?" e o D no centro;
C = o sistema do gancho com o terno (1, 2, 3) e o carimbo "SOLUÇÃO ÚNICA?" (sem dizer que é SPI)."""
import importlib.util, subprocess, sys
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
    s = "MATEMÁTICA ENEM · DETERMINANTES · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_amarelo(c):
    background(c); selo_topo(c)
    V.semaforo(c, 330, 600, 150, "amarelo", 1.0, 1.0)
    text(c, "D = 0", 1150, 380, 170, "black", AMBER)
    s = "IMPOSSÍVEL?"
    text(c, s, 1150, 560, fit(s, 150, 1100), "black", INK)
    V.camisetas(c, 870, 800, 95, "gemeas", 1.0)
    V.camisetas(c, 1430, 800, 95, "brigadas", 1.0)
    text_mid(c, "?", 1150, 790, 120, "black", AMBER)


def capa_planos(c):
    background(c); selo_topo(c, W / 2)
    s = "1, ∞ OU NENHUMA?"
    text(c, s, W / 2, 270, fit(s, 140, 1700), "black", INK)
    for k, tp in enumerate(("cruzam", "paralelas", "coincidentes")):
        V.retas(c, 150 + k * 560, 380, 500, 330, tp, 1.0)
    rrect(c, 0, 880, W, 200, 0, PURPLE)
    s2 = "DECIDA PELO DETERMINANTE"
    text(c, s2, W / 2, 1010, fit(s2, 96, 1700), "black", "#FFFFFF")


def capa_terno(c):
    background(c); selo_topo(c)
    V.sistema(c, ["x + y + z = 6", "x − y + 2z = 5", "2x + 3z = 11"], 150, 520, 80, 1.0)
    rrect(c, 180, 800, 700, 150, 30, mix("#FFFFFF", BLUE, 0.12))
    text_mid(c, "(1, 2, 3)", 530, 875, 96, "black", BLUE)
    c.save(); c.translate(1420, 470); c.rotate(-6)
    rrect(c, -400, -120, 800, 240, 36, "#FFFFFF", shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-400, -120, 800, 240), 36, 36), paint(RED, 1.0, stroke=10))
    text_mid(c, "SOLUÇÃO", 0, -45, 96, "black", RED)
    text_mid(c, "ÚNICA?", 0, 60, 96, "black", RED)
    c.restore()
    text(c, "o determinante avisa", 1420, 800, 56, "extrabold", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_d_zero_impossivel", capa_amarelo), ("capa_B_um_infinitas_nenhuma", capa_planos),
                     ("capa_C_solucao_unica", capa_terno)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
