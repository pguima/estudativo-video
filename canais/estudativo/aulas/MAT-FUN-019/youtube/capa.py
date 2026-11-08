"""Capas do MAT-FUN-019 (1280x720). Uso: python capa.py"""
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


def mini(c, x, y, w, h, fn, cor, x0=-0.4, x1=4.4, ymin=-3, ymax=24, largura=11, ate=(0, 4)):
    """eixos simples na caixa com a curva fn de ate[0] a ate[1]"""
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


h = lambda v: -5 * v * v + 20 * v


def a(c):  # o gancho: a altura máxima não é 2
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "altura", 84, 380, 150, "g", BR)
    E.escreve(c, "máxima?", 84, 540, 150, "g", BR)
    E.escreve(c, "2", 90, 860, 230, "g", VERMELHO)
    M.line(c, 70, 880, 250, 690, VERMELHO, 1, 16)
    E.escreve(c, "20", 330, 860, 230, "g", AMARELO)
    X, Y = mini(c, 1060, 260, 700, 640, h, BR)
    M.line(c, X(2), Y(20), X(2), Y(0), VERMELHO, 1, 7, dash=[18, 12])
    M.line(c, X(2), Y(20), X(0), Y(20), AMARELO, 1, 7, dash=[18, 12])
    c.drawCircle(X(2), Y(20), 26, M.paint(AMARELO))
    c.drawCircle(X(2), Y(20), 26, M.paint("#121214", 1, stroke=5))
    E.pilula(c, "quando", X(2), Y(0) + 60, 44, "g", fundo=VERMELHO)
    E.pilula(c, "quanto", X(0) + 30, Y(20) - 70, 44, "g", fundo=AMARELO, cor=COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Máximo e", "mínimo", "em problemas")


def d(c):  # o atalho: o topo fica no meio do voo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o topo fica no", 84, 400, 110, "i", claro)
    E.escreve(c, "meio do voo", 76, 600, 170, "g", BR)
    E.escreve(c, "sai no 0, volta no 4: topo em 2", 84, 800, 66, "i", AMARELO)
    X, Y = mini(c, 1240, 260, 560, 600, h, claro)
    for r in (0, 4):
        c.drawCircle(X(r), Y(0), 24, M.paint(AMARELO, 1, stroke=8))
    E.chave(c, X(0), X(4), Y(0) + 60, AMARELO, 1, 24, 6)
    M.line(c, X(2), Y(0), X(2), Y(20), BR, 0.8, 6, dash=[18, 12])
    c.drawCircle(X(2), Y(20), 24, M.paint(AMARELO))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_altura_maxima_nao_e_2", a), ("capa_B_maximo_e_minimo", b), ("capa_C_topo_no_meio_do_voo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
