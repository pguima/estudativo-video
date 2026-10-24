"""Capas — Função Modular e Funções por Partes, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = três "etiquetas de texto" do ENEM (conta de água, estacionamento, tolerância de 2 mm) com uma lupa que
revela "f(x)" por trás, título "A FUNÇÃO ESCONDIDA"; B = a conta de energia em escada de caixinhas e a pergunta
"250 kWh · R$ ???" com o palpite "275?" num selo âmbar; C = a avenida com o km 30 e o entregador "a 7 km", com dois
pontos de interrogação, um de cada lado ("ONDE ELE ESTÁ?"). Nenhuma mostra gabarito.
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
    s = "MATEMÁTICA ENEM · FUNÇÃO MODULAR · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_escondida(c):
    background(c)
    selo_topo(c, W / 2)
    s = "A FUNÇÃO ESCONDIDA"
    text(c, s, W / 2, 270, fit(s, 150, 1750), "black", INK)
    for k, (s, ic, col, rot) in enumerate((("conta de água", 0, BLUE, -4), ("estacionamento", 3, PURPLE, 3),
                                           ("tolerância de 2 mm", 6, AMBER, -2))):
        x = 330 + k * 630
        c.save(); c.translate(x, 530); c.rotate(rot)
        rrect(c, -270, -190, 540, 380, 36, mix("#F7F7F5", col, 0.16), 1, shadow=True)
        V.area_icone(c, ic, 0, -40, 0.75, 1)
        text(c, s, 0, 140, fit(s, 60, 480), "black", col)
        c.restore()
    # a lupa sobre o cartão do meio, revelando f(x)
    c.drawCircle(960, 905, 140, paint("#FFFFFF", 0.95))
    c.drawCircle(960, 905, 140, paint(INK, 1, stroke=18))
    line(c, 1060, 1005, 1150, 1095, INK, 1, 34)
    text_mid(c, "f(x)", 960, 905, 110, "black", PURPLE)


def capa_energia(c):
    background(c)
    selo_topo(c)
    s = "QUANTO VEM NA CONTA?"
    text(c, s, 84, 280, fit(s, 120, 1750), "black", INK, align="left")
    for k, (rot, col) in enumerate((("R$ 0,50", mix("#FFFFFF", INK2, 0.35)), ("R$ 0,80", BLUE), ("R$ 1,10", PURPLE))):
        h = 240 + k * 170
        x = 120 + k * 290
        rrect(c, x, 1000 - h, 260, h, 24, col, 1, shadow=True)
        text_mid(c, rot, x + 130, 1000 - h + 70, 52, "black", "#FFFFFF")
    V.area_icone(c, 1, 1100, 560, 0.75, 1)
    rrect(c, 1240, 430, 600, 260, 36, "#FFFFFF", 1, shadow=True)
    text_mid(c, "250 kWh", 1540, 510, 90, "black", INK)
    text_mid(c, "R$ ???", 1540, 620, 90, "black", PURPLE)
    rrect(c, 1300, 760, 480, 170, 30, mix("#FFFFFF", AMBER, 0.45), 1, shadow=True)
    text_mid(c, "R$ 275?", 1540, 845, 110, "black", INK)


def capa_avenida(c):
    background(c)
    selo_topo(c)
    s = "ONDE ELE ESTÁ?"
    text(c, s, 84, 290, fit(s, 160, 1750), "black", INK, align="left")
    y0 = 700
    rrect(c, 60, y0 - 70, 1800, 140, 20, mix("#FFFFFF", INK2, 0.55), 1)
    for k in range(12):
        rrect(c, 90 + k * 150, y0 - 8, 90, 16, 6, "#FFFFFF", 1)
    rrect(c, 820, y0 - 230, 280, 120, 18, GREEN, 1, shadow=True)
    text_mid(c, "km 30", 960, y0 - 170, 70, "black", "#FFFFFF")
    line(c, 960, y0 - 110, 960, y0 - 70, GREEN, 1, 10)
    for x in (380, 1540):
        c.drawCircle(x, y0 + 210, 95, paint(AMBER, 1))
        text_mid(c, "?", x, y0 + 210, 140, "black", "#FFFFFF")
        arrow(c, 960 + (60 if x > 960 else -60), y0 + 210, x + (-110 if x > 960 else 110), y0 + 210, PURPLE, 1, 12, 34)
    rrect(c, 760, y0 + 150, 400, 120, 60, PURPLE, 1, shadow=True)
    text_mid(c, "a 7 km", 960, y0 + 210, 72, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_funcao_escondida", capa_escondida), ("capa_B_quanto_vem_na_conta", capa_energia),
                     ("capa_C_onde_ele_esta", capa_avenida)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
