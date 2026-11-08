"""Capas do MAT-ANG-012 (1280x720). Uso: python capa.py"""
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
LILAS = "#C9C9FF"
_xt = (25 - 16 + 36) / 12
PEQ = ((0, 0), (6, 0), (_xt, math.sqrt(25 - _xt ** 2)))
_xg = (324 - 225 + 144) / 24
GRA = ((0, 0), (12, 0), (_xg, math.sqrt(324 - _xg ** 2)))


def coloca(pts, s, ox, oy):
    return [(ox + x * s, oy - y * s) for x, y in pts]


def arco(c, V, P, Q, r, cor, n=1):
    g1 = math.degrees(math.atan2(-(P[1] - V[1]), P[0] - V[0])) % 360
    g2 = math.degrees(math.atan2(-(Q[1] - V[1]), Q[0] - V[0])) % 360
    d = (g2 - g1) % 360
    if d > 180:
        g1, d = g2, 360 - d
    for k in range(n):
        rr = r - 16 * k
        ret = skia.Rect.MakeXYWH(V[0] - rr, V[1] - rr, 2 * rr, 2 * rr)
        if k == 0:
            p = skia.Path(); p.moveTo(*V); p.arcTo(ret, -g1, -d, False); p.close()
            c.drawPath(p, M.paint(cor, 0.4))
        c.drawArc(ret, -g1, -d, False, M.paint(cor, 1, stroke=7, cap_round=True))


def tri(c, T, cor=BR, larg=10):
    for i in range(3):
        M.line(c, *T[i], *T[(i + 1) % 3], cor, 1, larg)


def par(c, k=1.0):
    P = coloca(PEQ, 40, 90, 940)
    G = coloca(GRA, 40, 450, 940)
    tri(c, P); tri(c, G)
    arco(c, P[0], P[1], P[2], 60, LILAS); arco(c, P[1], P[2], P[0], 60, AMARELO, 2)
    arco(c, G[2], G[0], G[1], 80, LILAS); arco(c, G[0], G[1], G[2], 80, AMARELO, 2)
    return P, G


def a(c):  # o gancho: girado, x = ?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    P, G = par(c)
    E.escreve(c, "4", 270, 860, 90, "g", LILAS)
    E.escreve(c, "5", 90, 840, 90, "g", AMARELO)
    E.escreve(c, "12", 650, 1040, 100, "g", LILAS)
    E.escreve(c, "x", 960, 640, 120, "g", AMARELO)
    E.escreve(c, "girou.", 1100, 430, 140, "i", BR)
    E.escreve(c, "e agora?", 1100, 620, 170, "g", BR)
    E.escreve(c, "x = 15", 1110, 840, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Triângulos", "semelhantes", "critérios e razão")


def d(c):  # o atalho: maior com maior
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "maior com", 110, 420, 150, "g", BR)
    E.escreve(c, "maior", 110, 600, 190, "g", AMARELO)
    xs = (1150, 1390, 1630)
    for i, (s1, s2) in enumerate((("4", "12"), ("5", "15"), ("6", "18"))):
        cor = (claro, AMARELO, BR)[i]
        E.centro(c, s1, xs[i], 520, 130, "g", cor)
        M.line(c, xs[i], 560, xs[i], 680, cor, 1, 8, dash=[14, 12])
        E.centro(c, s2, xs[i], 810, 130, "g", cor)
    E.escreve(c, "× 3", 1300, 990, 110, "g", AMARELO)
    E.escreve(c, "sem ângulos", 110, 800, 110, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_girou_e_agora", a), ("capa_B_triangulos_semelhantes", b), ("capa_C_maior_com_maior", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
