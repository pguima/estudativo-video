"""Capas — Cartografia, Episódio 2: Coordenadas e orientação (tema claro). Gera 3 variações em 1280x720."""
import math, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
import mapas


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "CARTOGRAFIA · EPISÓDIO 2", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_gps(c):
    background(c)
    selo(c)
    painel(c)
    cx, cy, r, lon0, lat0 = 1470, 540, 300, -50, 0
    mapas.draw_globe(c, cx, cy, r, 1, lon0=lon0, lat0=lat0)
    mapas.globe_line(c, cx, cy, r, BLUE, 1, 8, lon0, lat0, lat=-23)
    mapas.globe_line(c, cx, cy, r, GREEN, 1, 8, lon0, lat0, lon=-46)
    x, y, _ = mapas.globe_xy(-46, -23, cx, cy, r, lon0, lat0)
    c.drawCircle(x, y, 26, paint(RED)); c.drawCircle(x, y, 26, paint("#FFFFFF", 1, stroke=6))
    pill(c, "23° S · 46° O", cx, 900, RED, size=44, anchor="center", bounds=(0, 1920))
    text(c, "2 NÚMEROS", 80, 340, 136, "black", INK, align="left")
    text(c, "ACHAM VOCÊ", 80, 470, 124, "black", INK, align="left")
    boxed(c, "NO PLANETA", 70, 520, 140, BLUE)
    text(c, "latitude e longitude do zero · ENEM", 90, 840, 50, "extrabold", INK2, align="left")


def capa_40o(c):
    background(c)
    selo(c)
    painel(c)
    gx, gy, gw, gh = 1200, 300, 540, 380
    for k, lon in enumerate((60, 50, 40, 30)):
        x = gx + k * gw / 3
        line(c, x, gy, x, gy + gh, LINE, 1, 3)
        text(c, f"{lon}° O", x, gy + gh + 50, 32, "black", GRAY)
    a, b = (gx + gw / 3, gy + 120), (gx + 2 * gw / 3, gy + 120)
    c.drawCircle(*a, 22, paint(INK)); c.drawCircle(*b, 22, paint(RED))
    arrow(c, a[0] + 30, a[1], b[0] - 30, b[1], GREEN, 1, 8, 26)
    text(c, "LESTE", (a[0] + b[0]) / 2, a[1] - 40, 44, "black", GREEN)
    text(c, "Greenwich →", 1470, 220, 40, "black", GREEN)
    text(c, "40° O FICA", 80, 340, 128, "black", INK, align="left")
    text(c, "A OESTE DE", 80, 470, 124, "black", INK, align="left")
    boxed(c, "50° O?", 70, 520, 150, AMBER, INK)
    text(c, "a pegadinha das coordenadas · ENEM", 90, 840, 50, "extrabold", INK2, align="left")


def capa_batalha(c):
    background(c)
    selo(c)
    painel(c)
    gx, gy, cs = 1220, 220, 62
    for i in range(9):
        line(c, gx + i * cs, gy, gx + i * cs, gy + 8 * cs, "#93C5FD", 1, 3)
        line(c, gx, gy + i * cs, gx + 8 * cs, gy + i * cs, "#93C5FD", 1, 3)
    rrect(c, gx, gy + cs, 8 * cs, cs, 0, BLUE, 0.2)
    rrect(c, gx + 4 * cs, gy, cs, 8 * cs, 0, GREEN, 0.2)
    cx, cy = gx + 4.5 * cs, gy + 1.5 * cs
    for k in range(8):
        ang = k * math.pi / 4
        line(c, cx, cy, cx + 48 * math.cos(ang), cy + 48 * math.sin(ang), AMBER, 1, 7)
    c.drawCircle(cx, cy, 22, paint(RED))
    text(c, "= latitude + longitude", 1470, 840, 40, "black", PURPLE)
    text(c, "COORDENADAS", 80, 340, 116, "black", INK, align="left")
    text(c, "SÃO UMA", 80, 470, 124, "black", INK, align="left")
    boxed(c, "BATALHA NAVAL", 70, 520, 116, PURPLE)
    text(c, "entenda de uma vez · ENEM", 90, 840, 52, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_dois_numeros", capa_gps), ("capa_B_40_oeste", capa_40o), ("capa_C_batalha_naval", capa_batalha)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
