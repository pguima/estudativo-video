"""Capas — Determinantes, Episódio 2: propriedades que poupam conta (tema claro). 3 variações em 1280x720.
A = a matriz 3 × 3 dobrada, o visor "det 5 → ?" e o palpite "10?" num selo âmbar;
B = a matriz (1 0 −1 / 3 2 1 / 5 4 3) com as setas "+ (2, 2, 2)" e "det = ? SEM SARRUS";
C = os três botões de volume ao lado das linhas, "3 BOTÕES DE VOLUME".
Nenhuma mostra gabarito (o 40 e o 0 não aparecem)."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · DETERMINANTES · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_dobrou(c):
    background(c); selo_topo(c)
    V.matriz(c, 520, 600, [["2·•"] * 3] * 3, 1, 210, 170, 80,
             cores={(i, j): PURPLE for i in range(3) for j in range(3)})
    s = "DOBROU TUDO."
    text(c, s, 1400, 330, fit(s, 130, 900), "black", INK)
    V.contador(c, 1400, 560, "5 → ?", 1, PURPLE, w=640)
    V.selo(c, 1420, 800, 1.0, "10 ?", AMBER, -8, 110)


def capa_sem_sarrus(c):
    background(c); selo_topo(c, W / 2)
    s = "det = ?  SEM SARRUS"
    text(c, s, W / 2, 300, fit(s, 150, 1780), "black", INK)
    V.matriz(c, 760, 680, V.M8, 1, 200, 150, 88)
    for i in range(2):
        y1, y2 = V.row_y(680, 3, 150, i), V.row_y(680, 3, 150, i + 1)
        arrow(c, 1130, y1 + 14, 1130, y2 - 14, GREEN, 1, 7, 22)
        pill(c, "+ (2, 2, 2)", 1170, (y1 + y2) / 2, GREEN, size=40, anchor="left", bounds=(0, 1920))
    V.selo(c, 1640, 900, 1.0, "PERCEBEU?", AMBER, -8, 56)


def capa_botoes(c):
    background(c); selo_topo(c, W / 2)
    s = "3 BOTÕES DE VOLUME"
    text(c, s, W / 2, 300, fit(s, 150, 1780), "black", INK)
    V.matriz(c, 720, 660, V.DOTS, 1, 170, 150, 80, row_hi=(0, 1, 2), row_col=PURPLE)
    for i in range(3):
        y = V.row_y(660, 3, 150, i)
        V.botao(c, 1120, y, 1, 0.8, "", PURPLE, r=56)
        pill(c, "× 2", 1210, y, PURPLE, size=44, anchor="left", bounds=(0, 1920))
    rrect(c, 0, 940, W, 140, 0, AMBER)
    text_mid(c, "dobrar a matriz não dobra o determinante", W / 2, 1010, 62, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_dobrou_tudo", capa_dobrou), ("capa_B_sem_sarrus", capa_sem_sarrus),
                     ("capa_C_tres_botoes", capa_botoes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
