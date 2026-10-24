"""Capas — Expressões Algébricas e Produtos Notáveis, Episódio 2: produtos notáveis e o sonho do calouro (tema claro).
3 variações em 1280x720, sem gabarito: A = fórmula errada gigante riscada sobre o quadrado em 4 pedaços;
B = piso de 7 × 7 lajotas ocupando a metade esquerda ("cadê as 24 lajotas?"); C = o termo do meio escondido numa caixa."""
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


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · ÁLGEBRA · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_calouro(c):
    background(c); selo_topo(c)
    V.quadrado(c, 1300, 300, 4.0, 2.4, 88, 1.0, blink=1.0, size=70, lado=None)
    shadow_rrect(c, 70, 330, 1180, 230, 30, 1, 1.4)
    rrect(c, 70, 330, 1180, 230, 30, "#FFFFFF")
    V.m(c, "(a+b)^2 = a^2 + b^2", 660, 445, 130)
    V.strike(c, 120, 445, 1200, 445, 1.0, RED)
    V.selo(c, 980, 330, 1.0, "SONHO DO CALOURO", RED, 6, 46)
    s = "O ERRO MAIS FAMOSO"
    text(c, s, 660, 720, fit(s, 120, 1150), "black", INK)
    text(c, "DA ÁLGEBRA", 660, 850, 110, "black", RED)
    pill(c, "faltou o quê?", 1580, 930, AMBER, size=40, anchor="center")


def capa_piso(c):
    background(c)
    V.piso(c, 90, 190, 118, 1.0, ret=1.0, blink=1.0)
    selo_topo(c, 1440)
    s1 = "CADÊ AS"
    text(c, s1, 1440, 330, 120, "black", INK)
    text(c, "24 LAJOTAS?", 1440, 470, fit("24 LAJOTAS?", 130, 960), "black", AMBER)
    rrect(c, 1010, 560, 860, 300, 30, "#FFFFFF", shadow=True)
    V.m(c, "7^2 = 49", 1440, 640, 90, hl={2: BLUE})
    V.m(c, "3^2 + 4^2 = 25", 1440, 780, 80, hl={4: RED})
    text(c, "produtos notáveis do zero", 1440, 960, 52, "extrabold", PURPLE)


def capa_meio(c):
    background(c); selo_topo(c, W / 2)
    s = "O TERMO QUE A PEGADINHA ESCONDE"
    text(c, s, W / 2, 290, fit(s, 120, 1780), "black", INK)
    shadow_rrect(c, 160, 400, 1600, 300, 36, 1, 1.4)
    rrect(c, 160, 400, 1600, 300, 36, "#FFFFFF")
    V.m(c, "(2x-3)^2 = 4x^2", 700, 550, 120)
    rrect(c, 1150, 470, 300, 160, 24, AMBER, 0.18)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1150, 470, 300, 160), 24, 24), paint(AMBER, 1.0, stroke=8))
    text_mid(c, "?", 1300, 550, 130, "black", AMBER)
    V.m(c, "+ 9", 1590, 550, 120)
    text(c, "6x? 12x? some?", W / 2, 840, 70, "black", RED)
    text(c, "produtos notáveis de cabeça", W / 2, 960, 52, "extrabold", PURPLE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_sonho_do_calouro", capa_calouro), ("capa_B_cade_as_24_lajotas", capa_piso),
                     ("capa_C_termo_escondido", capa_meio)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
