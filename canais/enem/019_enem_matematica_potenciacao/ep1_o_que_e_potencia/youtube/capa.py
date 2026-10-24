"""Capas — Potenciação e Radiciação, Episódio 1: O que é potência (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_zero(c):
    background(c); selo(c); painel(c)
    degraus = [("2^2", "4"), ("2^1", "2"), ("2^0", "1")]
    for i, (s, v) in enumerate(degraus):
        x, y = 1180 + i * 200, 220 + i * 170
        last = i == 2
        rrect(c, x, y, 190, 190, 20, mix(K.DEGRAU, GREEN, 0.3 if last else 0), 1, shadow=True)
        rrect(c, x, y, 190, 12, 6, GREEN if last else PURPLE, 1)
        K.expr(c, s, x + 95, y + 70, 60, 1)
        K.expr(c, v, x + 95, y + 145, 64, 1, cores={0: GREEN if last else PURPLE})
        if i < 2:
            K.fmid(c, "÷ 2", x + 200, y + 30, 40, "black", AMBER)
    K.expr(c, "2^0 = 1", 1470, 860, 110, 1, cores={2: GREEN})
    big(c, "POR QUE 2⁰", 340)
    big(c, "DÁ 1 E NÃO", 470)
    boxed(c, "ZERO?", 70, 520, 160, AMBER)
    text(c, "potência do zero, sem decorar", 90, 860, 46, "extrabold", INK2, align="left")


def capa_negativo(c):
    background(c); selo(c); painel(c)
    K.expr(c, "2^{-3}", 1470, 330, 170, 1)
    K.fmid(c, "≠ −8", 1470, 560, 110, "black", RED)
    K.expr(c, "= 1/8", 1470, 780, 130, 1, cores={0: GREEN, 1: GREEN})
    big(c, "EXPOENTE", 340)
    big(c, "NEGATIVO NÃO", 470)
    boxed(c, "DÁ NEGATIVO", 70, 520, 140, RED)
    text(c, "o erro que a prova deixa nas alternativas", 90, 860, 46, "extrabold", INK2, align="left")


def capa_seis(c):
    background(c); selo(c); painel(c)
    K.folha(c, 1450, 380, 760, 560, 3)
    K.contador(c, 1470, 720, 8, 1, "camadas", GREEN, 120)
    big(c, "2³ = 6?", 340)
    big(c, "ERRADO: SÃO", 470)
    boxed(c, "8 CAMADAS", 70, 520, 150, BLUE)
    text(c, "o que é potência, do zero", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_por_que_da_1", capa_zero), ("capa_B_negativo_nao_da_negativo", capa_negativo),
                     ("capa_C_nao_e_6", capa_seis)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
