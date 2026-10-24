"""Capas — Logaritmos, Episódio 2: as três propriedades e o kit log 2 e log 3 (tema claro). 3 variações em 1280x720.
Nenhuma mostra gabarito. A = a porta trancada grande à esquerda e a igualdade do gancho com "?" à direita, sem dizer se
vale; B = as três caixinhas do kit (2, 3 e 10) e "log 72 = ?" sem calculadora; C = faixa escura com a régua de cálculo
atravessando a capa e a pergunta "multiplicar somando?"."""
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
    s = "MATEMÁTICA ENEM · LOGARITMOS · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, col, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, col, fg, size=34, anchor="center", bounds=(0, 1920))


def capa_porta(c):
    background(c); selo_topo(c, None, AMBER)
    V.porta(c, 420, 600, 760, 1.0, 1.0)
    s = "A REGRA ÓBVIA"
    text(c, s, 1290, 300, fit(s, 120, 1040), "black", INK)
    shadow_rrect(c, 820, 380, 960, 330, 36, 1, 1.4)
    rrect(c, 820, 380, 960, 330, 36, mix("#FFFFFF", AMBER, 0.12))
    V.fm(c, [("log(10 + 10)", INK)], 1300, 470, 96, 1.0)
    V.fm(c, [("=  log 10 + log 10", INK), (" ?", AMBER)], 1300, 610, 96, 1.0)
    text(c, "cai em toda prova", 1300, 860, 76, "black", AMBER)


def capa_kit(c):
    background(c); selo_topo(c, W / 2, GREEN)
    s = "LOG 72 SEM CALCULADORA?"
    text(c, s, W / 2, 290, fit(s, 140, 1760), "black", INK)
    V.caixinhas(c, 190, 420, 1.0, (1, 1, 1), 470, 300, 60, False, 92)
    text(c, "só com estas 3 peças", W / 2, 900, 80, "extrabold", GREEN)


def capa_regua(c):
    background(c)
    rrect(c, 0, 0, W, H, 0, INK)
    pill(c, "MATEMÁTICA ENEM · LOGARITMOS · EP. 2", W / 2, 90, "#FFFFFF", INK, size=34, anchor="center",
         bounds=(0, 1920))
    s = "MULTIPLICAR SOMANDO?"
    text(c, s, W / 2, 300, fit(s, 150, 1780), "black", "#FFFFFF")
    V.regua(c, 250, 470, 1150, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0)
    text(c, "a ideia por trás das 3 propriedades do log", W / 2, 920, 64, "extrabold", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_regra_obvia", capa_porta), ("capa_B_kit_log72", capa_kit),
                     ("capa_C_regua_de_calculo", capa_regua)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
