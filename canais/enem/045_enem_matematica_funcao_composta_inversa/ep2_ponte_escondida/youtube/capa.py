"""Capas — Função Composta e Função Inversa, Episódio 2: composição em contexto e a função escondida (tema claro).
3 variações em 1280x720, sem gabarito. A = as três caixas com a ponte riscada; B = a caixa fechada gigante;
C = o balão ocupando a esquerda, com a pergunta do gancho."""
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
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO COMPOSTA · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_ponte(c):
    background(c); selo_topo(c, W / 2)
    s = "A PONTE SOME"
    text(c, s, W / 2, 330, fit(s, 190, 1700), "black", INK)
    xs = (330, 960, 1590)
    for x, tit, col in zip(xs, ("TEMPO", "ALTITUDE", "TEMPERATURA"), (BLUE, AMBER, PURPLE)):
        w, h = 520, 220
        shadow_rrect(c, x - w / 2, 560 - h / 2, w, h, 34, 1, 1.4)
        rrect(c, x - w / 2, 560 - h / 2, w, h, 34, mix("#FFFFFF", col, 0.14))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - w / 2, 560 - h / 2, w, h), 34, 34), paint(col, 1, stroke=8))
        text_mid(c, tit, x, 560, fit(tit, 72, w - 50), "black", col)
    line(c, 760, 480, 1160, 640, RED, 1.0, 16)
    line(c, 760, 640, 1160, 480, RED, 1.0, 16)
    text(c, "duas fórmulas viram UMA", W / 2, 860, 70, "black", GREEN)
    text(c, "função composta no ENEM", W / 2, 960, 46, "extrabold", INK2)


def capa_caixa(c):
    background(c); selo_topo(c)
    s1 = "A FUNÇÃO"
    text(c, s1, 520, 380, fit(s1, 150, 900), "black", INK)
    s2 = "ESCONDIDA"
    text(c, s2, 520, 540, fit(s2, 150, 900), "black", PURPLE)
    K.expr(c, "f(?) = 8x - 1", 520, 720, 96, 1.0, cores={0: PURPLE})
    text(c, "quem é a de dentro?", 520, 860, 56, "extrabold", INK2)
    V.caixa_q(c, 1430, 560, 1.0, 0.0, w=620, h=420)


def capa_balao(c):
    background(c); selo_topo(c)
    V.balao(c, 470, 400, 210, 1.0)
    pill(c, "0,2 km por minuto", 470, 980, BLUE, size=44, anchor="center")
    s = "10 MINUTOS DEPOIS"
    text(c, s, 1320, 330, fit(s, 110, 1000), "black", INK)
    text_mid(c, "? °C", 1320, 540, 240, "black", AMBER)
    text(c, "−6 °C a cada km de altura", 1320, 770, 52, "extrabold", PURPLE)
    text(c, "1 fórmula só, sem altitude", 1320, 880, 56, "black", GREEN)


if __name__ == "__main__":
    for nome, fn in (("capa_A_a_ponte_some", capa_ponte), ("capa_B_funcao_escondida", capa_caixa),
                     ("capa_C_balao_10_minutos", capa_balao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
