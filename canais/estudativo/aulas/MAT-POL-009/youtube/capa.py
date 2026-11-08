"""Capas do MAT-POL-009 (1280x720). Uso: python capa.py"""
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
AGUA = "#7CC4F5"


def cano(c, O, k):
    """o cano de raio 17 com a água de 9 de fundura (k px por cm)"""
    r = 17 * k
    y = O[1] + 8 * k
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    g = math.degrees(math.atan2(8, 15))
    path = skia.Path(); path.arcTo(ret, g, 180 - 2 * g, True); path.close()
    c.drawPath(path, M.paint(AGUA, 0.85))
    c.drawCircle(*O, r + 14, M.paint("#C9C9D6", 1, stroke=28))
    c.drawCircle(*O, r, M.paint(BR, 1, stroke=8))
    M.line(c, O[0] - 15 * k, y, O[0] + 15 * k, y, AMARELO, 1, 14)
    M.line(c, *O, O[0] - r * math.cos(math.radians(45)), O[1] - r * math.sin(math.radians(45)), BR, 1, 9)
    M.line(c, O[0] + 60, y, O[0] + 60, O[1] + r, BR, 1, 6, dash=[16, 12])
    c.drawCircle(*O, 12, M.paint(BR))
    return y


def a(c):  # o gancho: a largura da água
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    O, k = (470, 650), 20
    y = cano(c, O, k)
    E.escreve(c, "17", O[0] - 200, O[1] - 90, 90, "g", BR)
    E.escreve(c, "9", O[0] + 85, y + 120, 90, "g", BR)
    E.escreve(c, "?", O[0] - 40, y - 30, 120, "g", AMARELO)
    E.escreve(c, "largura", 1000, 380, 150, "g", BR)
    E.escreve(c, "da água?", 1000, 560, 150, "g", AMARELO)
    E.escreve(c, "+ 4 situações", 1010, 760, 100, "i", BR)
    E.escreve(c, "você resolve?", 1010, 900, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Polígonos", "e círculo", "5 situações")


def d(c):  # o atalho do regular: externo = 360 ÷ lados
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    cx, cy, r = 1440, 540, 310
    ini = 90 - 18
    pts = [(cx + r * math.cos(math.radians(ini + 36 * k)), cy + r * math.sin(math.radians(ini + 36 * k))) for k in range(10)]
    path = skia.Path(); path.addPoly(pts, True)
    c.drawPath(path, M.paint(BR, 0.08))
    pa = M.paint(BR, 1, stroke=10); pa.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, pa)
    V = pts[0]
    M.line(c, *V, V[0] + 230, V[1], claro, 1, 8, dash=[18, 12])
    ret = skia.Rect.MakeXYWH(V[0] - 190, V[1] - 190, 380, 380)
    p = skia.Path(); p.moveTo(*V); p.arcTo(ret, 0, -36, False); p.close()
    c.drawPath(p, M.paint(AMARELO, 0.85))
    E.escreve(c, "o atalho", 90, 360, 130, "i", BR)
    E.formula(c, "360 ÷ 10 = 36°", 90, 570, 130, "g", AMARELO)
    E.formula(c, "180 − 36 = 144°", 90, 760, 130, "g", BR)
    E.escreve(c, "cada ângulo do decágono", 90, 930, 74, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_largura_da_agua", a), ("capa_B_poligonos_e_circulo", b), ("capa_C_externo_360", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
