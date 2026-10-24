"""Capas — Progressão Geométrica, Episódio 1: a máquina de multiplicar (tema claro). 3 variações em 1280x720.
A = a corrida PA (+6, reta) × PG (×2, curva) e "QUEM GANHA NO FIM?"; B = a máquina roxa "×q" gigante com a ficha 2 entrando
e "?" saindo, "A MÁQUINA DE MULTIPLICAR"; C = "+5% AO ANO" e o fator "× 0,05 ?" contra "× 1,05 ?" com selo "QUAL?".
Nenhuma mostra gabarito (48 620, 1 458 g e 1 000 · 1,2ⁿ não aparecem)."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · PROGRESSÃO GEOMÉTRICA · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, PURPLE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, PURPLE, size=34, anchor="center", bounds=(0, 1920))


def capa_corrida(c):
    background(c); selo_topo(c)
    s = "QUEM GANHA"
    text(c, s, 84, 300, fit(s, 150, 900), "black", INK, align="left")
    s2 = "NO FIM?"
    text(c, s2, 84, 450, fit(s2, 150, 900), "black", PURPLE, align="left")
    pill(c, "SOMA 6", 100, 560, BLUE, size=48, bounds=(0, 1920))
    pill(c, "DOBRA", 100, 660, PURPLE, size=48, bounds=(0, 1920))
    V.corrida(c, 1080, 200, 760, 740, 6, 1.0, placar=False)
    rrect(c, 0, 990, W, 90, 0, PURPLE)
    text_mid(c, "progressão geométrica do zero", W / 2, 1035, 54, "black", "#FFFFFF")


def capa_maquina(c):
    background(c); selo_topo(c, W / 2)
    s = "A MÁQUINA DE MULTIPLICAR"
    text(c, s, W / 2, 300, fit(s, 130, 1780), "black", INK)
    V.maquina(c, W / 2, 640, "×q", 1.0, w=520, h=340)
    V.ficha(c, "2", W / 2 - 520, 750, 1.0, BLUE, w=200, h=140, size=90)
    V.ficha(c, "?", W / 2 + 520, 750, 1.0, AMBER, w=200, h=140, size=90)
    arrow(c, W / 2 - 400, 750, W / 2 - 280, 750, INK2, 1.0, 8, 26)
    arrow(c, W / 2 + 280, 750, W / 2 + 400, 750, INK2, 1.0, 8, 26)
    rrect(c, 0, 960, W, 120, 0, BLUE)
    text_mid(c, "qualquer termo sem listar os anteriores", W / 2, 1020, 56, "black", "#FFFFFF")


def capa_fator(c):
    background(c); selo_topo(c)
    s = "+5% AO ANO"
    text(c, s, 84, 330, fit(s, 170, 1100), "black", INK, align="left")
    for k, (f, col) in enumerate((("× 0,05", RED), ("× 1,05", GREEN))):
        x = 420 + k * 760
        shadow_rrect(c, x - 320, 450, 640, 330, 40, 1, 1.4)
        rrect(c, x - 320, 450, 640, 330, 40, "#FFFFFF")
        text_mid(c, f, x, 570, 140, "black", INK)
        text_mid(c, "?", x, 720, 70, "black", AMBER)
    V.selo(c, 1540, 270, 1.0, "QUAL?", AMBER, -6, 90)
    rrect(c, 0, 960, W, 120, 0, GREEN)
    text_mid(c, "porcentagem vira razão", W / 2, 1020, 60, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quem_ganha_no_fim", capa_corrida), ("capa_B_maquina_multiplicar", capa_maquina),
                     ("capa_C_qual_fator", capa_fator)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
