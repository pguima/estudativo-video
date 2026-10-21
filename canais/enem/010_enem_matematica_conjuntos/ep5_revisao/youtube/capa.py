"""Capas — Operações e Conjuntos Numéricos, Episódio 5: Revisão geral (tema claro). 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = V.ftext_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    V.fmid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA BÁSICA · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pegadinhas(c):
    background(c)
    selo(c)
    painel(c)
    for k, s in enumerate(("−3² = 9", "[−∞, 5]", "√9 é irracional")):
        y = 280 + k * 220
        V.fmid(c, s, 1470, y, 64, "black", RED)
        line(c, 1230, y - 4, 1710, y - 4, RED, 1, 6)
        V.selo_pegadinha(c, 1470, y + 80, 1, -4)
    text(c, "AS 6", 80, 340, 140, "black", INK, align="left")
    text(c, "PEGADINHAS", 80, 470, 128, "black", INK, align="left")
    boxed(c, "DO ENEM", 70, 520, 160, AMBER, INK)
    text(c, "revisão de matemática básica", 90, 860, 56, "extrabold", INK2, align="left")


def capa_v_ou_f(c):
    background(c)
    selo(c)
    painel(c)
    V.fmid(c, "\"apenas A\" =", 1470, 300, 60, "black", INK)
    V.fmid(c, "círculo A inteiro?", 1470, 390, 56, "black", INK)
    V.carimbo_falso(c, 1470, 560, 1)
    V.cronometro(c, 1470, 780, 0.5, 0, 2, 1, 70)
    text(c, "VERDADEIRO", 80, 340, 120, "black", INK, align="left")
    text(c, "OU FALSO?", 80, 470, 140, "black", INK, align="left")
    boxed(c, "PAUSE E RESPONDA", 70, 535, 84, PURPLE)
    text(c, "revisão com 5 questões inéditas", 90, 860, 56, "extrabold", INK2, align="left")


def capa_quatro(c):
    background(c)
    selo(c)
    painel(c)
    for k in range(4):
        x, y = (1310 if k % 2 == 0 else 1630), (340 if k < 2 else 690)
        V.icone_ep(c, k, x, y, 1, 1.15)
        text(c, V.EPS[k], x, y + 140, 30, "black", INK2)
    text(c, "4 AULAS", 80, 340, 140, "black", INK, align="left")
    text(c, "EM UMA", 80, 470, 140, "black", INK, align="left")
    boxed(c, "REVISÃO", 70, 520, 160, GREEN)
    text(c, "sinais, conjuntos, intervalos e Venn", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_pegadinhas", capa_pegadinhas), ("capa_B_verdadeiro_ou_falso", capa_v_ou_f),
                     ("capa_C_quatro_em_uma", capa_quatro)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
