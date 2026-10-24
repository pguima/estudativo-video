"""Capas — Progressão Geométrica, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos (sem repetir as revisões anteriores): A = três portas lado a lado (TERMO · SOMA · SOMA ∞) com ícones e a pergunta
"QUAL É A PERGUNTA?"; B = bola quicando ocupando a largura toda, "10 m" e "ATÉ PARAR: QUANTOS METROS?"; C = fundo escuro
com a dízima gigante "0,3636… = 36/100?" e o selo "VOCÊ CAI?". Nenhuma mostra gabarito.
Índices e potências só passam por V.ftext/V.fmid.
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
    while V.ftw(s, size, peso) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, cor=BLUE):
    s = "MATEMÁTICA ENEM · PROGRESSÃO GEOMÉTRICA · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_portas(c):
    background(c)
    selo_topo(c, W / 2)
    s = "QUAL É A PERGUNTA?"
    text(c, s, W / 2, 290, fit(s, 150, 1760), "black", INK)
    for k, (tit, ic, col) in enumerate((("TERMO", 0, BLUE), ("SOMA", 1, GREEN), ("SOMA ∞", 2, PURPLE))):
        x = 340 + k * 620
        rrect(c, x - 260, 370, 520, 640, 40, mix("#FFFFFF", col, 0.14), 1, shadow=True)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 260, 370, 520, 640), 40, 40), paint(col, 1, stroke=10))
        V.icone(c, ic, x, 610, 0.95, 1)
        V.ftext(c, tit, x, 900, 96, "black", col, 1, align="center")


def capa_bola(c):
    background(c)
    selo_topo(c)
    s = "ATÉ PARAR: QUANTOS METROS?"
    text(c, s, W / 2, 270, fit(s, 130, 1760), "black", PURPLE)
    ybase, x0 = 1000, 260
    line(c, 80, ybase, 1840, ybase, INK2, 1, 10)
    h, x = 560.0, x0
    p = skia.Path(); p.moveTo(x, ybase - h)
    for _ in range(6):
        p.lineTo(x + 60, ybase)
        h *= 0.6
        p.quadTo(x + 60 + 120, ybase - 2 * h, x + 300, ybase)
        x += 240
    c.drawPath(p, paint(BLUE, 1, stroke=14))
    c.drawCircle(x0, ybase - 560 - 40, 44, paint(AMBER))
    line(c, 160, ybase - 560, 160, ybase, INK2, 1, 6)
    V.ftext(c, "10 m", 140, ybase - 260, 64, "black", BLUE, 1, align="right")
    V.selo(c, 1440, 470, 1, "INFINITOS QUIQUES", GREEN, -6, 52)


def capa_dizima(c):
    rrect(c, 0, 0, W, H, 0, "#151A22", 1)
    selo_topo(c, W / 2, AMBER)
    V.ftext(c, "0,3636…", W / 2, 420, 230, "black", "#FFFFFF", 1, align="center")
    s = "= 36/100 ?"
    V.ftext(c, s, W / 2, 650, 170, "black", AMBER, 1, align="center")
    V.selo(c, W / 2, 870, 1, "VOCÊ CAI NESSA?", RED, -4, 70)


if __name__ == "__main__":
    for nome, fn in (("capa_A_qual_pergunta", capa_portas), ("capa_B_ate_parar", capa_bola),
                     ("capa_C_dizima_cai", capa_dizima)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
