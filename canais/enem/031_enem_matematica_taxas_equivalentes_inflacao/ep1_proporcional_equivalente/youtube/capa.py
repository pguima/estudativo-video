"""Capas — Taxas Equivalentes e Inflação, Episódio 1: proporcional × equivalente (tema claro). 3 variações em 1280x720.
Formatos: A = conta gigante riscada ("10% ao mês × 12 = 120%?") com selo; B = o gráfico reta × curva ocupando a capa, com a faixa
"juro sobre juro"; C = a tesoura cortando o "1," do fator. Nenhuma mostra a resposta das questões."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep1", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · TAXAS E INFLAÇÃO · EP. 1"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_conta(c):
    background(c); selo_topo(c, W / 2)
    s1 = "10% AO MÊS"
    text(c, s1, W / 2, 330, 150, "black", INK)
    V.linha(c, [("× 12 = ", INK2), ("120% AO ANO", RED)], W / 2, 500, 130, 1.0)
    w = text_w("× 12 = 120% AO ANO", "black", 130)
    strike(c, W / 2 - w / 2 - 20, 520, W / 2 + w / 2 + 20, 470, 1.0, RED, 1.0)
    rrect(c, 0, 690, W, 390, 0, PURPLE, 1.0)
    s = "ERROU POR QUASE 100 PONTOS"
    text(c, s, W / 2, 850, fit(s, 110, 1760), "black", "#FFFFFF")
    text(c, "taxa equivalente do zero", W / 2, 960, 56, "extrabold", "#E9E1FF")


def capa_grafico(c):
    background(c); selo_topo(c)
    V.GX, V.GY, V.GW, V.GH = 160, 250, 1180, 700
    V.grafico(c, 1.0, 1.0, 1.0, 1.0, rot=False)
    pill(c, "soma 2% por mês", V.gx(12) - 20, V.gy(24) + 150, PURPLE, size=40, anchor="right", bounds=(0, 1920))
    pill(c, "× 1,02 por mês", V.gx(12) - 20, V.gy(26.8) - 60, GREEN, size=40, anchor="right", bounds=(0, 1920))
    s = "2% AO MÊS"
    text(c, s, 1610, 420, fit(s, 120, 560), "black", INK)
    text(c, "=", 1610, 560, 120, "black", GRAY)
    text(c, "?% AO ANO", 1610, 720, fit("?% AO ANO", 120, 560), "black", PURPLE)
    V.selo(c, 1610, 880, 1.0, "NÃO É 24%", RED, -6, 56)


def capa_tesoura(c):
    background(c); selo_topo(c, W / 2)
    s = "FATOR PRIMEIRO, TAXA DEPOIS"
    text(c, s, W / 2, 290, fit(s, 120, 1780), "black", INK)
    size = 300
    w1 = V.ftext_w("1,", "black", size)
    wr = V.ftext_w("268", "black", size)
    x0 = W / 2 - (w1 + wr) / 2
    V.ftext(c, "1,", x0, 690, size, "black", RED, 0.9)
    V.ftext(c, "268", x0 + w1, 690, size, "black", INK, 1.0, align="left")
    V.tesoura(c, x0 + w1 + 30, 400, 240, 1.0, 0.7)
    rrect(c, 0, 820, W, 260, 0, GREEN, 1.0)
    s2 = "TIRE O 1 NO FIM"
    text(c, s2, W / 2, 975, fit(s2, 120, 1760), "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_errou_100_pontos", capa_conta), ("capa_B_reta_curva", capa_grafico),
                     ("capa_C_tire_o_1", capa_tesoura)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
