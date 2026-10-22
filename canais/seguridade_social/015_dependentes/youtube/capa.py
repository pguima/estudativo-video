"""Capas do vídeo Seguridade 015 — Dependentes (tema 'seguridade'). Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("seguridade")
from motor import *  # noqa

PREST, ASSIST, GEST = "#0F766E", "#E8A317", "#4F46E5"
C1, C2, C3 = PREST, GEST, ASSIST


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


def capa_antonio(c):
    background(c); selo(c); painel(c)
    text(c, "o Antônio faleceu e deixou", 1470, 220, 40, "black", GRAY)
    for k, s in enumerate(("a esposa", "filho de 23 anos", "filho de 16 anos", "a mãe")):
        text(c, s, 1190, 340 + k * 120, 46, "black", INK, align="left")
        text_mid(c, "?", 1740, 325 + k * 120, 54, "black", ASSIST)
    rrect(c, 1170, 780, 600, 120, 22, ASSIST)
    text_mid(c, "QUEM RECEBE?", 1470, 840, 48, "black", INK)
    text(c, "QUEM RECEBE", 80, 330, 124, "black", INK, align="left")
    text(c, "A PENSÃO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "POR MORTE?", 70, 510, 136, RED)
    text(c, "dependentes: o caso que a banca adora", 90, 820, 52, "extrabold", INK2, align="left")


def capa_classes(c):
    background(c); selo(c); painel(c)
    cls = (("I", "cônjuge · filho", "presumida", C1), ("II", "os pais", "comprovada", C2), ("III", "o irmão", "comprovada", C3))
    for k, (rom, s, dep, col) in enumerate(cls):
        y = 170 + k * 255
        rrect(c, 1170, y, 600, 220, 24, col)
        text_mid(c, "CLASSE " + rom, 1470, y + 62, 60, "black", "#FFFFFF")
        text_mid(c, s, 1470, y + 130, 40, "black", "#FFFFFF")
        text_mid(c, dep, 1470, y + 182, 30, "bold", "#FFFFFF")
    text(c, "AS 3 CLASSES", 80, 330, 124, "black", INK, align="left")
    text(c, "DE DEPENDENTES", 80, 460, 104, "black", INK, align="left")
    boxed(c, "ART. 16", 70, 510, 140, PREST)
    text(c, "família nuclear → pais → irmãos", 90, 820, 54, "extrabold", INK2, align="left")


def capa_exclui(c):
    background(c); selo(c); painel(c)
    def linha(s, y, ok, size=44):
        text(c, s, 1190, y, size, "black", INK, align="left")
        check_icon(c, 1740, y - 15, 30, 1, GREEN if ok else RED, "check" if ok else "x")
    linha("cônjuge + pais: rateio", 260, False, 40)
    linha("pais: presumida", 400, False)
    linha("faculdade até 24", 540, False)
    linha("emancipou: perde", 680, True)
    linha("enteado: comprova", 820, True)
    text(c, "NÃO É", 80, 330, 124, "black", INK, align="left")
    text(c, "PREFERÊNCIA:", 80, 460, 116, "black", INK, align="left")
    boxed(c, "EXCLUI!", 70, 510, 140, RED)
    text(c, "as pegadinhas dos dependentes do INSS", 90, 820, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_caso_antonio", capa_antonio), ("capa_B_tres_classes", capa_classes),
                     ("capa_C_exclui", capa_exclui)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
