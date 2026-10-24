"""Capas — Comparação de Propostas, Episódio 4: ponto de equilíbrio de um negócio e meta de lucro (tema claro).
3 variações em 1280x720. Formatos: A = o MURO do custo fixo pela metade à direita, tijolinho de R$ 20 subindo, e a
pergunta "QUANTAS PEÇAS PARA EMPATAR?" à esquerda; B = a conta errada gigante "6.000 ÷ 35" riscada, centralizada, com
"divida pela MARGEM" embaixo; C = dois placares lado a lado (PREJUÍZO vermelho → LUCRO verde) com "?" entre eles e o
título "VENDER QUANTO?" em cima."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · COMPARAÇÃO DE PROPOSTAS · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_muro(c):
    background(c); selo_topo(c)
    text(c, "QUANTAS", 84, 340, 140, "black", INK, align="left")
    text(c, "PEÇAS PARA", 84, 490, 140, "black", INK, align="left")
    text(c, "EMPATAR?", 84, 640, 150, "black", GREEN, align="left")
    text(c, "custo fixo R$ 6.000 · preço R$ 35", 84, 790, 52, "extrabold", INK2, align="left")
    V.muro(c, 1180, 300, 640, 560, 66, 1.0, cols=12, rows=10, rotulo="")
    text(c, "CUSTO FIXO", 1500, 940, 52, "black", INK2)
    c.drawRect(skia.Rect.MakeXYWH(960, 200, 190, 90), paint(V.BRICK))
    text_mid(c, "R$ 20", 1055, 245, 54, "black", "#FFFFFF")
    arrow(c, 1055, 300, 1250, 600, V.BRICK, 1.0, 10, 30)


def capa_preco(c):
    background(c); selo_topo(c, W / 2)
    s = "6.000 ÷ 35 ?"
    sz = fit(s, 230, 1600)
    text_mid(c, s, W / 2, 400, sz, "black", AMBER)
    tw = text_w(s, "black", sz)
    line(c, W / 2 - tw / 2 - 30, 430, W / 2 + tw / 2 + 30, 370, RED, 1.0, 22)
    s2 = "NÃO DIVIDA PELO PREÇO"
    text(c, s2, W / 2, 700, fit(s2, 120, 1700), "black", RED)
    pill(c, "divida pela MARGEM", W / 2, 860, GREEN, size=64, anchor="center", bounds=(0, 1920))


def capa_placar(c):
    background(c); selo_topo(c)
    s = "VENDER QUANTO?"
    text(c, s, 84, 330, fit(s, 170, 1750), "black", INK, align="left")
    for k, (rot, col) in enumerate((("PREJUÍZO", RED), ("LUCRO", GREEN))):
        x = 480 + k * 960
        rrect(c, x - 330, 440, 660, 480, 44, "#FFFFFF", shadow=True)
        text(c, "PEÇAS VENDIDAS", x, 530, 44, "black", GRAY)
        text_mid(c, "???", x, 650, 150, "black", INK)
        rrect(c, x - 290, 770, 580, 120, 28, col)
        text_mid(c, rot, x, 830, 72, "black", "#FFFFFF")
    arrow(c, 860, 680, 1080, 680, INK2, 1.0, 14, 40)
    text(c, "+1 peça", 970, 630, 44, "black", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_quantas_pecas", capa_muro), ("capa_B_nao_divida_pelo_preco", capa_preco),
                     ("capa_C_vender_quanto", capa_placar)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
