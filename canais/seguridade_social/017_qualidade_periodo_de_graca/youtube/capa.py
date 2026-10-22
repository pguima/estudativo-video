"""Capas do vídeo Seguridade 017 — Qualidade de segurado e período de graça (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

PREST, ASSIST, GEST, MANT = "#0F766E", "#E8A317", "#4F46E5", "#16A36A"


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "SEGURIDADE SOCIAL · INSS", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_carlos(c):
    background(c); selo(c); painel(c)
    text(c, "o caso do Carlos", 1470, 220, 46, "black", GRAY)
    for k, s in enumerate(("180 contribuições", "demitido", "registrado como", "desempregado")):
        text(c, s, 1190, 340 + k * 90, 46, "black", INK, align="left")
    for k, s in enumerate(("12?", "24?", "36?")):
        x = 1240 + k * 230
        rrect(c, x - 95, 730, 190, 130, 22, ASSIST)
        text_mid(c, s, x, 795, 60, "black", INK)
    text(c, "QUANTOS MESES", 80, 330, 112, "black", INK, align="left")
    text(c, "ELE CONTINUA", 80, 460, 112, "black", INK, align="left")
    boxed(c, "PROTEGIDO?", 70, 510, 140, MANT)
    text(c, "período de graça · o que mais cai no INSS", 90, 820, 50, "extrabold", INK2, align="left")


def capa_escada(c):
    background(c); selo(c); painel(c)
    for k, (n, sub, col) in enumerate((("12", "a regra", PREST), ("24", "+120 contrib. OU desemprego", ASSIST),
                                       ("36", "as duas juntas", MANT))):
        h = 230 + k * 140
        x = 1160 + k * 210
        rrect(c, x, 900 - h, 195, h, 22, col)
        text_mid(c, n, x + 97, 900 - h + 80, 86, "black", "#FFFFFF")
    text(c, "12 → 24 → 36", 1470, 230, 64, "black", INK)
    text(c, "DECORE", 80, 330, 124, "black", INK, align="left")
    text(c, "A ESCADA", 80, 460, 124, "black", INK, align="left")
    boxed(c, "DO PRAZO", 70, 510, 140, ASSIST, INK)
    text(c, "período de graça · art. 15, §§ 1º e 2º", 90, 820, 54, "extrabold", INK2, align="left")


def capa_prazos(c):
    background(c); selo(c); painel(c)
    rows = (("I", "benefício", "∞", MANT), ("II", "parou", "12", PREST), ("III", "segregação", "12", PREST),
            ("IV", "preso", "12", PREST), ("V", "militar", "3", GEST), ("VI", "facultativo", "6", GEST))
    for k, (rom, s, n, col) in enumerate(rows):
        y = 210 + k * 125
        text(c, rom, 1190, y + 20, 42, "black", GRAY, align="left")
        text(c, s, 1300, y + 20, 44, "black", INK, align="left")
        rrect(c, 1620, y - 40, 150, 90, 20, col)
        text_mid(c, n, 1695, y + 5, 54, "black", "#FFFFFF")
    text(c, "TRÊS É O", 80, 330, 124, "black", INK, align="left")
    text(c, "MILITAR,", 80, 460, 124, "black", INK, align="left")
    boxed(c, "SEIS É...", 70, 510, 140, GEST)
    text(c, "os 6 prazos do art. 15 que a banca cobra", 90, 820, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_caso_carlos", capa_carlos), ("capa_B_escada", capa_escada),
                     ("capa_C_prazos", capa_prazos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
