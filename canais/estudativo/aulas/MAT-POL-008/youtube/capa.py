"""Capas do MAT-POL-008 (1280x720). Uso: python capa.py"""
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


def dirg(g):
    return math.cos(math.radians(g)), -math.sin(math.radians(g))


def em(P, u, d):
    return P[0] + u[0] * d, P[1] + u[1] * d


def cordas(c, O, k, larg=12):
    """as cordas de verdade: raio √33, P a 3 do centro, pedaços 3, 8, 4 e 6 (k px por cm)"""
    p = dirg(250)
    P = em(O, p, 3 * k)
    g = math.degrees(math.atan2(-p[1], p[0]))
    u, v = dirg(g + math.degrees(math.acos(-2.5 / 3))), dirg(g - math.degrees(math.acos(-1 / 3)))
    A, B, Cc, D = em(P, u, -3 * k), em(P, u, 8 * k), em(P, v, -4 * k), em(P, v, 6 * k)
    c.drawCircle(*O, math.sqrt(33) * k, M.paint(BR, 1, stroke=larg))
    M.line(c, *A, *B, BR, 1, larg + 4)
    M.line(c, *Cc, *D, AMARELO, 1, larg + 4)
    c.drawCircle(*P, 16, M.paint(BR))
    return P, A, B, Cc, D


def a(c):  # o gancho: o pedaço que ninguém mediu
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    P, A, B, Cc, D = cordas(c, (480, 600), 62)
    for txt, Q, lado, cor, size in (("3", A, 1, BR, 90), ("8", B, -1, BR, 90), ("4", Cc, -1, AMARELO, 90), ("?", D, 1, AMARELO, 110)):
        ux, uy = Q[0] - P[0], Q[1] - P[1]
        n = math.hypot(ux, uy)
        E._cola(c, txt, (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2, uy / n * lado, -ux / n * lado, 22, size, "g", cor)
    E.escreve(c, "sem régua:", 1060, 400, 120, "i", BR)
    E.escreve(c, "? = 6", 1060, 660, 230, "g", AMARELO)
    E.escreve(c, "3 · 8 = 4 · 6", 1060, 860, 100, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Cordas", "e secantes", "pedaço × pedaço")


def d(c):  # o atalho: a tangente ao quadrado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    k = 34
    O, P = (1420, 600), (1420 - 10 * k, 600)
    c.drawCircle(*O, 8 * k, M.paint(BR, 1, stroke=10))
    M.line(c, *P, O[0] + 8 * k + 60, O[1], BR, 1, 8)
    M.line(c, *P, P[0] + 2 * k, P[1], AMARELO, 1, 16)
    T = em(P, dirg(-math.degrees(math.asin(0.8))), 6 * k)
    M.line(c, *P, *em(P, dirg(-math.degrees(math.asin(0.8))), 6 * k + 90), claro, 1, 12)
    c.drawCircle(*T, 16, M.paint(claro)); c.drawCircle(*P, 16, M.paint(BR))
    E.escreve(c, "o atalho", 90, 360, 130, "i", BR)
    E.formula(c, "tangente^2", 90, 560, 150, "g", claro)
    E.formula(c, "= fora · inteira", 90, 740, 120, "g", BR)
    E.formula(c, "2 · 18 = 36 → 6", 90, 940, 100, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sem_regua", a), ("capa_B_cordas_e_secantes", b), ("capa_C_tangente_ao_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
