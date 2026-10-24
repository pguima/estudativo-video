"""Capas — Velocidade, Densidade e Vazão, Episódio 2: velocidade média (tema claro). 3 variações em 1280x720, sem gabarito.
A = relógio gigante à direita com a pergunta "30 min = 0,30 h?" · B = linha do tempo do ônibus atravessando a capa, com a
parada cinza e o cronômetro · C = velocímetro e visor m/s frente a frente, com "÷ ou ×?" no meio."""
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
    s = "MATEMÁTICA ENEM · VELOCIDADE · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_relogio(c):
    background(c); selo_topo(c)
    V.relogio(c, 1440, 560, 330, 30, 1.0, GREEN, num_a=0)
    s1 = "30 min"
    text(c, s1, 520, 380, 170, "black", INK)
    text(c, "= 0,30 h?", 520, 580, 150, "black", RED)
    V.selo(c, 520, 800, 1.0, "O ERRO DO RELÓGIO", AMBER, -4, 60)
    text(c, "velocidade média do zero", 520, 960, 50, "extrabold", PURPLE)


def capa_parada(c):
    background(c); selo_topo(c, W / 2)
    s = "A PARADA ENTRA NA CONTA?"
    text(c, s, W / 2, 300, fit(s, 130, 1780), "black", INK)
    x, y, w = 140, 690, 1300
    segs = [(0, 1, GREEN), (1, 1.5, V.PARADO), (1.5, 2.5, GREEN)]
    for h0, h1, col in segs:
        x0, x1 = x + w * h0 / 2.5, x + w * h1 / 2.5
        rrect(c, x0 + 5, y - 34, x1 - x0 - 10, 68, 18, col)
    text(c, "PARADO", x + w * 1.25 / 2.5, y + 110, 52, "black", GRAY)
    V.onibus(c, x + w * 1.25 / 2.5, y - 60, 120, 1.0)
    V.cronometro(c, 1660, 640, "2 h 30 min", 1.0, r=190)
    text(c, "o cronômetro não para", W / 2, 960, 56, "extrabold", PURPLE)


def capa_fator(c):
    background(c); selo_topo(c, W / 2)
    s = "km/h → m/s: DIVIDE OU MULTIPLICA?"
    text(c, s, W / 2, 290, fit(s, 120, 1780), "black", INK)
    V.velocimetro(c, 470, 640, 260, 90, 120, 1.0, size=120)
    V.painel(c, 1450, 640, "?", 1.0, w=460)
    shadow_rrect(c, 760, 560, 400, 170, 40, 1, 1.4)
    rrect(c, 760, 560, 400, 170, 40, "#FFFFFF")
    text_mid(c, "÷  ou  ×", 960, 645, 90, "black", PURPLE)
    text(c, "o fator 3,6 sem inverter", W / 2, 990, 52, "extrabold", GREEN)


if __name__ == "__main__":
    for nome, fn in (("capa_A_erro_do_relogio", capa_relogio), ("capa_B_parada_conta", capa_parada),
                     ("capa_C_divide_ou_multiplica", capa_fator)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
