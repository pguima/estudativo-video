"""Capas (1080x1920, vertical) do Short 002 "quantos quadrados", com as peças do próprio vídeo (render_short.py).
python3 youtube/capa.py -> youtube/capa_A_quantos_quadrados.jpg, youtube/capa_B_nao_e_64.jpg"""
import sys
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJ))
sys.argv = sys.argv[:1]
import render_short as R  # noqa: E402
from render_short import *  # noqa: E402,F401
from tech import glow_text  # noqa: E402

FIG_Y = 1070                   # centro vertical da figura


def titulo(c, l1, l2, y1, y2, c2=AMB):
    for s, y, size, col, g in ((l1, y1, 150, WHITE, 0.12), (l2, y2, 150, c2, 0.2)):
        size = min(size, size * 960 / text_w(s, "black", size))
        glow_text(c, s, W / 2, y, size, "black", col, 1, glow=g)


def figura(N):
    """a grade do nível, centrada na capa, já desenhada por inteiro"""
    N = dict(N, t_hook=-10)
    N["x0"] = W / 2 - N["cols"] * N["cel"] / 2
    N["y0"] = FIG_Y - N["rows"] * N["cel"] / 2
    R.grade(c_, N, 0)
    return N


def capa(qual, out):
    global c_
    s = skia.Surface(W, H); c = c_ = s.getCanvas()
    BACKGROUND(c, 3.0)
    selo = "QUESTÃO DE MATEMÁTICA · 002"
    pill(c, selo, 52 + (text_w(selo, "extrabold", 24) + 29) / 2, 80, 24, AMB, BG0, 0.95, "extrabold")
    if qual == "a":
        pill(c, "DESAFIO", W / 2, 190, 46, RED, WHITE, 1)
        titulo(c, "QUANTOS", "QUADRADOS?", 420, 585)
        N = figura(dict(R.N1, cel=200))
        R.quadrado(c, N, 0, 0, 1, AMB, 1, fill=0.22)                 # um pequeno
        R.quadrado(c, N, 1, 0, 3, MNT, 1, fill=0.10)                 # e um 3 × 3
        xs = [W / 2 + (k - 1.5) * 235 for k in range(4)]
        for x, (L, n) in zip(xs, R.N1["opc"]):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 105, 1490, 210, 120), 24, 24)
            c.drawRRect(r, paint(BG2, 0.85)); c.drawRRect(r, paint(CYA, 0.5, stroke=3))
            badge(c, L, x - 62, 1550, 1, r=26)
            text_mid(c, n, x + 30, 1550, 66, "black", WHITE, 1)
        label(c, "comenta o seu palpite", W / 2, 1700, 1, 52, INK2, "bold")
    else:
        pill(c, "NÍVEL CHEFÃO", W / 2, 190, 46, RED, WHITE, 1)
        titulo(c, "NÃO É 64!", "QUANTOS SÃO?", 420, 585, MNT)
        N = figura(dict(R.N3, cel=88))
        R.quadrado(c, N, 0, 0, 1, AMB, 1, inset=6, width=8, fill=0.25)
        R.quadrado(c, N, 5, 1, 2, CYA, 1, inset=6, width=8, fill=0.2)
        R.quadrado(c, N, 1, 3, 4, MNT, 1, inset=8, width=9, fill=0.12)
        label(c, "o tabuleiro de xadrez esconde mais", W / 2, 1560, 1, 50, INK2, "bold")
        pill(c, "PAUSE E CONTE", W / 2, 1690, 50, AMB, BG0, 1)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 92)
    print(out)


if __name__ == "__main__":
    pasta = PROJ / "youtube"
    capa("a", pasta / "capa_A_quantos_quadrados.jpg")
    capa("b", pasta / "capa_B_nao_e_64.jpg")
