"""Capas — Função Composta e Inversa, Episódio 4: quem tem inversa e o espelho na reta y = x (tema claro).
3 variações em 1280x720.
A = o gancho: "x² = 9" com as bolas 3 e −3 e "3 OU −3?" numa faixa âmbar (sem dizer qual a função escolhe);
B = o plano com 2ˣ, log₂ x e a diagonal tracejada, "O ESPELHO DA INVERSA";
C = a tabela com a célula do 5 destacada e "f⁻¹(5) = ?" (sem a resposta)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import math
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
    s = "MATEMÁTICA ENEM · FUNÇÃO INVERSA · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def bola(c, x, y, s, col, r):
    c.drawCircle(x, y, r, paint("#FFFFFF"))
    c.drawCircle(x, y, r, paint(col, 1, stroke=12))
    V.fmid(c, s, x, y, r * 0.95, "black", col, 1)


def capa_duvida(c):
    background(c); selo_topo(c, W / 2)
    V.K.expr(c, "x^2 = 9", W / 2, 330, 190, 1, cores={0: INK})
    bola(c, 300, 625, "3", BLUE, 130)
    bola(c, 1620, 625, "−3", BLUE, 130)
    s = "3 OU −3?"
    sz = fit(s, 170, 640)
    w = text_w(s, "black", sz) + 80
    shadow_rrect(c, W / 2 - w / 2, 530, w, 190, 30, 1, 1.4)
    rrect(c, W / 2 - w / 2, 530, w, 190, 30, AMBER)
    text_mid(c, s, W / 2, 625, sz, "black", "#FFFFFF")
    s2 = "QUEM TEM INVERSA?"
    text(c, s2, W / 2, 940, fit(s2, 120, 1700), "black", PURPLE)


def capa_espelho(c):
    background(c); selo_topo(c)
    pl = V.Plano(560, 610, 760, -2, 9)
    pl.fundo(c, 1, diag=1, grade=True)
    pl.curva(c, V.exp2, -2, math.log2(9), V.COL_F, 1, 1.0, 12)
    pl.curva(c, V.exp2, -2, math.log2(9), V.COL_I, 1, 1.0, 12, k=-1)
    for s, y, col in (("O ESPELHO", 470, INK), ("DA INVERSA", 630, PURPLE)):
        text(c, s, 1430, y, fit(s, 150, 900), "black", col)
    V.K.expr(c, "(a,b) → (b,a)", 1430, 800, 96, 1, cores={0: V.COL_F, 2: V.COL_I})


def capa_tabela(c):
    background(c); selo_topo(c, W / 2)
    V.tabela(c, 230, 300, V.TAB9[:2], 1, cw=250, rh=170, lw=300, cor_rot={1: V.COL_F}, hl={(1, 1): AMBER})
    V.K.expr(c, "f⁻¹(5) = ?", W / 2, 790, 170, 1, cores={0: V.COL_I})
    s = "PROCURE ONDE?"
    sz = fit(s, 90, 900)
    w = text_w(s, "black", sz) + 70
    rrect(c, W / 2 - w / 2, 925, w, 130, 26, AMBER)
    text_mid(c, s, W / 2, 990, sz, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_3_ou_menos_3", capa_duvida), ("capa_B_espelho_da_inversa", capa_espelho),
                     ("capa_C_procure_onde", capa_tabela)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
