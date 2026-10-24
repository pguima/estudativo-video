"""Capas — Polinômios, Episódio 2: divisão, Briot-Ruffini e o teorema do resto (tema claro). 3 variações em 1280x720.
Formatos: A = a divisão gigante em cima e o "resto = ?" num cartão roxo embaixo; B = a esteira de Briot-Ruffini ocupando
a largura, com a casa do resto em "?"; C = fundo escuro com o duelo "3 ou −3?" para x + 3. Nenhuma mostra gabarito."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, col=BLUE):
    s = "MATEMÁTICA ENEM · POLINÔMIOS · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, col, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, col, size=34, anchor="center", bounds=(0, 1920))


def capa_sem_dividir(c):
    background(c); selo_topo(c, W / 2)
    V.linha(c, [("2x³ − x + 5", PURPLE), ("  ÷  ", INK), ("x + 1", BLUE)], W / 2, 300, 150, 1.0)
    shadow_rrect(c, 260, 450, 1400, 330, 40, 1, 1.4)
    rrect(c, 260, 450, 1400, 330, 40, PURPLE)
    s = "RESTO SEM DIVIDIR?"
    text_mid(c, s, W / 2, 570, fit(s, 140, 1300), "black", "#FFFFFF")
    text_mid(c, "troque x por UM número", W / 2, 690, 64, "extrabold", "#FFFFFF")
    V.selo(c, 1560, 870, 1.0, "resto = ?", AMBER, -6, 54)


def capa_esteira(c):
    background(c); selo_topo(c)
    s = "A ESTEIRA QUE DIVIDE"
    text(c, s, 84, 280, fit(s, 130, 1750), "black", INK, align="left")
    text(c, "Briot-Ruffini em uma linha", 88, 360, 56, "extrabold", PURPLE, align="left")
    xs, yb = V.esteira(c, 0, 220, 600, 2, V.POLY_B, 1.0, [1, 1, 1, 0], cw=300, size=96, rot_resto=False)
    x = xs[-1]
    rrect(c, x - 130, yb - 80, 260, 160, 26, mix("#FFFFFF", AMBER, 0.35))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 130, yb - 80, 260, 160), 26, 26), paint(AMBER, 1, stroke=6))
    text_mid(c, "?", x, yb, 120, "black", AMBER)
    text(c, "resto", x, yb + 130, 40, "black", AMBER)


def capa_lado_oposto(c):
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#1B1A2E"))
    selo_topo(c, W / 2, PURPLE)
    s = "DIVIDIR POR x + 3"
    text(c, s, W / 2, 300, fit(s, 130, 1700), "black", "#FFFFFF")
    for k, (v, col) in enumerate((("3", AMBER), ("−3", AMBER))):
        x = W / 2 - 360 + k * 720
        rrect(c, x - 260, 420, 520, 380, 40, "#26253D")
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 260, 420, 520, 380), 40, 40), paint(col, 1, stroke=8))
        text_mid(c, v, x, 600, 230, "black", col)
    text_mid(c, "OU", W / 2, 610, 90, "black", "#FFFFFF")
    text(c, "usa qual raiz?", W / 2, 920, 66, "extrabold", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_resto_sem_dividir", capa_sem_dividir), ("capa_B_esteira", capa_esteira),
                     ("capa_C_tres_ou_menos_tres", capa_lado_oposto)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
