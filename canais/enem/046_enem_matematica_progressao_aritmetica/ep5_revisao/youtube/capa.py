"""Capas — Progressão Aritmética, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = o nome "progressão aritmética" riscado no topo e os três disfarces (palitos, teatro, depósito) em cartões
inclinados, com o título "PA SEM O NOME"; B = fundo escuro com a escada de 12 degraus e a pergunta "DO 1º AO 12º:
QUANTOS SALTOS?"; C = a fila de postes com "1 km · a cada 40 m" e "QUANTOS POSTES?". Nenhuma mostra gabarito.
Índices (a₁) só passam por V.ftext/V.fmid.
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
    s = "MATEMÁTICA ENEM · PROGRESSÃO ARITMÉTICA · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_sem_nome(c):
    background(c)
    selo_topo(c, W / 2)
    rrect(c, 360, 165, 1200, 170, 85, "#FFFFFF", 1, shadow=True)
    text_mid(c, "“progressão aritmética”", W / 2, 250, 80, "black", INK2)
    line(c, 440, 255, 1480, 255, RED, 1, 16)
    for k, (s, ic, col, rot) in enumerate((("palitos", 0, BLUE, -4), ("teatro", 4, PURPLE, 2), ("depósito", 1, GREEN, -2))):
        x = 360 + k * 600
        c.save(); c.translate(x, 600); c.rotate(rot)
        rrect(c, -260, -200, 520, 400, 40, mix("#F7F7F5", col, 0.18), 1, shadow=True)
        V.area_icone(c, ic, 0, -40, 0.85, 1)
        text_mid(c, s.upper(), 0, 135, 66, "black", col)
        c.restore()
    s = "PA SEM O NOME"
    text(c, s, W / 2, 1000, fit(s, 160, 1700), "black", INK)


def capa_saltos(c):
    c.drawRect(skia.Rect.MakeWH(W, H), paint("#16181D", 1))
    selo_topo(c)
    for k in range(12):
        h = 40 + k * 36
        x = 100 + k * 76
        rrect(c, x, 1000 - h, 70, h, 10, mix("#2A2D35", PURPLE, 0.25 + 0.05 * k), 1)
        rrect(c, x, 1000 - h, 70, 12, 5, PURPLE, 1)
    V.ftext(c, "1º", 135, 940, 44, "black", "#FFFFFF", 1, align="center")
    V.ftext(c, "12º", 100 + 11 * 76 + 35, 1000 - 40 - 36 * 11 - 30, 50, "black", "#FFFFFF", 1, align="center")
    text(c, "DO 1º AO 12º", 1480, 300, 80, "black", mix("#FFFFFF", PURPLE, 0.4))
    text(c, "QUANTOS", 1480, 450, 130, "black", "#FFFFFF")
    text(c, "SALTOS?", 1480, 600, 150, "black", AMBER)
    V.selo(c, 1480, 820, 1, "12 OU 11?", RED, -8, 80)


def capa_postes(c):
    background(c)
    selo_topo(c)
    s = "QUANTOS POSTES?"
    text(c, s, 90, 300, fit(s, 170, 1740), "black", INK, align="left")
    V.fit(c, "1 km de estrada · um a cada 40 m · nas duas pontas", 90, 410, 56, 1740, "bold", INK2, 1)
    y0 = 900
    line(c, 80, y0, 1840, y0, INK2, 1, 10)
    xs = [150, 450, 750, 1170, 1470, 1770]
    for x in xs:
        V.poste_ic_um(c, x, y0, 330, 1, INK2)
    text_mid(c, "…", 960, y0 - 140, 160, "black", GRAY)
    for k in (0, 1, 3, 4):
        p = skia.Path(); p.moveTo(xs[k] + 20, y0 + 30); p.quadTo((xs[k] + xs[k + 1]) / 2, y0 + 110, xs[k + 1] - 20, y0 + 30)
        c.drawPath(p, paint(AMBER, 1, stroke=10))
    V.ftext(c, "40 m", 300, y0 + 150, 56, "black", AMBER, 1, align="center")
    V.selo(c, 960, 640, 1, "25 OU 26?", AMBER, -6, 56)


if __name__ == "__main__":
    for nome, fn in (("capa_A_pa_sem_o_nome", capa_sem_nome), ("capa_B_quantos_saltos", capa_saltos),
                     ("capa_C_quantos_postes", capa_postes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
