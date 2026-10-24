"""Capas — Escalas, Plantas e Mapas, Episódio 1: os três cálculos e a cadeia até o km (tema claro). 3 variações em 1280x720.
Formatos novos (sem o "texto à esquerda + painel à direita" das outras séries): A = título no alto e escada larga embaixo;
B = mapa ocupando a capa inteira, com faixa branca; C = três cartões lado a lado."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · ESCALAS · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_degrau(c):
    background(c); selo_topo(c, W / 2)
    s1 = "NÃO PARE NO MEIO"
    text(c, s1, W / 2, 300, fit(s1, 150, 1700), "black", INK)
    sz = 120
    w = text_w("DA ESCADA", "black", sz) + 80
    shadow_rrect(c, W / 2 - w / 2, 340, w, 150, 26, 1, 1.4)
    rrect(c, W / 2 - w / 2, 340, w, 150, 26, PURPLE)
    text_mid(c, "DA ESCADA", W / 2, 415, sz, "black", "#FFFFFF")
    V.cadeia(c, 360, 860, 1.0, (1, 1, 1), (1, 1), sw=400, sh=110, alt=200, size=90)
    V.selo(c, 1690, 560, 1.0, "ERRO × 100 000", RED, -6, 44)


def capa_mapa(c):
    background(c)
    V.mapa(c, -40, -40, W + 80, H + 80, 1.0, cidades=False)
    ya = (H + 80) * 0.55 - 40
    xa, xb = (W + 80) * 0.12 - 40, (W + 80) * 0.88 - 40
    line(c, xa, ya, xb, ya, RED, 1.0, 16)
    for x in (xa, xb):
        c.drawCircle(x, ya, 30, paint("#FFFFFF")); c.drawCircle(x, ya, 21, paint(RED))
    selo_topo(c)
    rrect(c, 0, 640, W, 330, 0, "#FFFFFF", 0.94)
    s = "6 cm NO MAPA. QUANTOS km?"
    text(c, s, W / 2, 780, fit(s, 130, 1760), "black", INK)
    text(c, "a escala do zero: os 3 cálculos que o ENEM cobra", W / 2, 900, 52, "extrabold", PURPLE)
    pill(c, "6 cm", W / 2, ya - 70, RED, size=56, anchor="center")


def capa_tres(c):
    background(c); selo_topo(c, W / 2)
    s = "OS 3 CÁLCULOS DE ESCALA"
    text(c, s, W / 2, 290, fit(s, 140, 1780), "black", INK)
    cards = [("ACHAR O REAL", "×", "mapa → mundo", GREEN), ("ACHAR O DESENHO", "÷", "mundo → mapa", AMBER),
             ("ACHAR A ESCALA", None, "desenho sobre real", PURPLE)]
    for k, (tit, op, sub, col) in enumerate(cards):
        x = 110 + k * 590
        shadow_rrect(c, x, 380, 520, 560, 34, 1, 1.4)
        rrect(c, x, 380, 520, 560, 34, "#FFFFFF")
        rrect(c, x, 380, 520, 100, 34, col, 0.16)
        text(c, tit, x + 260, 448, fit(tit, 46, 480), "black", col)
        if op:
            text_mid(c, op, x + 260, 680, 260, "black", col)
        else:
            K.fr(c, "desenho", "real", x + 260, 660, 84, INK, 1.0, num_col=BLUE, den_col=GREEN)
        text(c, sub, x + 260, 880, 40, "extrabold", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_meio_da_escada", capa_degrau), ("capa_B_mapa_quantos_km", capa_mapa),
                     ("capa_C_tres_calculos", capa_tres)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
