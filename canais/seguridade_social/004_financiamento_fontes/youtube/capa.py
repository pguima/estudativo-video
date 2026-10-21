"""Capas do vídeo Seguridade 004 — Financiamento: fontes do art. 195 (tema 'seguridade'). Gera 3 variações em 1280x720."""
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


def capa_dinheiro(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    text(c, "CF, art. 195", 1470, 300, 64, "black", PREST)
    for k, (l, nome) in enumerate((("E", "empregador"), ("T", "trabalhador"), ("C", "concursos"), ("I", "importador"))):
        y = 420 + k * 135
        text(c, l, 1250, y + 36, 110, "black", CUST)
        text(c, nome, 1340, y + 18, 54, "black", INK, align="left")
    text(c, "DE ONDE VEM", 80, 330, 124, "black", INK, align="left")
    text(c, "O DINHEIRO DO", 80, 460, 112, "black", INK, align="left")
    boxed(c, "INSS?", 70, 510, 140, PREST)
    text(c, "financiamento da Seguridade", 90, 820, 54, "extrabold", INK2, align="left")


def capa_farol(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (l, nome) in enumerate((("F", "olha"), ("R", "eceita"), ("L", "ucro"))):
        y = 300 + k * 190
        text(c, l, 1260, y + 50, 150, "black", CUST)
        text(c, nome, 1330, y + 30, 70, "black", INK, align="left")
    text(c, "= FAROL", 1470, 880, 64, "black", PREST)
    text(c, "O MACETE", 80, 330, 124, "black", INK, align="left")
    text(c, "DO FAROL", 80, 460, 124, "black", INK, align="left")
    boxed(c, "ART. 195", 70, 510, 140, CUST, INK)
    text(c, "as contribuições da empresa", 90, 820, 54, "extrabold", INK2, align="left")


def capa_fontes(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (s, col) in enumerate((("DIRETA", CUST), ("contribuições", INK2), ("INDIRETA", BLUE), ("orçamentos", INK2))):
        text(c, s, 1470, 300 + k * 150 + (60 if k > 1 else 0), 80 if k % 2 == 0 else 56, "black", col)
    text(c, "AS FONTES DA", 80, 330, 116, "black", INK, align="left")
    text(c, "SEGURIDADE", 80, 460, 124, "black", INK, align="left")
    boxed(c, "SOCIAL", 70, 510, 140, BLUE)
    text(c, "art. 195 + Lei 8.212 · INSS", 90, 820, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_dinheiro_inss", capa_dinheiro), ("capa_B_farol", capa_farol), ("capa_C_fontes", capa_fontes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
