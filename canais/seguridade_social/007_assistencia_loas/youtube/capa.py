"""Capas do vídeo Seguridade 007 — Assistência Social e LOAS (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

PREST, ASSIST = "#0F766E", "#E8A317"


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "SEGURIDADE SOCIAL · INSS", 84, 90, BLUE, size=40, bounds=(0, 1920))


def capa_precisa(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    text(c, "art. 203", 1470, 250, 56, "black", ASSIST)
    text(c, "a quem dela", 1470, 400, 64, "black", INK)
    text(c, "NECESSITAR", 1470, 490, 76, "black", ASSIST)
    line(c, 1240, 560, 1700, 560, LIGHT, 1, 4)
    text(c, "contribuição?", 1470, 680, 60, "black", INK)
    text(c, "NÃO EXIGE", 1470, 790, 80, "black", RED)
    text(c, "A ÚNICA", 80, 330, 124, "black", INK, align="left")
    text(c, "PERGUNTA DA", 80, 460, 124, "black", INK, align="left")
    boxed(c, "ASSISTÊNCIA", 70, 510, 128, ASSIST, INK)
    text(c, "arts. 203 e 204 + LOAS · INSS", 90, 820, 54, "extrabold", INK2, align="left")


def capa_funeral(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    text(c, "auxílio-funeral", 1470, 280, 62, "black", INK)
    text(c, "PREVIDÊNCIA", 1470, 430, 76, "black", RED)
    line(c, 1240, 405, 1700, 405, RED, 1, 9)
    text(c, "↓", 1470, 560, 90, "black", GRAY)
    text(c, "ASSISTÊNCIA", 1470, 700, 76, "black", GREEN)
    text(c, "benefício eventual", 1470, 790, 46, "bold", GRAY)
    text(c, "O BENEFÍCIO", 80, 330, 124, "black", INK, align="left")
    text(c, "QUE MUDOU", 80, 460, 124, "black", INK, align="left")
    boxed(c, "DE LADO", 70, 510, 140, RED)
    text(c, "a pegadinha da LOAS · INSS", 90, 820, 54, "extrabold", INK2, align="left")


def capa_macetes(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (s, col) in enumerate((("P · V · D", ASSIST), ("S · U · R · I · D", PREST), ("D · P · P", ASSIST))):
        text(c, s, 1470, 330 + k * 230, 84, "black", col)
        text(c, ("objetivos", "princípios", "diretrizes")[k], 1470, 400 + k * 230, 44, "bold", GRAY)
    text(c, "LOAS EM 3", 80, 330, 124, "black", INK, align="left")
    text(c, "MACETES", 80, 460, 124, "black", INK, align="left")
    boxed(c, "INSS", 70, 510, 140, PREST)
    text(c, "assistência social · Lei 8.742", 90, 820, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_unica_pergunta", capa_precisa), ("capa_B_auxilio_funeral", capa_funeral),
                     ("capa_C_macetes_loas", capa_macetes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
