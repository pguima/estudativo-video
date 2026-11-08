"""Capas do MAT-FUN-011 (1280x720). Uso: python capa.py"""
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
VERDE = "#3EE08F"
VERMELHO = "#FF4D55"


def eixos(c, x, y, w, h, x0, x1, y0, y1, tinta=BR):
    X = lambda v: x + (v - x0) / (x1 - x0) * w
    Y = lambda v: y + h - (v - y0) / (y1 - y0) * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), tinta, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, tinta, 1, 6, 24)
    return X, Y


def regiao(c, X, Y, fn, a, b, cor, alfa):
    pa = skia.Path()
    pa.moveTo(X(a), Y(0))
    for i in range(41):
        v = a + (b - a) * i / 40
        pa.lineTo(X(v), Y(fn(v)))
    pa.lineTo(X(b), Y(0))
    pa.close()
    c.drawPath(pa, M.paint(cor, alfa))


def sinal(c, cx, cy, s, cor):
    c.drawCircle(cx, cy, 46, M.paint(cor))
    E.centro(c, s, cx, cy + 26, 80, "g", BR)


def a(c):  # o gancho: positiva à direita? nem sempre
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "positiva", 76, 430, 160, "g", BR)
    E.escreve(c, "à direita?", 84, 610, 150, "i", BR)
    E.escreve(c, "nem sempre", 84, 800, 120, "g", AMARELO)
    g = lambda v: -3 * v + 12
    X, Y = eixos(c, 1140, 200, 640, 640, -1.5, 7.5, -10, 17)
    regiao(c, X, Y, g, -1.5, 4, VERDE, 0.6)
    regiao(c, X, Y, g, 4, 7.5, VERMELHO, 0.6)
    M.line(c, X(-1.2), Y(g(-1.2)), X(7.2), Y(g(7.2)), BR, 1, 12)
    c.drawCircle(X(4), Y(0), 22, M.paint(AMARELO))
    sinal(c, X(1.2), Y(3), "+", "#16A36A")
    sinal(c, X(6.2), Y(-3.4), "−", VERMELHO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Zero e", "sinal", "da função afim")


def d(c):  # o atalho: depois da raiz, o sinal do a
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "depois da raiz,", 84, 420, 110, "i", claro)
    E.escreve(c, "o sinal", 76, 620, 190, "g", BR)
    E.escreve(c, "do a", 84, 820, 170, "g", AMARELO)
    y = 600
    M.line(c, 1080, y, 1820, y, claro, 1, 8)
    M.line(c, 1080, y, 1450, y, VERMELHO, 1, 16)
    M.line(c, 1450, y, 1820, y, "#16A36A", 1, 16)
    c.drawCircle(1450, y, 22, M.paint(BR))
    sinal(c, 1265, y - 120, "−", VERMELHO)
    sinal(c, 1635, y - 120, "+", "#16A36A")
    E.centro(c, "raiz", 1450, y + 90, 60, "i", BR)
    E.centro(c, "a > 0", 1635, y + 200, 70, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_positiva_a_direita", a), ("capa_B_zero_e_sinal", b), ("capa_C_o_sinal_do_a", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
