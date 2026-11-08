"""Capas do MAT-ANG-014 (1280x720). Uso: python capa.py"""
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


def gravata(c, k=1.0, ox=0, oy=0, cor_a=LILAS, cor_b=AMARELO):
    """a figura da questão 4: AB em cima, CD embaixo, AC e BD se cruzando em M"""
    U = 62 * k
    A = (ox + 0, oy + 0); B = (ox + 6 * U, oy)
    g = math.radians(62)
    Mm = (A[0] + 4 * U * math.cos(g), A[1] + 4 * U * math.sin(g))
    C = (Mm[0] + 1.5 * (Mm[0] - A[0]), Mm[1] + 1.5 * (Mm[1] - A[1]))
    D = (Mm[0] + 1.5 * (Mm[0] - B[0]), Mm[1] + 1.5 * (Mm[1] - B[1]))
    for T, cor in (((A, Mm, B), cor_a), ((C, Mm, D), cor_b)):
        p = skia.Path(); p.addPoly(list(T), True)
        c.drawPath(p, M.paint(cor, 0.35))
    for P, Q in ((A, C), (B, D), (A, B), (D, C)):
        M.line(c, *P, *Q, BR, 1, 10)
    return A, B, C, D, Mm


def a(c):  # o gancho: 5 questões, você resolve?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    A, B, C, D, Mm = gravata(c, 1.0, 360, 290)
    E.escreve(c, "6", (A[0] + B[0]) / 2 - 25, A[1] - 30, 90, "g", LILAS)
    E.escreve(c, "9", (C[0] + D[0]) / 2 - 25, C[1] + 100, 90, "g", AMARELO)
    E.escreve(c, "x?", C[0] - 20, (Mm[1] + C[1]) / 2, 100, "g", BR)
    E.escreve(c, "5", 1120, 560, 330, "g", AMARELO)
    E.escreve(c, "questões", 1120, 740, 150, "g", BR)
    E.escreve(c, "você resolve?", 1130, 900, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Tales e", "semelhança", "5 questões")


def d(c):  # o atalho: siga os ângulos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    gravata(c, 0.95, 1180, 230, claro, AMARELO)
    E.escreve(c, "siga os", 110, 420, 150, "i", BR)
    E.escreve(c, "ângulos", 110, 610, 200, "g", BR)
    E.escreve(c, "4 : x = 6 : 9", 110, 830, 110, "g", AMARELO)
    E.escreve(c, "x = 6", 110, 990, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_questoes", a), ("capa_B_tales_e_semelhanca", b), ("capa_C_siga_os_angulos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
