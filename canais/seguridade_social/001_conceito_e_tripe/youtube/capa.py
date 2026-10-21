"""Capas do vídeo Seguridade 001 — Conceito e tripé (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

SAUDE, PREV, ASSIST = "#E5484D", "#0F766E", "#E8A317"


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "SEGURIDADE SOCIAL · INSS", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel_tripe(c, destaque_prev=False):
    x, y, w, h = 1120, 120, 700, 840
    card(c, x, y, w, h, r=36)
    for k, (nome, col, g) in enumerate((("SAÚDE", SAUDE, ""), ("PREVIDÊNCIA", PREV, ""), ("ASSISTÊNCIA", ASSIST, ""))):
        yy = y + 50 + k * 260
        a = 1.0 if (not destaque_prev or k == 1) else 0.35
        rrect(c, x + 40, yy, w - 80, 230, 24, col, 0.12 * a)
        icon(c, g, x + 130, yy + 115, 90, col, a)
        text(c, nome, x + 210, yy + 135, 56, "black", col, a, align="left")
        if destaque_prev and k == 1:
            pill(c, "R$", x + w - 80, yy + 115, PREV, size=44, anchor="right", bounds=(0, 1920))


def capa_tripe(c):
    background(c)
    selo(c)
    painel_tripe(c)
    text(c, "SEGURIDADE", 80, 330, 128, "black", INK, align="left")
    text(c, "SOCIAL", 80, 460, 128, "black", INK, align="left")
    boxed(c, "DO ZERO", 70, 510, 136, BLUE)
    text(c, "o tripé que cai no INSS", 90, 820, 58, "extrabold", INK2, align="left")


def capa_pegadinha(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    text(c, "“...dos Poderes", 1470, 330, 56, "bold", INK)
    text(c, "Públicos", 1470, 400, 56, "bold", INK)
    text(c, "e da sociedade”", 1470, 520, 60, "black", RED)
    line(c, 1250, 500, 1690, 500, RED, 1, 9)
    check_icon(c, 1470, 700, 70, 1, RED, "x")
    text(c, "1 PALAVRA", 80, 340, 136, "black", INK, align="left")
    text(c, "DERRUBA", 80, 475, 136, "black", INK, align="left")
    boxed(c, "VOCÊ NO INSS", 70, 525, 100, RED)
    text(c, "conceito de Seguridade Social", 90, 820, 54, "extrabold", INK2, align="left")


def capa_spa(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (l, col) in enumerate((("S", SAUDE), ("P", PREV), ("A", ASSIST))):
        text(c, l, 1270 + k * 200, 590, 250, "black", col)
    pill(c, "só o P é pago", 1470, 790, PREV, size=46, anchor="center", bounds=(0, 1920))
    text(c, "A SEGURIDADE", 80, 340, 124, "black", INK, align="left")
    text(c, "SOCIAL É", 80, 470, 124, "black", INK, align="left")
    boxed(c, "UM SPA", 70, 520, 140, BLUE)
    text(c, "o macete do tripé para o INSS", 90, 820, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_tripe", capa_tripe), ("capa_B_uma_palavra", capa_pegadinha), ("capa_C_spa", capa_spa)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
