"""Capas (thumbnails) do vídeo 002 — CRT, modo escuro. Gera 3 variações em 1280x720."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("escuro")
from motor import *  # noqa

CANDLES = [[50, 51.4, 49.6, 51.0], [51.0, 52.6, 50.6, 52.2], [52.2, 52.8, 50.9, 51.3], [51.3, 54.0, 51.0, 53.6],
           [53.6, 56.4, 53.2, 56.0], [56.0, 57.0, 54.6, 55.0], [55.0, 58.6, 54.8, 58.2], [58.2, 61.6, 57.9, 61.2],
           [61.2, 62.4, 59.9, 60.4]]
PDH = 59.0


def chart_panel(c, x, y, w, h, mode):
    card(c, x, y, w, h, r=36)
    ch = Chart(CANDLES, (x + 50, y + 90, w - 330, h - 160), pmin=46, pmax=72, max_body=44)
    hline(c, x + 40, x + w - 40, ch.y(PDH), AMBER, 1, 5, (16, 10))
    pill(c, "MÁXIMA DO DIA ANTERIOR", x + 46, ch.y(PDH) - 34, AMBER, size=26, bounds=(0, 1920))
    ch.draw(c, len(CANDLES))
    sx = ch.xr(len(CANDLES) - 1) + 40
    sy = ch.y(60.4)
    if mode in ("split", "opiniao"):
        arrow(c, sx, sy, sx + 190, ch.y(69), GREEN, 1, 12, 40)
        arrow(c, sx, sy, sx + 190, ch.y(49), RED, 1, 12, 40)
        if mode == "split":
            pill(c, "CONTINUAÇÃO", sx + 200, ch.y(69) - 4, GREEN, size=32, anchor="right", bounds=(0, 1920))
            pill(c, "REVERSÃO", sx + 200, ch.y(49) + 4, RED, size=32, anchor="right", bounds=(0, 1920))
        else:
            pill(c, "COMPRAR?", sx + 200, ch.y(69) - 4, GREEN, size=34, anchor="right", bounds=(0, 1920))
            pill(c, "VENDER?", sx + 200, ch.y(49) + 4, RED, size=34, anchor="right", bounds=(0, 1920))


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.0)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def big_daily(c, x, y, w, h):
    card(c, x, y, w, h, r=36)
    cx, top, bot = x + w / 2 - 60, y + 120, y + h - 90
    c.drawLine(cx, top - 30, cx, bot + 30, paint(GREEN, 1, stroke=8))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(cx - 95, top, cx + 95, bot - 60), 10, 10), paint(GREEN))
    for yy, lab in ((top - 30, "PDH"), (bot + 30, "PDL")):
        hline(c, cx - 140, x + w - 40, yy, AMBER, 1, 5, (16, 10))
        pill(c, lab, x + w - 46, yy, AMBER, size=34, anchor="right", bounds=(0, 1920))
    pill(c, "DIÁRIO", x + 30, y + 46, BLUE, size=30, bounds=(0, 1920))


def capa_split(c):
    background(c)
    chart_panel(c, 1040, 120, 820, 840, "split")
    text(c, "REVERSÃO", 80, 320, 140, "black", RED, align="left")
    text(c, "OU", 86, 450, 100, "black", INK, align="left")
    boxed(c, "CONTINUAÇÃO?", 70, 490, 90, GREEN)
    pill(c, "CANDLE RANGE THEORY · CRT", 84, 800, INK, size=40, bounds=(0, 1920))


def capa_diario(c):
    background(c)
    big_daily(c, 1100, 120, 760, 840)
    text(c, "1 CANDLE", 80, 320, 150, "black", INK, align="left")
    boxed(c, "DECIDE SEU DIA", 70, 370, 100, BLUE)
    text(c, "A estratégia CRT completa", 86, 640, 62, "extrabold", INK2, align="left")
    pill(c, "PDH · PDL · CISD", 84, 780, AMBER, size=44, bounds=(0, 1920))


def capa_opiniao(c):
    background(c)
    chart_panel(c, 1040, 120, 820, 840, "opiniao")
    text(c, "PARE DE", 80, 320, 150, "black", INK, align="left")
    boxed(c, "MUDAR DE IDEIA", 70, 370, 96, RED)
    text(c, "no meio do trade", 86, 640, 70, "extrabold", INK2, align="left")
    pill(c, "CANDLE RANGE THEORY", 84, 780, INK, size=40, bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_reversao_ou_continuacao", capa_split), ("capa_B_um_candle", capa_diario),
                     ("capa_C_mudar_de_ideia", capa_opiniao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
