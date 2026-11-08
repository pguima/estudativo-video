"""Capas do MAT-FUN-010 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o a não é o 40
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o a é", 84, 430, 130, "i", BR)
    E.escreve(c, "40?", 76, 660, 230, "g", BR)
    E.formula(c, "40 + 0,5x", 1000, 430, 150, "g", BR)
    w40 = E.larg("40", "g", 150)
    M.line(c, 990, 450, 1000 + w40 + 10, 320, VERMELHO, 1, 14)
    x05 = 1000 + E.larg("40 + ", "g", 150)
    w05 = E.larg("0,5x", "g", 150)
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x05 - 20, 290, w05 + 40, 190), 24, 24)
    c.drawRRect(r, M.paint(AMARELO, 1, stroke=10))
    E.escreve(c, "a = 0,5", x05, 620, 110, "g", AMARELO)
    E.escreve(c, "colado no x", x05, 740, 70, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Taxa de", "variação", "o a e o b da reta")


def d(c):  # o atalho: sobe ÷ anda
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "quanto", 84, 420, 120, "i", claro)
    E.escreve(c, "sobe ÷", 76, 620, 190, "g", BR)
    E.escreve(c, "quanto anda", 84, 820, 130, "i", AMARELO)
    X, Y = eixos(c, 1180, 220, 600, 620, -0.5, 5.5, -0.5, 6, claro)
    M.line(c, X(0), Y(0.5), X(5.2), Y(5.7), BR, 1, 12)
    M.arrow(c, X(1), Y(1.5), X(3.4), Y(1.5), AMARELO, 1, 9, 30)
    M.arrow(c, X(3.5), Y(1.5), X(3.5), Y(3.9), BR, 1, 9, 30)
    c.drawCircle(X(1), Y(1.5), 20, M.paint(BR))
    c.drawCircle(X(3.5), Y(4), 20, M.paint(BR))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_a_e_40", a), ("capa_B_taxa_de_variacao", b), ("capa_C_sobe_dividido_por_anda", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
