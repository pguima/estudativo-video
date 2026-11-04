"""Capas (1080x1920, vertical) do Short 006 "quantos apertos de mão", com as peças do próprio vídeo (render_short.py).
python3 youtube/capa.py -> youtube/capa_A_quantos_apertos.jpg, youtube/capa_B_nao_e_90.jpg"""
import sys
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJ))
sys.argv = sys.argv[:1]
import render_short as R  # noqa: E402
from render_short import *  # noqa: E402,F401
from tech import glow_text  # noqa: E402


def titulo(c, l1, l2, y1, y2, c2=AMB):
    for s, y, size, col, g in ((l1, y1, 150, WHITE, 0.12), (l2, y2, 150, c2, 0.2)):
        size = min(size, size * 960 / text_w(s, "black", size))
        glow_text(c, s, W / 2, y, size, "black", col, 1, glow=g)


def capa(qual, out):
    s = skia.Surface(W, H); c = s.getCanvas()
    BACKGROUND(c, 3.0)
    selo = "QUESTÃO DE MATEMÁTICA · 006"
    pill(c, selo, 52 + (text_w(selo, "extrabold", 24) + 29) / 2, 80, 24, AMB, BG0, 0.95, "extrabold")
    if qual == "a":
        pill(c, "DESAFIO", W / 2, 190, 46, RED, WHITE, 1)
        titulo(c, "QUANTOS", "APERTOS DE MÃO?", 420, 585)
        G = dict(R.R1, cy=1040.0, R=270.0, r=62)
        R.aperto(c, G, 0, 1, AMB, 1, 1.0, 11, 0.8)
        R.aperto(c, G, 0, 2, CYA, 1, 1.0, 11, 0.8)
        R.roda(c, G, 1, {0: AMB}, {0: 1.0})
        label(c, "cada um aperta a mão de todos, 1 vez", W / 2, 1400, 1, 40, INK2, "bold")
        xs = [W / 2 + (k - 1.5) * 235 for k in range(4)]
        for x, (L, n) in zip(xs, R.N1["opc"]):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 105, 1490, 210, 120), 24, 24)
            c.drawRRect(r, paint(BG2, 0.85)); c.drawRRect(r, paint(CYA, 0.5, stroke=3))
            badge(c, L, x - 62, 1550, 1, r=26)
            text_mid(c, n, x + 30, 1550, 66, "black", WHITE, 1)
        label(c, "comenta o seu palpite", W / 2, 1700, 1, 52, INK2, "bold")
    else:
        pill(c, "NÍVEL CHEFÃO", W / 2, 190, 46, RED, WHITE, 1)
        titulo(c, "NÃO É 90!", "QUANTOS SÃO?", 420, 585, MNT)
        G = dict(R.R3, cy=1050.0, R=300.0, r=40)
        for i, j in R.pares(G):
            R.aperto(c, G, i, j, MNT if i else AMB, 0.55 if i else 1, 1.0, 5 if i else 8, 0.4)
        R.roda(c, G, 1, {0: AMB}, {0: 1.0}, num=False)
        label(c, "10 amigos · todo mundo com todo mundo", W / 2, 1450, 1, 40, INK2, "bold")
        label(c, "conta antes de ver a resposta", W / 2, 1560, 1, 52, INK2, "bold")
        pill(c, "PAUSE E CONTE", W / 2, 1690, 50, AMB, BG0, 1)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 92)
    print(out)


if __name__ == "__main__":
    pasta = PROJ / "youtube"
    capa("a", pasta / "capa_A_quantos_apertos.jpg")
    capa("b", pasta / "capa_B_nao_e_90.jpg")
