"""Capas — Notação Científica, Episódio 5: prefixos e a armadilha de área e volume (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · EPISÓDIO 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_area(c):
    background(c); selo(c); painel(c)
    x0, y0, s = 1220, 200, 500
    rrect(c, x0, y0, s, s, 4, mix("#FFFFFF", BLUE, 0.35), 1)
    pg = paint("#FFFFFF", 0.9, stroke=1.2)
    for k in range(51):
        c.drawLine(x0 + k * s / 50, y0, x0 + k * s / 50, y0 + s, pg)
        c.drawLine(x0, y0 + k * s / 50, x0 + s, y0 + k * s / 50, pg)
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, s, s), paint(INK, 1, stroke=5))
    text(c, "1 m", x0 + s / 2, y0 - 20, 40, "black", INK2)
    K.expr(c, "100 × 100", 1470, 800, 80, 1)
    big(c, "1 m² NÃO", 340)
    big(c, "SÃO 100 cm²", 470)
    boxed(c, "SÃO 10 000", 70, 520, 150, GREEN)
    text(c, "a armadilha de área e volume", 90, 860, 46, "extrabold", INK2, align="left")


def capa_litros(c):
    background(c); selo(c); painel(c)
    V._tanque(c, 1470, 280, 420, 440, 1, 0.85, rotulo="? L")
    K.expr(c, "1 m^3 = ? L", 1470, 860, 90, 1, cores={3: AMBER})
    big(c, "QUANTOS LITROS", 340)
    big(c, "CABEM EM", 470)
    boxed(c, "1 m³?", 70, 520, 160, BLUE)
    text(c, "volume e capacidade sem decorar", 90, 860, 46, "extrabold", INK2, align="left")


def capa_prefixos(c):
    background(c); selo(c); painel(c)
    rows = [("tera", "10^{12}", PURPLE), ("giga", "10^9", PURPLE), ("mega", "10^6", PURPLE), ("quilo", "10^3", PURPLE),
            ("mili", "10^{-3}", BLUE), ("micro", "10^{-6}", BLUE), ("nano", "10^{-9}", BLUE), ("pico", "10^{-12}", BLUE)]
    for i, (n, p_, col) in enumerate(rows):
        y = 170 + i * 92
        rrect(c, 1170, y, 600, 78, 14, mix("#FFFFFF", col, 0.12), 1)
        rrect(c, 1170, y, 12, 78, 6, col, 1)
        text(c, n, 1220, y + 54, 46, "black", col, align="left")
        K.expr(c, p_, 1640, y + 39, 52, 1, cores={0: INK})
    big(c, "DE TERA", 340)
    big(c, "A PICO", 470)
    boxed(c, "SEM DECORAR", 70, 520, 140, GREEN)
    text(c, "prefixos são potências de 10 com apelido", 90, 860, 46, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_nao_sao_100", capa_area), ("capa_B_quantos_litros", capa_litros),
                     ("capa_C_de_tera_a_pico", capa_prefixos)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
