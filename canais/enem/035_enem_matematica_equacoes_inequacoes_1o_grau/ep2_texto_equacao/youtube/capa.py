"""Capas — Equações e Inequações do 1º Grau, Episódio 2: do texto à equação (tema claro). 3 variações em 1280x720.
Formatos: A = pai e filho gigantes com "+4" e a pergunta "+4 PARA QUEM?" no alto; B = uma etiqueta de preço enorme
atravessando a capa ("x = ?"); C = tanque à direita com duas setas (em cima e embaixo) e o título à esquerda.
Nenhuma mostra gabarito."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · EQUAÇÕES · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_idades(c):
    background(c); selo_topo(c, W / 2)
    s = "+4 ANOS PARA QUEM?"
    text(c, s, W / 2, 290, fit(s, 150, 1760), "black", INK)
    V.boneco(c, 700, 960, 560, V.PAI_C, 1.0)
    V.boneco(c, 1150, 960, 360, V.FILHO_C, 1.0)
    K.chip(c, "+4", 900, 430, GREEN, 1.0, 72)
    K.chip(c, "+4", 1310, 600, GREEN, 1.0, 72)
    V.selo(c, 1580, 520, 1.0, "PAI = 3 × FILHO", PURPLE, -6, 46)
    V.selo(c, 330, 600, 1.0, "52 ANOS", INK, 5, 50)


def capa_etiqueta(c):
    background(c); selo_topo(c)
    s = "DO TEXTO À EQUAÇÃO"
    text(c, s, 84, 300, fit(s, 120, 1700), "black", INK, align="left")
    c.save(); c.rotate(-4)
    V.etiqueta(c, "x = idade do filho, em anos", 140, 430, 1.0, 92)
    c.restore()
    text(c, "o roteiro de 4 passos para montar QUALQUER problema", 84, 820, 50, "extrabold", PURPLE, align="left")
    text(c, "idades · partes · frações · misturas", 84, 900, 42, "bold", GRAY, align="left")


def capa_tanque(c):
    background(c); selo_topo(c)
    for k, s in enumerate(("ENTROU", "ÁLCOOL.", "E O TANQUE?")):
        text(c, s, 84, 330 + k * 170, 150, "black", (INK, V.ALCOOL, RED)[k], align="left")
    text(c, "a pegadinha da mistura no ENEM", 84, 900, 50, "extrabold", PURPLE, align="left")
    V.tanque(c, 1280, 220, 400, 720, 50, 20, 56, 1.0)
    arrow(c, 1760, 900, 1760, 440, V.ALCOOL, 1.0, 14, 40)
    text(c, "álcool", 1760, 990, 40, "black", V.ALCOOL)
    arrow(c, 1200, 900, 1200, 330, BLUE, 1.0, 14, 40)
    text(c, "total", 1200, 990, 40, "black", BLUE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_mais_quatro_para_quem", capa_idades), ("capa_B_etiqueta_do_x", capa_etiqueta),
                     ("capa_C_tanque_mistura", capa_tanque)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
