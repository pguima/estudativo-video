"""Capas — Equação do 2º Grau, Episódio 2: a fórmula de Bhaskara e o que o Δ revela (tema claro).
3 variações em 1280x720, sem gabarito: A = "b = −7" gigante e as duas perguntas do sinal (b² = ? · −b = ?);
B = as três portas do porteiro Δ; C = a fórmula inteira com a chave mestra."""
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
    s = "MATEMÁTICA ENEM · 2º GRAU · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_sinal(c):
    background(c); selo_topo(c)
    s = "O SINAL DO b"
    text(c, s, 90, 300, fit(s, 150, 1000), "black", INK, align="left")
    text(c, "DERRUBA O BHASKARA", 90, 420, fit("DERRUBA O BHASKARA", 92, 1000), "black", RED, align="left")
    shadow_rrect(c, 90, 520, 900, 300, 36, 1, 1.4)
    rrect(c, 90, 520, 900, 300, 36, "#FFFFFF")
    V.m(c, "b = -7", 540, 670, 170, hl={2: AMBER})
    for k, s2 in enumerate(("b^2 = ?", "-b = ?")):
        y = 330 + k * 330
        shadow_rrect(c, 1120, y, 700, 250, 30, 1, 1.2)
        rrect(c, 1120, y, 700, 250, 30, mix("#FFFFFF", AMBER, 0.12))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1120, y, 700, 250), 30, 30), paint(AMBER, 1.0, stroke=6))
        V.m(c, s2, 1470, y + 125, 130, hl={2: AMBER})
    text(c, "erre um e as raízes saem trocadas", 540, 960, 50, "extrabold", PURPLE)


def capa_portas(c):
    background(c); selo_topo(c, W / 2)
    s = "2, 1 OU NENHUMA RAIZ?"
    text(c, s, W / 2, 260, fit(s, 130, 1780), "black", INK)
    portas = [("Δ > 0", 2, GREEN, "x^2 - 5x + 4", "Δ = ?"), ("Δ = 0", 1, BLUE, "x^2 - 4x + 4", "Δ = ?"),
              ("Δ < 0", 0, RED, "x^2 + 2x + 5", "Δ = ?")]
    for k, (tit, n, col, eq, dl) in enumerate(portas):
        x = 420 + k * 540
        c.save(); c.translate(x, 640); c.scale(1.25, 1.25); c.translate(-x, -640)
        V.porta(c, x, 640, tit, n, 1.0, 1.0, col, eq, dl)
        c.restore()
    text(c, "o Δ é o porteiro", W / 2, 1040, 50, "extrabold", PURPLE)


def capa_chave(c):
    background(c); selo_topo(c, W / 2)
    s = "A CHAVE QUE ABRE"
    text(c, s, W / 2, 270, fit(s, 130, 1780), "black", INK)
    text(c, "QUALQUER EQUAÇÃO DO 2º GRAU", W / 2, 390, fit("QUALQUER EQUAÇÃO DO 2º GRAU", 84, 1780), "black", PURPLE)
    shadow_rrect(c, 360, 470, 1200, 320, 40, 1, 1.4)
    rrect(c, 360, 470, 1200, 320, 40, "#FFFFFF")
    V.m(c, V.FORMULA, W / 2, 630, 150, col=PURPLE)
    V.chave(c, 250, 930, 110, 1.0)
    text(c, "sem errar sinal", 1250, 960, 64, "black", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_sinal_do_b", capa_sinal), ("capa_B_porteiro_delta", capa_portas),
                     ("capa_C_chave_mestra", capa_chave)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
