"""Capas — Expressões Algébricas e Produtos Notáveis, Episódio 1 (tema claro). 3 variações em 1280x720.
Formatos novos: A = duelo em diagonal (duas frases, duas expressões); B = uma expressão gigante no centro com a caixinha;
C = os apertos de mão em arco sobre (2x + 3)(x − 4), com faixa de título embaixo."""
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
    s = "MATEMÁTICA ENEM · ÁLGEBRA · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_duelo(c):
    background(c)
    p = skia.Path(); p.moveTo(W * 0.58, 0); p.lineTo(W, 0); p.lineTo(W, H); p.lineTo(W * 0.42, H); p.close()
    c.drawPath(p, paint(mix("#FFFFFF", PURPLE, 0.14)))
    selo_topo(c)
    text(c, "“o dobro de um número,", 90, 300, 56, "black", INK, align="left")
    text(c, "aumentado de 3”", 90, 370, 56, "black", INK, align="left")
    K.expr(c, "2x + 3", 380, 560, 190, 1.0, cores={i: BLUE for i in range(3)})
    text(c, "“o dobro da SOMA", W - 90, 300, 56, "black", INK, align="right")
    text(c, "de um número com 3”", W - 90, 370, 56, "black", INK, align="right")
    K.expr(c, "2(x+3)", W - 420, 720, 190, 1.0, cores={0: PURPLE})
    shadow_rrect(c, W / 2 - 110, 420, 220, 220, 110, 1, 1.4)
    c.drawCircle(W / 2, 530, 110, paint(AMBER))
    text_mid(c, "≠?", W / 2, 530, 110, "black", "#FFFFFF")
    s = "A MESMA FRASE?"
    text(c, s, W / 2, 990, fit(s, 120, 1700), "black", RED)


def capa_caixinha(c):
    background(c); selo_topo(c, W / 2)
    s = "MENOS DOIS AO QUADRADO"
    text(c, s, W / 2, 260, fit(s, 110, 1760), "black", INK)
    K.expr(c, "-2^2 = ?", 760, 560, 240, 1.0, cores={0: RED, 2: AMBER})
    V.caixinha(c, 1520, 640, 190, 1.0, 1.0, "(−2)", 1.0)
    rrect(c, 0, 850, W, 230, 0, PURPLE)
    s2 = "O SINAL QUE DERRUBA NO ENEM"
    text(c, s2, W / 2, 990, fit(s2, 100, 1760), "black", "#FFFFFF")


def capa_apertos(c):
    background(c); selo_topo(c, W / 2)
    xs = V.parenteses(c, V.DIST_A, V.DIST_B, W / 2, 470, 200, 1.0)
    V.apertos(c, xs, 470, 200, [1, 1, 1, 1])
    rrect(c, 0, 800, W, 280, 0, INK)
    s = "4 APERTOS DE MÃO"
    text(c, s, W / 2, 935, fit(s, 130, 1700), "black", "#FFFFFF")
    text(c, "multiplicar polinômios sem perder termo", W / 2, 1025, 52, "extrabold", BANANA_TXT)


BANANA_TXT = "#F2C531"

if __name__ == "__main__":
    for nome, fn in (("capa_A_mesma_frase", capa_duelo), ("capa_B_menos_dois_ao_quadrado", capa_caixinha),
                     ("capa_C_apertos_de_mao", capa_apertos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
