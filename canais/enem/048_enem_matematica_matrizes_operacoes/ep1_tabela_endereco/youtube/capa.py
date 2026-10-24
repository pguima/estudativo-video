"""Capas — Matrizes e Operações, Episódio 1: matriz é uma tabela com endereço (tema claro). 3 variações em 1280x720.
Formatos: A = sala de cinema em diagonal, com a poltrona acesa e o endereço a₂₃ = ?; B = duelo "−3 ou +3?" sobre a tabela
de gols (sem dizer qual leitura é a certa); C = a matriz simétrica gigante com a diagonal-espelho e uma casa apagada."""
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
    s = "MATEMÁTICA ENEM · MATRIZES · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_cinema(c):
    background(c); selo_topo(c)
    # sala grande à direita
    c.save(); c.translate(1170, 330); c.scale(1.5, 1.5); c.translate(-V.CIN["x"], -V.CIN["y"] + 60)
    V.cinema(c, 1.0, {(2, 3): (GREEN, 0.85)})
    c.restore()
    s = "FILEIRA OU POLTRONA?"
    text(c, s, 470, 330, fit(s, 96, 860), "black", INK)
    rrect(c, 120, 420, 700, 230, 34, "#FFFFFF", shadow=True)
    w = V.ind_w("a", "23", 150)
    V.ind(c, "a", "23", 470 - w / 2 - 110, 535, 150, GREEN, 1.0)
    text_mid(c, "= ?", 470 + w / 2 + 40, 535, 150, "black", INK)
    text(c, "matriz do zero: a tabela com endereço", 470, 760, 44, "extrabold", PURPLE)


def capa_duelo(c):
    background(c)
    V.matriz(c, V.G4, W / 2, 610, 210, 120, 0.13, 80)
    selo_topo(c, W / 2)
    s = "O MESMO TIME"
    text(c, s, W / 2, 260, fit(s, 110, 1600), "black", INK)
    for k, (v, col, rot) in enumerate((("−3", RED, -6), ("+3", AMBER, 6))):
        x = W / 2 + (-430 if k == 0 else 430)
        c.save(); c.translate(x, 560); c.rotate(rot)
        shadow_rrect(c, -260, -170, 520, 340, 40, 1, 1.4)
        rrect(c, -260, -170, 520, 340, 40, "#FFFFFF")
        rrect(c, -260, -170, 520, 340, 40, col, 0.12)
        text_mid(c, v, 0, -10, 230, "black", col)
        text(c, "linha − coluna" if k == 0 else "coluna − linha", 0, 130, 40, "extrabold", INK2)
        c.restore()
    text_mid(c, "?", W / 2, 560, 200, "black", PURPLE)
    rrect(c, 0, 880, W, 200, 0, PURPLE)
    s2 = "QUAL LEITURA ESTÁ CERTA?"
    text(c, s2, W / 2, 1010, fit(s2, 96, 1700), "black", "#FFFFFF")


def capa_espelho(c):
    background(c); selo_topo(c)
    S = [["0", "8", "5"], ["8", "0", "3"], [None, "3", "0"]]
    mx, my, cw, ch = 1330, 600, 220, 190
    x0, y0 = mx - 1.5 * cw, my - 1.5 * ch
    shadow_rrect(c, x0 - 40, y0 - 40, 3 * cw + 80, 3 * ch + 80, 40, 1, 1.4)
    rrect(c, x0 - 40, y0 - 40, 3 * cw + 80, 3 * ch + 80, 40, "#FFFFFF")
    for k in range(18):
        u0, u1 = k / 18, (k + 0.55) / 18
        line(c, x0 + 3 * cw * u0, y0 + 3 * ch * u0, x0 + 3 * cw * u1, y0 + 3 * ch * u1, PURPLE, 1.0, 10)
    V.matriz(c, S, mx, my, cw, ch, 1.0, 110, fundo={(0, 2): (AMBER, 0.35), (2, 0): (AMBER, 0.35)}, bcol=INK)
    text_mid(c, "?", x0 + 0.5 * cw, y0 + 2.5 * ch, 120, "black", AMBER)
    s = "A TABELA"
    text(c, s, 470, 360, 130, "black", INK)
    text(c, "DO ESPELHO", 470, 500, 130, "black", PURPLE)
    text(c, "qual número falta?", 470, 640, 56, "extrabold", INK2)
    pill(c, "matriz simétrica · do zero", 470, 760, BLUE, size=40, anchor="center")


if __name__ == "__main__":
    for nome, fn in (("capa_A_fileira_poltrona", capa_cinema), ("capa_B_menos3_mais3", capa_duelo),
                     ("capa_C_tabela_do_espelho", capa_espelho)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
