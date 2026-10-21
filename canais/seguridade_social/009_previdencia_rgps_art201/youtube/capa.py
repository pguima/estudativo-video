"""Capas do vídeo Seguridade 009 — Previdência Social e RGPS (art. 201) (tema 'seguridade'). Gera 3 variações em 1280x720."""
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


def capa_gratis(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (n, col, s, ok) in enumerate((("SAÚDE", "#E5484D", "de graça", True), ("ASSISTÊNCIA", ASSIST, "de graça", True),
                                         ("PREVIDÊNCIA", PREST, "só contribuindo", False))):
        y = 230 + k * 240
        rrect(c, 1190, y, 560, 100, 22, col)
        text_mid(c, n, 1470, y + 50, 50, "black", "#FFFFFF")
        text(c, s, 1470, y + 165, 46, "black", INK if ok else RED)
    text(c, "AQUI NINGUÉM", 80, 330, 124, "black", INK, align="left")
    text(c, "ENTRA DE", 80, 460, 124, "black", INK, align="left")
    boxed(c, "GRAÇA", 70, 510, 140, PREST)
    text(c, "previdência social · CF art. 201 · INSS", 90, 820, 50, "extrabold", INK2, align="left")


def capa_cfe(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (l, rest) in enumerate((("C", "ontributivo"), ("F", "iliação obrigatória"), ("E", "quilíbrio"))):
        y = 340 + k * 220
        text(c, l, 1260, y, 170, "black", PREST, align="center")
        text(c, rest, 1340, y - 20, 46, "black", INK, align="left")
    text(c, "ART. 201 EM", 80, 330, 124, "black", INK, align="left")
    text(c, "3 LETRAS", 80, 460, 124, "black", INK, align="left")
    boxed(c, "C · F · E", 70, 510, 140, ASSIST, INK)
    text(c, "o macete do RGPS · INSS", 90, 820, 54, "extrabold", INK2, align="left")


def capa_idades(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (tit, h, m, col) in enumerate((("REGRA GERAL", "65", "62", PREST), ("RURAL", "60", "55", ASSIST))):
        y0 = 230 + k * 380
        text(c, tit, 1470, y0, 44, "black", col)
        for j, (lab, n) in enumerate((("HOMEM", h), ("MULHER", m))):
            cx = 1320 + j * 300
            text(c, n, cx, y0 + 170, 150, "black", col)
            text(c, lab, cx, y0 + 230, 34, "black", GRAY)
    text(c, "IDADE PARA SE", 80, 330, 118, "black", INK, align="left")
    text(c, "APOSENTAR NO", 80, 460, 118, "black", INK, align="left")
    boxed(c, "INSS", 70, 510, 140, PREST)
    text(c, "art. 201, §7º · reforma de 2019", 90, 820, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_ninguem_entra_de_graca", capa_gratis), ("capa_B_cfe", capa_cfe),
                     ("capa_C_idades", capa_idades)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
