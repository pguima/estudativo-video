"""Capas do MAT-POL-003 (1280x720). Uso: python capa.py"""
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


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def peca(n, O, theta, L):
    pts, P, h = [O], O, theta
    for _ in range(n - 1):
        P = pt(P, L, h); pts.append(P); h += 360 / n
    return pts


def contorno(c, pts, cor, larg=10, fundo=None, alfa=0.0):
    p = skia.Path(); p.addPoly(pts, True)
    if fundo:
        c.drawPath(p, M.paint(fundo, alfa))
    pa = M.paint(cor, 1, stroke=larg); pa.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pa)


def cunha(c, O, g1, g2, r, cor, alfa=0.7):
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    p = skia.Path(); p.moveTo(*O); p.arcTo(ret, -g1, -(g2 - g1), False); p.close()
    c.drawPath(p, M.paint(cor, alfa))


def a(c):  # o gancho: hexágono fecha, pentágono não
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    O1 = (420, 600)
    for k in range(3):
        contorno(c, peca(6, O1, 120 * k - 90, 190), BR, 10, AMARELO, 0.9)
    O2 = (1150, 600)
    for k in range(3):
        contorno(c, peca(5, O2, 108 * k - 90, 190), BR, 10, BR, 0.15)
    cunha(c, O2, 234, 270, 200, "#FF5A5A", 0.85)
    E.escreve(c, "fecha", 270, 1010, 110, "g", AMARELO)
    E.escreve(c, "buraco!", 1020, 1010, 110, "g", "#FF8A8A")
    E.escreve(c, "por quê?", 1450, 330, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Polígonos", "regulares", "e pisos")


def d(c):  # o atalho: comece pelo externo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho", 90, 340, 130, "i", BR)
    E.formula(c, "externo = 360 ÷ n", 90, 560, 130, "g", BR)
    E.formula(c, "interno = 180 − externo", 90, 760, 110, "g", claro)
    E.formula(c, "octógono: 135°", 90, 960, 110, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_hexagono_fecha", a), ("capa_B_poligonos_regulares", b), ("capa_C_comece_pelo_externo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
