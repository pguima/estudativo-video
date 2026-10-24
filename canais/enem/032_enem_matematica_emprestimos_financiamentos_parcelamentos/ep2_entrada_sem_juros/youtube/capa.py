"""Capas — Empréstimos, Financiamentos e Parcelamentos, Episódio 2: entrada + 1 parcela e o falso "sem juros" (tema claro).
3 variações em 1280x720.
Formatos: A = cartaz vermelho "10× SEM JUROS" gigante à direita, com uma lupa sobre a letra pequena "ou R$ 900 à vista",
e "LEIA A LETRA PEQUENA" à esquerda; B = a linha do tempo ocupando a largura: R$ 1.000 parado em HOJE ("NÃO VIAJA") e
R$ 900 viajando em arco até 30 DIAS, com "?% ao mês" no alto; C = três frações grandes lado a lado (100/2.000, 100/1.900,
100/900), todas neutras, e a pergunta "DIVIDE POR QUAL?" em cima. Nenhuma mostra a resposta."""
import importlib.util, math, subprocess, sys
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


def fit(s, size, maxw, peso="black"):
    while text_w(s, peso, size) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · EMPRÉSTIMOS · EP. 2"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_letra(c):
    background(c); selo_topo(c)
    text(c, "LEIA A", 84, 380, 150, "black", INK, align="left")
    text(c, "LETRA", 84, 540, 150, "black", AMBER, align="left")
    text(c, "PEQUENA", 84, 700, 150, "black", AMBER, align="left")
    text(c, "o \"sem juros\" esconde uma taxa", 84, 820, 50, "extrabold", INK2, align="left")
    cx, cy, w, h = 1420, 520, 760, 560
    rrect(c, cx - w / 2, cy - h / 2, w, h, 40, RED, shadow=True)
    text(c, "10×", cx, cy - 40, 220, "black", "#FFFFFF")
    text(c, "SEM JUROS!", cx, cy + 110, 96, "black", "#FFE680")
    # lupa sobre a letra pequena
    lx, ly, r = cx + 170, cy + 300, 130
    c.drawCircle(lx, ly, r, paint("#FFFFFF", 0.92))
    c.drawCircle(lx, ly, r, paint(INK, 1.0, stroke=16))
    text(c, "ou R$ 900", lx, ly - 4, 52, "black", RED)
    text(c, "à vista", lx, ly + 54, 46, "black", RED)
    line(c, lx + r * 0.72, ly + r * 0.72, lx + r * 1.35, ly + r * 1.35, INK, 1.0, 30)


def big_nota(c, cx, cy, val, col, w=420, h=150):
    rrect(c, cx - w / 2, cy - h / 2, w, h, 22, mix("#FFFFFF", col, 0.18), shadow=True, stroke=6, stroke_color=col)
    text_mid(c, val, cx, cy, fit(val, 80, w - 40), "black", col)


def capa_tempo(c):
    background(c); selo_topo(c, W / 2)
    s = "QUANTO CUSTA ADIAR?"
    text(c, s, W / 2, 270, fit(s, 140, 1760), "black", INK)
    y, x0, x1 = 820, 420, 1540
    line(c, x0 - 160, y, x1 + 160, y, INK2, 1.0, 10)
    for x, r in ((x0, "HOJE"), (x1, "30 DIAS")):
        line(c, x, y - 34, x, y + 34, INK2, 1.0, 10)
        text(c, r, x, y + 100, 52, "black", INK2)
    big_nota(c, x0, y - 120, "R$ 1.000", BLUE)
    V.selo(c, x0, y - 260, 1.0, "NÃO VIAJA", BLUE, -6, 48)
    path = skia.Path()
    for k in range(41):
        s_ = k / 40
        xx = x0 + 200 + (x1 - x0 - 200) * s_
        yy = y - 220 - 200 * math.sin(math.pi * s_)
        path.moveTo(xx, yy) if k == 0 else path.lineTo(xx, yy)
    c.drawPath(path, paint(AMBER, 1.0, stroke=12, cap_round=True))
    big_nota(c, x1, y - 120, "R$ 900", AMBER)
    pill(c, "?% ao mês", (x0 + x1) / 2 + 100, 470, RED, size=60, anchor="center", bounds=(0, 1920))


def capa_fracoes(c):
    background(c); selo_topo(c)
    text(c, "DIVIDE", 84, 320, 160, "black", INK, align="left")
    text(c, "POR QUAL?", 84, 480, 160, "black", AMBER, align="left")
    text(c, "R$ 100 de juros", 1836, 320, 70, "extrabold", RED, align="right")
    text(c, "na geladeira", 1836, 400, 56, "extrabold", INK2, align="right")
    for k, den in enumerate(("2.000", "1.900", "900")):
        x = 360 + k * 600
        rrect(c, x - 240, 600, 480, 380, 40, "#FFFFFF", shadow=True)
        V.K.mdraw(c, f"100/{den}", x, 790, 120, PURPLE, 1.0, align="center")


if __name__ == "__main__":
    for nome, fn in (("capa_A_letra_pequena", capa_letra), ("capa_B_quanto_custa_adiar", capa_tempo),
                     ("capa_C_divide_por_qual", capa_fracoes)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
