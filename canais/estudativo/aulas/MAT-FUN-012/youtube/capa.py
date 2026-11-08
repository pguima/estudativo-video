"""Capas do MAT-FUN-012 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
VERMELHO = "#FF4D55"


def eixos(c, x, y, w, h, x0, x1, y0, y1, tinta=BR):
    X = lambda v: x + (v - x0) / (x1 - x0) * w
    Y = lambda v: y + h - (v - y0) / (y1 - y0) * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), tinta, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, tinta, 1, 6, 24)
    return X, Y


def a(c):  # o gancho: dois pontos e a fórmula
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2 pontos", 76, 430, 170, "g", BR)
    E.escreve(c, "e a fórmula", 84, 600, 130, "i", BR)
    E.escreve(c, "sai inteira", 84, 780, 130, "g", AMARELO)
    X, Y = eixos(c, 1180, 220, 600, 620, -0.6, 5, -0.6, 12.5)
    f = lambda v: 2 * v + 3
    M.line(c, X(-0.4), Y(f(-0.4)), X(4.6), Y(f(4.6)), BR, 1, 12)
    for u in (1, 3):
        c.drawCircle(X(u), Y(f(u)), 24, M.paint(AMARELO))
    E.formula(c, "f(x) = ?", X(0.4), Y(11.4), 70, "g", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "A lei por", "2 pontos", "função afim")


def d(c):  # o atalho: ande para trás até o x = 0
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o b sai", 84, 420, 130, "i", claro)
    E.escreve(c, "andando", 76, 620, 190, "g", BR)
    E.escreve(c, "para trás", 84, 820, 160, "g", AMARELO)
    X, Y = eixos(c, 1180, 220, 600, 620, -0.6, 3.6, -0.6, 10.6, claro)
    f = lambda v: 2 * v + 3
    M.line(c, X(-0.3), Y(f(-0.3)), X(3.4), Y(f(3.4)), BR, 1, 12)
    M.arrow(c, X(1), Y(5), X(0.04), Y(5), claro, 1, 9, 30)
    M.arrow(c, X(0), Y(5), X(0), Y(3.15), VERMELHO, 1, 9, 30)
    c.drawCircle(X(1), Y(5), 20, M.paint(BR))
    c.drawCircle(X(0), Y(3), 26, M.paint(AMARELO))
    E.escreve(c, "b", X(0) - 90, Y(3) + 30, 90, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dois_pontos_e_a_formula", a), ("capa_B_lei_por_dois_pontos", b), ("capa_C_ande_para_tras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
