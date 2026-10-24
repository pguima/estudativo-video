"""Capas — Velocidade, Densidade e Vazão, Episódio 3: a armadilha da média (tema claro). 3 variações em 1280x720, sem gabarito.
A = estrada larga atravessando a capa com o 50 riscado; B = balança de horas ocupando o centro; C = duas metades com ≠ gigante."""
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
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · VELOCIDADE · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_estrada(c):
    background(c); selo_topo(c, W / 2)
    s = "IDA A 60, VOLTA A 40"
    text(c, s, W / 2, 290, fit(s, 140, 1760), "black", INK)
    V.estrada(c, 160, 1760, 520, 1.0, 0.75, 0.55)
    s2 = "A MÉDIA NÃO É"
    text(c, s2, 760, 900, 120, "black", INK)
    text(c, "50", 1440, 920, 220, "black", AMBER)
    line(c, 1300, 960, 1590, 760, RED, 1.0, 22)
    V.selo(c, 1680, 640, 1.0, "PEGADINHA", AMBER, -8, 44)


def capa_balanca(c):
    background(c); selo_topo(c)
    s = "QUEM MANDA NA MÉDIA?"
    text(c, s, 84, 280, fit(s, 120, 1700), "black", INK, align="left")
    V.balanca(c, 1300, 500, 1.0, 1.0, 2, 3, "60 km/h · 2 h", "40 km/h · 3 h", half=400)
    text(c, "O RELÓGIO", 380, 560, 100, "black", PURPLE)
    cx, cy, r = 380, 780, 120
    c.drawCircle(cx, cy, r, paint(PURPLE))
    c.drawCircle(cx, cy, r - 16, paint("#FFFFFF"))
    line(c, cx, cy, cx, cy - 76, INK, 1.0, 12)
    line(c, cx, cy, cx + 56, cy + 24, INK, 1.0, 12)
    c.drawCircle(cx, cy, 12, paint(INK))


def capa_diferente(c):
    background(c)
    rrect(c, 0, 0, W / 2, H, 0, AMBER, 0.14)
    rrect(c, W / 2, 0, W / 2, H, 0, GREEN, 0.12)
    selo_topo(c, W / 2)
    text(c, "MÉDIA DAS", W / 4, 330, 96, "black", AMBER)
    text(c, "VELOCIDADES", W / 4, 440, fit("VELOCIDADES", 96, 860), "black", AMBER)
    text(c, "VELOCIDADE", 3 * W / 4, 330, fit("VELOCIDADE", 96, 860), "black", GREEN)
    text(c, "MÉDIA", 3 * W / 4, 440, 96, "black", GREEN)
    c.drawCircle(W / 2, 400, 120, paint("#FFFFFF"))
    text_mid(c, "≠", W / 2, 400, 200, "black", RED)
    s = "A ARMADILHA QUE O ENEM ADORA"
    rrect(c, 0, 760, W, 220, 0, "#FFFFFF", 0.94)
    text(c, s, W / 2, 900, fit(s, 104, 1760), "black", INK)


if __name__ == "__main__":
    for nome, fn in (("capa_A_media_nao_e_50", capa_estrada), ("capa_B_quem_manda_relogio", capa_balanca),
                     ("capa_C_media_diferente", capa_diferente)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
