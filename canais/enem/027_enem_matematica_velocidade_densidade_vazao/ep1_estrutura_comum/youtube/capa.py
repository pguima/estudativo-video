"""Capas — Velocidade, Densidade e Vazão, Episódio 1: a estrutura comum (tema claro). 3 variações em 1280x720.
A = mosaico das 6 unidades com barra e a faixa "6 ASSUNTOS? É 1 SÓ"; B = a barra de km/h gigante virando traço de fração;
C = o triângulo da taxa com "× ou ÷?"."""
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
    s = "MATEMÁTICA ENEM · TAXAS · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_mosaico(c):
    background(c); selo_topo(c, W / 2)
    for k, (n_, d_) in enumerate(V.UNIDS):
        x = 330 + (k % 3) * 630
        y = 290 + (k // 3) * 250
        shadow_rrect(c, x - 250, y - 105, 500, 210, 30, 1, 1.4)
        rrect(c, x - 250, y - 105, 500, 210, 30, "#FFFFFF")
        V.barra(c, n_, d_, x, y, 110, 1.0, 0)
    rrect(c, 0, 790, W, 290, 0, PURPLE)
    s = "6 ASSUNTOS? É 1 SÓ."
    text(c, s, W / 2, 975, fit(s, 170, 1780), "black", "#FFFFFF")


def capa_barra(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 120, 220, 860, 720, 40, 1, 1.4)
    rrect(c, 120, 220, 860, 720, 40, "#FFFFFF")
    V.barra(c, "km", "h", 550, 560, 230, 1.0, 1.0)
    s1, s2 = "A BARRA", "É DIVIDIR"
    text(c, s1, 1450, 470, fit(s1, 170, 840), "black", INK)
    sz = fit(s2, 150, 820)
    w = text_w(s2, "black", sz) + 70
    shadow_rrect(c, 1450 - w / 2, 540, w, 190, 28, 1, 1.4)
    rrect(c, 1450 - w / 2, 540, w, 190, 28, RED)
    text_mid(c, s2, 1450, 635, sz, "black", "#FFFFFF")
    text(c, "velocidade · densidade · vazão", 1450, 860, 50, "extrabold", PURPLE)


def capa_triangulo(c):
    background(c); selo_topo(c, W / 2)
    s = "MULTIPLICA OU DIVIDE?"
    text(c, s, W / 2, 290, fit(s, 150, 1780), "black", INK)
    V.triangulo(c, 620, 700, 640, 1.0, "km", "km/h", "h", "top")
    for k, (op, col, sub) in enumerate((("×", GREEN, "achar o de cima"), ("÷", PURPLE, "achar a taxa"))):
        y = 470 + k * 280
        shadow_rrect(c, 1100, y, 660, 230, 34, 1, 1.4)
        rrect(c, 1100, y, 660, 230, 34, "#FFFFFF")
        text_mid(c, op, 1230, y + 115, 190, "black", col)
        text(c, sub, 1560, y + 135, 46, "black", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_seis_e_um_so", capa_mosaico), ("capa_B_barra_e_dividir", capa_barra),
                     ("capa_C_multiplica_ou_divide", capa_triangulo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
