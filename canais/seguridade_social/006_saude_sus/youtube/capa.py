"""Capas do vídeo Seguridade 006 — Saúde e SUS na Constituição (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

SAUDE, PREST, CUST = "#E5484D", "#0F766E", "#E8A317"


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "SEGURIDADE SOCIAL · INSS", 84, 90, BLUE, size=40, bounds=(0, 1920))


def cruz(c, cx, cy, s, col):
    k = s / 3
    rrect(c, cx - k / 2, cy - s / 2, k, s, k * 0.25, col)
    rrect(c, cx - s / 2, cy - k / 2, s, k, k * 0.25, col)


def capa_contribuir(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    cruz(c, 1470, 380, 300, SAUDE)
    text(c, "direito de", 1470, 680, 60, "bold", GRAY)
    text(c, "TODOS", 1470, 800, 120, "black", SAUDE)
    text(c, "PRECISA PAGAR", 80, 330, 116, "black", INK, align="left")
    text(c, "INSS PARA USAR", 80, 460, 116, "black", INK, align="left")
    boxed(c, "O SUS?", 70, 510, 140, SAUDE)
    text(c, "saúde na Constituição · arts. 196 a 200", 90, 820, 50, "extrabold", INK2, align="left")


def capa_reducao(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    text(c, "art. 196", 1470, 250, 56, "black", SAUDE)
    text(c, "REDUÇÃO", 1470, 430, 100, "black", GREEN)
    text(c, "do risco", 1470, 510, 50, "bold", GRAY)
    text(c, "ELIMINAÇÃO", 1470, 720, 92, "black", RED)
    line(c, 1220, 690, 1720, 690, RED, 1, 10)
    text(c, "do risco", 1470, 800, 50, "bold", GRAY)
    text(c, "A PALAVRA QUE", 80, 330, 116, "black", INK, align="left")
    text(c, "DERRUBA NA", 80, 460, 116, "black", INK, align="left")
    boxed(c, "SAÚDE", 70, 510, 140, SAUDE)
    text(c, "a pegadinha do art. 196 · INSS", 90, 820, 54, "extrabold", INK2, align="left")


def capa_dap(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (l, rest) in enumerate((("D", "escentralização"), ("A", "tendimento"), ("P", "articipação"))):
        y = 330 + k * 200
        text(c, l, 1250, y + 40, 150, "black", PREST)
        text(c, rest, 1320, y + 20, 48, "black", INK, align="left")
    text(c, "SAÚDE E SUS", 80, 330, 124, "black", INK, align="left")
    text(c, "NA PROVA DO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "INSS", 70, 510, 140, PREST)
    text(c, "arts. 196 a 200 · diretrizes D-A-P", 90, 820, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_pagar_inss_sus", capa_contribuir), ("capa_B_reducao_eliminacao", capa_reducao),
                     ("capa_C_dap", capa_dap)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
