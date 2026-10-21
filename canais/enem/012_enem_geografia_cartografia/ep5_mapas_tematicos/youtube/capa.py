"""Capas — Cartografia, Episódio 5: Mapas temáticos e anamorfoses (tema claro). Gera 3 variações em 1280x720."""
import importlib.util, math, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "CARTOGRAFIA · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_india(c):
    background(c)
    selo(c)
    painel(c)
    V.balao_map(c, (1145, 180, 650, 330), 1, 0.0)
    text(c, "território", 1470, 560, 40, "black", INK2)
    V.balao_map(c, (1145, 600, 650, 330), 1, 1.0)
    text(c, "população", 1470, 960, 40, "black", AMBER)
    text(c, "A ÍNDIA", 80, 340, 140, "black", INK, align="left")
    text(c, "FICA", 80, 470, 140, "black", INK, align="left")
    boxed(c, "GIGANTE", 70, 520, 160, AMBER, INK)
    text(c, "anamorfose no ENEM", 90, 860, 56, "extrabold", INK2, align="left")


def capa_baloes(c):
    background(c)
    selo(c)
    painel(c)
    for k, (x, y, r, col) in enumerate(((1330, 420, 160, "#F59E0B"), (1640, 380, 70, "#93C5FD"), (1580, 680, 110, "#86C18A"))):
        c.drawOval(skia.Rect.MakeLTRB(x - r, y - r * 1.15, x + r, y + r * 0.9), paint(col))
        c.drawOval(skia.Rect.MakeLTRB(x - r, y - r * 1.15, x + r, y + r * 0.9), paint(INK2, 1, stroke=4))
        line(c, x, y + r * 0.9, x, 900, INK2, 1, 4)
    text(c, "UM MAPA", 80, 340, 140, "black", INK, align="left")
    text(c, "DE", 80, 470, 140, "black", INK, align="left")
    boxed(c, "BALÕES", 70, 520, 160, PURPLE)
    text(c, "anamorfose explicada do zero", 90, 860, 56, "extrabold", INK2, align="left")


def capa_legenda(c):
    background(c)
    selo(c)
    painel(c)
    V.estado(c, 1200, 290, 62, 1)
    V.legenda_box(c, 1330, 640, 1, [(V.RAIN[0], "menos"), (V.RAIN[1], ""), (V.RAIN[2], ""), (V.RAIN[3], "mais")], "Legenda", hi=0.25)
    text(c, "LEIA QUALQUER", 80, 340, 112, "black", INK, align="left")
    text(c, "MAPA EM", 80, 470, 128, "black", INK, align="left")
    boxed(c, "4 PASSOS", 70, 520, 160, GREEN)
    text(c, "mapas temáticos no ENEM", 90, 860, 56, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_india_gigante", capa_india), ("capa_B_mapa_de_baloes", capa_baloes), ("capa_C_4_passos", capa_legenda)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
