"""Capas — Cartografia, Episódio 1: Escala (tema claro). Gera 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

# reaproveita os desenhos do visual do episódio
_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34):
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "CARTOGRAFIA · EPISÓDIO 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_parede(c):
    background(c)
    selo(c)
    painel(c)
    V.world_map(c, 1160, 180, 620, 330, 1)
    text(c, "2 metros", 1470, 560, 44, "black", INK2)
    line(c, 1180, 600, 1760, 600, LINE, 1, 4)
    V.bairro(c, 1300, 650, 340, 220, 1)
    text(c, "escala MAIOR", 1470, 925, 44, "black", GREEN)
    text(c, "MAPA GIGANTE", 80, 340, 116, "black", INK, align="left")
    text(c, "COM ESCALA", 80, 470, 124, "black", INK, align="left")
    boxed(c, "PEQUENA?", 70, 520, 150, AMBER, INK)
    text(c, "escala do mapa do zero · ENEM", 90, 840, 54, "extrabold", INK2, align="left")


def capa_zoom(c):
    background(c)
    selo(c)
    painel(c)
    px, py, pw, ph = 1270, 170, 400, 740
    rrect(c, px, py, pw, ph, 54, INK, shadow=True)
    V.clip_rect(c, px + 22, py + 70, pw - 44, ph - 140, 22)
    V.bairro(c, px + 22, py + 70, pw - 44, ph - 140, 1, cols=4, rows=7)
    c.restore()
    for k, s in enumerate(("+", "−")):
        c.drawCircle(px + pw - 70, py + ph - 200 + k * 76, 30, paint("#FFFFFF"))
        text_mid(c, s, px + pw - 70, py + ph - 200 + k * 76, 44, "black", INK)
    text(c, "ESCALA", 80, 340, 140, "black", INK, align="left")
    text(c, "É SÓ O", 80, 470, 124, "black", INK, align="left")
    boxed(c, "ZOOM", 70, 520, 160, GREEN)
    text(c, "entenda de uma vez · ENEM", 90, 860, 54, "extrabold", INK2, align="left")


def capa_zeros(c):
    background(c)
    selo(c)
    painel(c)
    text(c, "1 : 500 000", 1470, 300, 74, "black", INK)
    x = 1250
    text(c, "5", x, 500, 120, "black", INK, align="left")
    x += text_w("5", "black", 120)
    for k in range(5):
        w = text_w("0", "black", 120)
        text(c, "0", x, 500, 120, "black", RED, align="left")
        line(c, x - 6, 480, x + w + 6, 420, RED, 1, 8)
        x += w
    arrow(c, 1470, 560, 1470, 650, GREEN, 1, 8, 26)
    text(c, "5 km", 1470, 790, 120, "black", GREEN)
    text(c, "CORTE", 80, 340, 140, "black", INK, align="left")
    text(c, "5 ZEROS", 80, 470, 140, "black", INK, align="left")
    boxed(c, "E ACERTE", 70, 520, 140, GREEN)
    text(c, "distância real no mapa · ENEM", 90, 840, 54, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_mapa_gigante", capa_parede), ("capa_B_escala_zoom", capa_zoom), ("capa_C_corte_5_zeros", capa_zeros)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
