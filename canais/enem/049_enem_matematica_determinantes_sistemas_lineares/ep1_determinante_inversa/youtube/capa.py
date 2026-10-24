"""Capas — Determinantes e Sistemas Lineares, Episódio 1: o que é o determinante (tema claro). 3 variações em 1280x720.
Formatos: A = o determinante do gancho gigante com a conta "15 − 8 = 7?" e o selo "VOCÊ ESCREVERIA?" (sem dar o 23);
B = o placar do Sarrus, TIME VERDE × TIME VERMELHO, sobre a 3 × 3 com as setas; C = o cadeado da chave com a matriz e
"A CHAVE ABRE?" (det = ?)."""
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
    s = "MATEMÁTICA ENEM · DETERMINANTES · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_sinal(c):
    background(c); selo_topo(c)
    V.matriz(c, V.GANCHO, 450, 560, 240, 220, 1.0, 130, barras=True,
             cor={(0, 0): BLUE, (1, 1): BLUE, (0, 1): AMBER, (1, 0): AMBER})
    rrect(c, 900, 330, 900, 300, 40, "#FFFFFF", shadow=True)
    rrect(c, 900, 330, 900, 300, 40, RED, 0.08)
    text_mid(c, "15 − 8 = 7 ?", 1350, 480, 130, "black", RED)
    c.save(); c.translate(1350, 760); c.rotate(-4)
    rrect(c, -360, -70, 720, 140, 30, AMBER)
    text_mid(c, "VOCÊ ESCREVERIA?", 0, 0, 64, "black", "#FFFFFF")
    c.restore()
    text(c, "o erro de sinal mais comum", 1350, 920, 46, "extrabold", INK2)


def capa_times(c):
    background(c); selo_topo(c, W / 2)
    s = "VERDE × VERMELHO"
    text(c, s, W / 2, 250, fit(s, 120, 1700), "black", INK)
    V.sarrus(c, V.S3, 560, 620, 150, 130, 1.0, 1.0, (1, 1, 1), (1, 1, 1), size=70)
    for k, (tit, col) in enumerate((("TIME VERDE", V.VERDE_T), ("TIME VERMELHO", V.VERM_T))):
        x = 1180 + k * 360
        rrect(c, x, 400, 320, 420, 34, "#FFFFFF", shadow=True)
        rrect(c, x, 400, 320, 80, 34, col, 0.18)
        text(c, tit, x + 160, 455, 34, "black", col)
        text_mid(c, "?", x + 160, 660, 200, "black", col)
    rrect(c, 0, 900, W, 180, 0, PURPLE)
    s2 = "DETERMINANTE 3 × 3 SEM ERRO"
    text(c, s2, W / 2, 1015, fit(s2, 90, 1700), "black", "#FFFFFF")


def capa_chave(c):
    background(c); selo_topo(c)
    s = "A CHAVE"
    text(c, s, 520, 380, 150, "black", INK)
    text(c, "ABRE?", 520, 540, 150, "black", PURPLE)
    pill(c, "det = 0 ou det ≠ 0", 520, 680, BLUE, size=44, anchor="center")
    text(c, "o teste da inversa", 520, 800, 50, "extrabold", INK2)
    rrect(c, 1080, 230, 720, 720, 50, "#FFFFFF", shadow=True)
    V.matriz(c, [["x", "3"], ["2", "x + 1"]], 1440, 470, 220, 150, 1.0, 80, barras=True, bcol=PURPLE)
    V.cadeado(c, 1440, 790, 120, 0.0, AMBER, 1.0)
    text_mid(c, "?", 1600, 760, 120, "black", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_quinze_menos_oito", capa_sinal), ("capa_B_verde_vermelho", capa_times),
                     ("capa_C_a_chave_abre", capa_chave)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
