"""Capas — Função Afim, Episódio 4: estudo do sinal, lucro e comparação de planos (tema claro). 3 variações em 1280x720.
A = o gráfico do ponto de equilíbrio (custo × receita, faixa vermelha e verde) com "QUANTAS PARA LUCRAR?";
B = a reta numérica com o zero de 2x − 6 (x = 3) e os dois lados "+ ou −" com "ONDE É POSITIVA?";
C = os dois aplicativos em duelo (A = 4 + 3x × B = 10 + 2x) com "QUAL APP COMPENSA?".
Nenhuma mostra gabarito (601, 5 km e 6 km não aparecem)."""
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
    s = "MATEMÁTICA ENEM · FUNÇÃO AFIM · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_lucro(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 70, 190, 1000, 820, 40, 1, 1.4)
    rrect(c, 70, 190, 1000, 820, 40, "#FFFFFF")
    R = lambda x: 25 * x
    Cx = lambda x: 2000 + 15 * x
    pl = V.Plano(170, 930, 760, 640, 340, 9000)
    line(c, pl.x0, pl.y0, pl.x0 + pl.w + 30, pl.y0, INK2, 1, 6)
    line(c, pl.x0, pl.y0, pl.x0, pl.y0 - pl.h - 30, INK2, 1, 6)
    pl.faixa(c, Cx, R, 0, 200, RED, 0.22)
    pl.faixa(c, R, Cx, 200, 340, GREEN, 0.22)
    pl.reta(c, Cx, 0, 340, BLUE, 1, 1, 12)
    pl.reta(c, R, 0, 340, PURPLE, 1, 1, 12)
    px, py = pl.P(200, 5000)
    c.drawCircle(px, py, 26, paint(AMBER, 1)); c.drawCircle(px, py, 26, paint(INK, 1, stroke=6))
    text(c, "PREJUÍZO", *pl.P(170, 900), 44, "black", RED)
    arrow(c, *pl.P(120, 1350), *pl.P(70, 1900), RED, 1, 6, 18)
    text(c, "LUCRO", pl.P(300, 0)[0], pl.P(0, 8900)[1], 52, "black", GREEN)
    s1, s2 = "QUANTAS", "PARA LUCRAR?"
    text(c, s1, 1480, 470, fit(s1, 170, 760), "black", INK)
    sz = fit(s2, 120, 740)
    w = text_w(s2, "black", sz) + 70
    shadow_rrect(c, 1480 - w / 2, 530, w, 190, 30, 1, 1.4)
    rrect(c, 1480 - w / 2, 530, w, 190, 30, GREEN)
    text_mid(c, s2, 1480, 625, sz, "black", "#FFFFFF")
    V.selo(c, 1480, 850, 1.0, "O EMPATE NÃO É LUCRO", AMBER, -5, 50)


def capa_sinal(c):
    background(c); selo_topo(c, W / 2)
    s = "ONDE É POSITIVA?"
    text(c, s, W / 2, 300, fit(s, 170, 1780), "black", INK)
    V.linha(c, [("f(x) = ", INK), ("2", PURPLE), ("x − 6", INK)], W / 2, 450, 110, 1.0)
    cy, w = 720, 1500
    rrect(c, W / 2 - w / 2, cy - 22, w, 44, 22, LIGHT, 1)
    line(c, W / 2 - w / 2 - 30, cy, W / 2 + w / 2 + 30, cy, INK2, 1, 6)
    c.drawCircle(W / 2, cy, 34, paint(INK, 1))
    text(c, "3", W / 2, cy + 110, 80, "black", INK)
    for x in (W / 2 - w / 4, W / 2 + w / 4):
        c.drawCircle(x, cy - 110, 66, paint(AMBER, 1))
        text_mid(c, "+ ou −", x, cy - 110, 40, "black", "#FFFFFF")
    rrect(c, 0, 900, W, 180, 0, PURPLE)
    text_mid(c, "quem manda no sinal é o a", W / 2, 990, 80, "black", "#FFFFFF")


def capa_apps(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL APP COMPENSA?"
    text(c, s, W / 2, 300, fit(s, 150, 1780), "black", INK)
    for k, (nome, lei, sub, col) in enumerate((("APP A", "4 + 3x", "larga na frente", AMBER),
                                                ("APP B", "10 + 2x", "km mais barato", BLUE))):
        x = 500 + k * 920
        shadow_rrect(c, x - 360, 400, 720, 470, 40, 1, 1.4)
        rrect(c, x - 360, 400, 720, 470, 40, "#FFFFFF")
        rrect(c, x - 360, 400, 720, 130, 40, col, 0.9)
        text_mid(c, nome, x, 465, 80, "black", "#FFFFFF")
        text_mid(c, lei, x, 650, 130, "black", col)
        text(c, sub, x, 810, 52, "extrabold", INK2)
    c.drawCircle(W / 2, 640, 95, paint(RED, 1))
    text_mid(c, "VS", W / 2, 640, 80, "black", "#FFFFFF")
    rrect(c, 0, 960, W, 120, 0, GREEN)
    text_mid(c, "a partir de quantos km?", W / 2, 1020, 64, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quantas_para_lucrar", capa_lucro), ("capa_B_onde_e_positiva", capa_sinal),
                     ("capa_C_qual_app_compensa", capa_apps)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
