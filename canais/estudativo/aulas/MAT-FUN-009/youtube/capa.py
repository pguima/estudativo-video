"""Capas do MAT-FUN-009 (1280x720). Uso: python capa.py"""
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


def eixos(c, x, y, w, h, x0, x1, y0, y1, tinta=BR):
    X = lambda v: x + (v - x0) / (x1 - x0) * w
    Y = lambda v: y + h - (v - y0) / (y1 - y0) * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), tinta, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, tinta, 1, 6, 24)
    return X, Y


def reta(c, X, Y, f, a, b, cor=BR, larg=12):
    M.line(c, X(a), Y(f(a)), X(b), Y(f(b)), cor, 1, larg)


def a(c):  # o gancho: dois pontos bastam
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "só", 84, 430, 130, "i", BR)
    E.escreve(c, "2 pontos", 76, 640, 200, "g", BR)
    E.escreve(c, "e a reta sai", 84, 840, 130, "i", AMARELO)
    X, Y = eixos(c, 1160, 220, 620, 620, -2, 4, -3, 6)
    f = lambda v: 2 * v - 1
    reta(c, X, Y, f, -1, 3.4)
    for u in (0, 2):
        c.drawCircle(X(u), Y(f(u)), 26, M.paint(AMARELO))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função", "afim", "lei e gráfico")


def d(c):  # o atalho: o ponto do x = 0 sai de graça
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o ponto", 84, 420, 130, "i", claro)
    E.escreve(c, "de graça", 76, 640, 200, "g", BR)
    E.formula(c, "x = 0 → b", 84, 840, 140, "g", AMARELO)
    X, Y = eixos(c, 1180, 220, 600, 620, -2, 4, -3, 6, claro)
    f = lambda v: 2 * v + 1
    reta(c, X, Y, f, -1.6, 2.4)
    c.drawCircle(X(0), Y(1), 24, M.paint(AMARELO))
    c.drawCircle(X(0), Y(1), 44, M.paint(AMARELO, 1, stroke=8))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dois_pontos_bastam", a), ("capa_B_funcao_afim", b), ("capa_C_o_ponto_de_graca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
