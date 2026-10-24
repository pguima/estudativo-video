"""Capas — Equações e Inequações do 1º Grau, Episódio 4 (tema claro). 3 variações em 1280x720.
Formatos: A = a pista da corrida na diagonal, os dois carrinhos lado a lado com os preços e "QUEM ULTRAPASSA?" no alto;
B = um leque de cartazes à direita com o contador "800 = R$ 400 = R$ 400" e "A PARTIR DE QUANTOS?" à esquerda (sem dizer a
resposta); C = fundo verde cheio com a fração do atalho gigante numa ficha branca e "O ATALHO EM 1 LINHA"."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep4", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def capa_corrida(c):
    background(c)
    pill(c, "MATEMÁTICA ENEM · EQUAÇÕES · EP. 4", W / 2, 80, BLUE, size=34, anchor="center", bounds=(0, 1920))
    s = "QUEM ULTRAPASSA?"
    text(c, s, W / 2, 260, fit(s, 170, 1760), "black", INK)
    c.save(); c.translate(W / 2, 700); c.rotate(-8)
    for k, (nome, col, dx, preco) in enumerate((("B", V.COR_B, 140, "R$ 60 + 0,80/km"), ("A", V.COR_A, -140, "R$ 90 + 0,50/km"))):
        y = -120 + k * 230
        rrect(c, -1100, y + 70, 2200, 34, 17, "#D9DCD6")
        for xx in range(-1060, 1100, 140):
            rrect(c, xx, y + 80, 70, 14, 7, "#FFFFFF")
        V.carro(c, dx, y, 130, col, 1.0, nome)
        pill(c, preco, dx - 420 if k else dx + 420, y - 20, col, size=40, anchor="center", bounds=(-2000, 2000))
    c.restore()
    V.selo(c, W / 2, 1000, 1.0, "EM QUE KM?", GREEN, -3, 56)


def capa_cartazes(c):
    background(c)
    pill(c, "MATEMÁTICA ENEM · EQUAÇÕES · EP. 4", 84, 90, BLUE, size=34, bounds=(0, 1920))
    for k in range(5):
        c.save(); c.translate(1420, 560); c.rotate(-18 + k * 9)
        col = V.COR_A if k % 2 == 0 else V.COR_B
        rrect(c, -190, -300, 380, 520, 24, "#FFFFFF", 1.0, shadow=True)
        rrect(c, -190, -300, 380, 90, 24, col)
        rrect(c, -190, -240, 380, 30, 0, col)
        for j in range(4):
            rrect(c, -140, -150 + j * 70, 280 - j * 40, 30, 10, "#E6E6E2")
        c.restore()
    rrect(c, 1130, 830, 580, 140, 30, INK)
    V.fmid(c, "800: R$ 400 nas duas", 1420, 900, 46, "black", "#FFFFFF")
    for k, (s, col) in enumerate((("A PARTIR", INK), ("DE QUANTOS", INK), ("CARTAZES?", RED))):
        text(c, s, 90, 380 + k * 170, fit(s, 160, 1000), "black", col, align="left")
    text(c, "o empate não é a resposta", 90, 920, 52, "extrabold", GRAY, align="left")


def capa_atalho(c):
    rrect(c, 0, 0, W, H, 0, GREEN)
    pill(c, "MATEMÁTICA ENEM · EQUAÇÕES · EP. 4", W / 2, 90, INK, size=34, anchor="center", bounds=(0, 1920))
    s = "O ATALHO EM 1 LINHA"
    text(c, s, W / 2, 290, fit(s, 150, 1760), "black", "#FFFFFF")
    rrect(c, 260, 380, 1400, 500, 40, "#FFFFFF", 1.0, shadow=True)
    V.frac(c, "diferença das taxas", "diferença dos preços", W / 2, 600, 92, 1.0, V.COR_B, V.COR_A)
    text(c, "qual plano compensa?", W / 2, 830, 50, "extrabold", GRAY)
    text(c, "o ponto de equilíbrio sem montar tabela", W / 2, 990, 54, "extrabold", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_quem_ultrapassa", capa_corrida), ("capa_B_a_partir_de_quantos", capa_cartazes),
                     ("capa_C_atalho_uma_linha", capa_atalho)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
