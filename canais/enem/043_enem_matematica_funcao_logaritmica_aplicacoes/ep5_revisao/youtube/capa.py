"""Capas — Função logarítmica e aplicações, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos: A = três faixas verticais (gota, sismógrafo, alto-falante) que convergem num selo "QUANTAS VEZES MAIOR?", com
"3 PROVAS · 1 REGRA" no alto; B = duelo de duas gotas, "pH 2,5" × "pH 4,5", e a pergunta "QUEM TEM MAIS ÁCIDO? QUANTAS
VEZES?"; C = a conta "80 dB + 80 dB =" gigante com a caixa "?" e o palpite "160?" num selo âmbar. Nenhuma mostra gabarito.
"""
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
    s = "MATEMÁTICA ENEM · FUNÇÃO LOGARÍTMICA · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_regra(c):
    background(c)
    selo_topo(c, W / 2)
    s = "3 PROVAS · 1 REGRA"
    text(c, s, W / 2, 270, fit(s, 140, 1750), "black", INK)
    for k, (ic, nome, col) in enumerate(((1, "QUÍMICA", GREEN), (2, "GEOGRAFIA", RED), (3, "FÍSICA", BLUE))):
        x = 330 + k * 630
        rrect(c, x - 270, 330, 540, 380, 36, mix("#F7F7F5", col, 0.14), 1, shadow=True)
        V.area_icone(c, ic, x, 480, 0.85, 1)
        text(c, nome, x, 670, 56, "black", col)
        arrow(c, x, 720, W / 2 + (k - 1) * 160, 800, INK2, 0.8, 7, 22)
    rrect(c, 360, 800, 1200, 170, 85, AMBER, 1, shadow=True)
    s = "QUANTAS VEZES MAIOR?"
    text_mid(c, s, W / 2, 885, fit(s, 96, 1100), "black", INK)


def capa_ph(c):
    background(c)
    selo_topo(c)
    s = "QUANTAS VEZES MAIS ÁCIDO?"
    text(c, s, 84, 280, fit(s, 120, 1750), "black", INK, align="left")
    for k, (ph, col) in enumerate((("pH 2,5", "#E5484D"), ("pH 4,5", "#F2C94C"))):
        x = 480 + k * 960
        c.save(); c.translate(x, 560); c.scale(1.35, 1.35)
        p = skia.Path(); p.moveTo(0, -160); p.quadTo(120, 10, 100, 60); p.quadTo(60, 150, 0, 150)
        p.quadTo(-60, 150, -100, 60); p.quadTo(-120, 10, 0, -160); p.close()
        c.drawPath(p, paint(mix("#FFFFFF", col, 0.55), 1))
        c.drawPath(p, paint(mix(col, INK, 0.3), 1, stroke=6))
        c.restore()
        text_mid(c, ph, x, 900, 110, "black", INK)
    rrect(c, 820, 500, 280, 160, 80, PURPLE, 1, shadow=True)
    text_mid(c, "× ?", 960, 580, 100, "black", "#FFFFFF")


def capa_db(c):
    background(c)
    selo_topo(c)
    V.area_icone(c, 3, 1700, 270, 0.75, 1)
    s = "80 dB + 80 dB ="
    text(c, s, 84, 580, fit(s, 230, 1300), "black", INK, align="left")
    rrect(c, 84, 680, 560, 300, 40, "#FFFFFF", 1, shadow=True)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(84, 680, 560, 300), 40, 40), paint(PURPLE, 1, stroke=10))
    text_mid(c, "? dB", 364, 830, 170, "black", PURPLE)
    rrect(c, 760, 740, 640, 180, 30, mix("#FFFFFF", AMBER, 0.45), 1, shadow=True)
    text_mid(c, "160 dB?", 1080, 830, 130, "black", INK)
    rrect(c, 1450, 760, 380, 140, 70, RED, 1)
    text_mid(c, "CERTEZA?", 1640, 830, 64, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_3_provas_1_regra", capa_regra), ("capa_B_quantas_vezes_mais_acido", capa_ph),
                     ("capa_C_80_mais_80_db", capa_db)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
