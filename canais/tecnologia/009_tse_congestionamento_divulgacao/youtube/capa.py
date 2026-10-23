"""Capas do vídeo Tecnologia 009 — O que aconteceu com o sistema do TSE durante a divulgação dos votos? (tema 'tech').
Gera 3 variações em 1280x720. Só motion graphics: nada de foto, manchete ou tela real; reconstruções com selo."""
import math, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
sys.path.insert(0, str(HERE.parent / "roteiro"))
import skia
import tech
from motor import *  # noqa
from tech import *  # noqa
import visual as V  # também troca a fonte mono para DejaVu Sans Mono


def base(c, col=CYAN, tag="TSE  ·  ELEIÇÕES 2026  ·  TECNOLOGIA"):
    tech.background(c, 3.0)
    m = 34
    for x, y, dx, dy in ((m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)):
        tech._bracket(c, x, y, dx, dy, col, 0.7)
    chip(c, tag, 84, 110, col, 1, size=34, filled=True)


def big(c, l1, l2, word, col):
    for s, y in ((l1, 330), (l2, 460)):
        size = min(120, 120 * 1000 / text_w(s, "black", 120))
        glow_text(c, s, 80, y, size, "black", INK, 1, align="left", glow=0.15)
    size = min(140, 140 * 900 / text_w(word, "black", 140))
    w = text_w(word, "black", size) + 70
    p = chamfer_path(70, 510, w, 175, 40)
    c.drawPath(p, blur_paint(col, 0.6, 26))
    c.drawPath(p, paint(col))
    text_mid(c, word, 70 + w / 2, 597, size, "black", "#03050B")


def lado_congelado(c):
    """tela de resultados congelada — reconstrução genérica, com selo"""
    x, y, w, h = 1140, 150, 680, 760
    panel(c, x, y, w, h, 1, ROSE, label="reconstrução")
    text(c, "TOTALIZAÇÃO", x + 50, y + 100, 34, "monob", INK2, 1, align="left")
    glow_text(c, "64%", x + w / 2, y + 360, 230, "black", GOLD, 1, glow=0.4)
    bar_meter(c, x + 50, y + 420, w - 100, 28, 0.64, GOLD, 1)
    V.pause_icon(c, x + w / 2, y + 560, 110, 1, ROSE)
    chip(c, "ATUALIZAÇÃO PAUSADA", x + w / 2, y + 670, ROSE, 1, anchor="center", size=30, filled=True)
    V.glitch(c, x, y, w, h, 2.3, 0.8)
    V.selo(c, x + w / 2, y + h + 50, 1, anchor="center", size=24)


def lado_relogio(c):
    x, y, w, h = 1140, 150, 680, 800
    panel(c, x, y, w, h, 1, GOLD, label="04/10/2026")
    for k, (hh, pct, col) in enumerate((("19h", "64%", GOLD), ("20h", "84%", LIME))):
        yy = y + 120 + k * 380
        glow_text(c, hh, x + 60, yy + 110, 96, "black", INK, 1, align="left", glow=0.15)
        glow_text(c, pct, x + w - 50, yy + 110, 120, "black", col, 1, align="right", glow=0.4)
        text(c, "por volta das", x + 64, yy + 10, 26, "mono", DIM, 1, align="left")
    glow_line(c, x + 60, y + 400, x + w - 60, y + 400, ROSE, 1, 5)
    chip(c, "CERCA DE 1 HORA SEM ATUALIZAR", x + w / 2, y + 400, ROSE, 1, anchor="center", size=26, filled=True)


def lado_etapas(c):
    x, y, w, h = 1140, 150, 680, 800
    panel(c, x, y, w, h, 1, VIOLET, label="3 etapas")
    labs = (("APURAÇÃO", CYAN), ("TOTALIZAÇÃO", VIOLET), ("DIVULGAÇÃO", GOLD))
    for k, (lab, col) in enumerate(labs):
        cy = y + 150 + k * 250
        if k:
            link(c, x + 170, cy - 250 + 70, x + 170, cy - 70, labs[k - 1][1], 1, 0.3, dash=(k == 2), pulses=0 if k == 2 else 3)
        node(c, x + 170, cy, 68, None, None, col, 1, 0.0)
        if k == 0:
            V.urna(c, x + 170, cy, 50, 1, col)
        elif k == 1:
            V.sigma(c, x + 170, cy, 58, 1, col)
        else:
            V.pause_icon(c, x + 170, cy, 60, 1, col)
        text(c, lab, x + 270, cy + 16, 50, "black", INK, 1, align="left")


def capa_aconteceu(c):
    base(c, CYAN)
    big(c, "O QUE ACONTECEU", "COM O SISTEMA", "DO TSE?", CYAN)
    text(c, "o travamento da divulgação dos votos", 90, 800, 44, "monob", INK2, align="left")
    lado_congelado(c)


def capa_uma_hora(c):
    base(c, GOLD)
    big(c, "CERCA DE 1 HORA", "SEM ATUALIZAR:", "64% → 84%", GOLD)
    text(c, "o que o TSE explicou e o que falta saber", 90, 800, 40, "monob", INK2, align="left")
    lado_relogio(c)


def capa_contagem(c):
    base(c, VIOLET)
    big(c, "A CONTAGEM", "DOS VOTOS", "PAROU?", VIOLET)
    text(c, "apuração · totalização · divulgação", 90, 800, 44, "monob", INK2, align="left")
    lado_etapas(c)


if __name__ == "__main__":
    for nome, fn in (("capa_A_o_que_aconteceu", capa_aconteceu), ("capa_B_uma_hora", capa_uma_hora),
                     ("capa_C_contagem_parou", capa_contagem)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
