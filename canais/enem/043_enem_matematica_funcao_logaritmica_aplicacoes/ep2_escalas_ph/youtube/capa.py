"""Capas — Função logarítmica e aplicações, Episódio 2: escalas logarítmicas e o pH (tema claro). 3 variações em 1280x720.
Nenhuma mostra gabarito. A = os dois copos (limão pH 2 e café pH 5) lado a lado e a pergunta "3 vezes mais ácido?" com
um "?" gigante, sem dizer quantas vezes; B = faixa escura com a "régua de zeros" (10⁻¹² a 1) atravessando a capa e os
arcos ×10; C = a conta "2 · 10⁻⁴ → pH = ?" com as duas parcelas coloridas e "sem calculadora"."""
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


def selo_topo(c, cx=None, col=BLUE, fg=None):
    s = "MATEMÁTICA ENEM · FUNÇÃO LOGARÍTMICA · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, col, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, col, fg, size=34, anchor="center", bounds=(0, 1920))


def capa_copos(c):
    background(c); selo_topo(c, None, AMBER)
    V.copo(c, 330, 820, 300, 420, V.LIMAO, 1.0)
    V.copo(c, 720, 820, 300, 420, V.CAFE, 1.0)
    pill(c, "pH 2", 330, 900, PURPLE, size=48, anchor="center")
    pill(c, "pH 5", 720, 900, PURPLE, size=48, anchor="center")
    s = "3 VEZES"
    text(c, s, 1400, 380, fit(s, 190, 900), "black", INK)
    s = "MAIS ÁCIDO?"
    text(c, s, 1400, 560, fit(s, 150, 900), "black", AMBER)
    shadow_rrect(c, 1010, 650, 780, 200, 36, 1, 1.4)
    rrect(c, 1010, 650, 780, 200, 36, mix("#FFFFFF", RED, 0.10))
    text_mid(c, "quase todo mundo erra", 1400, 750, 58, "black", RED)


def capa_regua(c):
    background(c)
    rrect(c, 0, 0, W, H, 0, INK)
    pill(c, "MATEMÁTICA ENEM · FUNÇÃO LOGARÍTMICA · EP. 2", W / 2, 90, "#FFFFFF", INK, size=34, anchor="center",
         bounds=(0, 1920))
    s = "UMA RÉGUA DE ZEROS"
    text(c, s, W / 2, 300, fit(s, 150, 1780), "black", "#FFFFFF")
    rrect(c, 120, 440, 1680, 260, 30, "#FFFFFF")
    V.regua_log(c, 220, 600, 1480, 1.0, 1.0)
    text(c, "cada passo igual = ×10 · pH, sons e terremotos", W / 2, 900, 60, "extrabold", "#FFFFFF")


def capa_conta(c):
    background(c); selo_topo(c, W / 2, PURPLE)
    s = "pH SEM CALCULADORA?"
    text(c, s, W / 2, 290, fit(s, 140, 1760), "black", INK)
    shadow_rrect(c, 160, 380, 1600, 300, 40, 1, 1.4)
    rrect(c, 160, 380, 1600, 300, 40, mix("#FFFFFF", PURPLE, 0.10))
    V.fm(c, [("[H⁺] = ", INK), ("2", BLUE), (" · ", INK), ("10^{−4}", PURPLE, "m"), ("  →  pH = ", INK), ("?", AMBER)],
         W / 2, 530, 120, 1.0)
    text(c, "com log 2 = 0,30 e uma regra só", W / 2, 880, 76, "extrabold", GREEN)


if __name__ == "__main__":
    for nome, fn in (("capa_A_tres_vezes", capa_copos), ("capa_B_regua_de_zeros", capa_regua),
                     ("capa_C_ph_sem_calculadora", capa_conta)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
