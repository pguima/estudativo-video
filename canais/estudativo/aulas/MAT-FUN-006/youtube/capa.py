"""Capas do MAT-FUN-006 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF4D55"


def grafico(c, x, y, w, h, curvas, regua=None, toques=(), cor_toque=AMARELO, tinta=BR):
    """eixos simples na caixa (x, y, w, h) de −3 a 3, curvas [(f, a, b)], régua vertical tracejada em `regua`"""
    X = lambda v: x + (v + 3) / 6 * w
    Y = lambda v: y + h - (v + 3) / 6 * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), tinta, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, tinta, 1, 6, 24)
    for fn, a, b in curvas:
        pa = skia.Path()
        ok = False
        for i in range(301):
            v = a + (b - a) * i / 300
            yv = fn(v)
            if yv is None:
                continue
            (pa.lineTo if ok else pa.moveTo)(X(v), Y(yv))
            ok = True
        p = M.paint(tinta, 1, stroke=12, cap_round=True)
        c.drawPath(pa, p)
    if regua is not None:
        M.line(c, X(regua), y - 10, X(regua), y + h + 10, cor_toque, 1, 8, dash=[22, 14])
    for v, yv in toques:
        c.drawCircle(X(v), Y(yv), 26, M.paint(cor_toque, 1, stroke=8))


def a(c):  # o gancho: o círculo não é função
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "isso é", 84, 470, 150, "i", BR)
    E.escreve(c, "função?", 76, 680, 210, "g", BR)
    r = lambda s: (lambda v: s * math.sqrt(max(0, 4 - v * v)) if abs(v) <= 2 else None)
    grafico(c, 1100, 220, 660, 660, [(r(1), -2, 2), (r(-1), -2, 2)], 1.0, [(1.0, math.sqrt(3)), (1.0, -math.sqrt(3))], VERMELHO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Gráfico de", "função", "do zero")


def d(c):  # o atalho: a régua em pé
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o teste da", 84, 420, 130, "i", claro)
    E.escreve(c, "régua", 76, 640, 230, "g", BR)
    E.escreve(c, "em pé", 84, 840, 170, "i", BR)
    grafico(c, 1120, 220, 640, 640, [(lambda v: v * v / 1.5 - 1.8, -2.9, 2.9)], 1.4, [(1.4, 1.4 * 1.4 / 1.5 - 1.8)], AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_isso_e_funcao", a), ("capa_B_grafico_de_funcao", b), ("capa_C_regua_em_pe", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
