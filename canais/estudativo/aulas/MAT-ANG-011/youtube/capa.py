"""Capas do MAT-ANG-011 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF6B6B"


def tri(B, u):
    """triângulo 6, 9, 10 com BC deitado, u pixels por unidade; D a 4 de B"""
    x = (36 - 81 + 100) / 20
    h = math.sqrt(36 - x * x)
    A = (B[0] + x * u, B[1] - h * u)
    C = (B[0] + 10 * u, B[1])
    D = (B[0] + 4 * u, B[1])
    return A, B, C, D


def figura(c, cor_ab=LILAS, cor_ac=AMARELO):
    A, B, C, D = tri((80, 900), 95)
    M.line(c, *A, *B, cor_ab, 1, 14)
    M.line(c, *A, *C, cor_ac, 1, 14)
    M.line(c, *B, *D, cor_ab, 1, 14)
    M.line(c, *D, *C, cor_ac, 1, 14)
    M.line(c, *A, *D, BR, 1, 10)
    c.drawCircle(*D, 16, M.paint(BR))
    return A, B, C, D


def a(c):  # o gancho: o chute 5 e 5 está errado
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    A, B, C, D = figura(c)
    E.escreve(c, "6", 80, 620, 110, "g", LILAS)
    E.escreve(c, "9", 700, 600, 110, "g", AMARELO)
    E.escreve(c, "4", 230, 1030, 120, "g", LILAS)
    E.escreve(c, "6", 720, 1030, 120, "g", AMARELO)
    E.escreve(c, "5 e 5?", 1150, 430, 160, "g", BR)
    M.line(c, 1140, 380, 1640, 380, VERMELHO, 1, 18)
    E.escreve(c, "4 e 6", 1150, 680, 210, "g", AMARELO)
    E.escreve(c, "sem medir", 1160, 860, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Tales no", "triângulo", "e a bissetriz")


def d(c):  # o atalho: divida em partes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "divida em", 120, 400, 130, "i", BR)
    E.escreve(c, "partes", 120, 590, 210, "g", BR)
    x0, x1, y = 120, 1800, 780
    w = (x1 - x0) / 5
    for i in range(5):
        M.rrect(c, x0 + i * w + 8, y - 45, w - 16, 90, 45, claro if i < 2 else AMARELO, 1)
        E.centro(c, "2", x0 + (i + 0.5) * w, y + 30, 80, "g", "#07070F")
    E.escreve(c, "4", x0 + w - 30, 960, 130, "g", claro)
    E.escreve(c, "6", x0 + 3.5 * w - 30, 960, 130, "g", AMARELO)
    E.escreve(c, "6 : 9 = 2 : 3", 1080, 560, 110, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_e_cinco", a), ("capa_B_tales_no_triangulo", b), ("capa_C_divida_em_partes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
