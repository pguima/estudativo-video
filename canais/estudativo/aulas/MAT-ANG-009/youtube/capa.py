"""Capas do MAT-ANG-009 (1280x720). Uso: python capa.py"""
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


def cunha(c, V, g1, g2, r, cor, alfa=0.55):
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    p = skia.Path(); p.moveTo(*V); p.arcTo(ret, -g1, -(g2 - g1), False); p.close()
    c.drawPath(p, M.paint(cor, alfa))
    c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor, 1, stroke=7, cap_round=True))


def figura(c, tinta=BR):
    """as paralelas da questão 1: A em cima, B e C embaixo"""
    A = (520, 330)
    B = (A[0] - 480 / math.tan(math.radians(55)), 810)
    Cc = (A[0] + 480 / math.tan(math.radians(65)), 810)
    for y in (A[1], B[1]):
        M.line(c, 60, y, 1000, y, tinta, 1, 10)
    cunha(c, A, 180, 235, 130, LILAS)
    cunha(c, A, 295, 360, 130, AMARELO)
    cunha(c, B, 0, 55, 110, LILAS)
    for P, Q in ((A, B), (B, Cc), (Cc, A)):
        M.line(c, *P, *Q, tinta, 1, 12)
    return A, B, Cc


def a(c):  # o gancho: cinco questões
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    A, B, Cc = figura(c)
    E.escreve(c, "2x + 15", 130, 470, 80, "g", LILAS)
    E.escreve(c, "65°", 690, 470, 80, "g", AMARELO)
    E.escreve(c, "x = ?", 330, 990, 130, "g", BR)
    E.escreve(c, "5", 1120, 560, 330, "g", AMARELO)
    E.escreve(c, "questões", 1120, 740, 150, "g", BR)
    E.escreve(c, "você resolve?", 1130, 900, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Ângulos e", "triângulos", "5 questões")


def d(c):  # o atalho: olhe só para o ponto A
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    A, B, Cc = figura(c)
    cunha(c, A, 235, 295, 90, BR, 0.4)
    E.escreve(c, "olhe só", 1080, 400, 130, "i", BR)
    E.escreve(c, "para o A", 1070, 580, 160, "g", BR)
    E.escreve(c, "180 − 55 − 65", 1080, 760, 100, "g", claro)
    E.escreve(c, "= 60°", 1080, 900, 120, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_questoes", a), ("capa_B_angulos_e_triangulos", b), ("capa_C_olhe_o_ponto_A", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
