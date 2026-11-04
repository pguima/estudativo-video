"""Capas (1080x1920, vertical) do Short 003 "quantos triângulos", com as peças do próprio vídeo (render_short.py).
python3 youtube/capa.py -> youtube/capa_A_quantos_triangulos.jpg, youtube/capa_B_nao_e_16.jpg"""
import sys
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJ))
sys.argv = sys.argv[:1]
import render_short as R  # noqa: E402
from render_short import *  # noqa: E402,F401
from tech import glow_text  # noqa: E402

DY, ESC = 445, 1.18            # desce o triângulo do chefão para o meio da capa e aumenta um pouco


def titulo(c, l1, l2, y1, y2, c2=AMB):
    for s, y, size, col, g in ((l1, y1, 150, WHITE, 0.12), (l2, y2, 150, c2, 0.2)):
        size = min(size, size * 960 / text_w(s, "black", size))
        glow_text(c, s, W / 2, y, size, "black", col, 1, glow=g)


def chefao(c):
    cy = R.G_TOPO + R.G_N * R.G_H / 2
    c.save(); c.translate(W / 2, cy + DY); c.scale(ESC, ESC); c.translate(-W / 2, -cy)
    R.figura_grade(c, 9, 0, 1)
    R.triang(c, R.SOBE[2][1], CYA, 1, fill=0.14)                   # um médio
    R.triang(c, R.SOBE[1][0], AMB, 1, fill=0.22)                   # um pequeno em pé
    R.triang(c, R.DESCE[1][3], RED, 1, fill=0.22)                  # e o de ponta-cabeça, que todo mundo esquece
    c.restore()


def capa(qual, out):
    s = skia.Surface(W, H); c = s.getCanvas()
    BACKGROUND(c, 3.0)
    selo = "QUESTÃO DE MATEMÁTICA · 003"
    pill(c, selo, 52 + (text_w(selo, "extrabold", 24) + 29) / 2, 80, 24, AMB, BG0, 0.95, "extrabold")
    if qual == "a":
        pill(c, "DESAFIO", W / 2, 190, 46, RED, WHITE, 1)
        titulo(c, "QUANTOS", "TRIÂNGULOS?", 420, 585)
        chefao(c)
        xs = [W / 2 + (k - 1.5) * 235 for k in range(4)]
        for x, (L, n) in zip(xs, R.N3["opc"]):
            r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 105, 1490, 210, 120), 24, 24)
            c.drawRRect(r, paint(BG2, 0.85)); c.drawRRect(r, paint(CYA, 0.5, stroke=3))
            badge(c, L, x - 62, 1550, 1, r=26)
            text_mid(c, n, x + 30, 1550, 66, "black", WHITE, 1)
        label(c, "comenta o seu palpite", W / 2, 1700, 1, 52, INK2, "bold")
    else:
        pill(c, "NÍVEL CHEFÃO", W / 2, 190, 46, RED, WHITE, 1)
        titulo(c, "NÃO É 16!", "QUANTOS SÃO?", 420, 585, MNT)
        chefao(c)
        label(c, "conta antes de ver a resposta", W / 2, 1560, 1, 52, INK2, "bold")
        pill(c, "PAUSE E CONTE", W / 2, 1690, 50, AMB, BG0, 1)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 92)
    print(out)


if __name__ == "__main__":
    pasta = PROJ / "youtube"
    capa("a", pasta / "capa_A_quantos_triangulos.jpg")
    capa("b", pasta / "capa_B_nao_e_16.jpg")
