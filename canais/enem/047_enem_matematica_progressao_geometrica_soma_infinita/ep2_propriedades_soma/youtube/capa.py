"""Capas — Progressão Geométrica, Episódio 2: propriedades e soma finita (tema claro). 3 variações em 1280x720.
A = o tabuleiro de xadrez com 1 · 2 · 4 · 8 … e "QUANTOS GRÃOS?"; B = a árvore da corrente com "NO 6º DIA: 729 · AO TODO: ?";
C = as três fichas x/q · x · x·q com o q cancelado e "O q SOME".
Nenhuma mostra gabarito (1 092, 728, 9 e 18 quintilhões não aparecem)."""
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
    s = "MATEMÁTICA ENEM · PROGRESSÃO GEOMÉTRICA · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_tabuleiro(c):
    background(c); selo_topo(c)
    V.tabuleiro(c, 480, 600, 700, 1.0)
    s1, s2 = "QUANTOS", "GRÃOS?"
    text(c, s1, 1390, 380, fit(s1, 170, 900), "black", INK)
    text(c, s2, 1390, 560, fit(s2, 190, 900), "black", AMBER)
    s3 = "1 + 2 + 4 + 8 + …"
    sz = fit(s3, 80, 860)
    w = text_w(s3, "black", sz) + 80
    shadow_rrect(c, 1390 - w / 2, 640, w, 140, 30, 1, 1.4)
    rrect(c, 1390 - w / 2, 640, w, 140, 30, PURPLE)
    text_mid(c, s3, 1390, 710, sz, "black", "#FFFFFF")
    rrect(c, 0, 990, W, 90, 0, INK)
    text_mid(c, "a soma da PG numa linha", W / 2, 1035, 54, "black", "#FFFFFF")


def capa_corrente(c):
    background(c); selo_topo(c, W / 2)
    V.arvore(c, 0, 0, 1.0, x0=200, y0=300, larg=900, dy=118, dias=6.0, rotulo=False)
    for k, (rot, val, col) in enumerate((("NO 6º DIA", "729", "#FFD166"), ("AO TODO", "?", "#7CE0B0"))):
        y = 330 + k * 300
        shadow_rrect(c, 1240, y, 560, 240, 34, 1, 1.4)
        rrect(c, 1240, y, 560, 240, 34, "#10141A")
        text(c, rot, 1520, y + 70, 48, "black", "#9AA3B2")
        text_mid(c, val, 1520, y + 160, 120, "black", col)
    rrect(c, 0, 990, W, 90, 0, AMBER)
    text_mid(c, "termo ou soma?", W / 2, 1035, 58, "black", "#FFFFFF")


def capa_simetrica(c):
    background(c); selo_topo(c, W / 2)
    s = "3 NÚMEROS EM PG"
    text(c, s, W / 2, 290, fit(s, 150, 1700), "black", INK)
    xs = [480, 960, 1440]
    for x, s_ in zip(xs, ("x/q", "x", "x·q")):
        shadow_rrect(c, x - 200, 420, 400, 240, 36, 1, 1.4)
        rrect(c, x - 200, 420, 400, 240, 36, "#FFFFFF")
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 200, 420, 400, 240), 36, 36), paint(PURPLE, 1, stroke=6))
        V.K.mdraw(c, s_, x, 540, 110, PURPLE, 1.0, align="center")
    V.strike(c, 440, 640, 540, 560, 1.0, RED, 1)
    V.strike(c, 1490, 590, 1590, 510, 1.0, RED, 1)
    V.selo(c, W / 2, 800, 1.0, "O q SOME", RED, -4, 90)
    rrect(c, 0, 990, W, 90, 0, PURPLE)
    text_mid(c, "produto e soma em poucas linhas", W / 2, 1035, 54, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quantos_graos", capa_tabuleiro), ("capa_B_neste_dia_ao_todo", capa_corrente),
                     ("capa_C_o_q_some", capa_simetrica)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
