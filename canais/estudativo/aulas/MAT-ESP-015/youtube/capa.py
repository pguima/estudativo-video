"""Capas do MAT-ESP-015 (1280x720). Uso: python capa.py"""
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
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))


def bola(c, cx, cy, r, cor=None):
    """esfera em traço branco com o equador; cor = corpo pintado"""
    if cor:
        c.drawCircle(cx, cy, r, M.paint(cor, 0.9))
    c.drawCircle(cx, cy, r, M.paint(BR, 1, stroke=8))
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r * SEN, 2 * r, 2 * r * SEN), 0, 180, False, M.paint(BR, 1, stroke=6))


def corte(c, cx, cy, r, k, cor):
    """o círculo do corte a k·r acima do centro e o triângulo retângulo"""
    rr = r * math.sqrt(1 - k * k)
    y = cy - k * r * COS
    c.drawOval(skia.Rect.MakeXYWH(cx - rr, y - rr * SEN, 2 * rr, 2 * rr * SEN), M.paint(cor, 0.95))
    c.drawOval(skia.Rect.MakeXYWH(cx - rr, y - rr * SEN, 2 * rr, 2 * rr * SEN), M.paint(BR, 1, stroke=6))
    pt = M.paint(BR, 1, stroke=9); pt.setStrokeJoin(skia.Paint.kRound_Join)
    p = skia.Path(); p.addPoly([(cx, cy), (cx, y), (cx + rr, y)], True)
    c.drawPath(p, pt)
    return (cx, y), (cx + rr, y)


def a(c):  # o gancho: o corte a 3 cm do centro de uma laranja de raio 5
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    cx, cy, r = 470, 620, 330
    bola(c, cx, cy, r)
    (ox, oy), (px, py) = corte(c, cx, cy, r, 0.6, AMARELO)
    E.escreve(c, "3", cx - 70, (cy + oy) / 2 + 60, 80, "g", BR)
    E.escreve(c, "5", (cx + px) / 2 + 30, (cy + py) / 2 + 60, 80, "g", BR)
    E.escreve(c, "?", (ox + px) / 2 - 25, oy - (px - ox) * SEN - 20, 100, "g", BR)
    E.escreve(c, "corte a 3 do centro", 950, 380, 84, "i", BR)
    E.escreve(c, "raio do", 950, 560, 110, "g", BR)
    E.escreve(c, "círculo?", 950, 720, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Esfera", "hemisfério,", "fuso e seção")


def d(c):  # o atalho: conte círculos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "área do hemisfério:", 84, 330, 96, "i", BR)
    E.escreve(c, "conte círculos", 80, 500, 130, "g", BR)
    for k in range(3):
        c.drawCircle(180 + k * 230, 700, 90, M.paint(AMARELO, 0.95))
        c.drawCircle(180 + k * 230, 700, 90, M.paint(BR, 1, stroke=6))
    E.formula(c, "= 3πr^2", 820, 740, 140, "g", AMARELO)
    E.escreve(c, "2 da casca + 1 da tampa", 84, 930, 70, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_raio_do_corte", a), ("capa_B_partes_da_esfera", b), ("capa_C_conte_circulos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
