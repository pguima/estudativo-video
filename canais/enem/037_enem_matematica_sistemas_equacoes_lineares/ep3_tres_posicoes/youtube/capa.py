"""Capas — Sistemas de Equações Lineares, Episódio 3 (tema claro). 3 variações em 1280x720.
Formatos: A = a conta terminando num "0 = 2" gigante em vermelho, com a borracha parada em cima e "ERREI A CONTA?" no alto;
B = faixa escura com as três situações em planos lado a lado e "1, NENHUMA OU INFINITAS?" (sem dizer qual é qual);
C = fundo roxo cheio com as três caixinhas de razões gigantes e "?" entre elas, "CLASSIFIQUE SEM RESOLVER"."""
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

TAG = "MATEMÁTICA ENEM · SISTEMAS · EP. 3"


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def capa_zero_dois(c):
    background(c)
    pill(c, TAG, 84, 90, BLUE, size=34, bounds=(0, 1920))
    s = "ERREI A CONTA?"
    text(c, s, 84, 300, fit(s, 150, 1100), "black", INK, align="left")
    V.expr(c, "x + 2y = 4", 420, 470, 70, 1.0)
    V.expr(c, "2x + 4y = 10", 420, 570, 70, 1.0)
    line(c, 130, 640, 760, 640, INK, 1.0, 6)
    V.expr(c, "0 = 2", 440, 820, 230, 1.0, cores={0: RED, 1: RED, 2: RED})
    c.save(); c.translate(1420, 560); c.rotate(-22)
    rrect(c, -230, -130, 460, 260, 40, "#F2B8C6", 1.0, shadow=True)
    rrect(c, -230, 30, 460, 100, 30, "#5B7DB1")
    c.restore()
    V.selo(c, 1420, 880, 1.0, "NÃO APAGUE!", GREEN, -4, 64)


def capa_tres_planos(c):
    background(c)
    rrect(c, 0, 0, W, 300, 0, INK)
    pill(c, TAG, W / 2, 70, BLUE, size=32, anchor="center", bounds=(0, 1920))
    s = "1, NENHUMA OU INFINITAS?"
    text(c, s, W / 2, 230, fit(s, 130, 1800), "black", "#FFFFFF")
    for k, tp in enumerate(("conc", "par", "coin")):
        V.mini(c, 330 + k * 630, 680, 470, 1.0, tp, 0.0)
    text(c, "quantas soluções tem cada sistema?", W / 2, 1010, 54, "extrabold", GRAY)


def capa_caixinhas(c):
    rrect(c, 0, 0, W, H, 0, PURPLE)
    pill(c, TAG, W / 2, 90, INK, size=34, anchor="center", bounds=(0, 1920))
    s = "CLASSIFIQUE SEM RESOLVER"
    text(c, s, W / 2, 280, fit(s, 140, 1800), "black", "#FFFFFF")
    rrect(c, 160, 380, 1600, 470, 40, "#FFFFFF", 1.0, shadow=True)
    V.caixas(c, W / 2, 610, [("1", "2"), ("2", "4"), ("4", "10")], [("?", 1.0), ("?", 1.0)], 1.0, 92, gap=150)
    text(c, "três razões e a resposta sai sem conta", W / 2, 990, 56, "extrabold", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_errei_a_conta", capa_zero_dois), ("capa_B_uma_nenhuma_infinitas", capa_tres_planos),
                     ("capa_C_sem_resolver", capa_caixinhas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
