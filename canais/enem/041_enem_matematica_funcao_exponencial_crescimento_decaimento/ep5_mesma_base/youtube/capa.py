"""Capas — Função Exponencial, Episódio 5: equações e inequações exponenciais, mesma base (tema claro). 3 variações em 1280x720.
A = a embalagem: 1 000 · 3^(t/2) = 81 000 com a caixa âmbar em volta do 1 000, "TIRE A EMBALAGEM" e "t = ?";
B = a balança: 81 se desfazendo em quatro fichas 3 num prato e 3^(t/2) no outro, com "MESMA BASE";
C = a ladeira: o gráfico de (1/3)ˣ e o sinal ">" com uma seta de giro e "O SINAL VIRA?".
Nenhuma mostra gabarito (o t = 8, as 12 h e o x < −2 não aparecem)."""
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
    s = "MATEMÁTICA ENEM · FUNÇÃO EXPONENCIAL · EP. 5"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_embalagem(c):
    background(c); selo_topo(c, W / 2)
    rrect(c, 120, 250, 1680, 300, 40, "#FFFFFF", 1.0, shadow=True)
    V.K.expr(c, f"{V.MIL} · 3^{{t/2}} = {V.OITENTA_MIL}", W / 2, 400, 150, 1.0,
             cores={0: AMBER, 1: AMBER, 2: INK, 3: PURPLE})
    w_ = V.K.math_w(f"{V.MIL} · 3^{{t/2}} = {V.OITENTA_MIL}", 150)
    x0 = W / 2 - w_ / 2 - 30
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, 300, V.K.math_w(V.MIL, 150) + 60, 200), 24, 24),
                paint(AMBER, 1.0, stroke=10))
    s1 = "TIRE A EMBALAGEM"
    text(c, s1, 110, 760, fit(s1, 150, 1150), "black", INK, align="left")
    text(c, "antes de comparar expoentes", 110, 870, 60, "black", AMBER, align="left")
    rrect(c, 1380, 640, 420, 280, 36, mix("#FFFFFF", PURPLE, 0.16))
    V.mx(c, "t = ?", 1590, 780, 130, 1.0, PURPLE)


def capa_balanca(c):
    background(c); selo_topo(c)
    s = "MESMA BASE"
    text(c, s, 110, 330, fit(s, 170, 900), "black", PURPLE, align="left")
    text(c, "e o x desce do expoente", 110, 440, 60, "black", INK, align="left")
    # 81 → 3 3 3 3
    text_mid(c, "81", 300, 820, 200, "black", INK)
    arrow(c, 480, 820, 600, 820, BLUE, 1.0, 10, 30)
    for k in range(4):
        V.chip(c, "3", 700 + k * 130, 820, BLUE, 1.0, size=80, w=110)
    V.balanca(c, 1480, 520, "3^{t/2}", "3^{■}", 1.0, size=70, w=520, alt=380)


def capa_ladeira(c):
    background(c); selo_topo(c)
    P = V.Plano(140, 250, 860, 700, (-3.5, 1.6), (-1, 30))
    P.eixos(c, 1.0, xt=(-3, -2, -1, 1), yt=(9, 27), size=30)
    P.curva(c, 1.0, lambda x: (1 / 3) ** x, PURPLE, width=16)
    line(c, P.x0, P.py(9), P.x0 + P.w, P.py(9), AMBER, 1.0, 6, dash=(20, 12))
    V.mx(c, "(1/3)^x > 9", P.px(0.2), P.py(23), 70, 1.0, PURPLE)
    for k, (s_, col) in enumerate((("O SINAL", INK), ("VIRA?", AMBER))):
        text(c, s_, 1450, 470 + k * 200, fit(s_, 190, 760), "black", col)
    text_mid(c, ">", 1330, 880, 150, "black", AMBER)
    arrow(c, 1430, 880, 1560, 880, INK2, 1.0, 10, 30)
    text_mid(c, "?", 1660, 880, 150, "black", AMBER)


if __name__ == "__main__":
    for nome, fn in (("capa_A_tire_a_embalagem", capa_embalagem), ("capa_B_mesma_base", capa_balanca),
                     ("capa_C_o_sinal_vira", capa_ladeira)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
