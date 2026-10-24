"""Capas — Juros Simples, Episódio 1: o vocabulário do dinheiro e a fórmula J = C · i · t (tema claro). 3 variações em 1280x720.
Formatos: A = a armadilha da vírgula gigante no centro (1,5% = 0,15?) com carimbo; B = pilha de notas e fileira de moedas
iguais ocupando a base, título no alto; C = duelo J × M em dois cartões grandes."""
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
    s = "MATEMÁTICA ENEM · JUROS SIMPLES · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_virgula(c):
    background(c); selo_topo(c, W / 2)
    s = "A VÍRGULA QUE DERRUBA"
    text(c, s, W / 2, 270, fit(s, 130, 1750), "black", INK)
    shadow_rrect(c, 260, 360, 1400, 400, 40, 1, 1.4)
    rrect(c, 260, 360, 1400, 400, 40, "#FFFFFF")
    V.linha(c, [("1,5%", PURPLE), ("  =  ", INK), ("0,15", RED), ("?", AMBER)], W / 2, 560, 230, 1.0)
    V.selo(c, 1560, 760, 1.0, "ERRADO!", RED, -10, 70)
    text(c, "juros ou montante? a fórmula J = C · i · t do zero", W / 2, 920, 52, "extrabold", PURPLE)


def capa_aluguel(c):
    background(c); selo_topo(c)
    text(c, "JUROS =", 84, 300, 120, "black", INK, align="left")
    text(c, "ALUGUEL DO DINHEIRO", 84, 440, fit("ALUGUEL DO DINHEIRO", 150, 1750), "black", BLUE, align="left")
    rrect(c, 0, 640, W, 440, 0, "#EAF4EC")
    V.pilha(c, 280, 960, 1.0, None, 8, 320, 90)
    for k in range(6):
        V.moeda(c, 640 + k * 210, 880, 82, 1.0, "30")
    V.linha(c, [("J = C · i · t", PURPLE), ("   ·   o aluguel é sempre o MESMO", GREEN)], 84, 565, 56, 1.0, align="left")


def capa_duelo(c):
    background(c); selo_topo(c, W / 2)
    s = "JUROS OU MONTANTE?"
    text(c, s, W / 2, 280, fit(s, 140, 1780), "black", INK)
    for k, (L, nome, sub, col) in enumerate((("J", "JUROS", "quanto RENDEU", GREEN), ("M", "MONTANTE", "quanto TERÁ", RED))):
        x = 200 + k * 820
        shadow_rrect(c, x, 360, 700, 600, 40, 1, 1.4)
        rrect(c, x, 360, 700, 600, 40, "#FFFFFF")
        rrect(c, x, 360, 700, 110, 40, col, 0.16)
        text(c, nome, x + 350, 440, 64, "black", col)
        text_mid(c, L, x + 350, 680, 300, "black", col)
        text(c, sub, x + 350, 910, 54, "extrabold", INK2)
    text_mid(c, "×", W / 2, 660, 140, "black", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_virgula_da_taxa", capa_virgula), ("capa_B_aluguel_do_dinheiro", capa_aluguel),
                     ("capa_C_juros_ou_montante", capa_duelo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
