"""Capas — Grandezas Proporcionais, Episódio 5: quando dobrar não dobra (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep5", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def big(c, s, y, maxw=1000, size=140):
    while text_w(s, "black", size) > maxw:
        size -= 4
    text(c, s, 80, y, size, "black", INK, align="left")


def boxed(c, s, x, y, size, bg_col, fg="#FFFFFF", pad=34, maxw=1000):
    while text_w(s, "black", size) + pad * 2 > maxw:
        size -= 4
    w = text_w(s, "black", size) + pad * 2
    h = size * 1.22
    shadow_rrect(c, x, y, w, h, 22, 1, 1.4)
    rrect(c, x, y, w, h, 22, bg_col)
    text_mid(c, s, x + w / 2, y + h / 2, size, "black", fg)


def selo(c):
    pill(c, "MATEMÁTICA ENEM · GRANDEZAS · EP. 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_luz(c):
    background(c); selo(c); painel(c)
    V.lampada(c, 1470, 230, 60, 1.0)
    V.parede(c, 1470, 620, 2, 140, 1.0, "1/4")
    text(c, "o dobro da distância", 1470, 900, 40, "black", INK2)
    big(c, "DOBROU A", 340)
    big(c, "DISTÂNCIA?", 470)
    boxed(c, "LUZ ÷ 4", 70, 520, 160, AMBER)
    text(c, "não é metade: o inverso do quadrado, do zero", 90, 860, 40, "extrabold", INK2, align="left")


def capa_piso(c):
    background(c); selo(c); painel(c)
    V.azulejos(c, 1290, 300, 2, 180, 1.0, rotulo=False)
    text(c, "lado × 2", 1470, 740, 52, "black", INK2)
    text(c, "4 azulejos", 1470, 840, 60, "black", GREEN)
    big(c, "O LADO DOBROU,", 340)
    big(c, "A ÁREA…", 470)
    boxed(c, "QUADRUPLICOU", 70, 520, 150, GREEN)
    text(c, "e o volume? fica 8 vezes maior", 90, 860, 44, "extrabold", INK2, align="left")


def capa_cubo(c):
    background(c); selo(c); painel(c)
    V.cubo_iso(c, 1470, 520, 2, 150, 1.0)
    text(c, "2 × 2 × 2 = 8", 1470, 890, 64, "black", PURPLE)
    big(c, "QUANDO DOBRAR", 340)
    big(c, "NÃO DOBRA", 470)
    boxed(c, "× 4 · × 8 · ÷ 4", 70, 520, 140, PURPLE)
    text(c, "a tabela de cada relação, explicada do zero", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_luz_cai_a_um_quarto", capa_luz), ("capa_B_area_quadruplica", capa_piso),
                     ("capa_C_dobrar_nao_dobra", capa_cubo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
