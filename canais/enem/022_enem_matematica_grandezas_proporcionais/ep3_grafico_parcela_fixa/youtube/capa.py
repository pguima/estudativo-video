"""Capas — Grandezas Proporcionais, Episódio 3: o gráfico de cada relação e a parcela fixa (tema claro). 3 variações em 1280x720."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
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
    pill(c, "MATEMÁTICA ENEM · GRANDEZAS · EP. 3", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_taxi(c):
    background(c); selo(c); painel(c)
    V.taxi(c, 1470, 300, 1.0, 1.2)
    V.taximetro(c, 1345, 470, "R$ 6,00", 1.0)
    text(c, "já marca ANTES de andar", 1470, 640, 36, "black", V.FIXO)
    K.ftext(c, "8 km → R$ 26", 1470, 760, 52, "black", INK)
    K.ftext(c, "16 km → R$ 52?", 1470, 860, 52, "black", RED)
    big(c, "DOBROU A CORRIDA,", 330)
    big(c, "DOBROU O PREÇO?", 470)
    boxed(c, "NÃO: A BANDEIRADA", 70, 520, 130, AMBER)
    text(c, "a armadilha da parcela fixa, do zero", 90, 860, 44, "extrabold", INK2, align="left")


def capa_desenho(c):
    background(c); selo(c); painel(c)
    fs = [(lambda x: 3 * x, 0, 10, GREEN, "DIRETA"), (lambda x: 40 / x, 40 / 28, 10.5, PURPLE, "INVERSA"),
          (lambda x: 2 * x + 10, 0, 10, RED, "NENHUMA")]
    for k, (f, v0, v1, col, nome) in enumerate(fs):
        y0 = 340 + k * 250
        g = V.Graf(1200, y0, 300, 190, 11, 30)
        g.eixos(c, 1.0)
        g.curva(c, f, v0, v1, col, 1.0, 1.0, 8)
        text_mid(c, nome, 1660, y0 - 90, 44, "black", col)
    big(c, "RETA, CURVA", 330)
    big(c, "OU NENHUMA?", 470)
    boxed(c, "LEIA O GRÁFICO", 70, 520, 130, PURPLE)
    text(c, "reconheça a proporção só pelo desenho", 90, 860, 44, "extrabold", INK2, align="left")


def capa_reta(c):
    background(c); selo(c); painel(c)
    g = V.Graf(1220, 760, 500, 520, 10, 50)
    g.eixos(c, 1.0)
    g.curva(c, lambda x: 4 * x, 0, 10, GREEN, 1.0, 1.0, 9)
    g.curva(c, lambda x: 3 * x + 15, 0, 10, RED, 1.0, 1.0, 9)
    c.drawCircle(g.x0, g.y0, 26, paint(GREEN, 1.0, stroke=7))
    c.drawCircle(g.x0, g.Y(15), 26, paint(RED, 1.0, stroke=7))
    check_icon(c, 1700, 270, 34, 1.0, RED, "x")
    check_icon(c, 1700, 400, 34, 1.0, GREEN)
    text(c, "a pergunta da origem", 1470, 870, 40, "black", PURPLE)
    big(c, "TODA RETA É", 330)
    big(c, "PROPORÇÃO?", 470)
    boxed(c, "NÃO!", 70, 520, 170, RED)
    text(c, "o teste de dois segundos no gráfico", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_bandeirada", capa_taxi), ("capa_B_reta_ou_curva", capa_desenho),
                     ("capa_C_toda_reta", capa_reta)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
