"""Capas — Empréstimos, Financiamentos e Parcelamentos, Episódio 3: o SAC (tema claro). 3 variações em 1280x720.
Formatos: A = título no alto e as 5 parcelas em colunas (azul + laranja) ocupando a base; B = boleto gigante de ponta a
ponta, com a parte dos juros marcada com "?"; C = escadinha dos juros na diagonal e faixa de título embaixo."""
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


def selo_topo(c, cx=None):
    s = "MATEMÁTICA ENEM · FINANCIAMENTOS · EP. 3"
    if cx is None:
        pill(c, s, 84, 90, BLUE, size=34, bounds=(0, 1920))
    else:
        pill(c, s, cx, 90, BLUE, size=34, anchor="center", bounds=(0, 1920))


def capa_colunas(c):
    background(c); selo_topo(c, W / 2)
    s = "POR QUE A PARCELA DIMINUI?"
    text(c, s, W / 2, 290, fit(s, 140, 1780), "black", INK)
    base = 1010
    for k, (_, saldo, j, am, par) in enumerate(V.SAC5):
        x = 140 + k * 290
        hb, hj = 300, j * 0.6
        shadow_rrect(c, x, base - hb - hj - 6, 220, hb + hj + 6, 16, 1, 1.2)
        rrect(c, x, base - hb, 220, hb, 16, V.FATIA)
        rrect(c, x, base - hb - hj - 6, 220, hj, 16, V.LARANJA)
        text_mid(c, "R$ " + V.rs(par), x + 110, base - hb - hj - 46, 42, "black", INK)
    pill(c, "juros", 1720, 640, V.LARANJA, size=44, anchor="center")
    pill(c, "fatia fixa", 1720, 860, V.FATIA, size=44, anchor="center")


def capa_boleto(c):
    background(c); selo_topo(c)
    s1 = "PAGOU R$ 2.400"
    text(c, s1, 84, 290, fit(s1, 150, 1700), "black", INK, align="left")
    s2 = "E A DÍVIDA CAIU SÓ R$ 2.000?"
    text(c, s2, 84, 420, fit(s2, 104, 1760), "black", V.FATIA, align="left")
    x, y, w, h = 84, 520, W - 168, 400
    shadow_rrect(c, x, y, w, h, 34, 1, 1.4)
    rrect(c, x, y, w, h, 34, "#FFFFFF")
    for kk in range(3):
        line(c, x + 60, y + 70 + kk * 34, x + 700 - kk * 140, y + 70 + kk * 34, "#D8D8D2", 1.0, 10)
    ba = (w - 120) * 2000 / 2400
    rrect(c, x + 60, y + 200, ba, 150, 22, V.FATIA)
    text_mid(c, "2.000", x + 60 + ba / 2, y + 275, 96, "black", "#FFFFFF")
    rrect(c, x + 70 + ba, y + 200, (w - 120) - ba - 10, 150, 22, V.LARANJA)
    text_mid(c, "400 ?", x + 70 + ba + ((w - 120) - ba - 10) / 2, y + 275, 72, "black", "#FFFFFF")


def capa_escada(c):
    background(c); selo_topo(c)
    vals = ["400", "320", "240", "160", "80"]
    for i, v in enumerate(vals):
        x, y = 140 + i * 330, 175 + i * 100
        shadow_rrect(c, x, y, 290, 140, 22, 1, 1.2)
        rrect(c, x, y, 290, 140, 22, mix("#FFFFFF", V.LARANJA, 0.18))
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, 290, 140), 22, 22), paint(V.LARANJA, 1.0, stroke=6))
        text_mid(c, v, x + 145, y + 70, 84, "black", V.LARANJA)
        if i:
            text(c, "− 80", x - 50, y + 120, 44, "black", RED)
    rrect(c, 0, 760, W, 320, 0, PURPLE)
    s = "TODOS OS JUROS DE UMA VEZ"
    text(c, s, W / 2, 900, fit(s, 120, 1780), "black", "#FFFFFF")
    text(c, "o SAC sem montar a tabela inteira", W / 2, 1010, 54, "extrabold", "#EDE7FF")


if __name__ == "__main__":
    for nome, fn in (("capa_A_parcela_diminui", capa_colunas), ("capa_B_boleto_400", capa_boleto),
                     ("capa_C_escadinha_juros", capa_escada)):
        surf = skia.Surface(W, H)
        fn(surf.getCanvas())
        png = HERE / f"{nome}_1920.png"
        surf.makeImageSnapshot().save(str(png), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(png), "-vf", "scale=1280:720:flags=lanczos",
                        "-q:v", "2", str(HERE / f"{nome}.jpg")], check=True)
        png.unlink()
        print(nome)
