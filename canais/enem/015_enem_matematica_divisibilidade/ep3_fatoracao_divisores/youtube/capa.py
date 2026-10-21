"""Capas — Matemática ENEM, Divisibilidade, Episódio 3: fatoração e a fórmula dos divisores (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_divisores(c):
    background(c); selo(c); painel(c)
    V.varal(c, 1180, 250, V.L360, [(1, 1)] * 7, size=56, lh=78, wleft=230)
    V.fmid(c, "2^3 · 3^2 · 5", 1470, 860, 64, "black", PURPLE)
    big(c, "O 360 TEM", 340)
    big(c, "QUANTOS", 470)
    boxed(c, "DIVISORES?", 70, 520, 140, AMBER)
    text(c, "conte em 15 segundos, sem listar", 90, 860, 50, "extrabold", INK2, align="left")


def capa_receita(c):
    background(c); selo(c); painel(c)
    text(c, "RECEITA DO 360", 1470, 230, 40, "black", INK, tracking=2)
    for k, n in enumerate((2, 2, 2, 3, 3, 5)):
        V.tijolo(c, 1290 + (k % 3) * 180, 400 + (k // 3) * 150, n, 1, 150, 100)
    V.fmid(c, "360 = 2^3 · 3^2 · 5", 1470, 760, 56, "black", PURPLE)
    big(c, "TODO NÚMERO", 340)
    big(c, "TEM UMA", 470)
    boxed(c, "RECEITA", 70, 520, 150, V.BRICK)
    text(c, "fatoração em primos, do zero", 90, 860, 50, "extrabold", INK2, align="left")


def capa_formula(c):
    background(c); selo(c); painel(c)
    V.fmid(c, "(3+1)(2+1)(1+1)", 1470, 330, 64, "black", PURPLE)
    V.fmid(c, "= 4 · 3 · 2", 1470, 450, 64, "black", INK)
    V.fmid(c, "= 24", 1470, 590, 110, "black", GREEN)
    V.fmid(c, "3 · 2 · 1 = 6", 1470, 800, 50, "black", RED)
    V.strike(c, 1320, 790, 1620, 790, 1, RED)
    big(c, "O ERRO DO", 340)
    big(c, "+1 QUE DERRUBA", 470)
    boxed(c, "TODO MUNDO", 70, 520, 122, RED)
    text(c, "a fórmula de quantos divisores tem um número", 90, 860, 38, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_360_divisores", capa_divisores), ("capa_B_receita", capa_receita), ("capa_C_erro_do_mais1", capa_formula)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
