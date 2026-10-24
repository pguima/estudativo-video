"""Capas — Conceito de Função, Episódio 3: o caminho de volta e as funções por partes (tema claro). 3 variações em
1280x720, sem gabarito.
A = recibo gigante + máquina rebobinando · B = relógio do estacionamento com a fração acendendo · C = duas etiquetas da margem
em duelo (dão o x × dão o y)."""
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
K = V.K


def fit(s, size, maxw, peso="black"):
    while V.ftext_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_recibo(c):
    background(c); selo_topo(c)
    s = "PAGOU R$ 30."
    V.ftext(c, s, 84, 300, fit(s, 150, 1000), "black", INK, align="left")
    s2 = "ANDOU QUANTO?"
    V.ftext(c, s2, 84, 460, fit(s2, 150, 1000), "black", AMBER, align="left")
    c.save(); c.translate(1150, 200); c.scale(1.6, 1.6)
    V.recibo(c, 0, 0, 1.0)
    c.restore()
    V.maquina(c, 520, 800, 1.0, entra=None, sai="R$ 30", prog=0.2, volta=True, s=1.15)
    V.selo(c, 1420, 880, 1.0, "P(30)? NÃO!", RED, -6, 56)


def capa_relogio(c):
    background(c); selo_topo(c, W / 2)
    s = "HORA OU FRAÇÃO?"
    V.ftext(c, s, W / 2, 300, fit(s, 160, 1760), "black", INK)
    V.relogio_estac(c, 200, 420, 150, 1.0, 1.0, bw=380, bh=180, acende=1.0, fracao_selo=0.0)
    cx, cy, r = 1640, 560, 150
    c.drawCircle(cx, cy, r, paint(PURPLE))
    c.drawCircle(cx, cy, r - 18, paint("#FFFFFF"))
    line(c, cx, cy, cx, cy - 110, INK, 1.0, 12)
    line(c, cx, cy, cx + 30, cy - 104, AMBER, 1.0, 10)
    c.drawCircle(cx, cy, 14, paint(INK))
    rrect(c, 0, 800, W, 280, 0, "#FFFFFF", 0.94)
    s3 = "5 MINUTOS = HORA INTEIRA?"
    V.ftext(c, s3, W / 2, 960, fit(s3, 110, 1760), "black", AMBER)


def capa_duelo(c):
    background(c)
    rrect(c, 0, 0, W / 2, H, 0, BLUE, 0.12)
    rrect(c, W / 2, 0, W / 2, H, 0, AMBER, 0.14)
    selo_topo(c, W / 2)
    V.ftext(c, "DÃO O x", W / 4, 420, 150, "black", BLUE)
    V.ftext(c, "calcule", W / 4, 540, 70, "bold", INK2)
    V.ftext(c, "DÃO O y", 3 * W / 4, 420, 150, "black", AMBER)
    V.ftext(c, "resolva", 3 * W / 4, 540, 70, "bold", INK2)
    c.drawCircle(W / 2, 400, 110, paint("#FFFFFF"))
    text_mid(c, "?", W / 2, 400, 170, "black", RED)
    rrect(c, 0, 760, W, 320, 0, "#FFFFFF", 0.94)
    s = "O ERRO QUE O ENEM COBRA"
    V.ftext(c, s, W / 2, 940, fit(s, 116, 1760), "black", INK)


if __name__ == "__main__":
    for nome, fn in (("capa_A_pagou_30_andou_quanto", capa_recibo), ("capa_B_hora_ou_fracao", capa_relogio),
                     ("capa_C_dao_x_dao_y", capa_duelo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
