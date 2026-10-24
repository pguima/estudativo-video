"""Capas — Função Exponencial, Episódio 2: o modelo Q₀ · aᵗ, da frase ao fator (tema claro). 3 variações em 1280x720.
Nenhuma mostra gabarito. A = carro grande à esquerda e o duelo "× 0,15 ? × 0,85 ?" à direita, sem dizer qual é o certo;
B = a máquina de tradução atravessando a capa (frase → ? ); C = faixa roxa cheia com a fórmula de Juros compostos de
gravata e a pergunta "é a mesma?"."""
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


def selo_topo(c, cx=None, col=BLUE):
    s = "MATEMÁTICA ENEM · EXPONENCIAL · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, col, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, col, size=34, anchor="center", bounds=(0, 1920))


def capa_carro(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 80, 190, 760, 800, 40, 1, 1.4)
    rrect(c, 80, 190, 760, 800, 40, "#FFFFFF")
    V.carrinho(c, 460, 470, 260, 1.0)
    text(c, "R$ 60 000", 460, 780, 120, "black", INK)
    pill(c, "perde 15% ao ano", 460, 880, AMBER, size=52, anchor="center")
    s = "DEPOIS DE 1 ANO:"
    text(c, s, 1380, 300, fit(s, 96, 960), "black", INK)
    for k, (s_, col) in enumerate((("× 0,15 ?", PURPLE), ("× 0,85 ?", PURPLE))):
        y = 420 + k * 260
        shadow_rrect(c, 980, y, 800, 210, 34, 1, 1.4)
        rrect(c, 980, y, 800, 210, 34, mix("#FFFFFF", col, 0.10))
        text_mid(c, s_, 1380, y + 105, 150, "black", col)
    V.selo(c, 1660, 960, 1.0, "UM NÚMERO DECIDE", RED, -6, 44)


def capa_maquina(c):
    background(c); selo_topo(c, W / 2, PURPLE)
    s = "DA FRASE À LEI"
    text(c, s, W / 2, 300, fit(s, 170, 1700), "black", INK)
    for k, fz in enumerate(("dobra", "cresce 3%", "triplica")):
        V.chip(c, fz, 560 + k * 400, 430, GRAY, 1.0, 44)
    cy = 680
    rrect(c, 0, cy - 170, W, 340, 0, mix("#FFFFFF", PURPLE, 0.08))
    c.save(); c.translate(1062, cy); c.scale(1.7, 1.7)
    V.maquina(c, 0, 0, 1.0, "perde 15%", "?", 1.0)
    c.restore()
    text(c, "toda questão de exponencial começa aqui", W / 2, 960, 56, "extrabold", PURPLE)


def capa_terno(c):
    background(c)
    rrect(c, 0, 0, W, H, 0, PURPLE)
    pill(c, "MATEMÁTICA ENEM · EXPONENCIAL · EP. 2", W / 2, 90, "#FFFFFF", PURPLE, size=34, anchor="center",
         bounds=(0, 1920))
    s = "VOCÊ JÁ CONHECE ESSA FUNÇÃO"
    text(c, s, W / 2, 290, fit(s, 120, 1780), "black", "#FFFFFF")
    shadow_rrect(c, 300, 380, 1320, 300, 40, 1, 1.6)
    rrect(c, 300, 380, 1320, 300, 40, "#FFFFFF")
    K.expr(c, "M = C · (1+i)^t", 900, 530, 150, 1.0, cores={i: INK for i in range(8)})
    V.gravata(c, 1520, 420, 220, 1.0, PURPLE)
    s2 = "é a mesma de"
    text(c, s2, 700, 860, 84, "black", "#FFFFFF")
    V.fm(c, V.Q0("#FFFFFF") + [(" · ", "#FFFFFF"), ("a^t", "#FFFFFF", "m"), (" ?", "#FFFFFF")], 1290, 830, 120, 1.0)


if __name__ == "__main__":
    for nome, fn in (("capa_A_carro_015_085", capa_carro), ("capa_B_da_frase_a_lei", capa_maquina),
                     ("capa_C_juros_de_terno", capa_terno)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
