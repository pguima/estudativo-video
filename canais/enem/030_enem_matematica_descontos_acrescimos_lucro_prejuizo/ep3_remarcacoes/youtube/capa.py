"""Capas — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 3: remarcações e liquidações (tema claro). 3 variações em 1280x720.
Formatos: A = etiqueta gigante inclinada à direita ("+50%" e "−33%" em selos) e a pergunta "SOBROU LUCRO?" à esquerda;
B = dois celulares lado a lado com o mesmo preço, selos +20% / −20% e "EMPATOU?" no alto; C = a régua do custo ocupando
a largura, com o "custo = 1" no centro, as setas ×1,5 e ×0,7 e o título "LUCRO OU PREJUÍZO?" em cima."""
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · DESCONTOS E LUCRO · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_etiqueta(c):
    background(c); selo_topo(c)
    text(c, "SOBROU", 84, 360, 170, "black", INK, align="left")
    text(c, "LUCRO?", 84, 540, 170, "black", GREEN, align="left")
    text(c, "etiqueta + 50%", 84, 700, 64, "extrabold", INK2, align="left")
    text(c, "liquidação − 33%", 84, 790, 64, "extrabold", AMBER, align="left")
    c.save(); c.translate(1380, 560); c.scale(2.1, 2.1)
    V.etiqueta(c, 0, 0, "R$ 150,00", "R$ ???", 1.0, risco=1.0, novo_a=1.0, w=390, h=210, rot=-8)
    c.restore()
    V.selo(c, 1580, 900, 1.0, "QUEIMA DE ESTOQUE", RED, -5, 52)


def capa_celulares(c):
    background(c); selo_topo(c, W / 2)
    s = "EMPATOU?"
    text(c, s, W / 2, 300, fit(s, 190, 1700), "black", AMBER)
    for k, (op, col) in enumerate((("+ 20%", GREEN), ("− 20%", RED))):
        x = 560 + k * 800
        rrect(c, x - 300, 400, 600, 560, 44, "#FFFFFF", shadow=True)
        rrect(c, x - 70, 440, 140, 230, 22, "#2B2F3A")
        rrect(c, x - 56, 458, 112, 194, 12, mix("#FFFFFF", BLUE, 0.35))
        text_mid(c, "R$ 600", x, 760, 100, "black", INK)
        pill(c, op, x, 880, col, size=56, anchor="center", bounds=(0, 1920))
    text_mid(c, "=", W / 2, 680, 140, "black", GRAY)


def capa_regua(c):
    background(c); selo_topo(c)
    text(c, "LUCRO OU", 84, 330, 150, "black", INK, align="left")
    text(c, "PREJUÍZO?", 84, 490, 150, "black", RED, align="left")
    text(c, "pense na RÉGUA DO CUSTO", 1836, 490, 56, "extrabold", PURPLE, align="right")
    y = 800
    x0, x1 = 160, 1760
    X = lambda v: x0 + (x1 - x0) * v / 2.0
    rrect(c, X(1.0), y - 40, x1 - X(1.0) + 20, 80, 18, GREEN, 0.16)
    rrect(c, x0 - 20, y - 40, X(1.0) - x0 + 20, 80, 18, RED, 0.14)
    line(c, x0 - 20, y, x1 + 20, y, INK2, 1.0, 10)
    c.drawCircle(X(1.0), y, 30, paint(BLUE))
    pill(c, "CUSTO = 1", X(1.0), y + 110, BLUE, size=48, anchor="center", bounds=(0, 1920))
    arrow(c, X(1.0) + 40, y - 70, X(1.5), y - 70, PURPLE, 1.0, 12, 34)
    pill(c, "× 1,5", (X(1.0) + X(1.5)) / 2, y - 140, PURPLE, size=48, anchor="center", bounds=(0, 1920))
    arrow(c, X(1.5), y + 70, X(1.08), y + 70, AMBER, 1.0, 12, 34)
    pill(c, "× 0,7", X(1.6) + 60, y + 110, AMBER, size=48, anchor="center", bounds=(0, 1920))


if __name__ == "__main__":
    for nome, fn in (("capa_A_sobrou_lucro", capa_etiqueta), ("capa_B_empatou", capa_celulares),
                     ("capa_C_regua_do_custo", capa_regua)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
