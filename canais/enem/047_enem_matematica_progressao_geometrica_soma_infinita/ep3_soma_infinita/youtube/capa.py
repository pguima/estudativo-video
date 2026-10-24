"""Capas — Progressão Geométrica, Episódio 3: soma infinita (tema claro). 3 variações em 1280x720.
A = a bola quicando para sempre (8 m, 3/4) com "INFINITOS QUIQUES · QUANTOS METROS?"; B = o quadrado pintado por metades
com "INFINITAS PARCELAS · UM NÚMERO FINITO?"; C = a dízima 0,2727… = ? com o "27/100?" riscado e o selo "CUIDADO".
Nenhuma mostra gabarito (56, 16, 3/11 e 13,5 não aparecem)."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · PROGRESSÃO GEOMÉTRICA · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_bola(c):
    background(c); selo_topo(c)
    V.bola_trajeto(c, 170, 1000, 92, 8, 0.75, 99, 1.0, passo=150)
    s1, s2 = "INFINITOS", "QUIQUES"
    text(c, s1, 1420, 330, fit(s1, 150, 860), "black", INK)
    text(c, s2, 1420, 480, fit(s2, 150, 860), "black", INK)
    s3 = "QUANTOS METROS?"
    sz = fit(s3, 84, 820)
    w = text_w(s3, "black", sz) + 70
    shadow_rrect(c, 1420 - w / 2, 560, w, 140, 28, 1, 1.4)
    rrect(c, 1420 - w / 2, 560, w, 140, 28, RED)
    text_mid(c, s3, 1420, 630, sz, "black", "#FFFFFF")
    V.selo(c, 1420, 800, 1.0, "PARA SEMPRE", AMBER, -5, 64)


def capa_quadrado(c):
    background(c); selo_topo(c, W / 2)
    V.quadrado(c, 140, 200, 760, 11, 1.0)
    s1, s2 = "INFINITAS PARCELAS", "UM NÚMERO FINITO?"
    text(c, s1, 1420, 400, fit(s1, 110, 900), "black", INK)
    text(c, s2, 1420, 540, fit(s2, 110, 900), "black", PURPLE)
    V.K.expr(c, "1/2 + 1/4 + 1/8 + … = ?", 1420, 720, 72, 1.0)
    rrect(c, 0, 990, W, 90, 0, GREEN)
    text_mid(c, "a soma infinita da PG", W / 2, 1035, 54, "black", "#FFFFFF")


def capa_dizima(c):
    background(c); selo_topo(c, W / 2)
    s = "0,272727…"
    text(c, s, W / 2, 400, fit(s, 230, 1700), "black", INK)
    text_mid(c, "= ?", W / 2, 540, 150, "black", AMBER)
    shadow_rrect(c, 1300, 600, 480, 300, 36, 1, 1.4)
    rrect(c, 1300, 600, 480, 300, 36, "#FFFFFF")
    V.K.expr(c, "27/100", 1540, 750, 120, 1.0)
    V.strike(c, 1380, 760, 1700, 740, 1.0, RED, 1)
    V.selo(c, 520, 760, 1.0, "CUIDADO", RED, -6, 90)
    rrect(c, 0, 990, W, 90, 0, PURPLE)
    text_mid(c, "a dízima é uma soma infinita", W / 2, 1035, 54, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_infinitos_quiques", capa_bola), ("capa_B_infinitas_parcelas", capa_quadrado),
                     ("capa_C_dizima_cuidado", capa_dizima)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
