"""Capas do MAT-FUN-007 (1280x720). Uso: python capa.py"""
import bisect, subprocess, sys
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
PTS = [(0, -2), (6, -4), (9, 0), (15, 8), (21, 0), (24, -3)]


def suave(pts):
    """a mesma curva da aula (interpolação monótona pelos pontos)"""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    n = len(pts)
    h = [xs[i + 1] - xs[i] for i in range(n - 1)]
    d = [(ys[i + 1] - ys[i]) / h[i] for i in range(n - 1)]
    m = [d[0]] + [0.0] * (n - 2) + [d[-1]]
    for i in range(1, n - 1):
        if d[i - 1] * d[i] > 0:
            w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])

    def f(x):
        i = min(max(bisect.bisect_right(xs, x) - 1, 0), n - 2)
        u = (x - xs[i]) / h[i]
        return ((2 * u ** 3 - 3 * u ** 2 + 1) * ys[i] + (u ** 3 - 2 * u ** 2 + u) * h[i] * m[i] + (-2 * u ** 3 + 3 * u ** 2) * ys[i + 1]
                + (u ** 3 - u ** 2) * h[i] * m[i + 1])
    return f


f = suave(PTS)


def grafico(c, x, y, w, h, tinta=BR):
    """eixos simples na caixa (x, y, w, h): x de −1 a 25, y de −5 a 9; devolve as funções valor → pixel"""
    X = lambda v: x + (v + 1) / 26 * w
    Y = lambda v: y + h - (v + 5) / 14 * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), tinta, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, tinta, 1, 6, 24)
    pa = skia.Path()
    for i in range(241):
        v = i / 10
        (pa.lineTo if i else pa.moveTo)(X(v), Y(f(v)))
    c.drawPath(pa, M.paint(tinta, 1, stroke=12, cap_round=True))
    return X, Y


def a(c):  # o gancho: a máxima não é 15
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a máxima", 84, 430, 130, "i", BR)
    E.escreve(c, "foi 15?", 76, 640, 210, "g", BR)
    X, Y = grafico(c, 1060, 200, 740, 680)
    M.line(c, X(15), Y(8), X(15), Y(0), VERMELHO, 1, 8, dash=[22, 14])
    M.line(c, X(15), Y(8), X(0), Y(8), AMARELO, 1, 8, dash=[22, 14])
    c.drawCircle(X(15), Y(8), 28, M.paint(AMARELO, 1, stroke=8))
    E.pilula(c, "15", X(15), Y(0) + 56, 54, "g", fundo=VERMELHO)
    E.pilula(c, "8", X(0) - 56, Y(8), 54, "g", fundo=AMARELO, cor="#121214")
    E.escreve(c, "15 é a hora!", 84, 850, 100, "i", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Ler um", "gráfico", "máxima e zeros")


def d(c):  # o atalho: a sombra do gráfico
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a", 84, 420, 130, "i", claro)
    E.escreve(c, "sombra", 76, 640, 230, "g", BR)
    E.escreve(c, "do gráfico", 84, 840, 150, "i", BR)
    X, Y = grafico(c, 1100, 220, 700, 640, claro)
    for i in range(0, 25):
        M.line(c, X(i), Y(f(i)), X(i), Y(0), AMARELO, 0.55, 4)
    M.line(c, X(0), Y(0), X(24), Y(0), AMARELO, 1, 18)
    M.line(c, X(0), Y(-4), X(0), Y(8), AMARELO, 1, 18)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_maxima_foi_15", a), ("capa_B_ler_um_grafico", b), ("capa_C_a_sombra_do_grafico", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
