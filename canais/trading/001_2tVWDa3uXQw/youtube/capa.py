"""Capas (thumbnails) do vídeo 001. Gera 3 variações em 1280x720 (JPG < 2 MB)."""
import subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
from motor import *  # noqa

CANDLES = [[40, 42.9, 39.6, 42.6], [42.6, 43.0, 40.8, 41.2], [41.2, 41.6, 39.8, 40.2], [40.2, 41.4, 38.9, 41.0],
           [41, 43.5, 40.6, 43.0], [43, 50, 42.8, 49.5], [49.5, 52.4, 46.5, 51.5], [51.5, 54.2, 51.1, 53.6],
           [53.6, 54.0, 50.6, 51.2], [51.2, 51.6, 45.2, 45.6], [45.6, 49.8, 45.0, 49.4], [49.4, 56.5, 49.0, 56.0]]
P_BOT, P_TOP = 43.5, 46.5
MID = (P_BOT + P_TOP) / 2


def bg(c):
    background(c)


def chart_panel(c, x, y, w, h, mode):
    card(c, x, y, w, h, r=36)
    ch = Chart(CANDLES, (x + 60, y + 70, w - 300, h - 130), pmin=37.5, pmax=57.5, max_body=46)
    right = x + w - 230
    ch.zone(c, 4, 4, P_BOT, P_TOP, AMBER, 1.0, ext=right - ch.xr(4), fill=0.28)
    hline(c, ch.xl(4), right, ch.y(MID), GREEN, 1, 5, (16, 10))
    if mode in ("borda", "estopado"):
        hline(c, ch.xl(4), right, ch.y(P_TOP), RED, 1, 5)
    ch.draw(c, len(CANDLES))
    # toque no meio
    ch.ring(c, 9, MID, GREEN, 1.0, 26)
    lx = right + 18
    if mode in ("borda", "estopado"):
        check_icon(c, lx + 34, ch.y(P_TOP) - 38, 30, 1.0, RED, "x")
        pill(c, "BORDA", lx + 74, ch.y(P_TOP) - 38, RED, size=30, bounds=(0, 1920))
    check_icon(c, lx + 34, ch.y(MID) + 24, 30, 1.0, GREEN)
    pill(c, "50%", lx + 74, ch.y(MID) + 24, GREEN, size=34, bounds=(0, 1920))
    if mode == "entre":
        arrow(c, ch.x(9) - 250, ch.y(MID) + 230, ch.x(9) - 34, ch.y(MID) + 24, INK, 1, 12, 40)
    return ch


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)
    return w


def capa_estopado(c):
    bg(c)
    chart_panel(c, 1070, 120, 790, 840, "estopado")
    text(c, "PARE DE SER", 90, 330, 128, "black", INK, align="left")
    boxed(c, "ESTOPADO", 80, 380, 138, RED)
    text(c, "no Fair Value Gap", 92, 690, 72, "extrabold", INK2, align="left")
    pill(c, "ICT · AULA COMPLETA", 90, 820, INK, size=40, bounds=(0, 1920))


def capa_entre(c):
    bg(c)
    chart_panel(c, 1070, 120, 790, 840, "entre")
    text(c, "FVG", 80, 400, 300, "black", AMBER, align="left")
    boxed(c, "ONDE ENTRAR", 80, 470, 108, GREEN)
    text(c, "(e quais ignorar)", 92, 760, 70, "extrabold", INK2, align="left")


def capa_borda(c):
    bg(c)
    chart_panel(c, 1070, 120, 790, 840, "borda")
    text(c, "NÃO ENTRE", 90, 330, 132, "black", INK, align="left")
    boxed(c, "NA BORDA", 80, 380, 140, RED)
    text(c, "Entre no meio do FVG", 92, 690, 66, "extrabold", INK2, align="left")
    pill(c, "FAIR VALUE GAP · ICT", 90, 820, INK, size=40, bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_estopado", capa_estopado), ("capa_B_onde_entrar", capa_entre), ("capa_C_borda", capa_borda)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
