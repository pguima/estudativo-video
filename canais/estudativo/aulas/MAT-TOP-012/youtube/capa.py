"""Capas do MAT-TOP-012 (1280x720). Uso: python capa.py"""
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


def hip(c, cx, cy, ka, kb, umax, cor, lw):
    for ramo in (1, -1):
        path = skia.Path()
        for i in range(81):
            u = -umax + 2 * umax * i / 80
            x, y = cx + ramo * ka * math.cosh(u), cy - kb * math.sinh(u)
            path.moveTo(x, y) if i == 0 else path.lineTo(x, y)
        c.drawPath(path, M.paint(cor, 1, stroke=lw, cap_round=True))


def a(c):  # o gancho: troque um sinal
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "troque um sinal:", 84, 330, 120, "i", BR)
    x = 84
    w1 = E.formula(None, "f{x^2}{9} ", 0, 0, 170, "g", a=0)
    E.formula(c, "f{x^2}{9}", x, 620, 170, "g", BR)
    M.rrect(c, x + w1 - 6, 500, 150, 150, 26, AMARELO)
    M.rrect(c, x + w1 + 24, 563, 90, 24, 8, COR)
    E.formula(c, "f{y^2}{16} = 1", x + w1 + 170, 620, 170, "g", BR)
    hip(c, 1500, 760, 120, 160, 1.25, BR, 14)
    for s in (1, -1):
        M.line(c, 1500 - 330, 760 + s * 440, 1500 + 330, 760 - s * 440, BR, 0.5, 5, dash=[16, 12])
    E.escreve(c, "dois pedaços", 84, 900, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Hipérbole", "e cônicas", "pela equação")


def d(c):  # o macete: a caixa
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a caixa", 84, 400, 200, "g", BR)
    E.escreve(c, "resolve tudo", 84, 600, 150, "i", BR)
    E.formula(c, "c^2 = a^2 + b^2", 84, 880, 130, "g", "#3CC7D3")
    cx, cy, k = 1480, 620, 62
    pt = M.paint(BR, 0.8, stroke=5); pt.setPathEffect(skia.DashPathEffect.Make([16, 12], 0))
    c.drawRect(skia.Rect.MakeLTRB(cx - 3 * k, cy - 4 * k, cx + 3 * k, cy + 4 * k), pt)
    for s in (1, -1):
        M.line(c, cx - 4.5 * k, cy + s * 6 * k, cx + 4.5 * k, cy - s * 6 * k, BR, 0.5, 5, dash=[16, 12])
    M.line(c, cx, cy, cx + 3 * k, cy - 4 * k, "#3CC7D3", 1, 12)
    hip(c, cx, cy, 3 * k, 4 * k, 1.1, BR, 10)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_troque_um_sinal", a), ("capa_B_hiperbole_e_conicas", b), ("capa_C_a_caixa", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
