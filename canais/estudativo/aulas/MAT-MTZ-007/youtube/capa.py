"""Capas do MAT-MTZ-007 (1280x720). Uso: python capa.py"""
import math
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


def proj(P, cx, cy, k):
    x, y, z = P
    return cx + (x + 0.55 * y * math.cos(math.radians(32))) * k, cy - (z + 0.55 * y * math.sin(math.radians(32))) * k


def face(c, pts, cx, cy, k, cor):
    pp = [proj(P, cx, cy, k) for P in pts]
    p = skia.Path(); p.addPoly(pp, True)
    c.drawPath(p, M.paint(cor, 0.28))
    c.drawPath(p, M.paint(cor, 1, stroke=6))


def a(c):  # o gancho: 0 = 2
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "0 = 2", 84, 560, 330, "g", AMARELO)
    E.escreve(c, "não é erro de conta", 84, 760, 110, "i", BR)
    E.escreve(c, "o sistema não tem solução", 84, 900, 90, "g", BR)
    cx, cy, k = 1380, 560, 170
    face(c, [(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0)], cx, cy, k, BR)
    face(c, [(0, 0, 1.8), (2, 0, 1.8), (2, 2, 1.8), (0, 2, 1.8)], cx, cy, k, AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Uma, infinitas", "ou nenhuma", "discutir um sistema")


def d(c):  # o atalho: as letras dobraram
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "impossível em 5 segundos:", 84, 380, 110, "i", BR)
    E.escreve(c, "as letras dobraram?", 76, 580, 170, "g", BR)
    E.escreve(c, "x + y + z = 3", 120, 790, 110, "g", BR)
    E.escreve(c, "2x + 2y + 2z = 7", 120, 930, 110, "g", AMARELO)
    E.escreve(c, "6 ≠ 7", 1320, 870, 150, "g", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_zero_igual_dois", a), ("capa_B_uma_infinitas_nenhuma", b), ("capa_C_as_letras_dobraram", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
