"""Capas — Razão, Proporção e Regra de Três, Episódio 5: Quando a regra de três NÃO funciona (tema claro). 3 variações em 1280x720."""
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
    pill(c, "MATEMÁTICA ENEM · REGRA DE TRÊS · EP. 5", 84, 90, BLUE, size=40, bounds=(0, 1920))


def painel(c):
    card(c, 1120, 120, 700, 840, r=36)


def capa_gatos(c):
    background(c); selo(c); painel(c)
    for k in range(4):
        r_, q = divmod(k, 2)
        x, y = 1300 + q * 330, 300 + r_ * 300
        V.gato(c, x, y, 150)
        V.rato(c, x + 15, y + 115, 70)
        V.crono(c, x + 120, y - 40, 42, 1.0, 1.0, "")
    text(c, "cada um: 2 min", 1470, 900, 48, "black", GREEN)
    big(c, "4 GATOS, 4 RATOS:", 330)
    big(c, "4 MINUTOS?", 470)
    boxed(c, "NÃO!", 70, 520, 170, RED)
    text(c, "quando a regra de três te engana", 90, 860, 44, "extrabold", INK2, align="left")


def capa_pizza(c):
    background(c); selo(c); painel(c)
    K.pizza(c, 1470, 330, 170, 8, 0, 1.0)
    text(c, "diâmetro ×2", 1470, 540, 40, "black", INK2)
    for k in range(4):
        x = 1290 + k * 120
        K.pizza(c, x, 690, 52, 6, 0, 1.0)
    K.fmid(c, "= 4 pizzas", 1470, 840, 64, "black", PURPLE)
    big(c, "O DOBRO DO", 330)
    big(c, "TAMANHO E…", 470)
    boxed(c, "4× MAIS PIZZA", 70, 520, 150, PURPLE)
    text(c, "área e volume não são regra de três", 90, 860, 44, "extrabold", INK2, align="left")


def capa_ouro(c):
    background(c); selo(c); painel(c)
    rrect(c, 1180, 230, 580, 200, 30, mix("#FFFFFF", V.OURO, 0.18))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(1180, 230, 580, 200), 30, 30), paint(V.OURO, 1.0, stroke=6))
    text(c, "dobrar a CAUSA", 1470, 315, 50, "black", INK)
    text(c, "dobra o EFEITO?", 1470, 385, 50, "black", INK)
    for j, (s, col) in enumerate((("SIM → pode", GREEN), ("NÃO → fora", RED))):
        y = 560 + j * 150
        rrect(c, 1220, y - 60, 500, 110, 24, mix("#FFFFFF", col, 0.15))
        text_mid(c, s, 1470, y - 5, 56, "black", col)
    big(c, "A PERGUNTA", 330)
    big(c, "ANTES DA", 470)
    boxed(c, "REGRA DE TRÊS", 70, 520, 150, V.OURO)
    text(c, "3 segundos que salvam a questão", 90, 860, 44, "extrabold", INK2, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quatro_gatos", capa_gatos), ("capa_B_pizza_dobro", capa_pizza),
                     ("capa_C_pergunta_de_ouro", capa_ouro)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
