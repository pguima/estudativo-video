"""Capas do MAT-FUN-020 (1280x720). Uso: python capa.py"""
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
VERDE = "#2BD487"


def ingresso(c, cx, cy, preco, cor, w=560, h=210, ang=0):
    c.save(); c.translate(cx, cy); c.rotate(ang)
    p = skia.Path()
    p.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), 26, 26))
    for sx in (-1, 1):
        f = skia.Path(); f.addCircle(sx * w / 2, 0, 32)
        p = skia.Op(p, f, skia.PathOp.kDifference_PathOp)
    c.drawPath(p, M.paint(cor))
    M.line(c, -w / 2 + 120, -h / 2 + 24, -w / 2 + 120, h / 2 - 24, COR, 0.5, 5, dash=[12, 10])
    E.centro(c, preco, 50, 34, 100, "g", COR)
    c.restore()


def mini(c, x, y, w, h, fn, cor, x0, x1, ymin, ymax, ate, largura=11):
    X = lambda v: x + (v - x0) / (x1 - x0) * w
    Y = lambda v: y + h - (v - ymin) / (ymax - ymin) * h
    M.arrow(c, x, Y(0), x + w + 26, Y(0), BR, 1, 6, 22)
    M.arrow(c, X(0), y + h, X(0), y - 26, BR, 1, 6, 22)
    pa = skia.Path()
    for i in range(201):
        v = ate[0] + (ate[1] - ate[0]) * i / 200
        (pa.lineTo if i else pa.moveTo)(X(v), Y(fn(v)))
    c.drawPath(pa, M.paint(cor, 1, stroke=largura, cap_round=True))
    return X, Y


R = lambda x: (40 - x) * (300 + 10 * x) / 1000


def a(c):  # o gancho: baixar o preço enche o caixa?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "baixar o preço", 84, 390, 120, "g", BR)
    E.escreve(c, "enche o caixa?", 84, 540, 120, "g", AMARELO)
    E.escreve(c, "qual preço dá mais dinheiro", 84, 700, 64, "i", BR)
    ingresso(c, 1440, 330, "R$ 40", BR, ang=-6)
    ingresso(c, 1440, 640, "R$ 35", AMARELO, ang=4)
    E.pilula(c, "?", 1740, 520, 70, "g", fundo=VERMELHO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Montar a", "função", "para otimizar")


def d(c):  # o atalho: não abra os parênteses
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "não abra os", 84, 400, 110, "i", claro)
    E.escreve(c, "parênteses", 76, 590, 170, "g", BR)
    E.formula(c, "(40 − x)(300 + 10x)", 84, 780, 80, "g", AMARELO)
    E.escreve(c, "o vértice fica no meio das raízes", 84, 900, 56, "i", BR)
    X, Y = mini(c, 1300, 300, 520, 520, R, claro, -36, 46, -1.5, 14, (-30, 40))
    for r in (-30, 40):
        c.drawCircle(X(r), Y(0), 22, M.paint(AMARELO, 1, stroke=8))
    M.line(c, X(5), Y(0), X(5), Y(12.25), BR, 0.8, 6, dash=[18, 12])
    c.drawCircle(X(5), Y(12.25), 22, M.paint(AMARELO))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_baixar_o_preco_enche_o_caixa", a), ("capa_B_montar_a_funcao", b), ("capa_C_nao_abra_os_parenteses", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
