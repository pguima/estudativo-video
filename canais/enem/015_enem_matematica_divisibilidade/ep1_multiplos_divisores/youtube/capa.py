"""Capas — Divisibilidade, Primos, MMC e MDC, Episódio 1: múltiplos, divisores e critérios (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_dois_segundos(c):
    background(c); selo(c); painel(c)
    V.numero(c, "6 813", 1470, 330, 150, 1.0)
    V.fmid(c, "6 + 8 + 1 + 3", 1470, 530, 64, "black", PURPLE)
    V.fmid(c, "= 18", 1470, 640, 80, "black", GREEN)
    V.fmid(c, "÷ 9  ✓", 1470, 810, 90, "black", GREEN)
    big(c, "6 813 É DIVISÍVEL", 340)
    big(c, "POR 9?", 470)
    boxed(c, "EM 2 SEGUNDOS", 70, 520, 140, GREEN)
    text(c, "múltiplos, divisores e os atalhos da divisão", 90, 860, 46, "extrabold", INK2, align="left")


def capa_retangulos(c):
    background(c); selo(c); painel(c)
    V.grade(c, 1470, 420, 36, 6, 58, 1.0)
    for k, s in enumerate(("1×36", "2×18", "3×12", "4×9", "6×6")):
        V.fmid(c, s, 1210 + k * 130, 820, 38, "black", PURPLE)
    big(c, "36 QUADRADINHOS:", 340)
    big(c, "QUANTOS", 470)
    boxed(c, "RETÂNGULOS?", 70, 520, 140, BLUE)
    text(c, "todos os divisores, sem esquecer nenhum", 90, 860, 46, "extrabold", INK2, align="left")


def capa_mesma_frase(c):
    background(c); selo(c); painel(c)
    V.fmid(c, "12 ÷ 3 = 4", 1470, 300, 90, "black", INK)
    arrow(c, 1400, 380, 1300, 520, BLUE, 1, 6, 22)
    arrow(c, 1540, 380, 1640, 520, GREEN, 1, 6, 22)
    text_mid(c, "3 é", 1300, 600, 48, "black", BLUE)
    text_mid(c, "DIVISOR", 1300, 665, 48, "black", BLUE)
    text_mid(c, "12 é", 1640, 600, 48, "black", GREEN)
    text_mid(c, "MÚLTIPLO", 1640, 665, 48, "black", GREEN)
    text_mid(c, "a mesma frase!", 1470, 830, 46, "black", PURPLE)
    big(c, "MÚLTIPLO OU", 340)
    big(c, "DIVISOR?", 470)
    boxed(c, "NUNCA MAIS CONFUNDA", 70, 520, 110, PURPLE)
    text(c, "a base de MMC, MDC e primos no ENEM", 90, 860, 48, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_dois_segundos", capa_dois_segundos), ("capa_B_retangulos", capa_retangulos),
                     ("capa_C_mesma_frase", capa_mesma_frase)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
