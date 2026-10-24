"""Capas — Progressão Geométrica, Episódio 4: a PG disfarçada (tema claro). 3 variações em 1280x720.
A = o carro de R$ 80.000 com barras caindo ano a ano e "?" no 3º ano: "PERDE 20% AO ANO. E EM 3 ANOS?";
B = as três esteiras (cofre, frasco, carro) entrando na mesma máquina "×q": "A PG DISFARÇADA";
C = o fator em dúvida: "PERDEU 20%:  × 0,2 ?  × 0,8 ?" com o carro.
Nenhuma mostra gabarito (R$ 40.960,00 não aparece)."""
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


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · PROGRESSÃO GEOMÉTRICA · EP. 4"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_carro(c):
    background(c); selo_topo(c)
    shadow_rrect(c, 70, 190, 960, 820, 40, 1, 1.4)
    rrect(c, 70, 190, 960, 820, 40, "#FFFFFF")
    V.carro(c, 250, 320, 190, 1)
    text(c, "R$ 80.000", 620, 345, 76, "black", V.CARRO)
    base, hmax = 930, 480
    for k, v in enumerate((1.0, 0.8, 0.64, None)):
        x = 150 + k * 215
        if v is None:
            c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, base - 0.42 * hmax, 160, 0.42 * hmax), 18, 18),
                        paint(AMBER, 1, stroke=8))
            text_mid(c, "?", x + 80, base - 0.21 * hmax, 130, "black", AMBER)
        else:
            rrect(c, x, base - v * hmax, 160, v * hmax, 18, mix("#FFFFFF", V.CARRO, 0.3 + 0.6 * (k == 0)))
        text(c, ("hoje", "1 ano", "2 anos", "3 anos")[k], x + 80, base + 50, 34, "bold", GRAY)
    s1 = "PERDE 20% AO ANO."
    text(c, s1, 1460, 430, fit(s1, 110, 800), "black", INK)
    s2 = "E EM 3 ANOS?"
    sz = fit(s2, 120, 740)
    w = text_w(s2, "black", sz) + 80
    shadow_rrect(c, 1460 - w / 2, 500, w, 200, 30, 1, 1.4)
    rrect(c, 1460 - w / 2, 500, w, 200, 30, AMBER)
    text_mid(c, s2, 1460, 600, sz, "black", "#FFFFFF")
    V.selo(c, 1460, 850, 1.0, "NÃO É TIRAR 16.000 POR ANO", RED, -5, 40)


def capa_maquinas(c):
    background(c); selo_topo(c, W / 2)
    s = "A PG DISFARÇADA"
    text(c, s, W / 2, 300, fit(s, 170, 1780), "black", INK)
    V.maquina(c, W / 2, 620, "×q", 1, w=360, h=220, size=110)
    for fn, col, rot, x, y in ((V.cofre, V.COFRE, "juros", 330, 480), (V.frasco, V.FRASCO, "remédio", 1590, 600),
                               (V.carro, V.CARRO, "carro usado", 330, 790)):
        fn(c, x, y, 180, 1)
        text(c, rot, x, y + 140, 40, "black", col)
    arrow(c, 470, 520, 760, 590, GRAY, 1, 8, 26)
    arrow(c, 470, 800, 760, 660, GRAY, 1, 8, 26)
    arrow(c, 1450, 620, 1170, 620, GRAY, 1, 8, 26)
    rrect(c, 0, 960, W, 120, 0, PURPLE)
    text_mid(c, "juros, meia-vida e carro usado: a mesma conta", W / 2, 1020, 60, "black", "#FFFFFF")


def capa_fator(c):
    background(c); selo_topo(c, W / 2)
    s = "PERDEU 20%:"
    text(c, s, W / 2, 310, fit(s, 170, 1780), "black", INK)
    for k, (s_, col) in enumerate((("× 0,2 ?", PURPLE), ("× 0,8 ?", PURPLE))):
        x = 560 + k * 800
        shadow_rrect(c, x - 330, 400, 660, 330, 44, 1, 1.4)
        rrect(c, x - 330, 400, 660, 330, 44, "#FFFFFF")
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 330, 400, 660, 330), 44, 44), paint(col, 1, stroke=10))
        text_mid(c, s_, x, 565, 150, "black", col)
    text_mid(c, "OU", W / 2, 565, 70, "black", GRAY)
    V.carro(c, 260, 860, 200, 1)
    rrect(c, 420, 800, 1400, 130, 30, AMBER)
    text_mid(c, "qual é o fator da PG?", 1120, 865, 76, "black", "#FFFFFF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_perde_20_por_ano", capa_carro), ("capa_B_pg_disfarcada", capa_maquinas),
                     ("capa_C_qual_fator", capa_fator)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
