"""Capas do vídeo Seguridade 010 — A estrutura do RGPS (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

PREST, ASSIST, GEST = "#0F766E", "#E8A317", "#4F46E5"


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "SEGURIDADE SOCIAL · INSS", 84, 90, BLUE, size=40, bounds=(0, 1920))


def capa_dois_tipos(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (n, sub, col) in enumerate((("SEGURADO", "quem contribui", PREST), ("DEPENDENTE", "quem depende", ASSIST))):
        y = 230 + k * 330
        rrect(c, 1180, y, 580, 150, 26, col)
        text_mid(c, n, 1470, y + 75, 66, "black", "#FFFFFF")
        text(c, sub, 1470, y + 230, 48, "black", INK)
    text(c, "SÓ EXISTEM", 80, 330, 124, "black", INK, align="left")
    text(c, "DOIS TIPOS NO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "INSS", 70, 510, 140, PREST)
    text(c, "a estrutura do RGPS · Lei 8.213", 90, 820, 54, "extrabold", INK2, align="left")


def capa_incisos(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, r in enumerate(("I", "II", "III", "IV", "V", "VI", "VII")):
        y = 175 + k * 108
        miss = r in ("III", "IV")
        rrect(c, 1290, y, 360, 88, 18, RED if miss else PREST)
        text_mid(c, r + (" revogado" if miss else ""), 1470, y + 44, 44 if not miss else 36, "black", "#FFFFFF")
    text(c, "CADÊ O III", 80, 330, 124, "black", INK, align="left")
    text(c, "E O IV DO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "ART. 11?", 70, 510, 140, RED)
    text(c, "segurados obrigatórios · INSS", 90, 820, 54, "extrabold", INK2, align="left")


def capa_macetes(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (s, sub, col) in enumerate((("E·E·C·T·S", "segurados obrigatórios", PREST), ("P · A", "só do dependente", ASSIST),
                                       ("8.212 · 8.213", "custeio · benefícios", GEST))):
        y = 320 + k * 230
        text(c, s, 1470, y, 76, "black", col)
        text(c, sub, 1470, y + 70, 42, "bold", GRAY)
    text(c, "O RGPS EM", 80, 330, 124, "black", INK, align="left")
    text(c, "3 MACETES", 80, 460, 124, "black", INK, align="left")
    boxed(c, "INSS", 70, 510, 140, PREST)
    text(c, "segurados, dependentes e prestações", 90, 820, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_dois_tipos", capa_dois_tipos), ("capa_B_incisos_revogados", capa_incisos),
                     ("capa_C_tres_macetes", capa_macetes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
