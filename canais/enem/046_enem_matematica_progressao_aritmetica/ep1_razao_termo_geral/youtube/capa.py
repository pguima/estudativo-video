"""Capas — Progressão Aritmética, Episódio 1: a razão e o "n − 1" (tema claro). 3 variações em 1280x720, sem gabarito.
Formatos: A = escada gigante na diagonal com o bonequinho no topo e o contador de saltos "?";
B = faixa roxa cheia com a fórmula enorme e o "(n − 1)" circulado; C = figura de palitos ocupando a largura, com a pergunta."""
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
    while V.ftext_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, cor=BLUE):
    s = "MATEMÁTICA ENEM · PA · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_escada(c):
    background(c); selo_topo(c)
    V.escadaria(c, 80, 1020, 12, 112, 52, 1.0, acesos=[1] * 12, rotulos=["1º"] + [""] * 10 + ["12º"], rot_size=34,
                rot_col=PURPLE)
    x, y = V.degrau_xy(80, 1020, 112, 52, 12)
    V.boneco(c, x, y, 90, 1.0)
    s1 = "DO 1º AO 12º DEGRAU:"
    V.ftext(c, s1, 84, 250, fit(s1, 96, 1100), "black", INK, align="left")
    s2 = "QUANTOS SALTOS?"
    V.ftext(c, s2, 84, 370, fit(s2, 120, 1100), "black", AMBER, align="left")
    shadow_rrect(c, 1500, 160, 330, 260, 30, 1, 1.4)
    rrect(c, 1500, 160, 330, 260, 30, "#FFFFFF")
    text_mid(c, "?", 1665, 270, 170, "black", AMBER)
    text(c, "saltos", 1665, 395, 40, "black", INK2)


def capa_formula(c):
    background(c)
    rrect(c, 0, 230, W, 560, 0, PURPLE)
    selo_topo(c, W / 2, PURPLE)
    s = "aₙ = a₁ + (n − 1) · r"
    sz = fit(s, 190, 1700)
    V.ftext(c, s, W / 2, 570, sz, "black", "#FFFFFF")
    wtot = V.ftext_w(s, "black", sz)
    x0 = W / 2 - wtot / 2 + V.ftext_w("aₙ = a₁ + ", "black", sz)
    wp = V.ftext_w("(n − 1)", "black", sz)
    c.drawOval(skia.Rect.MakeLTRB(x0 - 30, 570 - sz * 0.95, x0 + wp + 30, 570 + sz * 0.3), paint(AMBER, 1.0, stroke=14))
    s2 = "POR QUE O MENOS UM?"
    V.ftext(c, s2, W / 2, 940, fit(s2, 110, 1700), "black", INK)


def capa_palitos(c):
    background(c); selo_topo(c, W / 2, GREEN)
    s = "QUANTOS PALITOS NA FIGURA 50?"
    V.ftext(c, s, W / 2, 260, fit(s, 120, 1760), "black", INK)
    V.palitos_quad(c, 170, 420, 6, 230, 1.0, hl=1.0)
    text(c, "…", 1700, 600, 120, "black", GRAY)
    pill(c, "sem desenhar as 49 anteriores", W / 2, 960, GREEN, size=48, anchor="center")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quantos_saltos", capa_escada), ("capa_B_por_que_menos_um", capa_formula),
                     ("capa_C_palitos_figura_50", capa_palitos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
