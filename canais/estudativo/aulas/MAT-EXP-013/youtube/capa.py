"""Capas do MAT-EXP-013 (1280x720). Uso: python capa.py"""
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


def log2(c, txt, x, y, size, cor, depois=""):
    """escreve "log" + base pequena rebaixada + o resto (log₂ x)"""
    w = E.formula(c, "log", x, y, size, "g", cor)
    E.formula(c, txt, x + w + size * 0.02, y + size * 0.2, size * 0.56, "g", cor)
    w += E.formula(None, txt, 0, 0, size * 0.56, "g", a=0) + size * 0.14
    return w + E.formula(c, depois, x + w, y, size, "g", cor)


def a(c):  # o gancho: o espelho de 2ˣ
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o espelho", 84, 440, 170, "g", BR)
    E.escreve(c, "de", 84, 640, 150, "i", BR)
    E.formula(c, "2^x", 250, 650, 190, "g", AMARELO)
    E.escreve(c, "na diagonal", 84, 860, 130, "i", BR)
    # gráfico: 2ˣ, log₂ x e a diagonal
    ox, oy, k = 1290, 790, 78
    P = lambda x, y: (ox + x * k, oy - y * k)
    M.arrow(c, ox - 3.2 * k, oy, ox + 7.6 * k, oy, BR, 0.8, 5, 20)
    M.arrow(c, ox, oy + 3.2 * k, ox, oy - 7.6 * k, BR, 0.8, 5, 20)
    M.line(c, *P(-3, -3), *P(7, 7), BR, 0.7, 5, dash=[16, 12])
    for f, cor in ((lambda u: (u, 2 ** u), BR), (lambda u: (2 ** u, u), AMARELO)):
        path = skia.Path()
        us = [-3.2 + (math.log2(7.4) + 3.2) * i / 200 for i in range(201)]
        path.moveTo(*P(*f(us[0])))
        for u in us[1:]:
            path.lineTo(*P(*f(u)))
        c.drawPath(path, M.paint(cor, 1.0, stroke=12, cap_round=True))
    log2(c, "2", *P(4.1, 3.0), 64, AMARELO, " x")


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função", "logarítmica", "gráfico e inequações")


def d(c):  # o atalho: a base sobe e vira potência
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 340, 120, "i", claro)
    E.escreve(c, "a base sobe", 76, 560, 180, "g", BR)
    log2(c, "2", 84, 860, 170, BR, " x > 3")
    E.escreve(c, "→", 1010, 850, 150, "g", claro)
    E.formula(c, "x > 2^3", 1200, 860, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_espelho", a), ("capa_B_funcao_logaritmica", b), ("capa_C_a_base_sobe", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
