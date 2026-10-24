"""Capas — Função Exponencial, Episódio 6: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = "A FUNÇÃO DAS MANCHETES" em duas linhas à esquerda e, à direita, a curva exponencial subindo com os ícones
de área pendurados nela (bactéria, cifrão, átomo, termômetro); B = "PERDE 15%" no alto e dois cartões em duelo,
"0,15?" e "0,85?", com a pergunta "QUAL É O FATOR?" em faixa âmbar; C = a escada que multiplica (barras dobrando) ocupando a
metade esquerda e "DOBROU 6 VEZES" com "×12?" à direita. Nenhuma mostra gabarito.
"""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep6", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO EXPONENCIAL · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_manchetes(c):
    background(c)
    selo_topo(c)
    text(c, "A FUNÇÃO", 84, 400, fit("A FUNÇÃO", 190, 860), "black", INK, align="left")
    text(c, "DAS MANCHETES", 84, 560, fit("DAS MANCHETES", 150, 900), "black", GREEN, align="left")
    pill(c, "o ENEM conta uma história", 84, 700, AMBER, size=46, bounds=(0, 1920))
    pill(c, "9 pegadinhas + 5 questões", 84, 900, PURPLE, size=48, bounds=(0, 1920))
    x0, yb = 1060, 940
    arrow(c, x0 - 30, yb, 1880, yb, INK2, 1, 6, 18)
    arrow(c, x0, yb + 30, x0, 160, INK2, 1, 6, 18)
    V.curva_exp(c, x0 + 20, 210, 760, 700, GREEN, 1, 16)
    for k, (u, ic) in enumerate(((0.25, 0), (0.55, 3), (0.78, 1), (0.93, 2))):
        v = (2 ** (5 * u) - 1) / 31
        x, y = x0 + 20 + 760 * u, 210 + 700 - 700 * v
        c.drawCircle(x, y, 74, paint("#FFFFFF", 1))
        c.drawCircle(x, y, 74, paint(LIGHT, 1, stroke=6))
        V.area_icone(c, ic, x, y, 0.36, 1)


def capa_fator(c):
    background(c)
    selo_topo(c, W / 2)
    s = "PERDE 15% AO ANO"
    text(c, s, W / 2, 300, fit(s, 140, 1700), "black", RED)
    for k, s_ in enumerate(("0,15?", "0,85?")):
        x = 560 + k * 800
        rrect(c, x - 300, 380, 600, 380, 40, "#FFFFFF", 1, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 300, 380, 600, 380), 40, 40), paint(INK2, 1, stroke=8))
        text_mid(c, s_, x, 570, 150, "black", INK)
    text_mid(c, "OU", W / 2, 570, 80, "black", GRAY)
    rrect(c, 0, 840, W, 240, 0, mix("#FFFFFF", AMBER, 0.85))
    s = "QUAL É O FATOR?"
    text(c, s, W / 2, 1000, fit(s, 140, 1700), "black", INK)


def capa_escada(c):
    background(c)
    selo_topo(c)
    for k, v in enumerate((1, 2, 4, 8, 16, 32, 64)):
        hh = 11 * v
        x = 110 + k * 120
        rrect(c, x, 960 - hh, 96, hh, 12, mix("#FFFFFF", BLUE, 0.25 + 0.1 * k), 1)
        if k:
            text_mid(c, "×2", x + 48, 960 - hh - 40, 40, "black", GREEN)
    line(c, 80, 975, 960, 975, AMBER, 1, 6, dash=[18, 12])
    text(c, "DOBROU", 1080, 400, fit("DOBROU", 190, 800), "black", INK, align="left")
    text(c, "6 VEZES", 1080, 580, fit("6 VEZES", 190, 800), "black", BLUE, align="left")
    rrect(c, 1080, 660, 620, 260, 40, mix("#FFFFFF", AMBER, 0.30), 1, shadow=True)
    text_mid(c, "×12?", 1390, 790, 170, "black", RED)


if __name__ == "__main__":
    for nome, fn in (("capa_A_funcao_das_manchetes", capa_manchetes), ("capa_B_qual_e_o_fator", capa_fator),
                     ("capa_C_dobrou_6_vezes", capa_escada)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
