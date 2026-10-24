"""Capas — Polinômios, Episódio 3: caçando raízes (tema claro). 3 variações em 1280x720.
A = o molho de chaves em leque sobre x³ − 2x² − 5x + 6 = 0, com "QUAL CHAVE ABRE?" e o selo "SEM FÓRMULA";
B = o espelho: "RAIZ −2" de um lado e "(x ? 2)" do outro, com "+ OU −?";
C = o prédio do polinômio perdendo o andar de cima, "3º GRAU SEM BHASKARA?".
Nenhuma mostra gabarito (as raízes −2, 1 e 3 e o sinal do fator não aparecem)."""
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
    s = "MATEMÁTICA ENEM · POLINÔMIOS · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_chaves(c):
    background(c); selo_topo(c, W / 2)
    V.expr(c, "x^3 − 2x^2 − 5x + 6 = 0", W / 2, 250, 110, 1, cores={0: PURPLE})
    c.save(); c.translate(580, 800); c.scale(1.45, 1.45)
    V.molho(c, 0, 0, ["±1", "±2", "±3", "±6"], 1, raio=260, size=30)
    c.restore()
    s = "QUAL CHAVE"
    text(c, s, 1400, 560, fit(s, 130, 900), "black", INK)
    text(c, "ABRE?", 1400, 720, 160, "black", V.OURO_D)
    V.selo(c, 1560, 900, 1.0, "SEM FÓRMULA", GREEN, -6, 54)


def capa_espelho(c):
    background(c); selo_topo(c)
    rrect(c, 952, 260, 16, 520, 8, mix("#FFFFFF", BLUE, 0.5))
    text(c, "RAIZ", 520, 330, 50, "black", INK2, tracking=4)
    text(c, "FATOR", 1400, 330, 50, "black", INK2, tracking=4)
    V.expr(c, "−2", 520, 540, 220, 1, cores={0: RED})
    V.expr(c, "(x?2)", 1400, 540, 170, 1, cores={0: GREEN})
    rrect(c, 0, 820, W, 200, 0, INK)
    s = "+ OU − ?  O SINAL QUE DERRUBA"
    text_mid(c, s, W / 2, 920, fit(s, 100, 1760), "black", "#FFFFFF")


def capa_predio(c):
    background(c); selo_topo(c)
    c.save(); c.translate(260, 900); c.scale(1.6, 1.6)
    V.predio(c, 0, 0, ["x^0", "x", "x^2", "x^3"], 1, 0.45, w=290, h=110)
    c.restore()
    s = "3º GRAU"
    text(c, s, 1390, 400, fit(s, 150, 900), "black", PURPLE)
    s2 = "SEM BHASKARA?"
    text(c, s2, 1390, 560, fit(s2, 120, 900), "black", INK)
    pill(c, "derrube um andar", 1390, 700, AMBER, size=50, anchor="center", bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_qual_chave", capa_chaves), ("capa_B_espelho_sinal", capa_espelho),
                     ("capa_C_derrube_andar", capa_predio)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
