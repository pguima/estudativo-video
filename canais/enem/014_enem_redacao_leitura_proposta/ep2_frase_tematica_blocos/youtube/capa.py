"""Capas — Redação ENEM, Leitura da Proposta, Episódio 2: A frase temática bloco a bloco (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "REDAÇÃO ENEM · EPISÓDIO 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def pecas_verticais(c, segs, y0=200, gap=150, gone=()):
    for k, (s, col, lab, ob, _) in enumerate(segs):
        y = y0 + k * gap
        x, w = 1200, 540
        a = 0.25 if k in gone else 1
        V.piece(c, x, y, w, 90, col, a, lab, None, 1, k < len(segs) - 1)
        text_mid(c, s, x + w / 2, y + 45, 34 if len(s) < 24 else 28, "black", INK, a)
        if k in gone:
            V.xmark(c, x + w + 20, y + 45, 26, 1, RED, 8)


def capa_blocos(c):
    background(c); selo(c); painel(c)
    pecas_verticais(c, V.T23, 190, 150)
    big(c, "DESMONTE A", 340)
    big(c, "FRASE", 470)
    boxed(c, "TEMÁTICA", 70, 520, 150, GREEN)
    text(c, "bloco a bloco · redação do ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_esqueceu(c):
    background(c); selo(c); painel(c)
    pecas_verticais(c, V.T23, 190, 150, gone=(1, 3))
    big(c, "ESQUECEU UM", 340)
    big(c, "BLOCO? PERDEU", 470)
    boxed(c, "PONTOS", 70, 520, 150, RED)
    text(c, "o erro silencioso da redação do ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_porta(c):
    background(c); selo(c); painel(c)
    c.save(); c.translate(1470, 520); c.scale(0.9, 0.9); c.translate(-1470, -520)
    V.casa(c, 1470, 760, 1, BLUE, "O TEMA", [("frente", 1), ("fundos", 1), ("garagem", 1)])
    c.restore()
    text(c, "escolha a porta,", 1470, 860, 44, "black", GREEN)
    text(c, "não troque de endereço", 1470, 912, 40, "black", RED)
    big(c, "FOCO OU", 340)
    big(c, "CORTE DO", 470)
    boxed(c, "TEMA?", 70, 520, 150, AMBER, INK)
    text(c, "como escolher o foco na redação", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_desmonte_a_frase", capa_blocos), ("capa_B_esqueceu_um_bloco", capa_esqueceu),
                     ("capa_C_foco_ou_corte", capa_porta)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
