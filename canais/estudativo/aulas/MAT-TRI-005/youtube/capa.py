"""Capas do MAT-TRI-005 (1280x720). Uso: python capa.py"""
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
R3 = math.sqrt(3)


def figura(c, x0, gy, u, cor_linha=BR):
    """morro visto de A (30°) e de B (60°); u = px por metro, A–B = 100 m"""
    A, B, F = (x0, gy), (x0 + 100 * u, gy), (x0 + 150 * u, gy)
    T = (F[0], gy - 50 * R3 * u)
    p = skia.Path()
    p.moveTo(F[0] - 40 * u, gy); p.lineTo(*T); p.quadTo(F[0] + 15 * u, T[1] + 15 * u, F[0] + 45 * u, gy); p.close()
    c.drawPath(p, M.paint(BR, 0.18))
    M.line(c, x0 - 40, gy, F[0] + 60 * u, gy, cor_linha, 0.8, 6)
    for P in (A, B):
        M.line(c, *P, *T, cor_linha, 0.9, 5, dash=[16, 12])
        c.drawCircle(*P, 12, M.paint(cor_linha))
    M.line(c, *T, *F, AMARELO, 1.0, 12)
    for P, r, s, dx in ((A, 120, "30°", 135), (B, 80, "60°", 95)):
        ang = 30 if s == "30°" else 60
        c.drawArc(skia.Rect.MakeXYWH(P[0] - r, P[1] - r, 2 * r, 2 * r), -ang, ang, False, M.paint(BR, 1.0, stroke=6))
        E.escreve(c, s, P[0] + dx, P[1] - 18, 52, "g", BR)
    E.escreve(c, "100 m", (A[0] + B[0]) / 2 - 75, gy + 70, 56, "g", BR)
    E.escreve(c, "?", F[0] + 30, (gy + T[1]) / 2 + 30, 120, "g", AMARELO)


def a(c):  # o gancho: dois ângulos e a altura
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2 ângulos", 84, 400, 170, "g", BR)
    E.escreve(c, "= a altura", 84, 580, 150, "i", BR)
    figura(c, 860, 980, 5.4)
    E.formula(c, "h = 50r{3} ≈ 85 m", 84, 820, 96, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Dois", "ângulos", "de visão")


def d(c):  # o atalho: o triângulo isósceles
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sem sistema", 84, 380, 170, "g", BR)
    E.escreve(c, "o atalho do isósceles", 84, 540, 100, "i", BR)
    u = 5.0
    A, B = (900, 960), (900 + 100 * u, 960)
    T = (900 + 150 * u, 960 - 50 * R3 * u)
    path = skia.Path(); path.addPoly([A, B, T], True)
    c.drawPath(path, M.paint(COR, 0.4))
    M.line(c, *A, *B, BR, 1.0, 8); M.line(c, *B, *T, BR, 1.0, 8); M.line(c, *A, *T, BR, 0.7, 6)
    M.line(c, *T, T[0], 960, AMARELO, 1.0, 10)
    E.escreve(c, "100", (A[0] + B[0]) / 2 - 50, 1040, 60, "g", BR)
    E.escreve(c, "100", B[0] - 10, 790, 60, "g", BR)
    E.formula(c, "h = 100 · sen 60°", 84, 840, 90, "g", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dois_angulos_altura", a), ("capa_B_dois_angulos_de_visao", b), ("capa_C_atalho_isosceles", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
