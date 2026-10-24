"""Capas — Função Quadrática, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = "x OU y?" gigante à esquerda e a parábola triste à direita, com as linhas tracejadas do vértice até os dois
eixos (pílulas "x do vértice" e "y do vértice"); B = as duas parábolas (sorrindo e triste) lado a lado, com a pergunta
"a > 0 TEM MÁXIMO?" em faixa âmbar; C = "−b ÷ 2a" num cartão central cercado pelos 5 ícones das questões, com
"5 QUESTÕES · 1 FÓRMULA". Nenhuma mostra gabarito.
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
    s = "MATEMÁTICA ENEM · FUNÇÃO QUADRÁTICA · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_x_ou_y(c):
    background(c)
    selo_topo(c)
    text(c, "x OU y", 84, 400, fit("x OU y", 230, 820), "black", INK, align="left")
    text(c, "DO VÉRTICE?", 84, 560, fit("DO VÉRTICE?", 140, 820), "black", RED, align="left")
    pill(c, "o ENEM põe os dois nas alternativas", 84, 700, AMBER, size=44, bounds=(0, 1920))
    pill(c, "9 pegadinhas + 5 questões", 84, 900, GREEN, size=48, bounds=(0, 1920))
    x0, yb = 1000, 860
    arrow(c, x0 - 30, yb, 1860, yb, INK2, 1, 6, 18)
    arrow(c, x0, yb + 30, x0, 200, INK2, 1, 6, 18)
    V.arco(c, x0 + 90, yb, 700, 300, PURPLE, 1, 14)
    xv, yv = x0 + 440, yb - 300
    line(c, xv, yv, xv, yb, BLUE, 1, 8, dash=[18, 12])
    line(c, xv, yv, x0, yv, RED, 1, 8, dash=[18, 12])
    c.drawCircle(xv, yv, 26, paint(INK, 1))
    pill(c, "x?", xv, yb + 70, BLUE, size=60, anchor="center", bounds=(0, 1920))
    pill(c, "y?", x0 + 40, yv - 80, RED, size=60, bounds=(0, 1920))


def capa_maximo(c):
    background(c)
    selo_topo(c, W / 2)
    c.save(); c.translate(560, 520); c.scale(1.7, 1.7)
    V.arco(c, -150, -60, 300, 140, GREEN, 1, 9, triste=False)
    c.restore()
    c.save(); c.translate(1360, 560); c.scale(1.7, 1.7)
    V.arco(c, -150, 60, 300, 140, PURPLE, 1, 9, triste=True)
    c.restore()
    text_mid(c, "a > 0", 560, 300, 90, "black", GREEN)
    text_mid(c, "a < 0", 1360, 300, 90, "black", PURPLE)
    text_mid(c, "?", 560, 560, 120, "black", GREEN)
    text_mid(c, "?", 1360, 520, 120, "black", PURPLE)
    rrect(c, 0, 820, W, 200, 0, mix("#FFFFFF", AMBER, 0.85))
    s = "a > 0 TEM MÁXIMO?"
    text(c, s, W / 2, 955, fit(s, 130, 1700), "black", INK)


def capa_formula(c):
    background(c)
    selo_topo(c, W / 2)
    s = "5 QUESTÕES · 1 FÓRMULA"
    text(c, s, W / 2, 280, fit(s, 120, 1700), "black", INK)
    rrect(c, W / 2 - 420, 420, 840, 300, 44, mix("#FFFFFF", PURPLE, 0.14), 1, shadow=True)
    V.fmid(c, "xV = −b ÷ 2a", W / 2, 570, 130, "black", PURPLE, 1)
    for k, (x, y) in enumerate(((240, 470), (240, 800), (1680, 470), (1680, 800), (W / 2, 900))):
        V.area_icone(c, k, x, y, 0.62 if k < 4 else 0.45, 1)


if __name__ == "__main__":
    for nome, fn in (("capa_A_x_ou_y_do_vertice", capa_x_ou_y), ("capa_B_a_positivo_tem_maximo", capa_maximo),
                     ("capa_C_cinco_questoes_uma_formula", capa_formula)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
