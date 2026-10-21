"""Capas — Operações e Conjuntos Numéricos, Episódio 4: Diagrama de Venn (tema claro). 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = V.ftext_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    V.fmid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA BÁSICA · EPISÓDIO 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_apenas(c):
    background(c)
    selo(c)
    painel(c)
    v = V.Venn2(1470, 500, 170, 190, rect_pad=50)
    v.pinta(c, "a", AMBER, 1, 0.45)
    v.base(c, 1, "P", "Q", universo=True)
    v.num(c, "a", "80", 1, AMBER, 70)
    v.num(c, "m", "40", 1, V.MEIO, 54)
    V.apenas_txt(c, "apenas P", 1470, 830, 64, INK, 1, align="center")
    text(c, "UMA PALAVRA", 80, 340, 108, "black", INK, align="left")
    text(c, "MUDA TUDO:", 80, 470, 108, "black", INK, align="left")
    boxed(c, "APENAS", 70, 520, 160, AMBER, INK)
    text(c, "diagrama de Venn do zero", 90, 860, 56, "extrabold", INK2, align="left")


def capa_ponto(c):
    background(c)
    selo(c)
    painel(c)
    v = V.Venn2(1470, 450, 170, 190, rect_pad=50)
    v.pinta(c, "m", V.MEIO, 1, 0.5)
    v.base(c, 1, "A", "B")
    v.num(c, "m", "?", 1, V.MEIO, 90)
    V.fmid(c, "só + e −", 1470, 800, 64, "black", GREEN)
    text(c, "QUESTÃO", 80, 340, 140, "black", INK, align="left")
    text(c, "PONTO", 80, 470, 140, "black", INK, align="left")
    boxed(c, "GARANTIDO", 70, 520, 150, GREEN)
    text(c, "cai quase todo ano no ENEM", 90, 860, 56, "extrabold", INK2, align="left")


def capa_contado(c):
    background(c)
    selo(c)
    painel(c)
    v = V.Venn2(1470, 430, 160, 180)
    v.pinta(c, "m", V.MEIO, 1, 0.35)
    v.base(c, 1, "noiva", "noivo")
    for k in range(3):
        V.pessoa(c, 1470, 380 + k * 50, V.MEIO, 1, 1.0)
        V.pessoa(c, 1490, 370 + k * 50, V.MEIO, 0.4, 1.0)
    V.fmid(c, "30 + 25 − 5 = 50", 1470, 760, 56, "black", PURPLE)
    text(c, "contado duas vezes: desconte uma", 1470, 850, 30, "black", INK2)
    text(c, "QUEM FOI", 80, 340, 140, "black", INK, align="left")
    text(c, "CONTADO", 80, 470, 140, "black", INK, align="left")
    boxed(c, "DUAS VEZES?", 70, 530, 118, V.MEIO)
    text(c, "diagrama de Venn sem fórmula", 90, 860, 56, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_apenas", capa_apenas), ("capa_B_ponto_garantido", capa_ponto),
                     ("capa_C_contado_duas_vezes", capa_contado)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
