"""Capas (1080x1920, vertical) do Short 004 "quantos retângulos", com as peças do próprio vídeo (render_short.py).
python3 youtube/capa.py -> youtube/capa_A_quantos_retangulos.jpg, youtube/capa_B_nao_e_9.jpg"""
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


def grade(c, G, cy):
    """a grade do nível, centrada em cy, já desenhada por inteiro"""
    G = dict(G, y0=cy - G["rows"] * G["ch"] / 2)
    R.figura(c, G, 9, 0, 1)
    return G


def capa(qual, out):
    s = skia.Surface(W, H); c = s.getCanvas()
    BACKGROUND(c, 3.0)
    selo = "QUESTÃO DE MATEMÁTICA · 004"
    pill(c, selo, 52 + (text_w(selo, "extrabold", 24) + 29) / 2, 80, 24, AMB, BG0, 0.95, "extrabold")
    if qual == "a":
        pill(c, "DESAFIO", W / 2, 190, 46, RED, WHITE, 1)
        titulo(c, "QUANTOS", "RETÂNGULOS?", 420, 585)
        G = grade(c, dict(R.G2, x0=150.0, cw=260.0, ch=210.0), 1050)
        R.ret(c, G, (0, 1, 0, 1), AMB, 1, fill=0.22)                  # uma casa
        R.ret(c, G, (1, 3, 0, 2), MNT, 1, fill=0.10)                  # e um maior
        xs = [W / 2 + (k - 1.5) * 235 for k in range(4)]
        for x, (L, n) in zip(xs, R.N2["opc"]):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 105, 1490, 210, 120), 24, 24)
            c.drawRRect(r, paint(BG2, 0.85)); c.drawRRect(r, paint(CYA, 0.5, stroke=3))
            badge(c, L, x - 62, 1550, 1, r=26)
            text_mid(c, n, x + 30, 1550, 66, "black", WHITE, 1)
        label(c, "comenta o seu palpite", W / 2, 1700, 1, 52, INK2, "bold")
    else:
        pill(c, "NÍVEL CHEFÃO", W / 2, 190, 46, RED, WHITE, 1)
        titulo(c, "NÃO É 9!", "QUANTOS SÃO?", 420, 585, MNT)
        G = grade(c, dict(R.G3, x0=225.0, cw=210.0, ch=210.0), 1060)
        R.ret(c, G, (0, 1, 0, 1), AMB, 1, fill=0.22)
        R.ret(c, G, (1, 3, 0, 1), CYA, 1, inset=16, fill=0.14)
        R.ret(c, G, (0, 2, 1, 3), MNT, 1, fill=0.10)
        label(c, "conta antes de ver a resposta", W / 2, 1560, 1, 52, INK2, "bold")
        pill(c, "PAUSE E CONTE", W / 2, 1690, 50, AMB, BG0, 1)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 92)
    print(out)


if __name__ == "__main__":
    pasta = PROJ / "youtube"
    capa("a", pasta / "capa_A_quantos_retangulos.jpg")
    capa("b", pasta / "capa_B_nao_e_9.jpg")
