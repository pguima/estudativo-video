"""Capas do vídeo Seguridade 003 — Princípios parte 2 (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

PREST, CUST, GEST = "#0F766E", "#E8A317", "#4F46E5"


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "SEGURIDADE SOCIAL · INSS", 84, 90, BLUE, size=40, bounds=(0, 1920))


def capa_piso(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    text(c, "auxílio-acidente", 1470, 330, 56, "black", PREST)
    text(c, "< 1 salário", 1470, 500, 92, "black", INK)
    text(c, "mínimo", 1470, 600, 92, "black", INK)
    check_icon(c, 1470, 760, 60, 1, GREEN)
    text(c, "BENEFÍCIO", 80, 330, 124, "black", INK, align="left")
    text(c, "MENOR QUE O", 80, 460, 124, "black", INK, align="left")
    boxed(c, "MÍNIMO?", 70, 510, 140, RED)
    text(c, "a pegadinha do piso no INSS", 90, 820, 54, "extrabold", INK2, align="left")


def capa_teag(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (l, nome) in enumerate((("T", "trabalhadores"), ("E", "empregadores"), ("A", "aposentados"), ("G", "Governo"))):
        y = 260 + k * 185
        text(c, l, 1250, y + 40, 130, "black", GEST)
        text(c, nome, 1340, y + 20, 54, "black", INK, align="left")
    text(c, "QUEM MANDA", 80, 330, 124, "black", INK, align="left")
    text(c, "NA SEGURIDADE", 80, 460, 108, "black", INK, align="left")
    boxed(c, "SOCIAL?", 70, 510, 140, GEST)
    text(c, "gestão quadripartite · INSS", 90, 820, 54, "extrabold", INK2, align="left")


def capa_parte2(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (rom, nome, col) in enumerate((("IV", "Irredutibilidade", PREST), ("V", "Equidade", CUST),
                                          ("VI", "Diversidade", CUST), ("VII", "Gestão", GEST))):
        y = 250 + k * 180
        w = text_w(rom, "black", 64) + 44
        rrect(c, 1170, y - 52, w, 104, 18, col)
        text_mid(c, rom, 1170 + w / 2, y, 64, "black", "#FFFFFF")
        text(c, nome, 1200 + w, y + 20, 52, "black", INK, align="left")
    text(c, "7 PRINCÍPIOS", 80, 330, 124, "black", INK, align="left")
    text(c, "DO INSS", 80, 460, 124, "black", INK, align="left")
    boxed(c, "PARTE 2", 70, 510, 140, BLUE)
    text(c, "o assunto mais cobrado", 90, 820, 58, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_piso_salario_minimo", capa_piso), ("capa_B_quem_manda", capa_teag), ("capa_C_parte2", capa_parte2)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
