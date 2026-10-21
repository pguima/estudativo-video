"""Capas do vídeo Seguridade 005 — Contrapartida, noventena, imunidade e orçamento (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

SAUDE, PREST, CUST, GEST = "#E5484D", "#0F766E", "#E8A317", "#4F46E5"


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "SEGURIDADE SOCIAL · INSS", 84, 90, BLUE, size=40, bounds=(0, 1920))


def capa_isenta(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    text(c, "§7º", 1470, 260, 64, "black", SAUDE)
    text(c, "o texto diz", 1470, 380, 48, "bold", GRAY)
    text(c, "ISENTAS", 1470, 480, 90, "black", INK)
    line(c, 1250, 540, 1690, 540, LIGHT, 1, 4)
    text(c, "a natureza é", 1470, 640, 48, "bold", GRAY)
    text(c, "IMUNIDADE", 1470, 750, 90, "black", SAUDE)
    text(c, "ISENÇÃO OU", 80, 330, 124, "black", INK, align="left")
    text(c, "IMUNIDADE?", 80, 460, 124, "black", INK, align="left")
    boxed(c, "PEGADINHA", 70, 510, 130, SAUDE)
    text(c, "os parágrafos do art. 195", 90, 820, 54, "extrabold", INK2, align="left")


def capa_numeros(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (num, s, col) in enumerate((("TOTAL", "custeio · §5º", PREST), ("90", "dias · §6º", CUST), ("60", "meses · §11", SAUDE))):
        y = 290 + k * 240
        text(c, num, 1470, y + 20, 120, "black", col)
        text(c, s, 1470, y + 90, 46, "bold", INK2)
    text(c, "AS PALAVRAS", 80, 330, 120, "black", INK, align="left")
    text(c, "QUE A BANCA", 80, 460, 120, "black", INK, align="left")
    boxed(c, "TROCA", 70, 510, 140, CUST, INK)
    text(c, "contrapartida, noventena e mais", 90, 820, 54, "extrabold", INK2, align="left")


def capa_paragrafos(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (tag, s, col) in enumerate((("§5º", "contrapartida", PREST), ("§6º", "noventena", CUST),
                                        ("§7º", "imunidade", SAUDE), ("LOA", "orçamento", BLUE))):
        y = 250 + k * 175
        rrect(c, 1200, y, 170, 110, 20, col)
        text_mid(c, tag, 1285, y + 55, 52, "black", "#FFFFFF")
        text_mid(c, s, 1400, y + 55, 52, "black", INK, align="left")
    text(c, "CONTRAPARTIDA", 80, 330, 108, "black", INK, align="left")
    text(c, "E NOVENTENA", 80, 460, 116, "black", INK, align="left")
    boxed(c, "ART. 195", 70, 510, 140, PREST)
    text(c, "imunidade e orçamento · INSS", 90, 820, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_isencao_imunidade", capa_isenta), ("capa_B_palavras_banca", capa_numeros),
                     ("capa_C_paragrafos", capa_paragrafos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
