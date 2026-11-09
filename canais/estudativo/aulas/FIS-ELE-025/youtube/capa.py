"""Capas do FIS-ELE-025 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def circuito(c, x0, x1, x2, yt, yb, cor):
    """três ramos: resistor em cima nos três, pilha embaixo nos dois de fora; os fios param nas peças"""
    M.line(c, x0, yt, x2, yt, cor, 1, 12)
    M.line(c, x0, yb, x2, yb, cor, 1, 12)
    yr0, yr1 = yt + 70, yt + 196
    yp = (yt + yb) / 2 + 60
    for x in (x0, x1, x2):
        M.line(c, x, yt, x, yr0, cor, 1, 12)
        pts = [(x, yr0)] + [(x + 26 * (1 if k % 2 else -1), yr0 + 18 * k) for k in range(1, 7)] + [(x, yr1)]
        for A, B in zip(pts, pts[1:]):
            M.line(c, *A, *B, BR, 1, 9)
        if x == x1:
            M.line(c, x, yr1, x, yb, cor, 1, 12)
        else:
            M.line(c, x, yr1, x, yp - 20, cor, 1, 12)
            M.line(c, x - 70, yp - 20, x + 70, yp - 20, BR, 1, 10, cap_round=False)
            M.line(c, x - 36, yp + 22, x + 36, yp + 22, BR, 1, 26, cap_round=False)
            M.line(c, x, yp + 22, x, yb, cor, 1, 12)
    for P in ((x1, yt), (x1, yb)):
        c.drawCircle(*P, 18, M.paint(BR))


def a(c):  # o gancho: duas malhas viram um sistema
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "duas malhas", 84, 380, 130, "i", BR)
    E.escreve(c, "viram um", 84, 560, 170, "g", BR)
    M.rrect(c, 70, 620, 860, 230, 30, BR)
    E.escreve(c, "sistema", 110, 795, 170, "g", COR)
    circuito(c, 1180, 1480, 1780, 260, 820, E.mix(COR, BR, 0.85))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Duas", "malhas", "Kirchhoff")


def d(c):  # o macete: a tensão entre os dois nós resolve numa equação
    palco_capa(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "dois nós?", 84, 360, 130, "i", BR)
    E.escreve(c, "uma equação só", 84, 540, 150, "g", BR)
    E.formula(c, "f{10 − U}{2} + f{6 − U}{2} = U", 84, 820, 110, "g", E.mix(COR, BR, 0.35))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_duas_malhas_um_sistema", a), ("capa_B_duas_malhas", b), ("capa_C_uma_equacao_so", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
