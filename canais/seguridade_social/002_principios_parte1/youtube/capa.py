"""Capas do vídeo Seguridade 002 — Princípios parte 1 (tema 'seguridade'). Gera 3 variações em 1280x720."""
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


def capa_mais_cobrado(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (rom, nome) in enumerate((("I", "Universalidade"), ("II", "Uniformidade"), ("III", "Seletividade"))):
        y = 290 + k * 230
        w = text_w(rom, "black", 70) + 50
        rrect(c, 1170, y - 55, w, 110, 18, PREST)
        text_mid(c, rom, 1170 + w / 2, y, 70, "black", "#FFFFFF")
        text(c, nome, 1200 + w, y + 22, 54, "black", INK, align="left")
    text(c, "O ASSUNTO", 80, 330, 128, "black", INK, align="left")
    text(c, "MAIS COBRADO", 80, 460, 120, "black", INK, align="left")
    boxed(c, "DO INSS", 70, 510, 136, RED)
    text(c, "princípios da Seguridade · parte 1", 90, 820, 52, "extrabold", INK2, align="left")


def capa_cobertura(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    text(c, "COBERTURA", 1470, 330, 76, "black", BLUE)
    text(c, "= COISA", 1470, 420, 64, "black", INK)
    text(c, "ATENDIMENTO", 1470, 640, 72, "black", GEST)
    text(c, "= ALGUÉM", 1470, 730, 64, "black", INK)
    text(c, "COBERTURA", 80, 330, 124, "black", INK, align="left")
    text(c, "OU", 80, 460, 124, "black", INK, align="left")
    boxed(c, "ATENDIMENTO?", 70, 510, 108, RED)
    text(c, "a pegadinha que mais derruba", 90, 820, 54, "extrabold", INK2, align="left")


def capa_mnemonico(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    words = ["Um", "Universo", "Seleto", "Irredutível", "Equilibra", "Diversas", "Comunidades"]
    cols = [PREST, PREST, PREST, PREST, CUST, CUST, GEST]
    for k, (wd, col) in enumerate(zip(words, cols)):
        y = 220 + k * 108
        text(c, wd[0], 1220, y, 74, "black", col, align="left")
        text(c, wd[1:], 1220 + text_w(wd[0], "black", 74), y, 74, "black", INK, align="left")
    text(c, "DECORE OS", 80, 330, 128, "black", INK, align="left")
    text(c, "7 PRINCÍPIOS", 80, 460, 120, "black", INK, align="left")
    boxed(c, "COM 1 FRASE", 70, 510, 120, BLUE)
    text(c, "art. 194 · Seguridade Social", 90, 820, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_mais_cobrado", capa_mais_cobrado), ("capa_B_cobertura_atendimento", capa_cobertura),
                     ("capa_C_frase_7_principios", capa_mnemonico)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
