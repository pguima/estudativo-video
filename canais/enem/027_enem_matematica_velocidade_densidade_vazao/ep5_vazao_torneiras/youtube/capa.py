"""Capas — Velocidade, Densidade e Vazão, Episódio 5: vazão, torneiras e ralos (tema claro). 3 variações em 1280x720, sem gabarito.
A = tanque gigante com duas torneiras e o "9 h?" riscado; B = faixa escura no alto + banheira com o ralo sabotador;
C = tanque fatiado com a fração "1/6 por hora" enorme."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, y=90):
    s = "MATEMÁTICA ENEM · VAZÃO · EP. 5"
    if cx is None:
        pill(c, s, 84, y, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, y, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_nove(c):
    background(c); selo_topo(c)
    V.torneira(c, 360, 300, 1.0, V.T1, 1.5, 1.0, 120)
    V.torneira(c, 640, 300, 1.0, V.T2, 1.5, 1.0, 120)
    text(c, "6 h", 200, 330, 64, "black", V.T1)
    text(c, "3 h", 480, 330, 64, "black", V.T2)
    V.tanque(c, 250, 420, 500, 560, 6, 3.4, 1.0, rot=False)
    s = "JUNTAS:"
    text(c, s, 1330, 360, 120, "black", INK)
    text(c, "9 h?", 1330, 640, 300, "black", RED)
    line(c, 1050, 690, 1620, 480, RED, 1.0, 26)
    V.selo(c, 1330, 860, 1.0, "QUASE TODO MUNDO ERRA", AMBER, -5, 52)


def capa_ralo(c):
    background(c)
    rrect(c, 0, 0, W, 300, 0, INK, 1.0)
    pill(c, "MATEMÁTICA ENEM · VAZÃO · EP. 5", W / 2, 70, BLUE, size=30, anchor="center", bounds=(0, 1920))
    s = "TORNEIRA SOMA, RALO SUBTRAI"
    text(c, s, W / 2, 230, fit(s, 120, 1800), "black", "#FFFFFF")
    V.torneira(c, 700, 560, 1.0, V.T1, 1.4, 1.0, 120)
    V.banheira(c, 820, 960, 1.0, 0.45, 2.4)
    text(c, "+", 500, 560, 200, "black", GREEN)
    text(c, "O RALO É", 1530, 560, 90, "black", INK)
    text(c, "O SABOTADOR", 1530, 680, 96, "black", RED)
    arrow(c, 1400, 760, 1160, 920, RED, 1.0, 14, 40)
    text(c, "−", 1300, 1000, 160, "black", RED)


def capa_fatias(c):
    background(c); selo_topo(c, W / 2 + 300)
    V.tanque(c, 160, 160, 520, 840, 6, 1.0, 1.0, rot=False)
    V.tanque(c, 160, 160, 520, 840, 6, 1.0, 1.0, rot=False, pintado=1.0)
    text(c, "PENSE EM", 1230, 350, 110, "black", INK)
    text(c, "FATIAS", 1230, 480, 150, "black", PURPLE)
    K.expr(c, "1/6", 1000, 760, 200, 1.0, cores={0: BLUE})
    text(c, "do tanque", 1420, 740, 70, "black", INK)
    text(c, "por hora", 1420, 830, 70, "black", INK)


if __name__ == "__main__":
    for nome, fn in (("capa_A_juntas_nove_horas", capa_nove), ("capa_B_ralo_sabotador", capa_ralo),
                     ("capa_C_pense_em_fatias", capa_fatias)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
