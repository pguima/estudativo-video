"""Capas — Juros Simples, Episódio 5: revisão, 9 pegadinhas e 5 questões inéditas (tema claro). 3 variações em 1280x720.
Formatos: A = título à esquerda e um boleto gigante inclinado à direita, com as unidades circuladas (a conversão escondida);
B = placar 3 × 3 de cartas viradas "V ou F?" ocupando a metade direita; C = ampulheta enorme no centro com o "3×" e a
pergunta no alto. Nenhuma mostra gabarito."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · JUROS SIMPLES · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def circulo(c, cx, cy, w, h, col, sw=8):
    c.drawOval(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), paint(col, 1.0, stroke=sw))


def capa_boleto(c):
    background(c); selo_topo(c)
    text(c, "O ENEM", 84, 330, 150, "black", INK, align="left")
    text(c, "ESCONDE", 84, 480, 150, "black", INK, align="left")
    text(c, "A CONVERSÃO", 84, 630, fit("A CONVERSÃO", 150, 980), "black", AMBER, align="left")
    text(c, "9 pegadinhas · 5 questões inéditas", 84, 790, 54, "extrabold", PURPLE, align="left")
    c.save(); c.translate(1450, 560); c.rotate(6)
    shadow_rrect(c, -330, -420, 660, 840, 30, 1, 1.6)
    rrect(c, -330, -420, 660, 840, 30, "#FFFFFF")
    rrect(c, -330, -420, 660, 120, 30, mix("#FFFFFF", BLUE, 0.25))
    text(c, "CONTA / EMPRÉSTIMO", 0, -342, 40, "black", BLUE)
    for j, (k_, v) in enumerate((("valor", "R$ 6.000,00"), ("taxa", "15% ao ANO"), ("prazo", "10 MESES"))):
        y = -200 + j * 150
        text(c, k_, -280, y, 38, "bold", GRAY, align="left")
        text(c, v, 280, y, 58, "black", INK, align="right")
        line(c, -290, y + 40, 290, y + 40, LIGHT, 1.0, 3)
    for j, v in ((1, "15% ao ANO"), (2, "10 MESES")):
        w = text_w(v, "black", 58)
        circulo(c, 280 - w / 2, -200 + j * 150 - 20, w + 70, 110, AMBER)
    for j in range(22):
        line(c, -270 + j * 25, 250, -270 + j * 25, 360, INK, 1.0, 4 + 3 * (j % 3))
    c.restore()
    V.selo(c, 1000, 960, 1.0, "PEGADINHA", AMBER, -8, 60)


def capa_placar(c):
    background(c); selo_topo(c)
    text(c, "VOCÊ CAI", 84, 330, 150, "black", INK, align="left")
    text(c, "EM QUANTAS?", 84, 480, fit("EM QUANTAS?", 150, 900), "black", RED, align="left")
    text(c, "9 pegadinhas de", 84, 640, 64, "extrabold", INK2, align="left")
    text(c, "JUROS SIMPLES", 84, 730, 80, "black", BLUE, align="left")
    text(c, "+ 5 questões estilo ENEM", 84, 850, 54, "extrabold", GREEN, align="left")
    for k in range(9):
        r_, q = divmod(k, 3)
        x, y = 1080 + q * 260, 200 + r_ * 270
        shadow_rrect(c, x, y, 220, 230, 26, 1, 1.3)
        rrect(c, x, y, 220, 230, 26, "#FFFFFF")
        rrect(c, x, y, 220, 230, 26, AMBER, 0.12)
        badge_num(c, k + 1, x + 34, y + 34, 1.0, 22, bg=INK2)
        text_mid(c, "V", x + 62, y + 125, 64, "black", GREEN)
        text_mid(c, "ou", x + 112, y + 128, 30, "bold", GRAY)
        text_mid(c, "F", x + 162, y + 125, 64, "black", RED)
        text_mid(c, "?", x + 112, y + 190, 44, "black", INK2)


def capa_ampulheta(c):
    background(c); selo_topo(c, W / 2)
    s = "QUANDO O DINHEIRO TRIPLICA?"
    text(c, s, W / 2, 270, fit(s, 120, 1780), "black", INK)
    V.area_icone(c, 4, W / 2, 640, 3.4, 1.0)
    for k in range(3):
        V.nota(c, 300, 520 + k * 34 - 30, 300, 86, 1.0)
    text(c, "1×", 450, 760, 90, "black", BLUE)
    for k in range(3):
        for j in range(3):
            V.nota(c, 1330 + j * 30, 470 + k * 120 - j * 26, 300, 86, 1.0)
    text(c, "3×", 1500, 860, 110, "black", GREEN)
    text(c, "a 5% ao mês, em juros simples", W / 2, 1000, 56, "extrabold", PURPLE)


if __name__ == "__main__":
    for nome, fn in (("capa_A_conversao_escondida", capa_boleto), ("capa_B_voce_cai_em_quantas", capa_placar),
                     ("capa_C_quando_triplica", capa_ampulheta)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
