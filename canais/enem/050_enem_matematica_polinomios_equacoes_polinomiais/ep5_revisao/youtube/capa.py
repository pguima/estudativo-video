"""Capas — Polinômios e Equações Polinomiais, Episódio 5: Revisão (tema claro). 3 variações em 1280x720.
Formatos (sem repetir as revisões anteriores): A = título à esquerda "3 FRASES RESOLVEM QUASE TUDO" e, à direita, as três
frases numeradas em faixas coloridas; B = fundo escuro com a esteira de Briot-Ruffini gigante e o resto "?" aceso,
"O RESTO SEM DIVIDIR"; C = o gráfico da questão 4 (toca e atravessa) com "QUAL É A LEI?". Nenhuma mostra gabarito.
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
    while V.ftw(s, size, peso) > maxw:
        size -= 4
    return size


def selo_topo(c, cx=None, cor=BLUE):
    s = "MATEMÁTICA ENEM · POLINÔMIOS · REVISÃO"
    if cx is None:
        pill(c, s, 84, 90, cor, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, cor, size=34, anchor="center", bounds=(0, 1920))


def capa_frases(c):
    background(c)
    selo_topo(c)
    for k, s in enumerate(("3 FRASES", "RESOLVEM", "QUASE TUDO")):
        text(c, s, 84, 330 + k * 150, fit("QUASE TUDO", 140, 860), "black", INK if k < 2 else PURPLE, align="left")
    for k, (s, col) in enumerate((("P(a) = 0", BLUE), ("resto = P(a)", PURPLE), ("raiz baixa o grau", GREEN))):
        y = 260 + k * 250
        shadow_rrect(c, 1000, y, 840, 200, 100, 1, 1.3)
        rrect(c, 1000, y, 840, 200, 100, mix("#FFFFFF", col, 0.20))
        c.drawCircle(1100, y + 100, 64, paint(col, 1))
        text_mid(c, str(k + 1), 1100, y + 100, 80, "black", "#FFFFFF")
        text(c, s, 1200, y + 128, fit(s, 76, 600), "black", col, align="left")


def capa_esteira(c):
    c.drawRect(skia.Rect.MakeWH(W, H), paint(INK, 1))
    selo_topo(c, W / 2, AMBER)
    s = "O RESTO SEM DIVIDIR"
    text(c, s, W / 2, 290, fit(s, 150, 1760), "black", "#FFFFFF")
    shadow_rrect(c, 230, 400, 1460, 520, 50, 1, 1.4)
    rrect(c, 230, 400, 1460, 520, 50, "#FFFFFF")
    x0, y0, cw = 330, 520, 220
    line(c, x0 + cw, y0 - 40, x0 + cw, y0 + 300, INK, 1, 10)
    line(c, x0 + cw - 50, y0 + 150, x0 + cw * 6 + 20, y0 + 150, INK, 1, 10)
    text_mid(c, "−2", x0 + cw / 2, y0 + 60, 110, "black", PURPLE)
    for j, v in enumerate(("1", "0", "−3", "1", "2")):
        cx = x0 + cw * (j + 1.5)
        if v == "0":
            rrect(c, cx - 90, y0 - 10, 180, 140, 26, mix("#FFFFFF", AMBER, 0.5))
        text_mid(c, v, cx, y0 + 60, 110, "black", INK)
    rrect(c, x0 + cw * 5 + 20, y0 + 175, cw - 40, 150, 26, mix("#FFFFFF", GREEN, 0.4))
    text_mid(c, "?", x0 + cw * 5.5, y0 + 250, 130, "black", GREEN)


def capa_grafico(c):
    background(c)
    selo_topo(c, W / 2)
    s = "QUAL É A LEI?"
    text(c, s, W / 2, 290, fit(s, 170, 1760), "black", INK)
    shadow_rrect(c, 160, 360, 1600, 660, 50, 1, 1.4)
    rrect(c, 160, 360, 1600, 660, 50, "#FFFFFF")
    cx, cy, sx, sy = 1000, 700, 150, 11
    line(c, 280, cy, 1600, cy, INK2, 1, 8)
    line(c, cx, 400, cx, 990, INK2, 1, 8)
    p = skia.Path(); first = True; xv = -3.75
    while xv <= 1.95:
        yv = -2 * (xv - 1) ** 2 * (xv + 3)
        X, Y = cx + xv * sx, max(390, min(990, cy - yv * sy))
        if first:
            p.moveTo(X, Y); first = False
        else:
            p.lineTo(X, Y)
        xv += 0.02
    c.drawPath(p, paint(BLUE, 1, stroke=14))
    for xr, s_, col, dy in ((1, "toca", AMBER, -60), (-3, "atravessa", GREEN, 150)):
        c.drawCircle(cx + xr * sx, cy, 28, paint(col, 1))
        text_mid(c, s_ + "?", cx + xr * sx + (0 if xr == 1 else -150), cy + dy, 62, "black", col)
    c.drawCircle(cx, cy + 6 * sy, 24, paint(PURPLE, 1))
    text(c, "(0, −6)", cx + 40, cy + 6 * sy + 70, 60, "black", PURPLE, align="left")


if __name__ == "__main__":
    for nome, fn in (("capa_A_tres_frases", capa_frases), ("capa_B_resto_sem_dividir", capa_esteira),
                     ("capa_C_qual_e_a_lei", capa_grafico)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
