"""Capas — Determinantes e Sistemas Lineares, Episódio 3: a regra de Cramer (tema claro). 3 variações em 1280x720.
Formatos: A = a lanchonete com três cartões e só a SALADA em destaque, "SÓ O PREÇO DA SALADA?" e "2 determinantes";
B = a TROCA DE FIGURINHA: a matriz com a coluna de x saindo e a coluna das respostas entrando, "TROCA DE FIGURINHA";
C = a fração D_x sobre D com o D "no chão" gigante e o selo "QUEM FICA EMBAIXO?" (sem resposta de questão)."""
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
    s = "MATEMÁTICA ENEM · DETERMINANTES · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_salada(c):
    background(c); selo_topo(c, W / 2)
    s = "SÓ O PREÇO DA SALADA?"
    text(c, s, W / 2, 270, fit(s, 130, 1760), "black", INK)
    for k, (nome, col) in enumerate((("SUCO", GRAY), ("SANDUÍCHE", GRAY), ("SALADA", PURPLE))):
        x = 330 + k * 450
        c.save(); c.translate(x + 150, 560); c.scale(1.15, 1.15); c.translate(-(x + 150), -560)
        V.item_card(c, x, 410, nome, "R$ ?", col, 1.0 if k == 2 else 0.45, 1.0 if k == 2 else 0)
        c.restore()
    rrect(c, 0, 880, W, 200, 0, PURPLE)
    V.linha(c, [("2 determinantes: ", "#FFFFFF"), ("D", "#FFFFFF"), (" e ", "#FFFFFF"), ("D_z", "#FFFFFF")], W / 2,
            975, 84, 1.0)


def capa_troca(c):
    background(c); selo_topo(c)
    text(c, "TROCA DE", 80, 380, 140, "black", INK, align="left")
    text(c, "FIGURINHA", 80, 530, 140, "black", PURPLE, align="left")
    text(c, "a regra de Cramer em 1 imagem", 84, 640, 50, "extrabold", INK2, align="left")
    rrect(c, 1020, 220, 820, 700, 50, "#FFFFFF", shadow=True)
    V.troca(c, [["a", "b"], ["c", "d"]], ["e", "f"], 0, 1340, 500, 180, 160, 1.0, 0.28, 86)
    V.linha(c, [("D_x", PURPLE)], 1340, 300, 80, 1.0)
    text(c, "sai x · entram as respostas", 1430, 860, 40, "black", AMBER)


def capa_chao(c):
    background(c); selo_topo(c)
    rrect(c, 120, 220, 860, 760, 50, "#FFFFFF", shadow=True)
    V.linha(c, [("x =", INK)], 190, 600, 120, 1.0, align="left")
    V.chao(c, "D_x", "D", 640, 600, 150, 1.0)
    text(c, "QUEM FICA", 1440, 430, 120, "black", INK)
    text(c, "EMBAIXO?", 1440, 580, 120, "black", RED)
    c.save(); c.translate(1440, 760); c.rotate(-4)
    rrect(c, -360, -60, 720, 120, 30, AMBER)
    text_mid(c, "REGRA DE CRAMER", 0, 0, 58, "black", "#FFFFFF")
    c.restore()


if __name__ == "__main__":
    for nome, fn in (("capa_A_so_a_salada", capa_salada), ("capa_B_troca_de_figurinha", capa_troca),
                     ("capa_C_quem_fica_embaixo", capa_chao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
