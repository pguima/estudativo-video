"""Capas — Função Modular e Funções por Partes, Episódio 1: funções por partes (tema claro). 3 variações em 1280x720, sem
gabarito.
A = duas casas: 10 m³ → R$ 40 e 20 m³ → "R$ 80?" · B = o prédio de três andares com o 26 no elevador · C = a escada do
estacionamento com "2 h 05 = 3 h?"."""
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
    while V.ftext_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÕES POR PARTES · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_dobro(c):
    background(c); selo_topo(c, W / 2)
    s = "GASTOU O DOBRO."
    V.ftext(c, s, W / 2, 270, fit(s, 150, 1760), "black", INK)
    for k, (x, m3, val, col) in enumerate(((140, "10 m³", "R$ 40", BLUE), (1000, "20 m³", "R$ 80?", AMBER))):
        rrect(c, x, 360, 780, 380, 30, mix("#FFFFFF", col, 0.14), shadow=True)
        V.ftext(c, m3, x + 390, 520, 150, "black", INK)
        V.ftext(c, val, x + 390, 680, 120, "black", col)
    text_mid(c, "→", 960, 550, 110, "black", GRAY)
    rrect(c, 0, 800, W, 280, 0, "#FFFFFF", 0.94)
    s3 = "PAGOU O DOBRO?"
    V.ftext(c, s3, W / 2, 980, fit(s3, 150, 1760), "black", RED)


def capa_predio(c):
    background(c); selo_topo(c)
    s = "EM QUE ANDAR"
    V.ftext(c, s, 84, 300, fit(s, 130, 900), "black", INK, align="left")
    s2 = "MORA O 26?"
    V.ftext(c, s2, 84, 450, fit(s2, 130, 900), "black", PURPLE, align="left")
    V.ftext(c, "ache a faixa antes de calcular", 84, 560, 50, "bold", INK2, align="left")
    c.save(); c.translate(1080, 260); c.scale(1.0, 1.0)
    V.predio(c, 0, 80, 1.0, aceso=-1, prog=0.0, valor="26 m³", fw=560, fh=200)
    c.restore()
    V.selo(c, 520, 860, 1.0, "A REGRA MUDA NO MEIO", AMBER, -5, 60)


def capa_escada(c):
    background(c); selo_topo(c, W / 2)
    V.escada_estac(c, 120, 170, 1080, 860, 1.0, bol=1.0, marca=2 + 5 / 60)
    rrect(c, 1240, 260, 600, 600, 30, "#FFFFFF", 0.96, shadow=True)
    V.ftext(c, "2 h 05", 1540, 430, 130, "black", INK)
    V.ftext(c, "=", 1540, 560, 110, "black", GRAY)
    V.ftext(c, "3 h?", 1540, 720, 150, "black", AMBER)
    V.selo(c, 1540, 940, 1.0, "O GRÁFICO PULA", PURPLE, -5, 56)


if __name__ == "__main__":
    for nome, fn in (("capa_A_gastou_o_dobro", capa_dobro), ("capa_B_em_que_andar", capa_predio),
                     ("capa_C_escada_2h05", capa_escada)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
