"""Capas — Juros Compostos, Episódio 1: juros sobre juros e a fórmula M = C · (1 + i)ᵗ (tema claro). 3 variações em 1280x720.
Formatos: A = título à esquerda e a bola de neve gigante à direita com os ×1,1 em volta; B = gráfico de duas barras
(simples × compostos) com o pedaço âmbar "+ R$ 64,10?" ocupando a capa; C = a fórmula gigante numa faixa roxa de ponta a ponta."""
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
    s = "MATEMÁTICA ENEM · JUROS COMPOSTOS · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_bola(c):
    background(c); selo_topo(c)
    text(c, "JUROS", 84, 330, 170, "black", INK, align="left")
    text(c, "SOBRE", 84, 500, 170, "black", INK, align="left")
    text(c, "JUROS", 84, 670, 170, "black", AMBER, align="left")
    text(c, "a bola de neve do seu dinheiro", 84, 790, 50, "extrabold", BLUE, align="left")
    V.bola(c, 1400, 600, 330, 1.0, rot=0.6)
    for k, (x, y) in enumerate(((1010, 300), (1760, 330), (1030, 900), (1780, 880))):
        pill(c, "× 1,1", x, y, BLUE, size=48, anchor="center")


def capa_barras(c):
    background(c); selo_topo(c, W / 2)
    s = "OS MESMOS 10%. DE ONDE VEIO ISSO?"
    text(c, s, W / 2, 250, fit(s, 96, 1780), "black", INK)
    base = 990
    rrect(c, 360, base - 440, 420, 440, 24, BLUE)
    text(c, "SIMPLES", 570, base - 470, 60, "black", BLUE)
    rrect(c, 1140, base - 440, 420, 440, 24, GREEN)
    rrect(c, 1140, base - 590, 420, 140, 24, AMBER)
    text(c, "COMPOSTOS", 1350, base - 620, 60, "black", GREEN)
    text_mid(c, "?", 1350, base - 520, 120, "black", "#FFFFFF")
    text(c, "R$ 1.000,00 a 10% ao mês", 960, 1050, 44, "extrabold", GRAY)


def capa_formula(c):
    background(c); selo_topo(c, W / 2)
    s = "A FÓRMULA QUE FAZ A DÍVIDA CRESCER"
    text(c, s, W / 2, 280, fit(s, 104, 1780), "black", INK)
    rrect(c, 0, 400, W, 380, 0, mix("#FFFFFF", PURPLE, 0.12))
    V.formula(c, W / 2, 600, 210, 1.0)
    text(c, "juros compostos do zero, sem calculadora", W / 2, 900, 56, "extrabold", PURPLE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_bola_de_neve", capa_bola), ("capa_B_mesmos_10", capa_barras),
                     ("capa_C_formula_gigante", capa_formula)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
