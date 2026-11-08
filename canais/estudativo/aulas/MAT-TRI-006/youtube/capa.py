"""Capas do MAT-TRI-006 (1280x720). Uso: python capa.py"""
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


def antena(c, u=22):
    """antena de 15 m com o cabo a 30°"""
    B = (1660, 960)
    T = (B[0], B[1] - 15 * u)
    A = (B[0] - 15 * R3 * u, B[1])
    M.line(c, A[0] - 60, 960, B[0] + 80, 960, BR, 0.8, 6)
    M.line(c, *B, *T, BR, 1.0, 10)
    for k in range(1, 6):
        y = B[1] - k * 15 * u / 6
        M.line(c, B[0] - 20, y, B[0] + 20, y, BR, 1.0, 4)
    M.line(c, *A, *T, AMARELO, 1.0, 10)
    c.drawArc(skia.Rect.MakeXYWH(A[0] - 120, A[1] - 120, 240, 240), -30, 30, False, M.paint(BR, 1.0, stroke=6))
    E.escreve(c, "30°", A[0] + 135, A[1] - 16, 52, "g", BR)
    E.escreve(c, "15 m", B[0] + 34, B[1] - 150, 56, "g", BR)
    E.escreve(c, "cabo?", (A[0] + T[0]) / 2 - 170, (A[1] + T[1]) / 2 - 30, 64, "g", AMARELO)


def a(c):  # o gancho: a armadilha do cabo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "4 problemas", 84, 400, 150, "g", BR)
    E.escreve(c, "pause e resolva", 84, 560, 110, "i", BR)
    E.formula(c, "cabo = 7,5 m?", 84, 820, 110, "g", BR)
    E.risco(c, 80, 790, 780, 784, 9, 0, AMARELO, 12)
    antena(c)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "sen, cos, tg", "4 problemas")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho do 30°", 84, 360, 120, "i", BR)
    E.escreve(c, "hipotenusa", 84, 560, 170, "g", BR)
    E.escreve(c, "= 2 × oposto", 84, 760, 150, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "2 × 15 = 30 m", 84, 940, 90, "g", AMARELO)
    u = 22
    B = (1720, 960); T = (B[0], B[1] - 15 * u); A = (B[0] - 15 * R3 * u, B[1])
    path = skia.Path(); path.addPoly([A, B, T], True)
    c.drawPath(path, M.paint(COR, 0.45))
    M.line(c, *A, *B, BR, 0.7, 6); M.line(c, *B, *T, "#D98A00", 1.0, 12); M.line(c, *A, *T, E.mix(COR, BR, 0.55), 1.0, 12)
    c.drawArc(skia.Rect.MakeXYWH(A[0] - 110, A[1] - 110, 220, 220), -30, 30, False, M.paint(BR, 1.0, stroke=6))
    E.escreve(c, "30°", A[0] + 125, A[1] - 14, 50, "g", BR)
    E.escreve(c, "15", B[0] + 26, B[1] - 150, 60, "g", "#FFB84D")
    E.escreve(c, "30", (A[0] + T[0]) / 2 - 90, (A[1] + T[1]) / 2 - 30, 60, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_pause_e_resolva", a), ("capa_B_praticando", b), ("capa_C_atalho_30", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
