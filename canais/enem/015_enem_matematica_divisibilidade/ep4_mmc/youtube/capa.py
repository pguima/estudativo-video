"""Capas — Divisibilidade, Primos, MMC e MDC, Episódio 4: MMC (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4_mmc", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 4", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_coincidir(c):
    background(c); selo(c); painel(c)
    for k, col in enumerate((V.COR_A, V.COR_B, V.COR_C)):
        V.onibus(c, 1300 + k * 170, 260, 1.1, 1, col)
    series = [dict(step=6, col=V.COR_A, label="6 em 6"), dict(step=8, col=V.COR_B, label="8 em 8")]
    V.linha_tempo(c, 0, 1150, 400, 640, 26, series, coinc=(24,), coinc_a=1.0, unit="h", tick=4, label_w=150, row_h=80)
    text(c, "juntos de novo às 24 h", 1470, 800, 38, "black", V.GLOW)
    big(c, "QUANDO VOLTAM", 340)
    big(c, "A COINCIDIR?", 470)
    boxed(c, "É MMC", 70, 520, 150, GREEN)
    text(c, "ônibus, lâmpadas e remédios no ENEM", 90, 860, 50, "extrabold", INK2, align="left")


def capa_quantas(c):
    background(c); selo(c); painel(c)
    text(c, "Nos 10 minutos seguintes,", 1470, 260, 34, "bold", INK2)
    text(c, "QUANTAS VEZES?", 1470, 320, 46, "black", AMBER)
    rrect(c, 1180, 400, 580, 170, 24, mix("#FFFFFF", RED, 0.10))
    text(c, "60", 1340, 520, 110, "black", RED)
    check_icon(c, 1620, 485, 46, 1, RED, "x")
    rrect(c, 1180, 620, 580, 170, 24, mix("#FFFFFF", GREEN, 0.10))
    text(c, "10", 1340, 740, 110, "black", GREEN)
    check_icon(c, 1620, 705, 46, 1, GREEN)
    big(c, "ACHOU O MMC", 340)
    big(c, "E PAROU?", 470)
    boxed(c, "ERROU", 70, 520, 150, RED)
    text(c, "a pegadinha do “quantas vezes”", 90, 860, 50, "extrabold", INK2, align="left")


def capa_varal(c):
    background(c); selo(c); painel(c)
    V.varal(c, 1190, 240, V.ROWS, 9, 1.0, size=50, lh=82, colw=120)
    V.fbox(c, "MMC = 180", 1470, 830, 60, 1.0, GREEN)
    big(c, "MMC DE TRÊS", 340)
    big(c, "NÚMEROS EM", 470)
    boxed(c, "30 SEGUNDOS", 70, 520, 112, PURPLE)
    text(c, "o varal da decomposição simultânea", 90, 860, 50, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quando_coincidem", capa_coincidir), ("capa_B_quantas_vezes", capa_quantas),
                     ("capa_C_varal", capa_varal)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
