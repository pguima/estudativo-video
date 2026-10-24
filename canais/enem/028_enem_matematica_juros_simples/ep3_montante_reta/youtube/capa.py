"""Capas — Juros Simples, Episódio 3: o montante é uma reta (tema claro). 3 variações em 1280x720.
Formatos: A = título empilhado à esquerda e um gráfico grande à direita com dois pontos e o triângulo "taxa = ?";
B = a escada de degraus iguais atravessando a capa na diagonal, título no alto; C = duelo RETA × CURVA (simples × compostos)."""
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
    s = "MATEMÁTICA ENEM · JUROS SIMPLES · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_grafico(c):
    background(c); selo_topo(c)
    text(c, "UMA RETA.", 84, 330, 120, "black", INK, align="left")
    text(c, "DOIS PONTOS.", 84, 470, 120, "black", INK, align="left")
    text(c, "A TAXA SAI", 84, 640, 110, "black", PURPLE, align="left")
    text(c, "DAQUI.", 84, 770, 110, "black", PURPLE, align="left")
    shadow_rrect(c, 960, 190, 900, 800, 40, 1, 1.4)
    rrect(c, 960, 190, 900, 800, 40, "#FFFFFF")
    g = V.Graf(1080, 330, 680, 500, 10, 800, 1600)
    g.eixos(c, 1.0, (), (), 30, "meses", "R$", grid=False)
    V.reta_m(c, g, 0, 1000, 10, 1500, 1.0, 1.0, RED, 10)
    V.triangulo(c, g, 2, 1100, 8, 1400, 1.0, "tempo", "subida", PURPLE, 40)
    V.ponto(c, g, 2, 1100, 1.0, RED, 18)
    V.ponto(c, g, 8, 1400, 1.0, RED, 18)
    x, y = g.P(0, 1000)
    c.drawCircle(x, y, 40, paint(BLUE, 0.25)); V.ponto(c, g, 0, 1000, 1.0, BLUE, 18)
    V.selo(c, 1320, 925, 1.0, "TAXA = ?", GREEN, -6, 64)


def capa_escada(c):
    background(c); selo_topo(c, W / 2)
    s = "O MONTANTE SOBE UMA ESCADA"
    text(c, s, W / 2, 270, fit(s, 120, 1780), "black", INK)
    g = V.Graf(160, 380, 1500, 620, 6, 950, 1300)
    V.escada_juros(c, g, 1000, 50, 6, 1.0, 1.0, None, GREEN)
    for k in range(6):
        xb, yb = g.P(k + 1, 1000 + 50 * (k + 1))
        _, ya = g.P(k, 1000 + 50 * k)
        pill(c, "+ R$ 50", xb + 20, (ya + yb) / 2, GREEN, size=34, bounds=(0, 1920))
    V.reta_m(c, g, 0, 1000, 6, 1300, 1.0, 1.0, RED, 10)
    text(c, "degraus IGUAIS", 120, 1000, 64, "black", GREEN, align="left")


def capa_duelo(c):
    background(c); selo_topo(c, W / 2)
    s = "RETA OU CURVA?"
    text(c, s, W / 2, 280, fit(s, 140, 1780), "black", INK)
    for k, (nome, sub, col) in enumerate((("RETA", "juros SIMPLES", RED), ("CURVA", "juros COMPOSTOS", PURPLE))):
        x = 200 + k * 820
        shadow_rrect(c, x, 360, 700, 620, 40, 1, 1.4)
        rrect(c, x, 360, 700, 620, 40, "#FFFFFF")
        text(c, nome, x + 350, 450, 76, "black", col)
        g = V.Graf(x + 110, 500, 480, 300, 10, 900, 1700)
        g.eixos(c, 1.0, (), (), 24, "", "", grid=False)
        if k == 0:
            V.reta_m(c, g, 0, 1000, 10, 1500, 1.0, 1.0, col, 10)
        else:
            pts = [g.P(tt / 4, 1000 * 1.05 ** (tt / 4)) for tt in range(41)]
            p = skia.Path(); p.moveTo(*pts[0])
            for q in pts[1:]:
                p.lineTo(*q)
            c.drawPath(p, paint(col, 1.0, stroke=10))
        text(c, sub, x + 350, 920, 54, "extrabold", INK2)
    text_mid(c, "×", W / 2, 660, 140, "black", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_reta_dois_pontos", capa_grafico), ("capa_B_escada_degraus", capa_escada),
                     ("capa_C_reta_ou_curva", capa_duelo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
