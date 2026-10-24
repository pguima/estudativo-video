"""Capas — Polinômios, Episódio 4: Girard e gráficos (tema claro). 3 variações em 1280x720.
A = o gráfico de (x + 1)²(x − 3) com as duas bolas e "TOCA OU ATRAVESSA?";
B = a equação do gancho + o bloco com as arestas "?" e "VOLUME = ?" + "SEM ACHAR AS ARESTAS";
C = o par de meias: a meia "1 − i" e a outra com "?" + "QUEM VEM JUNTO?".
Nenhuma mostra gabarito (o 8, a lei da Q5 e o 1 + i não aparecem)."""
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
    s = "MATEMÁTICA ENEM · POLINÔMIOS · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_grafico(c):
    background(c); selo_topo(c)
    X, Y = V.grafico(c, V.f_ex, (-2.2, 3.6), (-11, 11), (80, 220, 840, 760), 1, 1.0, PURPLE,
                     ((-1, "−1"), (3, "3")), lw=10)
    V.bola(c, X(-1), Y(0) - 34, 1, r=32)
    V.bola(c, X(3), Y(0) - 34, 1, r=32)
    pill(c, "?", X(-1), Y(0) - 120, AMBER, size=44, anchor="center", bounds=(0, 1920))
    pill(c, "?", X(3) - 70, Y(0) - 120, AMBER, size=44, anchor="center", bounds=(0, 1920))
    s = "TOCA OU"
    text(c, s, 1500, 470, fit(s, 150, 760), "black", INK)
    s2 = "ATRAVESSA?"
    text(c, s2, 1500, 630, fit(s2, 150, 760), "black", PURPLE)
    pill(c, "a multiplicidade decide", 1500, 760, GREEN, size=46, anchor="center", bounds=(0, 1920))


def capa_bloco(c):
    background(c); selo_topo(c, W / 2)
    V.expr(c, "2x^3 − 14x^2 + 28x − 16 = 0", W / 2, 250, 84, 1, cores={0: PURPLE})
    V.bloco_iso(c, 560, 640, 520, 300, 240, 1, ("?", "?", "?"), 1.0)
    text(c, "VOLUME", 1400, 560, 130, "black", INK)
    text(c, "= ?", 1400, 720, 150, "black", PURPLE)
    V.selo(c, 1400, 900, 1.0, "SEM ACHAR AS ARESTAS", AMBER, -4, 50)


def capa_meias(c):
    background(c); selo_topo(c)
    c.save(); c.scale(1.8, 1.8)
    V.meias(c, 470 / 1.8, 640 / 1.8, 1, "1 − i", "?", 1.0)
    c.restore()
    s = "RAIZ NÃO REAL"
    text(c, s, 1420, 420, fit(s, 110, 900), "black", INK)
    s2 = "QUEM VEM"
    text(c, s2, 1420, 580, fit(s2, 140, 900), "black", BLUE)
    text(c, "JUNTO?", 1420, 730, 140, "black", BLUE)
    pill(c, "o par de meias dos polinômios", 1420, 860, PURPLE, size=40, anchor="center", bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_toca_ou_atravessa", capa_grafico), ("capa_B_volume_sem_arestas", capa_bloco),
                     ("capa_C_par_de_meias", capa_meias)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
