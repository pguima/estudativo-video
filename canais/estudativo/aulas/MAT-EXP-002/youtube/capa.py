"""Capas do MAT-EXP-002 (1280x720). Uso: python capa.py"""
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


def grafico(c, x, y, w, h, curvas, xr=(0, 50), yr=(0, 50), tinta=BR):
    """eixos simples na caixa (x, y, w, h); curvas = [(f, a, b, cor, tracejada)]"""
    X = lambda v: x + (v - xr[0]) / (xr[1] - xr[0]) * w
    Y = lambda v: y + h - (v - yr[0]) / (yr[1] - yr[0]) * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), tinta, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, tinta, 1, 6, 24)
    for fn, a, b, cor, tr in curvas:
        pa = skia.Path()
        for i in range(301):
            v = a + (b - a) * i / 300
            (pa.lineTo if i else pa.moveTo)(X(v), Y(fn(v)))
        p = M.paint(cor, 1, stroke=13, cap_round=True)
        if tr:
            p.setPathEffect(skia.DashPathEffect.Make([26, 18], 0))
        c.drawPath(pa, p)
    return X, Y


def a(c):  # o gancho: +300 ou +3%?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "+300", 84, 420, 170, "g", BR)
    E.escreve(c, "ou", 84 + E.larg("+300", "g", 170) + 40, 420, 120, "i", BR)
    E.escreve(c, "+3%?", 84, 640, 200, "g", AMARELO)
    E.escreve(c, "em 50 anos: 25 mil contra 43 mil", 84, 860, 66, "i", BR)
    X, Y = grafico(c, 1180, 220, 620, 620, [(lambda t: 10 + 0.3 * t, 0, 50, BR, True), (lambda t: 10 * 1.03 ** t, 0, 50, AMARELO, False)])


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Somar ou", "multiplicar?", "crescer e decair")


def d(c):  # o atalho: olhe os saltos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 380, 120, "i", claro)
    E.escreve(c, "olhe os saltos", 76, 590, 190, "g", BR)
    for i, (v, s) in enumerate((("100", "+30"), ("130", "+39"), ("169", "+50,7"), ("219,7", None))):
        x = 200 + i * 420
        E.centro(c, v, x, 900, 110, "g", BR)
        if s:
            M.arrow(c, x + 90, 760, x + 330, 760, AMARELO, 1, 8, 26)
            E.centro(c, s, x + 210, 730, 64, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_300_ou_3", a), ("capa_B_somar_ou_multiplicar", b), ("capa_C_olhe_os_saltos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
