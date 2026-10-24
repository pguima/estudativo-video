"""Capas — Potenciação e Radiciação, Episódio 5: Simplificar radicais (tema claro). 3 variações em 1280x720."""
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


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34, maxw=1000):
    while text_w(s, "black", size) + pad * 2 > maxw:
        size -= 4
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_simplificar(c):
    background(c); selo(c); painel(c)
    K.expr(c, "√{50}", 1470, 300, 170, 1)
    K.fmid(c, "=", 1470, 480, 110, "black", GREEN)
    K.expr(c, "5√{2}", 1470, 660, 170, 1, cores={0: GREEN})
    K.fmid(c, "o mesmo número", 1470, 860, 46, "black", INK2)
    big(c, "SUA RESPOSTA SUMIU", 340)
    big(c, "DAS ALTERNATIVAS?", 470)
    boxed(c, "SIMPLIFIQUE A RAIZ", 70, 520, 120, GREEN)
    text(c, "simplificar radicais do zero, sem decorar", 90, 860, 40, "extrabold", INK2, align="left")


def capa_soma(c):
    background(c); selo(c); painel(c)
    K.expr(c, "2√{3} + 3√{2}", 1470, 300, 100, 1)
    K.fmid(c, "≠ 5√5", 1470, 450, 110, "black", RED)
    V.maca(c, 1335, 690, 85, 1, "√{3}", 56)
    K.fmid(c, "+", 1470, 690, 80, "black", INK)
    V.laranja(c, 1605, 690, 85, 1, "√{2}", 56)
    big(c, "2√3 + 3√2", 340)
    big(c, "NÃO É 5√5", 470)
    boxed(c, "MAÇÃ COM LARANJA", 70, 520, 120, RED)
    text(c, "quando dá (e quando não dá) para somar raízes", 90, 860, 40, "extrabold", INK2, align="left")


def capa_porta(c):
    background(c); selo(c); painel(c)
    K.expr(c, "180 = 2 · 2 · 3 · 3 · 5", 1470, 230, 50, 1, cores={2: GREEN, 4: GREEN, 6: GREEN, 8: GREEN, 10: AMBER})
    V.casa(c, 1340, 340, 450, 200, 1, porta_a=0)
    V.ficha(c, 1190, 452, 76, "2", GREEN, 1)
    K.fmid(c, "·", 1240, 452, 50, "black", INK)
    V.ficha(c, 1290, 452, 76, "3", GREEN, 1)
    V.ficha(c, 1650, 452, 76, "5", AMBER, 1)
    K.expr(c, "√{180} = 6√{5}", 1470, 700, 90, 1, cores={2: GREEN})
    K.fmid(c, "cada DUPLA sai como UM só", 1470, 850, 38, "black", INK2)
    big(c, "SIMPLIFIQUE √180", 340)
    big(c, "PELA PORTA DA RAIZ", 470)
    boxed(c, "OS PARES SAEM", 70, 520, 130, PURPLE)
    text(c, "o método da fatoração, passo a passo", 90, 860, 40, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_resposta_sumiu", capa_simplificar), ("capa_B_maca_com_laranja", capa_soma),
                     ("capa_C_porta_da_raiz", capa_porta)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
