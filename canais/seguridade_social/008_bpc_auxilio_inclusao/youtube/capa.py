"""Capas do vídeo Seguridade 008 — BPC e auxílio-inclusão (tema 'seguridade'). Gera 3 variações em 1280x720."""
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


def capa_nao_e(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    text(c, "BPC", 1470, 300, 150, "black", ASSIST)
    text(c, "pago pelo INSS", 1470, 420, 52, "black", INK)
    text(c, "1 salário mínimo", 1470, 500, 52, "black", INK)
    line(c, 1240, 570, 1700, 570, LIGHT, 1, 4)
    text(c, "natureza", 1470, 670, 46, "bold", GRAY)
    text(c, "ASSISTENCIAL", 1470, 780, 72, "black", GREEN)
    text(c, "PAGO PELO INSS", 80, 330, 108, "black", INK, align="left")
    text(c, "MAS NÃO É", 80, 460, 124, "black", INK, align="left")
    boxed(c, "PREVIDÊNCIA", 70, 510, 128, RED)
    text(c, "BPC e auxílio-inclusão · LOAS art. 20", 90, 820, 50, "extrabold", INK2, align="left")


def capa_naos(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, s in enumerate(("contribuição", "carência", "13º salário", "pensão por morte", "acumular")):
        y = 260 + k * 150
        w = text_w("NÃO", "black", 50) + 36
        rrect(c, 1180, y - 42, w, 72, 14, RED)
        text_mid(c, "NÃO", 1180 + w / 2, y - 6, 50, "black", "#FFFFFF")
        text(c, s, 1180 + w + 24, y + 12, 50, "black", INK, align="left")
    text(c, "OS 5 NÃOS", 80, 330, 124, "black", INK, align="left")
    text(c, "QUE CAEM NO", 80, 460, 124, "black", INK, align="left")
    boxed(c, "BPC", 70, 510, 140, ASSIST, INK)
    text(c, "a pegadinha favorita da banca · INSS", 90, 820, 50, "extrabold", INK2, align="left")


def capa_numeros(c):
    background(c)
    selo(c)
    card(c, 1120, 120, 700, 840, r=36)
    for k, (n, s, col) in enumerate((("65", "anos de idade", PREST), ("¼", "do SM por pessoa", ASSIST),
                                      ("2", "anos de impedimento", GEST), ("50%", "auxílio-inclusão", RED))):
        y = 290 + k * 180
        text(c, n, 1420, y, 96, "black", col, align="right")
        text(c, s, 1445, y - 10, 34, "bold", INK, align="left")
    text(c, "BPC NA PROVA", 80, 330, 124, "black", INK, align="left")
    text(c, "DO INSS EM", 80, 460, 124, "black", INK, align="left")
    boxed(c, "4 NÚMEROS", 70, 510, 128, PREST)
    text(c, "LOAS art. 20 + auxílio-inclusão", 90, 820, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_e_previdencia", capa_nao_e), ("capa_B_cinco_naos", capa_naos),
                     ("capa_C_quatro_numeros", capa_numeros)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
