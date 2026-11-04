"""Capas — Redação ENEM, Introdução, Episódio 1: os três movimentos (tema claro). 3 variações em 1280x720."""
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


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "REDAÇÃO ENEM · INTRODUÇÃO · EP. 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_perguntas(c):
    background(c); selo(c); painel(c)
    for k, key in enumerate(V.K3):
        y = 300 + k * 240
        V.icone_peca(c, key, 1250, y, 1, 1.4)
        V.para(c, "“" + V.PERG[key] + "”", 1350, y - 18, 40, "black", V.MOV[key], 1, 430, 46)
    big(c, "AS 3 PERGUNTAS", 340)
    big(c, "DO 1º PARÁGRAFO", 470)
    boxed(c, "DA REDAÇÃO", 70, 520, 130, V.MOV["tese"])
    text(c, "que a sua introdução precisa responder", 90, 860, 46, "extrabold", INK2, align="left")


def capa_etiqueta(c):
    background(c); selo(c); painel(c)
    V.etiqueta_intro(c, 1160, 250, 620, 1.0, keys=V.K3, movs=0, rowh=150, ok=[1, 1, 1], title="INTRODUÇÃO")
    big(c, "A INTRODUÇÃO", 340)
    big(c, "EM 3 MOVIMENTOS", 470)
    boxed(c, "MAPA · TESE · LISTA", 70, 530, 84, GREEN)
    text(c, "o primeiro parágrafo do ENEM, do zero", 90, 860, 46, "extrabold", INK2, align="left")


def capa_mito(c):
    background(c); selo(c); painel(c)
    for k in range(3):
        V.paper(c, 1180, 200 + k * 30, 580, 560, 1.0, lh=48, top=300 + k * 30, rot=(k - 1) * 3)
    for k in range(3):
        badge_num(c, k + 1, 1300, 380 + k * 120, 1, 40, bg=INK2)
        line(c, 1360, 380 + k * 120, 1700 - k * 60, 380 + k * 120, LIGHT, 1, 14)
    V.selo(c, 1470, 520, 1, "MITO", RED, -10, 110)
    big(c, "PRECISA TER", 340)
    big(c, "3 FRASES?", 470)
    boxed(c, "NÃO!", 70, 520, 150, RED)
    text(c, "o que o Inep cobra na introdução", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_3_perguntas", capa_perguntas), ("capa_B_3_movimentos", capa_etiqueta), ("capa_C_mito_3_frases", capa_mito)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
