"""Capas — Razão, Proporção e Regra de Três, Episódio 4: Regra de três composta (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · RAZÃO · EP. 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_uma_de_cada(c):
    background(c); selo(c); painel(c)
    V.sala(c, 1150, 160, 640, 560, 1.0, rotulo=False)
    V.colunas(c, 1190, 290, [V.COLS[0]], 1.0, destaque=0, cw=250, ch=300)
    V.colunas(c, 1500, 290, [V.COLS[2]], 1.0, cw=250, ch=300)
    rrect(c, 1250, 780, 440, 110, 26, PURPLE, 0.3)
    text_mid(c, "horas/dia: lá fora", 1470, 835, 44, "black", PURPLE)
    big(c, "3 GRANDEZAS?", 340)
    big(c, "INTERROGUE", 470)
    boxed(c, "UMA DE CADA VEZ", 70, 520, 130, PURPLE)
    text(c, "regra de três composta sem pânico", 90, 860, 46, "extrabold", INK2, align="left")


def capa_pacote(c):
    background(c); selo(c); painel(c)
    V.pacote(c, 1450, 420, 330, "1 440", 1.0)
    K.expr(c, "12 · 8 · 15", 1470, 720, 64, 1.0)
    K.expr(c, "= 18 · 10 · x", 1470, 830, 64, 1.0, cores={5: AMBER})
    big(c, "O ATALHO DOS", 340)
    big(c, "HOMENS-HORA", 470)
    boxed(c, "SEM DIRETA NEM INVERSA", 70, 520, 110, GREEN)
    text(c, "multiplique tudo de um lado e iguale", 90, 860, 46, "extrabold", INK2, align="left")


def capa_simples(c):
    background(c); selo(c); painel(c)
    for k, (s, col) in enumerate((("comparar", BLUE), ("inverter", PURPLE), ("multiplicar", GREEN))):
        y = 230 + k * 230
        rrect(c, 1200, y, 540, 170, 30, col)
        text_mid(c, s, 1470, y + 85, 70, "black", "#FFFFFF")
    big(c, "COMPOSTA É SÓ", 340)
    big(c, "A SIMPLES", 470)
    boxed(c, "REPETIDA", 70, 520, 160, BLUE)
    text(c, "o método em 4 passos, do zero", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_uma_de_cada_vez", capa_uma_de_cada), ("capa_B_homens_hora", capa_pacote),
                     ("capa_C_simples_repetida", capa_simples)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
