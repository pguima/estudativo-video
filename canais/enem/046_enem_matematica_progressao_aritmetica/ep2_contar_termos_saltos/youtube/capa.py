"""Capas — Progressão Aritmética, Episódio 2: contar termos e saltos (tema claro). 3 variações em 1280x720, sem gabarito.
Formatos: A = duelo 56 × 57 com a fila de bolinhas embaixo; B = a rodovia ocupando a faixa de baixo, título no alto;
C = os três cartões x − r · x · x + r com o r riscado."""
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
    s = "MATEMÁTICA ENEM · PA · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_duelo(c):
    background(c); selo_topo(c, W / 2)
    s = "QUANTOS MÚLTIPLOS DE 7?"
    text(c, s, W / 2, 270, fit(s, 120, 1760), "black", INK)
    text(c, "de 105 até 497", W / 2, 360, 64, "extrabold", PURPLE)
    for k, (v, col) in enumerate((("56", AMBER), ("57", BLUE))):
        x = W / 2 + (k - 0.5) * 620
        shadow_rrect(c, x - 230, 420, 460, 300, 40, 1, 1.4)
        rrect(c, x - 230, 420, 460, 300, 40, "#FFFFFF")
        text_mid(c, v, x, 570, 220, "black", col)
    text_mid(c, "OU", W / 2, 570, 90, "black", GRAY)
    V.fila(c, 260, 1660, 900, [""] * 9, 1.0, r=40)
    V.selo(c, 1640, 470, 1.0, "ERRO POR UM?", RED, -6, 44)


def capa_rodovia(c):
    background(c); selo_topo(c)
    s1 = "7 POSTES."
    text(c, s1, 84, 290, 170, "black", INK, align="left")
    s2 = "QUANTOS VÃOS?"
    w = text_w(s2, "black", 130) + 80
    shadow_rrect(c, 70, 330, w, 170, 30, 1, 1.4)
    rrect(c, 70, 330, w, 170, 30, AMBER)
    text_mid(c, s2, 70 + w / 2, 415, 130, "black", "#FFFFFF")
    c.save(); c.translate(W / 2, 900); c.scale(1.5, 1.5)
    V.rodovia(c, -560, 560, 0, 1.0, 1.0, 6, rotulos=True, cor_vao=AMBER, txt_vao="?")
    c.restore()


def capa_trio(c):
    background(c); selo_topo(c, W / 2)
    s = "3 NÚMEROS EM PA"
    text(c, s, W / 2, 280, fit(s, 140, 1760), "black", INK)
    text(c, "em uma linha", W / 2, 380, 70, "extrabold", GREEN)
    c.save(); c.translate(W / 2, 660); c.scale(1.7, 1.7)
    V.trio(c, 0, 0, 1.0, 1.0, 64)
    c.restore()
    V.selo(c, 1600, 930, 1.0, "O r SOME!", RED, -5, 56)


if __name__ == "__main__":
    for nome, fn in (("capa_A_56_ou_57", capa_duelo), ("capa_B_postes_vaos", capa_rodovia),
                     ("capa_C_tres_em_pa", capa_trio)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
