"""Capas do MAT-FUN-016 (1280x720). Uso: python capa.py"""
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


def parabola(c, x, y, w, h, fn, cor, largura=12, a=-3, b=3, ymin=-3, ymax=3):
    """eixos simples na caixa e a curva fn de a até b"""
    X = lambda v: x + (v + 3) / 6 * w
    Y = lambda v: y + h - (v - ymin) / (ymax - ymin) * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), BR, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, BR, 1, 6, 24)
    pa = skia.Path()
    for i in range(201):
        v = a + (b - a) * i / 200
        (pa.lineTo if i else pa.moveTo)(X(v), Y(fn(v)))
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x - 10, y - 10, w + 20, h + 20))
    c.drawPath(pa, M.paint(cor, 1, stroke=largura, cap_round=True))
    c.restore()
    return X, Y


def a(c):  # o gancho: sorriso ou cara triste?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sorriso ou", 84, 420, 130, "i", BR)
    E.escreve(c, "cara triste?", 76, 620, 170, "g", BR)
    E.formula(c, "x^2 − 4x + 3", 84, 860, 120, "g", AMARELO)
    parabola(c, 1180, 240, 300, 300, lambda v: 0.6 * v * v - 1.8, BR)
    parabola(c, 1500, 560, 300, 300, lambda v: -0.6 * v * v + 1.8, E.mix(COR, BR, 0.55))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função", "quadrática", "a parábola")


def d(c):  # o atalho: a parábola em 2 segundos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a parábola em", 84, 400, 130, "i", claro)
    E.escreve(c, "2 segundos", 76, 620, 200, "g", BR)
    E.escreve(c, "sinal do a + o c", 84, 840, 110, "i", AMARELO)
    X, Y = parabola(c, 1260, 260, 540, 600, lambda v: 0.5 * v * v - 0.5 * v - 1.2 + 0.0, claro, a=-2.9, b=3.0, ymin=-3, ymax=4)
    c.drawCircle(X(0), Y(-1.2), 28, M.paint(AMARELO, 1, stroke=9))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sorriso_ou_cara_triste", a), ("capa_B_funcao_quadratica", b), ("capa_C_parabola_em_2_segundos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
