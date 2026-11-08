"""Capas do MAT-ANG-005 (1280x720). Uso: python capa.py"""
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


def iso(B, BC, base):
    A = (B[0] + BC / 2, B[1] - BC / 2 * math.tan(math.radians(base)))
    return A, B, (B[0] + BC, B[1])


def cunha(c, V, g1, g2, r, cor, alfa=0.55):
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    p = skia.Path(); p.moveTo(*V); p.arcTo(ret, -g1, -(g2 - g1), False); p.close()
    c.drawPath(p, M.paint(cor, alfa))
    c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor, 1, stroke=8, cap_round=True))


def triangulo(c, A, B, Cc, base, cor_base, cor_topo, tinta=BR, r=120):
    cunha(c, B, 0, base, r, cor_base)
    cunha(c, Cc, 180 - base, 180, r, cor_base)
    cunha(c, A, 270 - (90 - base), 270 + (90 - base), r * 0.8, cor_topo)
    for P, Q in ((A, B), (B, Cc), (Cc, A)):
        M.line(c, *P, *Q, tinta, 1, 12)
    for P, Q in ((A, B), (A, Cc)):  # tracinhos de lados iguais
        mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
        dx, dy = Q[0] - P[0], Q[1] - P[1]
        n = math.hypot(dx, dy)
        M.line(c, mx - dy / n * 26, my + dx / n * 26, mx + dy / n * 26, my - dx / n * 26, tinta, 1, 8)


def a(c):  # o gancho: base de 40° não dá 70 e 70
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    A, B, Cc = iso((90, 900), 860, 40)
    triangulo(c, A, B, Cc, 40, AMARELO, BR)
    E.escreve(c, "40°", 250, 860, 100, "g", AMARELO)
    E.escreve(c, "70 e 70?", 1060, 470, 170, "g", BR)
    E.risco(c, 1040, 520, 1780, 340, 9, 0, AMARELO, 30)
    E.escreve(c, "topo ou base?", 1060, 760, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Classificar", "triângulos", "lados e ângulos")


def d(c):  # o atalho: olhe o maior ângulo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    B, Cc = (300, 920), (900, 920)
    A = pt(B, 360, 115)
    cunha(c, B, 0, 115, 110, claro, 0.6)
    for P, Q in ((A, B), (B, Cc), (Cc, A)):
        M.line(c, *P, *Q, BR, 1, 12)
    E.escreve(c, "olhe só", 1000, 420, 130, "i", BR)
    E.escreve(c, "o maior", 990, 640, 200, "g", claro)
    E.escreve(c, "ângulo", 1000, 820, 130, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_topo_ou_base", a), ("capa_B_classificar_triangulos", b), ("capa_C_olhe_o_maior", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
