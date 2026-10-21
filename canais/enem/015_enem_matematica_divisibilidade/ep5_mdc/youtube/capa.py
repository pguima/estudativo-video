"""Capas — Divisibilidade, Primos, MMC e MDC, Episódio 5: MDC (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5_mdc", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pedacos(c):
    background(c); selo(c); painel(c)
    text(c, "Quantos pedaços?", 1470, 250, 44, "black", AMBER)
    V.medir(c, 1170, 320, 600, 60, 1.0, 1.0, 1.0, h=50, ok_col=GREEN)
    rrect(c, 1180, 430, 580, 170, 24, mix("#FFFFFF", RED, 0.10))
    text(c, "60", 1340, 555, 110, "black", RED)
    check_icon(c, 1620, 515, 46, 1, RED, "x")
    rrect(c, 1180, 640, 580, 170, 24, mix("#FFFFFF", GREEN, 0.10))
    text(c, "10", 1340, 765, 110, "black", GREEN)
    check_icon(c, 1620, 725, 46, 1, GREEN)
    big(c, "ACHOU O MDC", 340)
    big(c, "E PAROU?", 470)
    boxed(c, "ERROU", 70, 520, 150, RED)
    text(c, "os 2 passos da questão de MDC no ENEM", 90, 860, 48, "extrabold", INK2, align="left")


def capa_regua(c):
    background(c); selo(c); painel(c)
    for k, r in enumerate((4, 6)):
        y = 260 + k * 300
        text(c, f"régua de {r} cm", 1470, y, 34, "black", RED if r == 4 else GREEN)
        V.medir(c, 1180, y + 40, 12, r, 42, 1.0, 1.0, h=40, label=False)
        V.medir(c, 1180, y + 110, 18, r, 32, 1.0, 1.0, h=40, label=False)
    big(c, "A MAIOR RÉGUA", 340)
    big(c, "QUE CABE", 470)
    boxed(c, "CERTINHO", 70, 520, 150, GREEN)
    text(c, "MDC do zero: tábuas, grupos e pedaços", 90, 860, 50, "extrabold", INK2, align="left")


def capa_euclides(c):
    background(c); selo(c); painel(c)
    V.euclides(c, 1170, 300, 5.0, 1.0, 4)
    V.fbox(c, "MDC = 24", 1470, 780, 60, 1.0, GREEN)
    big(c, "MDC CORTANDO", 340)
    big(c, "EM QUADRADOS", 470)
    boxed(c, "EUCLIDES", 70, 520, 150, PURPLE)
    text(c, "fatoração ou divisões sucessivas", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_achou_mdc_parou", capa_pedacos), ("capa_B_maior_regua", capa_regua),
                     ("capa_C_euclides", capa_euclides)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
