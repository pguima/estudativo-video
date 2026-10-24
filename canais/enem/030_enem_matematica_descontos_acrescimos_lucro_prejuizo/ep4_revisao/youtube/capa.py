"""Capas — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 4: revisão, 9 pegadinhas e 5 questões inéditas (tema claro).
3 variações em 1280x720. Formatos: A = etiqueta de preço GIGANTE inclinada no centro com "DE QUÊ?" e, embaixo, as três bases
possíveis (custo · venda · etiqueta) como fichas; B = "20% + 10% = 30%?" num cupom fiscal à direita, com o selo PEGADINHA,
e o título empilhado à esquerda; C = a pizza do preço gigante à esquerda com a fatia do lucro destacada e a pergunta
"o lucro passa de 100% da venda?" à direita. Nenhuma mostra gabarito."""
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
    s = "MATEMÁTICA ENEM · DESCONTOS E LUCRO · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_etiqueta(c):
    background(c); selo_topo(c, W / 2)
    s = "PORCENTAGEM"
    text(c, s, W / 2, 250, fit(s, 120, 1700), "black", INK)
    c.save(); c.translate(W / 2 - 40, 560); c.scale(3.4, 3.4); c.rotate(-4)
    V.etiqueta(c, 1.0, "DE QUÊ?", AMBER, 300, 110)
    c.restore()
    for k, (s_, col) in enumerate((("do CUSTO?", BLUE), ("da VENDA?", GREEN), ("da ETIQUETA?", PURPLE))):
        V.chip(c, s_, 440 + k * 520, 890, col, 1.0, 56)
    text(c, "9 pegadinhas · 5 questões inéditas", W / 2, 1010, 50, "extrabold", INK2)


def capa_cupom(c):
    background(c); selo_topo(c)
    text(c, "VOCÊ", 84, 330, 150, "black", INK, align="left")
    text(c, "SOMOU OS", 84, 480, 150, "black", INK, align="left")
    text(c, "DESCONTOS?", 84, 630, fit("DESCONTOS?", 150, 960), "black", RED, align="left")
    text(c, "revisão com 9 pegadinhas", 84, 780, 56, "extrabold", INK2, align="left")
    text(c, "e 5 questões estilo ENEM", 84, 860, 56, "extrabold", GREEN, align="left")
    c.save(); c.translate(1500, 560); c.rotate(3)
    shadow_rrect(c, -300, -420, 600, 840, 16, 1, 1.6)
    rrect(c, -300, -420, 600, 840, 16, "#FFFFFF")
    text(c, "CUPOM FISCAL", 0, -330, 44, "black", INK2)
    for j in range(3):
        line(c, -250, -250 + j * 50, 250 - (j == 2) * 140, -250 + j * 50, LIGHT, 1.0, 10)
    text(c, "desconto  −20%", -250, -40, 52, "black", INK, align="left")
    text(c, "no caixa  −10%", -250, 50, 52, "black", INK, align="left")
    line(c, -250, 100, 250, 100, INK2, 1.0, 4)
    text(c, "total  −30% ?", -250, 200, 64, "black", RED, align="left")
    c.restore()
    V.selo(c, 1560, 860, 1.0, "PEGADINHA", AMBER, -8, 60)


def capa_pizza(c):
    background(c); selo_topo(c)
    c.save(); c.translate(520, 600); c.scale(3.2, 3.2)
    V.pizza(c, 1.0)
    c.restore()
    text(c, "O LUCRO", 1010, 360, 120, "black", INK, align="left")
    text(c, "É UMA FATIA", 1010, 500, 120, "black", GREEN, align="left")
    text(c, "da pizza ou do custo?", 1010, 640, 64, "extrabold", INK2, align="left")
    V.chip(c, "MARGEM × MARKUP", 1340, 790, PURPLE, 1.0, 54)
    text(c, "revisão completa · Matemática ENEM", 1010, 940, 46, "extrabold", BLUE, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_de_que", capa_etiqueta), ("capa_B_somou_descontos", capa_cupom),
                     ("capa_C_pizza_do_lucro", capa_pizza)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
