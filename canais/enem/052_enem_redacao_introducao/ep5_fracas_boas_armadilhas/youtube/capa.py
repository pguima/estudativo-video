"""Capas — Redação ENEM, Introdução, Episódio 5: introduções fracas × boas e as armadilhas (tema claro). 3 variações em 1280x720."""
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
    pill(c, "REDAÇÃO ENEM · INTRODUÇÃO · EP. 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_aristoteles(c):
    background(c); selo(c); painel(c)
    c.save(); c.translate(1470, 360); c.rotate(-6)
    V.cartao_postal(c, -230, -140, 460, 280, 1)
    c.restore()
    text(c, "“Segundo Aristóteles…”", 1470, 600, 44, "black", INK2)
    V.selo(c, 1470, 760, 1, "REPERTÓRIO DE BOLSO", RED, -5, 46)
    big(c, "ARISTÓTELES", 340)
    big(c, "NA INTRODUÇÃO?", 470)
    boxed(c, "CUIDADO", 70, 520, 140, RED)
    text(c, "3 versões, só 1 funciona no ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_versoes(c):
    background(c); selo(c); painel(c)
    for k, (oks, lab, col) in enumerate((([0, 0, 0, 0], "VERSÃO 1", RED), ([0, 0, 0, 0], "VERSÃO 2", RED),
                                         ([1, 1, 1, 1], "VERSÃO 3", GREEN))):
        y = 310 + k * 265
        text(c, lab, 1470, y - 112, 26, "black", col, tracking=2)
        V.mini_etiqueta(c, 1470, y, 1, oks, 1.1)
    big(c, "3 INTRODUÇÕES,", 340)
    big(c, "SÓ 1 FUNCIONA", 470)
    boxed(c, "QUAL?", 70, 520, 140, AMBER)
    text(c, "fraca × boa, lado a lado, no ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_armadilhas(c):
    background(c); selo(c); painel(c)
    for k, s in enumerate(("“Desde os primórdios…”", "“Pesquisas mostram que 90%…”", "“Até quando?”")):
        y = 260 + k * 220
        rrect(c, 1170, y, 600, 130, 16, V.PAPER, 1, shadow=True)
        text_mid(c, s, 1470, y + 65, 38 if len(s) < 25 else 32, "black", V.PEN)
        V.selo(c, 1690, y + 10, 1, "PEGADINHA", AMBER, 6, 26)
    big(c, "7 ARMADILHAS", 340)
    big(c, "DO 1º PARÁGRAFO", 470)
    boxed(c, "VOCÊ USA?", 70, 520, 140, AMBER)
    text(c, "introdução da redação do ENEM", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_aristoteles", capa_aristoteles), ("capa_B_tres_versoes", capa_versoes),
                     ("capa_C_7_armadilhas", capa_armadilhas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
