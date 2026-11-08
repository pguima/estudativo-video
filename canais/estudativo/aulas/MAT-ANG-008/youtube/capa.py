"""Capas do MAT-ANG-008 (1280x720). Uso: python capa.py"""
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


def icone(c, tipo, cx, cy, k, linha=AMARELO, tinta=BR):
    """triângulo com uma das quatro linhas"""
    B, Cc, A = (cx - 150 * k, cy + 90 * k), (cx + 150 * k, cy + 90 * k), (cx - 40 * k, cy - 130 * k)
    p = skia.Path(); p.addPoly([A, B, Cc], True)
    pt = M.paint(tinta, 1, stroke=9 * k)
    pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    Mm = ((B[0] + Cc[0]) / 2, B[1])
    s = 26 * k
    if tipo == "altura":
        M.line(c, *A, A[0], B[1], linha, 1, 12 * k)
        M.line(c, A[0] + s, B[1], A[0] + s, B[1] - s, linha, 1, 6 * k)
        M.line(c, A[0], B[1] - s, A[0] + s, B[1] - s, linha, 1, 6 * k)
    elif tipo == "mediana":
        M.line(c, *A, *Mm, linha, 1, 12 * k)
        for x in ((B[0] + Mm[0]) / 2, (Mm[0] + Cc[0]) / 2):
            M.line(c, x, B[1] - 20 * k, x, B[1] + 20 * k, linha, 1, 7 * k)
    elif tipo == "bissetriz":
        ab, ac = math.dist(A, B), math.dist(A, Cc)
        f = ab / (ab + ac)
        D = (B[0] + (Cc[0] - B[0]) * f, B[1])
        M.line(c, *A, *D, linha, 1, 12 * k)
    else:
        M.line(c, Mm[0], cy - 160 * k, Mm[0], cy + 160 * k, linha, 1, 12 * k)
        M.line(c, Mm[0] + s, Mm[1], Mm[0] + s, Mm[1] - s, linha, 1, 6 * k)
        M.line(c, Mm[0], Mm[1] - s, Mm[0] + s, Mm[1] - s, linha, 1, 6 * k)


def a(c):  # o gancho: quatro nomes parecidos
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i, tipo in enumerate(("altura", "mediana", "bissetriz", "mediatriz")):
        icone(c, tipo, 250 + i * 470, 420, 1.05)
    E.escreve(c, "qual é qual?", 90, 900, 190, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Altura ou", "mediana?", "as 4 linhas")


def d(c):  # o atalho: no isósceles, uma linha faz tudo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    B, Cc = (1180, 960), (1720, 960)
    A = (1450, 960 - 270 * math.tan(math.radians(70)))
    p = skia.Path(); p.addPoly([A, B, Cc], True)
    pt = M.paint(BR, 1, stroke=12); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    M.line(c, *A, A[0], B[1], AMARELO, 1, 14)
    E.escreve(c, "no isósceles", 90, 400, 120, "i", BR)
    E.escreve(c, "1 linha", 90, 620, 200, "g", BR)
    E.escreve(c, "faz as 3", 90, 840, 170, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_e_qual", a), ("capa_B_altura_ou_mediana", b), ("capa_C_isosceles", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
