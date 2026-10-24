"""Capas — Escalas, Plantas e Mapas, Episódio 2: escala gráfica × numérica e grande × pequena (tema claro).
3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · ESCALAS · EP. 2", 84, 90, BLUE, size=34, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_fotocopia(c):
    background(c); selo(c); painel(c)
    V.folha_mapa(c, 1180, 170, 0.62, 1.0)
    text(c, "original", 1180 + V.FW * 0.31, 160, 30, "black", GRAY)
    V.folha_mapa(c, 1180, 400, 1.32, 1.0)
    text(c, "cópia ampliada", 1470, 396, 30, "black", GRAY, align="left")
    K.selo(c, 1320, 890, 1.0, "BARRA: CERTA", GREEN, -4, 30)
    K.selo(c, 1640, 890, 1.0, "NÚMERO: ERRADO", RED, 4, 30)
    big(c, "AMPLIOU O MAPA?", 330)
    big(c, "O NÚMERO", 470)
    boxed(c, "MENTE", 70, 520, 170, RED)
    text(c, "escala gráfica × numérica, sem decorar", 90, 860, 44, "extrabold", INK2, align="left")


def capa_barra(c):
    background(c); selo(c); painel(c)
    V.scale_bar(c, 1220, 330, 500, 1.0, ("0", "5", "10 km"), 40, 34)
    V.regua_cm(c, 1220, 480, 4, 125, 1.0)
    text(c, "4 cm  =  10 km", 1470, 690, 64, "black", INK)
    text(c, "1 : ?", 1470, 840, 120, "black", PURPLE)
    big(c, "TRANSFORME", 330)
    big(c, "A BARRINHA", 470)
    boxed(c, "EM NÚMERO", 70, 520, 150, PURPLE)
    text(c, "escala gráfica → numérica em 3 passos", 90, 860, 44, "extrabold", INK2, align="left")


def capa_fracao(c):
    background(c); selo(c); painel(c)
    K.pizza(c, 1270, 360, 120, 2, 1, 1.0)
    K.pizza(c, 1670, 360, 120, 20, 1, 1.0)
    text_mid(c, ">", 1470, 360, 110, "black", GREEN)
    K.fr(c, "1", "10 000", 1260, 680, 60, BLUE)
    K.fr(c, "1", "10 000 000", 1660, 680, 46, PURPLE)
    text_mid(c, ">", 1470, 680, 90, "black", GREEN)
    text(c, "escala MAIOR", 1260, 870, 38, "black", GREEN)
    text(c, "escala menor", 1660, 870, 34, "black", GRAY)
    big(c, "ESCALA GRANDE", 330)
    big(c, "TEM NÚMERO", 470)
    boxed(c, "PEQUENO", 70, 520, 170, GREEN)
    text(c, "o raciocínio da fração, para nunca mais trocar", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_numero_mente", capa_fotocopia), ("capa_B_barra_em_numero", capa_barra),
                     ("capa_C_fracao_pizza", capa_fracao)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
