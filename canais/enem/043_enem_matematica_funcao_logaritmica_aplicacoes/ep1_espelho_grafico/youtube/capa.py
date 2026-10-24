"""Capas — Função Logarítmica, Episódio 1: o espelho da exponencial (tema claro). 3 variações em 1280x720.
A = o treino: a curva P(t) = 20 · log t ocupando a base, "40 PONTOS: 100 h" e "60 PONTOS: ? h" (o 1 000 não aparece);
B = o espelho: 2ˣ e log₂ x dobrando sobre a reta y = x tracejada, com "O LOG É UM ESPELHO";
C = a escada do log (degraus iguais, cada vez mais compridos) com "POR QUE O LOG CANSA?".
Nenhuma mostra gabarito (a Q7 e o 0,2 não aparecem)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO LOGARÍTMICA · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_treino(c):
    background(c); selo_topo(c, W / 2)
    P = V.Plano(140, 520, 1640, 440, (0, 1100), (0, 70))
    P.eixos(c, 1.0, xt=(), yt=(), grade=False, rot=("h", "pts"))
    P.curva(c, 1.0, lambda x: 20 * __import__("math").log10(max(x, 1e-3)), BLUE, xa=1, xb=1100, width=16)
    P.ponto(c, 100, 40, BLUE, 1.0, None, r=18)
    P.ponto(c, 1000, 60, AMBER, 1.0, None, r=18)
    V.linha(c, [("40 PONTOS: ", INK), ("100 h", BLUE)], 540, 290, 96, 1.0)
    V.linha(c, [("60 PONTOS: ", INK), ("? h", AMBER)], 1380, 420, 96, 1.0)
    V.selo(c, 640, 800, 1.0, "200 h?", RED, -6, 60)
    s = "200 h?"
    w_ = text_w(s, "black", 60)
    strike(c, 640 - w_ / 2 - 20, 800, 640 + w_ / 2 + 20, 800, 1.0, RED)


def capa_espelho(c):
    background(c); selo_topo(c)
    P = V.Plano(1000, 200, 760, 760, (-2.5, 9), (-2.5, 9))
    P.eixos(c, 1.0, xt=(), yt=(), grade=False)
    line(c, P.px(-2.5), P.py(-2.5), P.px(9), P.py(9), GRAY, 1.0, 5, dash=(22, 14))
    P.curva(c, 1.0, lambda x: 2 ** x, PURPLE, width=14)
    P.curva(c, 1.0, lambda x: V.lg(2, max(x, 1e-4)), BLUE, xa=0.01, xb=9, width=14)
    for (a, b) in ((0, 1), (1, 2), (3, 8)):
        line(c, P.px(a), P.py(b), P.px(b), P.py(a), GREEN, 1.0, 4, dash=(10, 8))
        P.ponto(c, a, b, PURPLE, 1.0, None, r=14)
        P.ponto(c, b, a, BLUE, 1.0, None, r=14)
    for k, (s_, col) in enumerate((("O LOG", INK), ("É UM", INK), ("ESPELHO", PURPLE))):
        text(c, s_, 110, 400 + k * 190, fit(s_, 190, 820), "black", col, align="left")
    V.mx(c, "2^x", 1150, 280, 72, 1.0, PURPLE)
    V.lrow(c, [("log", "2", BLUE), ("m", "x", BLUE)], 1660, 760, 72, 1.0)


def capa_escada(c):
    background(c); selo_topo(c)
    s = "POR QUE O LOG CANSA?"
    text(c, s, 110, 300, fit(s, 140, 1700), "black", INK, align="left")
    x0, base, alt = 140, 960, 150
    larg = (110, 280, 620)
    rot = ("10", "100", "1 000")
    line(c, x0 - 30, base, x0 + sum(larg) + 700, base, INK2, 1.0, 6)
    x = x0
    for k, w_ in enumerate(larg):
        top = base - alt * (k + 1)
        rrect(c, x, top, w_, alt * (k + 1), 12, mix("#FFFFFF", PURPLE, 0.3 + 0.18 * k))
        text(c, rot[k], x + w_ - 14, top + 70, 54, "black", "#FFFFFF" if k else PURPLE, align="right")
        x += w_
    V.selo(c, 1550, 620, 1.0, "+1 CUSTA ×10", GREEN, -5, 64)


if __name__ == "__main__":
    for nome, fn in (("capa_A_40_pontos_60_pontos", capa_treino), ("capa_B_log_espelho", capa_espelho),
                     ("capa_C_por_que_o_log_cansa", capa_escada)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
