"""Capas — Logaritmos, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = o enunciado "use log 2 = 0,30" num cartão de prova à esquerda, com três saídas à direita (um tempo? uma
contagem? um expoente?) e "A FERRAMENTA DO ENEM" no alto; B = três cartões de V ou F empilhados com pegadinhas de log, cada
um com a caixinha "V ou F?" vazia; C = "3⁵⁰" gigante e uma fileira de caixinhas de algarismos com "?", e a pergunta
"QUANTOS ALGARISMOS?". Nenhuma mostra gabarito.
"""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · LOGARITMOS · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_ferramenta(c):
    background(c)
    selo_topo(c)
    s = "A FERRAMENTA DO ENEM"
    text(c, s, 84, 290, fit(s, 130, 1750), "black", INK, align="left")
    rrect(c, 84, 380, 820, 520, 36, "#FFFFFF", 1, shadow=True)
    rrect(c, 84, 380, 24, 520, 10, BLUE, 1)
    text(c, "ENUNCIADO", 160, 470, 38, "black", GRAY, align="left", tracking=3)
    text(c, "“use", 160, 620, 110, "black", INK, align="left")
    text(c, "log 2 = 0,30”", 160, 790, fit("log 2 = 0,30”", 130, 700), "black", PURPLE, align="left")
    for k, (s_, col, ic) in enumerate((("UM TEMPO?", GREEN, 7), ("UMA CONTAGEM?", BLUE, 6), ("UM EXPOENTE?", PURPLE, None))):
        y = 400 + k * 180
        arrow(c, 920, 640, 1010, y + 75, INK2, 1, 7, 22)
        rrect(c, 1030, y, 800, 150, 30, "#FFFFFF", 1, shadow=True)
        if ic is None:
            V.icone(c, 2, 1120, y + 75, 0.36, 1)
        else:
            V.area_icone(c, ic, 1120, y + 75, 0.40, 1)
        text(c, s_, 1210, y + 100, fit(s_, 70, 600), "black", col, align="left")


def capa_vf(c):
    background(c)
    selo_topo(c, W / 2)
    s = "VOCÊ CAI EM QUANTAS?"
    text(c, s, W / 2, 270, fit(s, 130, 1750), "black", INK)
    for k, s_ in enumerate(("log(M + N) = log M + log N", "log 0 = 0", "log₂ 10 = log 2 ÷ log 10")):
        y = 340 + k * 225
        rrect(c, 160, y, 1600, 190, 34, "#FFFFFF", 1, shadow=True)
        rrect(c, 160, y, 24, 190, 10, AMBER, 1)
        text_mid(c, V.nb(s_), 820, y + 95, fit(V.nb(s_), 92, 1100), "black", INK)
        rrect(c, 1500, y + 30, 220, 130, 24, mix("#FFFFFF", AMBER, 0.30), 1)
        text_mid(c, "V ou F?", 1610, y + 95, 50, "black", INK)


def capa_algarismos(c):
    background(c)
    selo_topo(c)
    text(c, "3", 84, 560, 380, "black", INK, align="left")
    text(c, "50", 84 + text_w("3", "black", 380) + 10, 380, 190, "black", PURPLE, align="left")
    s = "QUANTOS"
    text(c, s, 900, 360, fit(s, 170, 950), "black", INK, align="left")
    s = "ALGARISMOS?"
    text(c, s, 900, 530, fit(s, 150, 950), "black", BLUE, align="left")
    for k in range(9):
        x = 84 + k * 196
        rrect(c, x, 730, 170, 210, 26, "#FFFFFF", 1, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, 730, 170, 210), 26, 26), paint(LIGHT, 1, stroke=6))
        text_mid(c, "?", x + 85, 835, 120, "black", GRAY if k < 8 else AMBER)
    rrect(c, 1360, 600, 500, 100, 50, mix("#FFFFFF", GREEN, 0.20), 1)
    text_mid(c, "log 3 = 0,477", 1610, 650, 54, "black", GREEN)


if __name__ == "__main__":
    for nome, fn in (("capa_A_ferramenta_do_enem", capa_ferramenta), ("capa_B_voce_cai_em_quantas", capa_vf),
                     ("capa_C_quantos_algarismos", capa_algarismos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
