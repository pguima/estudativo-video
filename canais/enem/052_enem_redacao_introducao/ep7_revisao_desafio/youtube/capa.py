"""Capas — Redação ENEM, Introdução, Episódio 7: revisão e desafio (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_intro_ep7", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "REDAÇÃO ENEM · INTRODUÇÃO · EP. 7", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pegadinhas(c):
    background(c); selo(c); painel(c)
    V.selo(c, 1470, 300, 1, "VERDADEIRO", GREEN, -6, 62)
    V.selo(c, 1470, 500, 1, "FALSO", RED, 5, 80)
    V.selo(c, 1470, 720, 1, "PEGADINHA", AMBER, -4, 64)
    big(c, "VOCÊ CAI", 340)
    big(c, "NESSAS", 470)
    boxed(c, "10 PEGADINHAS?", 70, 520, 100, AMBER)
    text(c, "revisão da introdução da redação", 90, 860, 50, "extrabold", INK2, align="left")


def capa_desafio(c):
    background(c); selo(c); painel(c)
    V.cronometro(c, 1470, 380, 170, 1, 0.7, "10 min")
    for k, (ano, _) in enumerate(V.TEMAS):
        pill(c, ano, 1470 + (k - 1) * 190, 720, BLUE, size=44, anchor="center", bounds=(0, 1920))
    big(c, "DESAFIO:", 340)
    big(c, "3 TEMAS REAIS", 470)
    boxed(c, "2 INTRODUÇÕES", 70, 520, 110, AMBER)
    text(c, "mapa, ponte, tese e dois eixos", 90, 860, 50, "extrabold", INK2, align="left")


def capa_mapa(c):
    background(c); selo(c); painel(c)
    for k in range(6):
        V.icone(c, k, 1300 + (k % 2) * 340, 260 + (k // 2) * 240, 1, 1.4, label=True)
    big(c, "TUDO SOBRE", 340)
    big(c, "A INTRODUÇÃO", 470)
    boxed(c, "EM 1 AULA", 70, 520, 140, PURPLE)
    text(c, "a revisão completa da série", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_pegadinhas", capa_pegadinhas), ("capa_B_desafio_3_temas", capa_desafio), ("capa_C_revisao_completa", capa_mapa)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
