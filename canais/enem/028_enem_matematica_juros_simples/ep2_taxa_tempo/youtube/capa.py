"""Capas — Juros Simples, Episódio 2: taxa e tempo na mesma unidade (tema claro). 3 variações em 1280x720, sem gabarito.
A = as duas fichas (18% AO ANO × 8 MESES) com um cadeado âmbar gigante no meio: "a fórmula travou" · B = o boleto atrasado:
o ingresso (multa) e o taxímetro (juros de mora) lado a lado, "quanto você paga?" · C = a pergunta "2% ao mês = ?% ao ano"
em letras enormes, com as setas ÷ 12 e × 12 em dúvida."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · JUROS SIMPLES · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_cadeado(c):
    background(c); selo_topo(c, W / 2)
    s = "AO ANO × MESES"
    text(c, s, W / 2, 300, fit(s, 150, 1760), "black", INK)
    V.ficha(c, 430, 640, "TAXA", "18%", "ao ano", PURPLE, 1.0, w=640, h=330, vsize=170)
    V.ficha(c, 1490, 640, "TEMPO", "8", "meses", BLUE, 1.0, w=640, h=330, vsize=170)
    V.cadeado(c, W / 2, 660, 140, 1.0)
    V.selo(c, W / 2, 940, 1.0, "A FÓRMULA TRAVOU", AMBER, -3, 64)


def capa_boleto(c):
    background(c); selo_topo(c)
    text(c, "BOLETO", 84, 300, 150, "black", INK, align="left")
    text(c, "ATRASADO:", 84, 450, 150, "black", RED, align="left")
    text(c, "quanto você paga?", 84, 580, 74, "extrabold", PURPLE, align="left")
    V.ingresso(c, 1430, 380, "2%", 1.0, w=640, h=300, sub="multa: uma vez só")
    V.taximetro(c, 1430, 780, 15, "1% ao mês", 1.0, w=640, h=320)
    text(c, "multa  +  juros de mora", 520, 880, 56, "black", INK2)


def capa_sentido(c):
    background(c); selo_topo(c, W / 2)
    text(c, "2% ao mês", W / 2, 380, 190, "black", INK)
    text(c, "= ?% ao ano", W / 2, 600, 170, "black", AMBER)
    for k, (s, col) in enumerate((("÷ 12", PURPLE), ("× 12", GREEN))):
        x = 600 + k * 720
        rrect(c, x - 200, 720, 400, 170, 40, mix("#FFFFFF", col, 0.14))
        text_mid(c, s, x, 805, 110, "black", col)
    text_mid(c, "ou", W / 2, 805, 60, "black", INK2)
    text(c, "taxa e tempo na mesma língua", W / 2, 1000, 50, "extrabold", PURPLE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_formula_travou", capa_cadeado), ("capa_B_boleto_atrasado", capa_boleto),
                     ("capa_C_divide_ou_multiplica", capa_sentido)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
