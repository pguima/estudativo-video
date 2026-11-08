"""Capas do MAT-ESP-007 (1280x720). Uso: python capa.py"""
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


def embalagem(c, x, y, b, hh, L, ponta=True):
    """o prisma triangular deitado, com a ponta de frente pintada"""
    V = [(0, 0, 0), (b, 0, 0), (b / 2, hh, 0), (0, 0, L), (b, 0, L), (b / 2, hh, L)]
    F = [(0, 1, 2), (3, 4, 5), (0, 1, 4, 3), (1, 2, 5, 4), (2, 0, 3, 5)]
    pts = E._solido(c, 99, 0, V, F, E._vista_obliqua(), x, y, BR, 0.0, largura=8, escuro=True)
    if ponta:
        p = skia.Path(); p.addPoly(pts[:3], True)
        c.drawPath(p, M.paint(AMARELO, 0.9))
        E._solido(c, 99, 0, V, F, E._vista_obliqua(), x, y, BR, 0.0, largura=8, escuro=True)
    return pts


def a(c):  # o gancho: multiplicar tudo dá o dobro
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    embalagem(c, 110, 900, 440, 300, 720)
    E.escreve(c, "6 × 4 × 10 = 240", 900, 400, 110, "g", BR)
    M.line(c, 890, 420, 1830, 340, "#FF5A5A", 1, 14)
    E.escreve(c, "o dobro!", 900, 540, 100, "i", BR)
    E.escreve(c, "120 cm³", 890, 790, 210, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Prisma", "volume", "e área total")


def d(c):  # o atalho: perímetro da base vezes a altura
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho da área lateral", 84, 340, 96, "i", BR)
    E.escreve(c, "perímetro", 80, 540, 160, "g", BR)
    E.escreve(c, "× altura", 84, 700, 130, "i", BR)
    E.escreve(c, "uma conta só", 80, 930, 130, "g", AMARELO)
    x, y, s, h = 1180, 420, 34, 420
    for w_, n in ((5, "5"), (5, "5"), (6, "6")):
        r = skia.Rect.MakeXYWH(x, y, w_ * s, h)
        c.drawRect(r, M.paint(COR, 0.85)); c.drawRect(r, M.paint(BR, 1, stroke=6))
        E.centro(c, n, x + w_ * s / 2, y + h + 90, 80, "g", BR)
        x += w_ * s


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_dobro", a), ("capa_B_prisma_volume_e_area", b), ("capa_C_perimetro_vezes_altura", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
