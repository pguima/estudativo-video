"""Capas — Polinômios, Episódio 1: polinômio, grau, valor numérico e modelagem (tema claro). 3 variações em 1280x720.
A = o polinômio do gancho gigante, (x² − 3x + 3)²⁰, com "SOMA DOS COEFICIENTES = ?" e o selo "SEM DESENVOLVER";
B = a caixa de papelão com as três medidas nas arestas e "V(x) = ?";
C = o prédio dos expoentes com o andar de cima aceso e "QUAL É O GRAU?".
Nenhuma mostra gabarito (o 1, o 40 e o 4x³ − 78x² + 360x não aparecem)."""
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
    s = "MATEMÁTICA ENEM · POLINÔMIOS · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_soma(c):
    background(c); selo_topo(c, W / 2)
    V.expr(c, "(x^2−3x+3)^{20}", W / 2, 400, 210, 1, cores={0: PURPLE})
    rrect(c, 0, 660, W, 190, 0, INK)
    s = "SOMA DOS COEFICIENTES = ?"
    text_mid(c, s, W / 2, 755, fit(s, 110, 1760), "black", "#FFFFFF")
    V.selo(c, 1560, 930, 1.0, "SEM DESENVOLVER", GREEN, -6, 54)


def capa_caixa(c):
    background(c); selo_topo(c)
    V.caixa_iso(c, 620, 640, 640, 380, 190, 1, ("24 − 2x", "15 − 2x", "x"), 1.0)
    s = "A CAIXA VIRA"
    text(c, s, 1440, 360, fit(s, 120, 860), "black", INK)
    s2 = "POLINÔMIO"
    text(c, s2, 1440, 500, fit(s2, 130, 860), "black", PURPLE)
    rrect(c, 1170, 600, 540, 150, 28, mix("#FFFFFF", PURPLE, 0.16))
    text_mid(c, "V(x) = ?", 1440, 675, 96, "black", PURPLE)


def capa_predio(c):
    background(c); selo_topo(c)
    V.predio(c, 260, 980, [("x^0", "7"), ("x", "1"), ("x^2", "−5"), ("x^3", "2")], 1, 3, w=520, h=170)
    s = "QUAL É O"
    text(c, s, 1390, 380, fit(s, 130, 900), "black", INK)
    text(c, "GRAU?", 1390, 540, 170, "black", PURPLE)
    pill(c, "o andar mais alto do prédio", 1390, 680, AMBER, size=46, anchor="center", bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_soma_coeficientes", capa_soma), ("capa_B_caixa_polinomio", capa_caixa),
                     ("capa_C_predio_grau", capa_predio)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
