"""Capas do MAT-ARE-009 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF6B6B"
LILAS = "#C9C9FF"


def portao(c, x, y, u, tinta=BR):
    w, h, r = 4 * u, 3 * u, 2 * u
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(LILAS, 0.3))
    path = skia.Path(); path.moveTo(x + w, y); path.arcTo(skia.Rect.MakeXYWH(x + w / 2 - r, y - r, 2 * r, 2 * r), 0, -180, False); path.close()
    c.drawPath(path, M.paint(LILAS, 0.3))
    p = M.paint(tinta, 1, stroke=12); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), p)
    M.line(c, x, y, x + w, y, VERMELHO, 1, 18)


def a(c):  # o gancho: o contorno do portão
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    portao(c, 180, 540, 110)
    E.escreve(c, "4 m", 340, 1000, 80, "g", BR)
    E.escreve(c, "16 m", 900, 420, 200, "g", AMARELO)
    E.escreve(c, "ou 20 m?", 900, 620, 170, "g", BR)
    E.escreve(c, "o contorno do portão", 900, 800, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Figuras", "compostas", "somar e subtrair")


def d(c):  # o atalho: retângulo menos os cantos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    s, x0, y0 = 90, 1180, 360
    P = lambda i, j: (x0 + i * s, y0 + (4 - j) * s)
    for vs in ([(0, 0), (2, 0), (0, 1)], [(6, 0), (6, 3), (2, 0)], [(6, 4), (4, 4), (6, 3)], [(0, 4), (0, 1), (4, 4)]):
        path = skia.Path(); path.addPoly([P(*v) for v in vs], True)
        c.drawPath(path, M.paint(AMARELO, 0.75))
    path = skia.Path(); path.addPoly([P(2, 0), P(6, 3), P(4, 4), P(0, 1)], True)
    c.drawPath(path, M.paint(LILAS, 0.8))
    for i in range(7):
        M.line(c, x0 + i * s, y0, x0 + i * s, y0 + 4 * s, BR, 0.35, 2)
    for j in range(5):
        M.line(c, x0, y0 + j * s, x0 + 6 * s, y0 + j * s, BR, 0.35, 2)
    c.drawRect(skia.Rect.MakeXYWH(x0, y0, 6 * s, 4 * s), M.paint(BR, 1, stroke=8))
    E.escreve(c, "área na malha:", 110, 380, 110, "i", BR)
    E.escreve(c, "retângulo", 110, 560, 150, "g", BR)
    E.escreve(c, "− cantos", 110, 730, 150, "g", AMARELO)
    E.escreve(c, "24 − 14 = 10", 110, 920, 110, "g", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_16_ou_20", a), ("capa_B_figuras_compostas", b), ("capa_C_retangulo_menos_cantos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
