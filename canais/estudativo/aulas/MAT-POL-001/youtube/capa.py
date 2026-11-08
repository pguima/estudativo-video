"""Capas do MAT-POL-001 (1280x720). Uso: python capa.py"""
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


def contorno(c, pts, cor, larg=12):
    p = skia.Path(); p.addPoly(pts, True)
    pa = M.paint(cor, 1, stroke=larg); pa.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pa)


def cunha(c, V, g1, g2, r, cor, alfa=0.55):
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    p = skia.Path(); p.moveTo(*V); p.arcTo(ret, -g1, -(g2 - g1), False); p.close()
    c.drawPath(p, M.paint(cor, alfa))
    c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor, 1, stroke=7, cap_round=True))


def a(c):  # o gancho: um quadrado é um retângulo?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, y, l = 130, 330, 560
    pts = [(x, y + l), (x + l, y + l), (x + l, y), (x, y)]
    c.drawPath((lambda p: (p.addPoly(pts, True), p)[1])(skia.Path()), M.paint(BR, 0.12))
    contorno(c, pts, BR, 14)
    s = 90
    for V, dx, dy in ((pts[0], 1, -1), (pts[1], -1, -1), (pts[2], -1, 1), (pts[3], 1, 1)):
        r = skia.Rect.MakeXYWH(min(V[0], V[0] + dx * s), min(V[1], V[1] + dy * s), s, s)
        c.drawRect(r, M.paint(AMARELO, 0.75))
        c.drawRect(r, M.paint(AMARELO, 1, stroke=7))
    E.escreve(c, "quadrado", 860, 400, 150, "i", BR)
    E.escreve(c, "é retângulo?", 850, 620, 150, "g", BR)
    E.escreve(c, "é, sim!", 860, 890, 210, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Quadriláteros", "sem decorar", "regra por regra")


def d(c):  # o atalho: só duas medidas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    A = (120, 900); B = (820, 900); D = pt(A, 420, 62); Cc = (D[0] + 700, D[1])
    cunha(c, A, 0, 62, 120, claro)
    cunha(c, Cc, 180, 242, 120, claro)
    cunha(c, B, 62, 180, 95, BR, 0.35)
    cunha(c, D, 242, 360, 95, BR, 0.35)
    contorno(c, [A, B, Cc, D], BR, 12)
    E.formula(c, "α", 270, 860, 100, "g", claro)
    E.formula(c, "α", 830, 660, 100, "g", claro)
    E.escreve(c, "o atalho", 1100, 330, 120, "i", BR)
    E.escreve(c, "só 2", 1100, 540, 200, "g", BR)
    E.escreve(c, "medidas", 1100, 720, 150, "g", claro)
    E.formula(c, "α  e  180° − α", 1100, 900, 90, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quadrado_e_retangulo", a), ("capa_B_quadrilateros", b), ("capa_C_duas_medidas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
