"""Capas — Potenciação e Radiciação, Episódio 7: Revisão geral (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike, check_icon  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep7", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 7", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pegadinhas(c):
    background(c); selo(c); painel(c)
    itens = [("2^3 = 6", False), ("2^{-3} > 0", True), ("√{x^2} = x", False)]
    for k, (s, ver) in enumerate(itens):
        y = 270 + k * 230
        K.expr(c, s, 1390, y, 96, 1)
        if not ver:
            w = K.expr_w(s, 96)
            strike(c, 1390 - w / 2 - 10, y + 6, 1390 + w / 2 + 10, y + 6, 1, RED, 1)
        K.chip(c, "V" if ver else "F", 1700, y, GREEN if ver else RED, 1, 70)
    big(c, "10 PEGADINHAS:", 340)
    big(c, "QUANTAS VOCÊ", 470)
    boxed(c, "ACERTA?", 70, 520, 160, AMBER)
    text(c, "revisão de potência e raiz para o ENEM", 90, 860, 46, "extrabold", INK2, align="left")


def capa_questoes(c):
    background(c); selo(c); painel(c)
    for k, s in enumerate(("(27^2·9)/3^6", "√{75} + √{12}", "10/√{5}")):
        y = 290 + k * 250
        K.expr(c, s, 1470, y, 90 if k else 84, 1)
    check_icon(c, 1740, 830, 40, 1, GREEN)
    big(c, "5 QUESTÕES", 340)
    big(c, "ESTILO ENEM", 470)
    boxed(c, "RESOLVIDAS", 70, 520, 150, GREEN)
    text(c, "potenciação e radiciação, passo a passo", 90, 860, 46, "extrabold", INK2, align="left")


def capa_revisao(c):
    background(c); selo(c); painel(c)
    for k in range(6):
        x, y = 1300 + (k % 2) * 340, 260 + (k // 2) * 250
        V.icone(c, k, x, y, 1.15, 1)
    big(c, "POTÊNCIA E RAIZ", 340, maxw=960)
    big(c, "EM UMA SÓ", 470, maxw=960)
    boxed(c, "REVISÃO", 70, 520, 160, PURPLE)
    text(c, "6 episódios em uma aula", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_10_pegadinhas", capa_pegadinhas), ("capa_B_5_questoes", capa_questoes),
                     ("capa_C_revisao", capa_revisao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
