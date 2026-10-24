"""Capas — Função Quadrática, Episódio 2: o vértice (tema claro). 3 variações em 1280x720.
A = o lançamento com o topo aceso e as duas fichas "QUANDO? → x" e "QUANTO? → y", título "x OU y DO VÉRTICE?";
B = a folha dobrada no eixo de simetria (as raízes se encontram), título "O VÉRTICE MORA NO MEIO";
C = as duas parábolas (sorri × triste) com "MÍNIMO OU MÁXIMO?" em faixa escura.
Nenhuma mostra gabarito (sem 3 s, 45 m, 30 peças, R$ 3 200 ou 4 m)."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO QUADRÁTICA · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=32, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=32, anchor="center", bounds=(0, 1920))


def capa_xy(c):
    background(c); selo_topo(c)
    pl = V.Plano(130, 300, 900, 640, (0, 6.4), (0, 50), 1, 10)
    pl.desenha(c, 1.0, nums=False, rx="t", ry="h")
    V.parab(c, pl, lambda x: -5 * x * x + 30 * x, 0, 6, PURPLE, 1.0, width=14)
    px, py = pl.P(3, 45)
    import math
    for k in range(12):
        ang = math.radians(k * 30)
        line(c, px + 30 * math.cos(ang), py + 30 * math.sin(ang), px + 80 * math.cos(ang), py + 80 * math.sin(ang), AMBER, 1, 8)
    c.drawCircle(px, py, 24, paint("#FFFFFF"))
    c.drawCircle(px, py, 18, paint(AMBER))
    ox, oy = pl.P(0, 0)
    line(c, px, py, px, oy, BLUE, 1, 7, dash=[16, 12])
    line(c, px, py, ox, py, GREEN, 1, 7, dash=[16, 12])
    s1, s2 = "x OU y", "DO VÉRTICE?"
    text(c, s1, 1460, 380, fit(s1, 170, 820), "black", INK)
    text(c, s2, 1460, 520, fit(s2, 120, 820), "black", PURPLE)
    V.chip(c, "QUANDO? → x", 1460, 700, BLUE, 1, 64)
    V.chip(c, "QUANTO? → y", 1460, 860, GREEN, 1, 64)


def capa_dobra(c):
    background(c); selo_topo(c, W / 2)
    s = "O VÉRTICE MORA NO MEIO"
    text(c, s, W / 2, 260, fit(s, 130, 1780), "black", INK)
    rrect(c, 360, 330, 1200, 660, 16, V.K.PAPEL, 1, shadow=True)
    pl = V.Plano(460, 380, 1000, 560, (-0.5, 4.5), (-3, 6), 1, 1)
    pl.desenha(c, 1.0, grade=False, nums=False)
    V.parab(c, pl, V.f286, -0.1, 2, BLUE, 1.0, width=12, so="esq", eixo=2)
    V.parab(c, pl, V.f286, 2, 4.1, BLUE, 0.35, width=12, eixo=2, dobra=0.35)
    V.eixo_sim(c, pl, 2, 1.0, rot=None)
    for x in (1, 3):
        px, py = pl.P(x, 0)
        c.drawCircle(px, py, 22, paint("#FFFFFF"))
        c.drawCircle(px, py, 17, paint(RED))
    p1, p3 = pl.P(1, 0), pl.P(3, 0)
    arrow(c, p3[0] + 10, p3[1] + 60, p3[0] - 120, p3[1] + 60, AMBER, 1, 8, 24)
    pill(c, "DOBRE AO MEIO", 1500, 420, PURPLE, size=44, anchor="right", bounds=(0, 1920))
    px, py = pl.P(2, -2)
    c.drawCircle(px, py, 26, paint("#FFFFFF"))
    c.drawCircle(px, py, 20, paint(PURPLE))
    pill(c, "vértice = ?", px + 40, py + 10, PURPLE, size=40, bounds=(0, 1920))


def capa_maxmin(c):
    background(c); selo_topo(c)
    V.carinha(c, 520, 560, 560, 1.0, True, rotulo=False)
    V.carinha(c, 1400, 560, 560, 1.0, False, rotulo=False)
    pill(c, "a > 0", 520, 340, GREEN, size=56, anchor="center", bounds=(0, 1920))
    pill(c, "a < 0", 1400, 340, RED, size=56, anchor="center", bounds=(0, 1920))
    rrect(c, 0, 850, W, 230, 0, INK)
    s = "MÍNIMO OU MÁXIMO?"
    text_mid(c, s, W / 2, 965, fit(s, 150, 1800), "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_x_ou_y_do_vertice", capa_xy), ("capa_B_mora_no_meio", capa_dobra),
                     ("capa_C_minimo_ou_maximo", capa_maxmin)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
