"""Capas do MAT-FUN-021 (1280x720). Uso: python capa.py"""
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

f = lambda v: 2 * (v - 1) * (v - 5)


def mini(c, x, y, w, h, fn, cor, x0=-1, x1=7, ymin=-10, ymax=13, ate=(-0.1, 6.1), largura=11):
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


def marcas(c, X, Y, cor_r=AMARELO):
    for r in (1, 5):
        c.drawCircle(X(r), Y(0), 24, M.paint(cor_r, 1, stroke=8))
    c.drawCircle(X(0), Y(10), 22, M.paint(BR))
    E.pilula(c, "1", X(1), Y(0) + 70, 46, "g", fundo=cor_r, cor=COR)
    E.pilula(c, "5", X(5), Y(0) + 70, 46, "g", fundo=cor_r, cor=COR)
    E.pilula(c, "10", X(0) + 90, Y(10), 46, "g", fundo=BR, cor=COR)


def a(c):  # o gancho: 3 números, a lei inteira
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 números", 84, 390, 140, "g", AMARELO)
    E.escreve(c, "e a lei sai", 84, 550, 140, "g", BR)
    E.escreve(c, "y = ?", 84, 790, 160, "g", BR)
    X, Y = mini(c, 1100, 230, 660, 680, f, BR)
    marcas(c, X, Y)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "A lei da", "parábola", "pelas raízes")


def d(c):  # o atalho: a = c ÷ produto das raízes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o a sem equação", 84, 380, 100, "i", claro)
    E.escreve(c, "a =", 84, 640, 170, "g", BR)
    E.formula(c, "f{c}{produto das raízes}", 400, 640, 110, "g", AMARELO)
    E.escreve(c, "10 ÷ (1 · 5) = 2", 84, 900, 90, "g", BR)
    X, Y = mini(c, 1380, 300, 440, 520, f, claro, largura=9)
    for r in (1, 5):
        c.drawCircle(X(r), Y(0), 20, M.paint(AMARELO, 1, stroke=7))
    c.drawCircle(X(0), Y(10), 18, M.paint(BR))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tres_numeros_e_a_lei", a), ("capa_B_lei_da_parabola", b), ("capa_C_a_sem_equacao", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
