"""Capas do MAT-EXP-001 (1280x720). Uso: python capa.py"""
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


def grafico(c, x, y, w, h, curvas, xr=(-3, 3), yr=(-1, 9), tinta=BR, pontos=()):
    """eixos simples na caixa (x, y, w, h); curvas = [(f, a, b, cor)]"""
    X = lambda v: x + (v - xr[0]) / (xr[1] - xr[0]) * w
    Y = lambda v: y + h - (v - yr[0]) / (yr[1] - yr[0]) * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), tinta, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, tinta, 1, 6, 24)
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x - 10, y - 10, w + 20, h + 20))
    for fn, a, b, cor in curvas:
        pa = skia.Path()
        for i in range(301):
            v = a + (b - a) * i / 300
            (pa.lineTo if i else pa.moveTo)(X(v), Y(fn(v)))
        c.drawPath(pa, M.paint(cor, 1, stroke=13, cap_round=True))
    c.restore()
    for v, yv, cor in pontos:
        c.drawCircle(X(v), Y(yv), 20, M.paint(cor))
    return X, Y


def a(c):  # o gancho: dobrar a folha 10 vezes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "dobre 10 vezes", 84, 400, 120, "i", BR)
    E.escreve(c, "×1.024", 70, 680, 270, "g", AMARELO)
    E.formula(c, "2^{10}", 90, 900, 150, "g", BR)
    grafico(c, 1230, 230, 560, 640, [(lambda v: 2 ** v, -3, 3.17, BR)], pontos=[(0, 1, AMARELO), (3, 8, AMARELO)])


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função", "exponencial", "lei e gráfico")


def d(c):  # o atalho: o espelho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho do", 84, 400, 130, "i", claro)
    E.escreve(c, "espelho", 76, 640, 230, "g", BR)
    E.formula(c, "(f{1}{2})^x = 2^{−x}", 90, 900, 120, "g", BR)
    X, Y = grafico(c, 1150, 230, 660, 640, [(lambda v: 2 ** v, -3, 3.17, claro), (lambda v: 0.5 ** v, -3.17, 3, BR)])
    M.line(c, X(0), 200, X(0), 900, AMARELO, 1, 8, dash=[22, 14])


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobre_10_vezes", a), ("capa_B_funcao_exponencial", b), ("capa_C_espelho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
