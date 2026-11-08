"""Capas do MAT-TOP-013 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def hip(c, cx, cy, ka, kb, umax, cor, lw):
    for ramo in (1, -1):
        path = skia.Path()
        for i in range(81):
            u = -umax + 2 * umax * i / 80
            x, y = cx + ramo * ka * math.cosh(u), cy - kb * math.sinh(u)
            path.moveTo(x, y) if i == 0 else path.lineTo(x, y)
        c.drawPath(path, M.paint(cor, 1, stroke=lw, cap_round=True))


def a(c):  # cinco situações com as três cônicas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5", 84, 560, 380, "g", AMARELO)
    E.escreve(c, "situações", 370, 450, 130, "i", BR)
    E.escreve(c, "no plano", 370, 570, 130, "g", BR)
    E.escreve(c, "pause e resolva", 84, 860, 110, "i", BR)
    c.drawOval(skia.Rect.MakeXYWH(1240, 180, 520, 300), M.paint(BR, 1, stroke=12))
    hip(c, 1500, 790, 90, 120, 1.15, BR, 12)
    for fx in (1500 - 207, 1500 + 207):
        c.drawCircle(fx, 330, 16, M.paint(AMARELO))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Praticando", "cônicas", "e distâncias")


def d(c):  # o macete: alinhados pela inclinação
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "alinhados?", 84, 380, 170, "g", BR)
    E.escreve(c, "sem determinante", 84, 560, 120, "i", BR)
    E.formula(c, "f{4}{2} ≠ f{3}{1}", 84, 880, 170, "g", "#3CC7D3")
    k, x0, y0 = 90, 1300, 960
    P = lambda x, y: (x0 + (x - 1) * k * 1.4, y0 - (y - 1) * k)
    M.line(c, *P(1, 1), *P(3, 5), BR, 0.8, 7)
    M.line(c, *P(3, 5), *P(4, 8), AMARELO, 1, 7)
    for p_ in ((1, 1), (3, 5), (4, 8)):
        c.drawCircle(*P(*p_), 20, M.paint(BR))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_situacoes", a), ("capa_B_praticando_conicas", b), ("capa_C_alinhados_sem_determinante", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
