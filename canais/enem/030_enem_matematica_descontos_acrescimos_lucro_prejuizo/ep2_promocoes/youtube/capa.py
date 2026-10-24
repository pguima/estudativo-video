"""Capas — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 2: promoções, descontos encadeados e faixas (tema claro).
3 variações em 1280x720, sem gabarito: A = dois cartazes duelando ("qual dá mais desconto?"); B = a tela do carrinho com os
três carimbos e o total escondido; C = o prédio das faixas de desconto."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · DESCONTOS · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_duelo(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL DÁ MAIS DESCONTO?"
    text(c, s, W / 2, 290, fit(s, 140, 1780), "black", INK)
    V.cartaz(c, "2ª UNIDADE", "com 50% de desconto", 520, 640, 700, 380, 1.0, RED, -4)
    V.cartaz(c, "30% OFF", "em cada unidade", 1400, 640, 700, 380, 1.0, BLUE, 4)
    w = 200
    c.drawCircle(W / 2, 650, w / 2 + 10, paint("#FFFFFF"))
    c.drawCircle(W / 2, 650, w / 2, paint(AMBER))
    text_mid(c, "VS", W / 2, 650, 90, "black", "#FFFFFF")
    V.selo(c, 520, 920, 1.0, "PARECE IMBATÍVEL...", AMBER, -3, 46)


def capa_carrinho(c):
    background(c); selo_topo(c)
    s1, s2 = "3 CARIMBOS", "NO PREÇO"
    text(c, s1, 84, 330, fit(s1, 150, 900), "black", INK, align="left")
    text(c, s2, 84, 480, fit(s2, 150, 900), "black", PURPLE, align="left")
    text(c, "liquidação, Pix e frete: soma ou multiplica?", 84, 600, 44, "extrabold", INK2, align="left")
    x, y, w = 1060, 170, 780
    shadow_rrect(c, x, y, w, 800, 34, 1, 1.4)
    rrect(c, x, y, w, 800, 34, "#FFFFFF")
    rrect(c, x, y, w, 100, 34, BLUE, 0.12)
    text(c, "CARRINHO", x + 50, y + 66, 44, "black", BLUE, align="left", tracking=3)
    text(c, "etiqueta", x + 50, y + 190, 44, "bold", INK2, align="left")
    text(c, "R$ 300,00", x + w - 50, y + 190, 50, "black", INK, align="right")
    for k, (lbl, f, col) in enumerate((("cupom −20%", "× 0,80", RED), ("Pix −5%", "× 0,95", RED),
                                       ("frete +10%", "× 1,10", AMBER))):
        yy = y + 300 + k * 130
        text(c, lbl, x + 50, yy + 14, 44, "bold", INK2, align="left")
        V.carimbo(c, f, x + w - 190, yy, 1.0, col, (-7, 6, -5)[k], 46)
    line(c, x + 40, y + 650, x + w - 40, y + 650, INK, 1.0, 4)
    text(c, "TOTAL", x + 50, y + 730, 56, "black", INK, align="left")
    text(c, "R$ ???", x + w - 50, y + 732, 72, "black", GREEN, align="right")


def capa_predio(c):
    background(c); selo_topo(c)
    s1, s2 = "O DESCONTO", "TEM ANDARES"
    text(c, s1, 84, 330, fit(s1, 150, 1000), "black", INK, align="left")
    text(c, s2, 84, 480, fit(s2, 150, 1000), "black", GREEN, align="left")
    text(c, "por que 10% em tudo é ERRADO", 84, 600, 50, "extrabold", RED, align="left")
    V.pill(c, "desconto progressivo, sem cair na pegadinha", 84, 700, PURPLE, size=36, bounds=(0, 1920)) \
        if hasattr(V, "pill") else None
    V.predio(c, 1180, 990, 560, 230, 1.0, 500, topo=200)


if __name__ == "__main__":
    for nome, fn in (("capa_A_qual_da_mais_desconto", capa_duelo), ("capa_B_tres_carimbos", capa_carrinho),
                     ("capa_C_desconto_tem_andares", capa_predio)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
