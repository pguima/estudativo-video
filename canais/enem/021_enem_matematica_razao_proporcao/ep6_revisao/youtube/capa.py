"""Capas — Razão, Proporção e Regra de Três, Episódio 6: Revisão geral (tema claro). 3 variações em 1280x720.
Evita o formato "N PEGADINHAS: QUANTAS VOCÊ ACERTA?", já usado nas revisões das séries 019 e 020."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep6", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 6", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_pronto(c):
    background(c); selo(c); painel(c)
    itens = [("pães × preço", "DIRETA", V.DIR), ("pintores × dias", "INVERSA", V.INV), ("lado × área", "NÃO É PROPORCIONAL", AMBER)]
    for k, (s, dec, col) in enumerate(itens):
        y = 250 + k * 240
        text_mid(c, s, 1470, y, 56, "black", INK)
        K.chip(c, dec, 1470, y + 90, col, 1, 54 if len(dec) < 10 else 36)
    big(c, "REGRA DE TRÊS:", 340)
    big(c, "VOCÊ ESTÁ", 470)
    boxed(c, "PRONTO?", 70, 520, 160, GREEN)
    text(c, "treino, V ou F e 5 questões estilo ENEM", 90, 860, 46, "extrabold", INK2, align="left")


def capa_retorno(c):
    background(c); selo(c); painel(c)
    pos = [(1295, 270), (1645, 270), (1295, 540), (1645, 540), (1470, 790)]
    for k, (x, y) in enumerate(pos):
        V.icone(c, k, x, y, 0.88, 1)
    big(c, "O ASSUNTO DE", 340)
    big(c, "MAIOR RETORNO", 470)
    boxed(c, "DA MATEMÁTICA", 70, 520, 140, BLUE)
    text(c, "revisão de razão, proporção e regra de três", 90, 860, 46, "extrabold", INK2, align="left")


def capa_vf(c):
    background(c); selo(c); painel(c)
    itens = [("20 operários → 12 dias", False), ("1 : 50 000 > 1 : 250 000", True), ("lado × 2 → área × 2", False)]
    for k, (s, ver) in enumerate(itens):
        y = 280 + k * 230
        sz = 46
        while K.ftext_w(s, "black", sz) > 470:
            sz -= 2
        K.fmid(c, s, 1390, y, sz, "black", INK)
        if not ver:
            w = K.ftext_w(s, "black", sz)
            strike(c, 1390 - w / 2 - 10, y + 4, 1390 + w / 2 + 10, y + 4, 1, RED, 1)
        K.chip(c, "V" if ver else "F", 1720, y, GREEN if ver else RED, 1, 64)
    big(c, "VERDADEIRO", 340)
    big(c, "OU FALSO?", 470)
    boxed(c, "9 PEGADINHAS", 70, 520, 150, AMBER)
    text(c, "da regra de três no ENEM, uma por uma", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_voce_esta_pronto", capa_pronto), ("capa_B_maior_retorno", capa_retorno),
                     ("capa_C_verdadeiro_ou_falso", capa_vf)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
