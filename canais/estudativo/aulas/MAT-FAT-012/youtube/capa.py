"""Capas do MAT-FAT-012 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def fra(c, cima, baixo, cx, y, size, cor):
    w = max(E.formula(None, cima, 0, 0, size, a=0), E.formula(None, baixo, 0, 0, size, a=0)) + size * 0.3
    E.formula(c, cima, cx, y - size * 0.32, size, cor=cor, align="center")
    b = size * 0.07
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - b / 2, w, b), b / 2, b / 2), M.paint(cor))
    E.formula(c, baixo, cx, y + size * 0.98, size, cor=cor, align="center")
    return w


def livro(c, cx, cy, e, d, cor, w=260, h=330):
    for k, s in enumerate((e, d)):
        x = cx - w if k == 0 else cx
        M.rrect(c, x, cy - h / 2, w, h, 18, BR)
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, cy - h / 2, w, h), 18, 18), M.paint("#141414", 1, stroke=5))
        for i in range(4):
            yy = cy - h / 2 + 56 + i * 38
            M.line(c, x + 34, yy, x + w - 34, yy, "#D8D8E0", 1, 5)
        E.formula(c, s, x + w / 2, cy + h / 2 - 40, 90, cor=cor, align="center")
    M.line(c, cx, cy - h / 2, cx, cy + h / 2, "#141414", 1, 6)


def a(c):  # o gancho: duas páginas seguidas com produto 156
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    livro(c, 1580, 470, "?", "?", COR)
    E.formula(c, "? · ? = 156", 84, 500, 190, cor=BR)
    E.escreve(c, "que páginas são?", 84, 730, 130, "g", AMARELO)
    E.escreve(c, "uma das respostas não serve", 84, 990, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Problemas", "do 2º grau", "e o filtro")


def d(c):  # o atalho: perto da raiz do produto
    palco(c)
    E.escreve(c, "o atalho dos números seguidos", 84, 330, 100, "i", BR)
    E.formula(c, "12 · 12 = 144", 84, 520, 120, cor="#9C97C8")
    E.formula(c, "13 · 13 = 169", 84, 690, 120, cor="#9C97C8")
    E.formula(c, "12 · 13 = 156", 84, 900, 170, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_paginas", a), ("capa_B_problemas", b), ("capa_C_numeros_seguidos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
