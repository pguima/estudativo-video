"""Capas — Redação ENEM, Introdução, Episódio 3: a ponte e o teste da retirada (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

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
    pill(c, "REDAÇÃO ENEM · INTRODUÇÃO · EP. 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def folha_aristoteles(c, riscar=True):
    V.paper(c, 1170, 200, 600, 520, 1.0, lh=60, top=260)
    linhas = ["Segundo Aristóteles,", "o homem é um", "animal político..."]
    for k, ln in enumerate(linhas):
        V.hand(c, ln, 1270, 340 + k * 60, 44, V.PEN)
        if riscar:
            strike(c, 1260, 326 + k * 60, 1280 + V.hand_w(ln, 44), 326 + k * 60, 1.0, RED, 1.0)


def capa_apagada(c):
    background(c); selo(c); painel(c)
    folha_aristoteles(c)
    V.selo(c, 1470, 820, 1, "REPERTÓRIO DE BOLSO", AMBER, -5, 46)
    big(c, "SUA CITAÇÃO", 340)
    big(c, "DE FILÓSOFO", 470)
    boxed(c, "PODE SUMIR?", 70, 520, 130, RED)
    text(c, "o teste da retirada na redação do ENEM", 90, 860, 46, "extrabold", INK2, align="left")


def capa_teste(c):
    background(c); selo(c); painel(c)
    folha_aristoteles(c)
    V.selo(c, 1470, 820, 1, "NADA MUDOU", RED, -5, 70)
    big(c, "TIROU A", 340)
    big(c, "REFERÊNCIA?", 470)
    boxed(c, "NADA MUDOU?", 70, 530, 112, AMBER)
    text(c, "então ela não estava trabalhando", 90, 860, 50, "extrabold", INK2, align="left")


def capa_ponte(c):
    background(c); selo(c); painel(c)
    V.mapa_rua(c, 1170, 220, 600, 500, 1.0, rua=1.0, casa=1.0)
    V.selo(c, 1470, 820, 1, "PONTE = RUA DE ACESSO", GREEN, -4, 40)
    big(c, "A FRASE QUE", 340)
    big(c, "LIGA TUDO", 470)
    boxed(c, "A PONTE", 70, 520, 150, GREEN)
    text(c, "da referência ao tema da redação", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_citacao_apagada", capa_apagada), ("capa_B_nada_mudou", capa_teste), ("capa_C_a_ponte", capa_ponte)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
