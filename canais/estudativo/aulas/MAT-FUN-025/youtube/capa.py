"""Capas do MAT-FUN-025 (1280x720). Uso: python capa.py"""
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


def hiperbole(c, x, y, w, h, k, vmax, cor, larg=12, eixos=BR):
    """eixos e a curva y = k/x na caixa (x, y, w, h), de 0 a vmax nos dois eixos"""
    X = lambda v: x + v * w / vmax
    Y = lambda v: y + h - v * h / vmax
    M.arrow(c, x, y + h, x + w + 30, y + h, eixos, 1, 7, 26)
    M.arrow(c, x, y + h, x, y - 30, eixos, 1, 7, 26)
    p = skia.Path()
    v0 = k / vmax
    for i in range(201):
        v = v0 + (vmax - v0) * i / 200
        p.lineTo(X(v), Y(k / v)) if i else p.moveTo(X(v), Y(k / v))
    c.drawPath(p, M.paint(cor, 1.0, stroke=larg, cap_round=True))
    return X, Y


def a(c):  # o gancho: o número que nunca muda
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o número que", 84, 360, 120, "i", BR)
    E.escreve(c, "nunca muda", 76, 560, 190, "g", BR)
    E.formula(c, "x · y = 12", 84, 820, 150, "g", AMARELO)
    X, Y = hiperbole(c, 1300, 300, 500, 560, 12, 13, BR)
    for xv, yv in ((2, 6), (4, 3)):
        r = skia.Rect.MakeLTRB(X(0), Y(yv), X(xv), Y(0))
        c.drawRect(r, M.paint(AMARELO, 0.22))
        c.drawRect(r, M.paint(AMARELO, 1, stroke=6))
        c.drawCircle(X(xv), Y(yv), 20, M.paint(AMARELO))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Hipérbole", "y = k/x", "do zero")


def d(c):  # o atalho: um ponto basta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "um ponto", 76, 420, 200, "g", BR)
    E.escreve(c, "dá a lei", 84, 600, 150, "i", claro)
    E.formula(c, "k = x · y", 84, 850, 150, "g", AMARELO)
    X, Y = hiperbole(c, 1300, 300, 500, 560, 12, 13, claro)
    c.drawCircle(X(3), Y(4), 26, M.paint(AMARELO))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_numero_que_nunca_muda", a), ("capa_B_hiperbole", b), ("capa_C_um_ponto_da_a_lei", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
