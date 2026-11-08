"""Capas do MAT-TOP-001 (1280x720). Uso: python capa.py"""
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


def binom(c, n, p, cx, cy, size, cor=BR):
    w = max(E.larg(str(n), "g", size), E.larg(str(p), "g", size))
    E.centro(c, str(n), cx, cy - size * 0.1, size, "g", cor)
    E.centro(c, str(p), cx, cy + size * 0.82, size, "g", cor)
    h, k = size * 0.98, size * 0.24
    for lado in (-1, 1):
        x0 = cx + lado * (w / 2 + size * 0.22)
        path = skia.Path(); path.moveTo(x0, cy - h); path.quadTo(x0 + lado * k * 1.6, cy, x0, cy + h)
        c.drawPath(path, M.paint(cor, 1, stroke=size * 0.075, cap_round=True))


def a(c):  # o gancho: não é fração, vale 10
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    binom(c, 5, 2, 330, 520, 300)
    E.escreve(c, "=", 620, 640, 240, "g", BR)
    E.escreve(c, "10", 840, 660, 300, "g", AMARELO)
    E.fracao(c, 5, 2, 1600, 500, 170, BR)
    E.risco(c, 1470, 680, 1730, 320, 9, 0, AMARELO, 26)
    E.escreve(c, "não é fração!", 1330, 850, 90, "i", BR)
    E.escreve(c, "número binomial", 84, 1000, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Triângulo", "de Pascal", "sem decorar")


def d(c):  # o atalho: some a linha
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 360, 140, "i", BR)
    E.escreve(c, "some a linha", 76, 560, 190, "g", BR)
    linha = [1, 4, 6, 4, 1]
    for i, v in enumerate(linha):
        E.centro(c, str(v), 220 + i * 210, 860, 150, "g", BR)
        if i < 4:
            E.centro(c, "+", 325 + i * 210, 845, 120, "g", E.mix(COR, BR, 0.5))
    E.formula(c, "= 2^4", 1260, 860, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_fracao", a), ("capa_B_triangulo_de_pascal", b), ("capa_C_some_a_linha", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
