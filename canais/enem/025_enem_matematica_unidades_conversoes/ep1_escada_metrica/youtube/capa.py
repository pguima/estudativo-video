"""Capas — Unidades de Medida e Conversões, Episódio 1: a escada do sistema métrico (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · UNIDADES DE MEDIDA · EP. 1", 84, 90, BLUE, size=34, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_escada(c):
    background(c); selo(c); painel(c)
    V.escada(c, 1150, 260, 92, 70, V.COMP, 1.0, {0, 3}, PURPLE, ball=3.0, ball_a=1.0, path=(0, 3), size=30)
    text(c, "3 degraus  =  × 1 000", 1470, 880, 44, "black", GREEN)
    big(c, "CONVERTA QUALQUER", 330)
    big(c, "MEDIDA CONTANDO", 470)
    boxed(c, "DEGRAUS", 70, 520, 160, PURPLE)
    text(c, "km, m, cm, mm, kg, g, mg: uma escada só", 90, 860, 44, "extrabold", INK2, align="left")


def capa_tonelada(c):
    background(c); selo(c); painel(c)
    text(c, "1 tonelada =", 1470, 330, 64, "black", INK)
    text(c, "100 kg", 1470, 470, 96, "black", RED)
    line(c, 1300, 440, 1640, 440, RED, 1.0, 10)
    text(c, "1 000 kg", 1470, 640, 104, "black", GREEN)
    text(c, "um quilo de quilos", 1470, 760, 40, "black", PURPLE)
    big(c, "1 TONELADA", 330)
    big(c, "NÃO É 100 kg", 470)
    boxed(c, "O ERRO SILENCIOSO", 70, 520, 130, RED)
    text(c, "comprimento e massa sem errar a vírgula", 90, 860, 44, "extrabold", INK2, align="left")


def capa_katia(c):
    background(c); selo(c); painel(c)
    palavras = [("K", "Kátia", "km"), ("H", "Hoje", "hm"), ("D", "Dançou", "dam"), ("M", "Muito", "m"),
                ("D", "Dançou", "dm"), ("C", "Com", "cm"), ("M", "Marcos", "mm")]
    for k, (l, w_, u) in enumerate(palavras):
        y = 210 + k * 100
        c.drawCircle(1250, y, 34, paint(PURPLE, 1.0))
        text_mid(c, l, 1250, y, 40, "black", "#FFFFFF")
        text(c, w_, 1310, y + 16, 48, "black", GREEN, align="left")
        text(c, u, 1720, y + 16, 44, "black", BLUE, align="right")
    big(c, "A FRASE QUE", 330)
    big(c, "NUNCA MAIS", 470)
    boxed(c, "TE DEIXA ERRAR", 70, 520, 140, GREEN)
    text(c, "a ordem das unidades, do maior ao menor", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_conte_degraus", capa_escada), ("capa_B_tonelada", capa_tonelada),
                     ("capa_C_frase_katia", capa_katia)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
