"""Capas do MAT-EQU-017 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o livro com 60 páginas faltando
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "leu 1/2 e 1/5", 84, 400, 140, "g", BR)
    E.escreve(c, "faltam 60 páginas", 84, 580, 130, "g", AMARELO)
    E.escreve(c, "quantas tem o livro?", 84, 780, 120, "i", BR)
    x, y, w, h = 84, 860, 1100, 110
    q = w / 10
    c.drawRect(skia.Rect.MakeXYWH(x, y, 5 * q, h), M.paint(BR))
    c.drawRect(skia.Rect.MakeXYWH(x + 5 * q, y, 2 * q, h), M.paint(E.mix(COR, BR, 0.55)))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(BR, 1, stroke=6))
    E.centro(c, "60", x + 8.5 * q, y + 82, 80, "g", AMARELO)
    E.bola(c, 1620, 640, 170, AMARELO); E.centro(c, "?", 1620, 730, 240, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "problemas", "e inequações")


def d(c):  # o macete: a fração que falta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "ache a fração", 76, 520, 150, "g", BR)
    E.escreve(c, "que falta", 76, 680, 150, "g", BR)
    E.formula(c, "f{3}{10} = 60", 84, 920, 130, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "→ livro: 200", 600, 920, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantas_paginas", a), ("capa_B_problemas_inequacoes", b), ("capa_C_fracao_que_falta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
