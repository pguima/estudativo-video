"""Capas — Matrizes e Operações, Episódio 3: multiplicação de matrizes, linha por coluna (tema claro). 3 variações em 1280x720.
A = o cupom do mercado à esquerda virando linha × coluna à direita (sem o total); B = dois dominós grandes com a pergunta
"existe?" (sem dizer qual encaixa); C = mapa de quatro cidades em fundo escuro com "A² conta rotas?" (sem rota acesa)."""
import importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(next(d / "_ferramentas" for d in HERE.parents if (d / "_ferramentas").is_dir())))
import skia
import motor
motor.set_theme("claro")
from motor import *  # noqa

_spec = importlib.util.spec_from_file_location("visual_ep3", HERE.parent / "roteiro" / "visual.py")
V = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(V)
motor.set_theme("claro")
K = V.K


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, cor=BLUE):
    s = "MATEMÁTICA ENEM · MATRIZES · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_cupom(c):
    background(c); selo_topo(c)
    s1 = "O CUPOM DO MERCADO"
    text(c, s1, 84, 250, fit(s1, 120, 1750), "black", INK, align="left")
    sz = 104
    w = text_w("É UMA MATRIZ?", "black", sz) + 70
    shadow_rrect(c, 84, 290, w, 140, 26, 1, 1.4)
    rrect(c, 84, 290, w, 140, 26, GREEN)
    text_mid(c, "É UMA MATRIZ?", 84 + w / 2, 360, sz, "black", "#FFFFFF")
    itens = [("arroz", "10 kg", "R$ 5", "", 1), ("feijão", "5 kg", "R$ 9", "", 1), ("óleo", "4 L", "R$ 8", "", 1)]
    V.cupom(c, 110, 500, 620, itens, 1.0, 1.0, total="R$ ?")
    arrow(c, 780, 740, 900, 740, AMBER, 1.0, 10, 30)
    V.matriz(c, [[10, 5, 4]], 1170, 640, 1.0, cell=150, row=0)
    text_mid(c, "·", 1440, 640, 110, "black", GRAY)
    V.matriz(c, [[5], [9], [8]], 1600, 760, 1.0, cell=150, cellh=105, col=0)
    text(c, "LINHA × COLUNA", 1170, 900, 64, "black", PURPLE)


def capa_domino(c):
    background(c); selo_topo(c, W / 2, PURPLE)
    s = "ESSE PRODUTO EXISTE?"
    text(c, s, W / 2, 290, fit(s, 140, 1780), "black", INK)
    for k, (o1, o2) in enumerate((((2, 3), (3, 2)), ((3, 2), (3, 2)))):
        cy = 520 + k * 290
        V.domino(c, o1, o2, W / 2 - 160, cy, 1.0, u=0.0, size=96, ok=True, res_a=0, tw=360, th=170)
        text_mid(c, "?", W / 2 + 560, cy, 170, "black", AMBER)
    text(c, "a regra do dominó das matrizes", W / 2, 1010, 50, "extrabold", PURPLE)


def capa_rotas(c):
    c.drawColor(skia.Color4f.FromColor(skia.Color(0x1C, 0x1C, 0x1E)))
    selo_topo(c, None, GREEN)
    text(c, "A² CONTA", 84, 330, 150, "black", "#FFFFFF", align="left")
    text(c, "ROTAS?", 84, 490, 150, "black", GREEN, align="left")
    text(c, "quantos caminhos com 1 escala", 84, 600, 50, "extrabold", "#C7C7CC", align="left")
    rrect(c, 1040, 170, 800, 800, 40, "#FFFFFF", 1.0)
    V.voos(c, V.VOOS_E, 1440, 570, 1.0, L=250, r=70, size=60)
    rrect(c, 262, 655, 416, 390, 24, "#FFFFFF", 1.0)
    V.matriz(c, V.ME, 470, 850, 1.0, cell=80, size=44)


if __name__ == "__main__":
    for nome, fn in (("capa_A_cupom_matriz", capa_cupom), ("capa_B_domino_existe", capa_domino),
                     ("capa_C_a2_conta_rotas", capa_rotas)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
