"""Capas — Taxas Equivalentes e Inflação, Episódio 2: taxa nominal × efetiva (tema claro). 3 variações em 1280x720.
Formatos: A = duas etiquetas iguais "24% ao ano" lado a lado e, embaixo de cada uma, um visor de caixa com "?" (a
pergunta "QUAL É O PREÇO REAL?" em cima); B = a VITRINE × o CAIXA gigantes, com "24%" na vitrine e "26,8%" no visor
escuro e o título "VITRINE ≠ CAIXA" (mostra o conceito, não gabarito de questão); C = o extrato de três meses (+10%,
+20%, −10%) à direita e a soma "= 20%?" riscada à esquerda, com "SOMAR TAXAS?" em cima."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa
from aula import strike  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep2", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · TAXAS E INFLAÇÃO · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def visor(c, cx, cy, s, w=460, h=170, size=96):
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, "#1F2937")
    text_mid(c, s, cx, cy, size, "black", "#7CF29A")


def etiqueta(c, cx, cy, s, w=560, h=190, size=100):
    rrect(c, cx - w / 2, cy - h / 2, w, h, 26, "#FFF7E0", stroke=8, stroke_color=AMBER)
    text_mid(c, s, cx, cy, size, "black", INK)


def capa_dois_contratos(c):
    background(c); selo_topo(c, W / 2)
    s = "QUAL É O PREÇO REAL?"
    text(c, s, W / 2, 290, fit(s, 140, 1760), "black", INK)
    for k in range(2):
        x = 520 + k * 880
        etiqueta(c, x, 470, "24% ao ano", w=640, size=92)
        arrow(c, x, 580, x, 680, PURPLE, 1.0, 10, 30)
        visor(c, x, 800, "? %", w=420, h=170, size=110)
    text_mid(c, "≠", W / 2, 800, 150, "black", RED)


def capa_vitrine_caixa(c):
    background(c); selo_topo(c)
    text(c, "VITRINE", 84, 300, 150, "black", BLUE, align="left")
    text(c, "≠ CAIXA", 84, 450, 150, "black", GREEN, align="left")
    text(c, "a taxa anunciada não é", 84, 590, 56, "extrabold", INK2, align="left")
    text(c, "a que você paga", 84, 660, 56, "extrabold", INK2, align="left")
    etiqueta(c, 1440, 380, "24% a.a.", w=600, h=200, size=110)
    text(c, "anúncio", 1440, 520, 40, "bold", GRAY)
    arrow(c, 1440, 560, 1440, 660, PURPLE, 1.0, 10, 30)
    visor(c, 1440, 800, "26,8%", w=600, h=200, size=120)
    text(c, "capitalizados mensalmente", 1440, 960, 40, "bold", AMBER)


def capa_extrato(c):
    background(c); selo_topo(c)
    text(c, "SOMAR", 84, 330, 160, "black", INK, align="left")
    text(c, "TAXAS?", 84, 500, 160, "black", RED, align="left")
    text_mid(c, "= 20%", 300, 700, 130, "black", RED)
    strike(c, 90, 700, 540, 700, 1.0, RED, 1.0)
    x0, y0, w = 1060, 230, 780
    rrect(c, x0, y0, w, 700, 30, "#FFFFFF", shadow=True)
    text(c, "EXTRATO DO FUNDO", x0 + 50, y0 + 80, 40, "black", INK2, align="left")
    for k, (m, tx, col) in enumerate((("mês 1", "+ 10%", GREEN), ("mês 2", "+ 20%", GREEN), ("mês 3", "− 10%", RED))):
        yy = y0 + 130 + k * 170
        rrect(c, x0 + 40, yy, w - 80, 140, 22, mix("#FFFFFF", col, 0.12))
        text_mid(c, m, x0 + 90, yy + 70, 48, "bold", INK2, align="left")
        text_mid(c, tx, x0 + w - 230, yy + 70, 84, "black", col)


if __name__ == "__main__":
    for nome, fn in (("capa_A_dois_contratos", capa_dois_contratos), ("capa_B_vitrine_caixa", capa_vitrine_caixa),
                     ("capa_C_somar_taxas", capa_extrato)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
