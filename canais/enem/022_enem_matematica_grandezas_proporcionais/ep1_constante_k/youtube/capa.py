"""Capas — Grandezas Proporcionais, Episódio 1: a constante k (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · GRANDEZAS · EP. 1", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_k(c):
    background(c); selo(c); painel(c)
    V.etiqueta(c, 1170, 190, 1.0, "CARNE", "R$ 20/kg", glow=1.0, rot=-4, w=600, h=240)
    for k, (kg, rs) in enumerate((("2 kg", "40"), ("3 kg", "60"), ("5 kg", "100"))):
        y = 540 + k * 120
        K.ftext(c, f"{rs} ÷ {kg.split()[0]} =", 1440, y, 48, "black", INK, align="right")
        text(c, "20", 1560, y, 56, "black", GREEN)
    text(c, "k = o que NÃO muda", 1470, 900, 40, "black", PURPLE)
    big(c, "O NÚMERO QUE", 330)
    big(c, "NUNCA MUDA:", 470)
    boxed(c, "A CONSTANTE k", 70, 520, 150, PURPLE)
    text(c, "direta e inversa resolvidas numa conta só", 90, 860, 44, "extrabold", INK2, align="left")


def capa_relogio(c):
    background(c); selo(c); painel(c)
    V.relogio(c, 1470, 450, 250, 36, 1.0)
    text(c, "0,6 h = 36 min", 1470, 830, 64, "black", GREEN)
    text(c, "e não 60", 1470, 900, 40, "black", RED)
    big(c, "1,6 HORA", 330)
    big(c, "NÃO É 1 h 60", 470)
    boxed(c, "É 1 h 36!", 70, 520, 170, AMBER)
    text(c, "o erro do relógio que o ENEM adora", 90, 860, 44, "extrabold", INK2, align="left")


def capa_bolo(c):
    background(c); selo(c); painel(c)
    for k, (n, v, tt) in enumerate(((6, "40 km/h", "6 h"), (4, "60 km/h", "4 h"), (3, "80 km/h", "3 h"))):
        y = 200 + k * 190
        text(c, v, 1290, y + 30, 32, "black", INK)
        V.bolo(c, 1170, y + 50, 520, 80, n, 1.0)
        text(c, tt, 1750, y + 104, 36, "black", BLUE)
    K.ftext(c, "v × t = 240", 1470, 850, 64, "black", PURPLE)
    big(c, "DIRETA DIVIDE.", 330)
    big(c, "INVERSA", 470)
    boxed(c, "MULTIPLICA", 70, 520, 170, BLUE)
    text(c, "o jeito de achar o k em qualquer relação", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_o_numero_que_nao_muda", capa_k), ("capa_B_relogio", capa_relogio),
                     ("capa_C_divide_multiplica", capa_bolo)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
