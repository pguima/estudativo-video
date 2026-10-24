"""Capas — Função Modular e Funções por Partes, Episódio 4: equações e inequações modulares e tolerância (tema claro).
3 variações em 1280x720. Formatos: A = a CICLOVIA larga embaixo, com o posto no meio e dois ciclistas com "?" (antes e
depois), e o título "A 4 km DO POSTO: QUANDO?" em cima; B = a equação |x| = 5 gigante no centro com "x = 5" e o selo
âmbar "SÓ ISSO?"; C = o ELÁSTICO: alfinete no 500 g, o elástico esticando 8 g para cada lado e as pontas "?" com o título
"TOLERÂNCIA VIRA MÓDULO". Nenhuma mostra gabarito."""
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
    s = "MATEMÁTICA ENEM · FUNÇÃO MODULAR · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_ciclovia(c):
    background(c); selo_topo(c)
    s = "A 4 km DO POSTO:"
    text(c, s, 84, 320, fit(s, 150, 1750), "black", INK, align="left")
    s2 = "QUANDO?"
    text(c, s2, 84, 480, 150, "black", RED, align="left")
    x0, x1, y = 160, 1760, 900
    X = V._X(x0, x1, 0, 24)
    rrect(c, x0 - 20, y - 16, x1 - x0 + 40, 32, 16, "#E7EBF2")
    rrect(c, X(12) - 70, y - 300, 140, 100, 18, AMBER)
    text_mid(c, "POSTO", X(12), y - 250, 34, "black", "#FFFFFF")
    line(c, X(12), y - 200, X(12), y - 16, AMBER, 1, 8)
    for kk, col in ((8, BLUE), (16, PURPLE)):
        V.bike(c, X(kk), y - 18, 1, col, 1.6)
        text_mid(c, "?", X(kk), y - 280, 90, "black", col)
        line(c, X(min(kk, 12)), y + 60, X(max(kk, 12)), y + 60, RED, 1, 8)
        text(c, "4 km", (X(kk) + X(12)) / 2, y + 130, 54, "black", RED)


def capa_so_isso(c):
    background(c); selo_topo(c, W / 2)
    s = "|x| = 5"
    text_mid(c, s, W / 2, 430, 260, "black", INK)
    rrect(c, W / 2 - 330, 640, 660, 170, 30, mix("#FFFFFF", BLUE, 0.12))
    text_mid(c, "x = 5", W / 2, 725, 130, "black", BLUE)
    V.selo(c, 1540, 560, 1.0, "SÓ ISSO?", AMBER, -8, 90)


def capa_elastico(c):
    background(c); selo_topo(c)
    s = "TOLERÂNCIA VIRA MÓDULO"
    text(c, s, 84, 300, fit(s, 140, 1750), "black", INK, align="left")
    text(c, "500 g com tolerância de 8 g", 84, 420, 64, "extrabold", INK2, align="left")
    x0, x1, y = 260, 1660, 800
    V.reta(c, x0, x1, y, 488, 512, 1.0, marcas=(500,), size=48)
    V.elastico(c, x0, x1, y, 488, 512, 500, 8, 1.0, u=1, cheia=True, col=GREEN, rot_c="", rot_r="")
    X = V._X(x0, x1, 488, 512)
    for v in (492, 508):
        text_mid(c, "?", X(v), y + 90, 90, "black", RED)
    for xa, xb in ((X(492), X(500)), (X(500), X(508))):
        text(c, "8 g", (xa + xb) / 2, y - 40, 50, "black", GREEN)


if __name__ == "__main__":
    for nome, fn in (("capa_A_quando", capa_ciclovia), ("capa_B_so_isso", capa_so_isso),
                     ("capa_C_elastico", capa_elastico)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
