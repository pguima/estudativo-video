"""Capas — Taxas Equivalentes e Inflação, Episódio 3: inflação e poder de compra (tema claro). 3 variações em 1280x720.
Formatos: A = a nota de R$ 100 à direita, meio apagada, e a pergunta "PREÇOS DOBRARAM. VOCÊ PERDEU QUANTO?" à esquerda,
com "100%?" num selo âmbar; B = o carrinho de 100 itens no centro, com o preço R$ 1,00 → R$ 1,25 e o título
"QUANTO SOBRA NO CARRINHO?" em cima; C = duas escadas rolantes (rápida e lenta, as duas subindo) ocupando a largura e o
título "A INFLAÇÃO CAIU. E O PREÇO?"."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · TAXAS E INFLAÇÃO · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_nota(c):
    background(c); selo_topo(c)
    text(c, "PREÇOS", 84, 330, 150, "black", INK, align="left")
    text(c, "DOBRARAM.", 84, 480, 150, "black", RED, align="left")
    text(c, "Você perdeu", 84, 640, 90, "extrabold", INK2, align="left")
    text(c, "quanto?", 84, 760, 90, "extrabold", BLUE, align="left")
    c.save(); c.translate(1480, 600); c.rotate(-8); c.scale(1.75, 1.75)
    V.nota(c, 0, 0, 0.75, 380, 190)
    c.restore()
    V.selo(c, 1480, 880, 1.0, "PERDEU 100%?", AMBER, -5, 64)


def capa_carrinho(c):
    background(c); selo_topo(c, W / 2)
    s = "QUANTO SOBRA NO CARRINHO?"
    text(c, s, W / 2, 270, fit(s, 120, 1760), "black", INK)
    V.carrinho(c, 1010, 650, 1.0, sai=0.0, preco_novo="R$ 1,25", troca=1.0, s=1.25)
    pill(c, "+ 25%", 1650, 560, RED, size=72, anchor="center", bounds=(0, 1920))
    text(c, "100 itens", 1650, 700, 56, "black", INK2)
    text(c, "R$ 100 no bolso", 1650, 770, 44, "bold", GRAY)


def capa_escada(c):
    background(c); selo_topo(c)
    text(c, "A INFLAÇÃO CAIU.", 84, 320, 120, "black", INK, align="left")
    text(c, "E O PREÇO?", 84, 460, 130, "black", AMBER, align="left")
    V.escada(c, 140, 640, 700, 300, 1.0, 0.0, vel=2.0, n=10)
    V.escada(c, 1060, 760, 700, 180, 1.0, 1.3, vel=1.0, n=10)
    pill(c, "8%", 330, 640, PURPLE, size=64, anchor="center", bounds=(0, 1920))
    pill(c, "4%", 1250, 700, PURPLE, size=64, anchor="center", bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_preco_dobrou", capa_nota), ("capa_B_carrinho", capa_carrinho),
                     ("capa_C_escada_rolante", capa_escada)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
