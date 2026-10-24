"""Capas — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 1: lucro e prejuízo, porcentagem de quê? (tema claro).
3 variações em 1280x720 (sem gabarito).
A = as duas barras (custo 80 e venda 100) com o mesmo lucro e "25% OU 20%?"; B = "POR CENTO DE QUÊ?" gigante com as etiquetas
"DONO?"; C = a pizza do preço com a fatia do lucro e a pilha do markup: "MARKUP ≠ MARGEM"."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · LUCRO · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_barras(c):
    background(c); selo_topo(c)
    s = "LUCREI 25% OU 20%?"
    text(c, s, W / 2, 330, fit(s, 170, 1780), "black", INK)
    X0, ESC = 260, 10.5
    shadow_rrect(c, 120, 420, 1680, 560, 40, 1, 1.4)
    rrect(c, 120, 420, 1680, 560, 40, "#FFFFFF")
    V.barra_reais(c, X0, 480, 80 * ESC, 150, V.CUSTO, 1.0, None, "CUSTO R$ 80")
    rrect(c, X0 + 80 * ESC, 480, 20 * ESC, 150, 14, mix("#FFFFFF", V.LUCRO, 0.55))
    text_mid(c, "+20", X0 + 90 * ESC, 555, 64, "black", V.LUCRO)
    V.barra_reais(c, X0, 740, 100 * ESC, 150, V.VENDA, 1.0, None, "VENDA R$ 100")
    rrect(c, X0 + 80 * ESC, 740, 20 * ESC, 150, 14, mix("#FFFFFF", V.LUCRO, 0.55))
    text_mid(c, "20", X0 + 90 * ESC, 815, 64, "black", V.LUCRO)
    V.dono(c, "DONO?", 1610, 555, V.CUSTO, 1.0, 46)
    V.dono(c, "DONO?", 1610, 815, V.VENDA, 1.0, 46)


def capa_pergunta(c):
    background(c); selo_topo(c, W / 2)
    s1, s2 = "POR CENTO", "DE QUÊ?"
    text(c, s1, W / 2, 400, fit(s1, 230, 1700), "black", INK)
    sz = fit(s2, 230, 1500)
    w = text_w(s2, "black", sz) + 120
    shadow_rrect(c, W / 2 - w / 2, 470, w, 290, 40, 1, 1.4)
    rrect(c, W / 2 - w / 2, 470, w, 290, 40, AMBER)
    text_mid(c, s2, W / 2, 615, sz, "black", "#FFFFFF")
    V.etiqueta(c, 420, 930, 440, 130, 1.0, "do CUSTO", V.CUSTO, -5)
    V.etiqueta(c, 1500, 930, 440, 130, 1.0, "da VENDA", V.VENDA, 5)
    text_mid(c, "ou", W / 2, 930, 70, "black", INK2)


def capa_pizza(c):
    background(c); selo_topo(c)
    V.K.pizza(c, 560, 610, 360, 4, 1, 1.0, sel_col=V.LUCRO, pull=0.8)
    s1 = "MARKUP"
    s2 = "≠ MARGEM"
    text(c, s1, 1440, 430, fit(s1, 190, 820), "black", V.LUCRO)
    sz = fit(s2, 170, 820)
    w = text_w(s2, "black", sz) + 70
    shadow_rrect(c, 1440 - w / 2, 500, w, 220, 30, 1, 1.4)
    rrect(c, 1440 - w / 2, 500, w, 220, 30, V.VENDA)
    text_mid(c, s2, 1440, 610, sz, "black", "#FFFFFF")
    text(c, "a fatia do lucro", 1440, 840, 60, "extrabold", INK2)
    text(c, "nunca é a pizza inteira", 1440, 920, 60, "extrabold", INK2)


if __name__ == "__main__":
    for nome, fn in (("capa_A_25_ou_20", capa_barras), ("capa_B_por_cento_de_que", capa_pergunta),
                     ("capa_C_markup_margem", capa_pizza)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
