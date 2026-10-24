"""Capas — Função Modular, Episódio 3: módulo é distância (tema claro). 3 variações em 1280x720.
A = as barrinhas do gancho: "|−3| + |3| = 6" em cima e "|−3 + 3| = ?" embaixo, com "MESMAS BARRINHAS?";
B = o sinal que engana: o V cinza de |x| e o rótulo "y = |x − 3|" com duas setas (← ?  ? →) e "PARA ONDE VAI O V?";
C = o gráfico rebatido |x² − 4| com a régua horizontal e o contador "? cortes" ("QUANTAS SOLUÇÕES?").
Nenhuma mostra gabarito (o 0 do gancho, a direita do V e o "quatro" da Q6 não aparecem)."""
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
    while V.ftext_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO MODULAR · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_barrinhas(c):
    background(c); selo_topo(c, W / 2)
    rrect(c, 160, 200, 1600, 270, 36, "#FFFFFF", shadow=True)
    V.linha(c, [("|−3|", BLUE), (" + ", INK2), ("|3|", BLUE), (" = ", INK2), ("6", GREEN)], W / 2, 335, 170, 1.0)
    rrect(c, 160, 510, 1600, 270, 36, mix("#FFFFFF", AMBER, 0.22))
    V.linha(c, [("|−3 + 3|", PURPLE), (" = ", INK2), ("?", AMBER)], W / 2, 645, 170, 1.0)
    s = "MESMAS BARRINHAS?"
    text(c, s, W / 2, 940, fit(s, 120, 1700), "black", INK)


def capa_sinal(c):
    background(c); selo_topo(c)
    P = V.Plano(1010, 260, 790, 640, (-4.2, 4.2), (-0.6, 4.4))
    P.eixos(c, 1.0, xt=(), yt=(), grade=False)
    P.curva(c, 1.0, abs, GRAY, width=12)
    arrow(c, P.px(-0.4), P.py(-0.3) + 10, P.px(-3.4), P.py(-0.3) + 10, AMBER, 1.0, 14, 40)
    arrow(c, P.px(0.4), P.py(-0.3) + 10, P.px(3.4), P.py(-0.3) + 10, AMBER, 1.0, 14, 40)
    text(c, "?", P.px(-2.2), P.py(1.2), 120, "black", AMBER)
    text(c, "?", P.px(2.2), P.py(1.2), 120, "black", AMBER)
    for k, (s_, col) in enumerate((("PARA", INK), ("ONDE", INK), ("VAI O V?", PURPLE))):
        text(c, s_, 110, 360 + k * 170, fit(s_, 170, 840), "black", col, align="left")
    rrect(c, 110, 830, 820, 140, 30, mix("#FFFFFF", BLUE, 0.14))
    V.linha(c, [("y = |x − 3|", BLUE)], 520, 900, 90, 1.0)


def capa_cortes(c):
    background(c); selo_topo(c)
    s = "QUANTAS SOLUÇÕES?"
    text(c, s, 110, 300, fit(s, 130, 1700), "black", INK, align="left")
    P = V.Plano(140, 390, 1100, 580, (-3.3, 3.3), (-0.4, 6.0))
    P.eixos(c, 1.0, xt=(), yt=(), grade=False)
    P.curva(c, 1.0, V.g, PURPLE, width=14)
    line(c, P.x0 - 20, P.py(3), P.x0 + P.w + 20, P.py(3), AMBER, 1.0, 10)
    V.linha(c, [("|x² − 4| = 3", PURPLE)], 1530, 560, 84, 1.0)
    rrect(c, 1380, 680, 300, 260, 36, mix("#FFFFFF", GREEN, 0.16))
    text_mid(c, "?", 1530, 790, 150, "black", GREEN)
    text(c, "cortes", 1530, 905, 40, "black", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_mesmas_barrinhas", capa_barrinhas), ("capa_B_para_onde_vai_o_v", capa_sinal),
                     ("capa_C_quantas_solucoes", capa_cortes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
