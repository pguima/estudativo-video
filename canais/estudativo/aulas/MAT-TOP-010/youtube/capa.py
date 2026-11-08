"""Capas do MAT-TOP-010 (1280x720). Uso: python capa.py"""
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


def parabola(c, ox, oy, k, xmax, cor, w=12, kq=8):
    """x² = kq·y em pixels: 1 unidade = k px, vértice em (ox, oy)"""
    pts = [(ox + u * k / 10, oy - (u / 10) ** 2 / kq * k) for u in range(-xmax * 10, xmax * 10 + 1)]
    path = skia.Path(); path.moveTo(*pts[0])
    for p in pts[1:]:
        path.lineTo(*p)
    c.drawPath(path, M.paint(cor, 1, stroke=w, cap_round=True))


def a(c):  # o gancho: o foco não é (0, 8)
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    ox, oy, k = 1380, 760, 60
    parabola(c, ox, oy, k, 8, BR)
    M.line(c, ox - 520, oy + 2 * k, ox + 480, oy + 2 * k, AMARELO, 1, 8, dash=[26, 18])
    c.drawCircle(ox, oy - 2 * k, 26, M.paint(AMARELO))
    E.escreve(c, "F", ox + 40, oy - 2 * k - 20, 90, "g", AMARELO)
    E.formula(c, "x^2 = 8y", 84, 470, 220, "g", BR)
    E.escreve(c, "foco em 8?", 84, 680, 130, "i", BR)
    E.risco(c, 70, 700, 640, 600, 9, 0, AMARELO, 24)
    E.escreve(c, "foco em 2", 84, 870, 150, "g", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Parábola:", "foco e reta", "de olho na equação")


def d(c):  # o atalho: largura 4p no foco
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 360, 140, "i", BR)
    E.escreve(c, "largura 4p", 76, 570, 200, "g", BR)
    E.escreve(c, "na altura do foco", 84, 740, 110, "i", BR)
    ox, oy, k = 1520, 960, 50
    parabola(c, ox, oy, k, 8, BR, 10)
    M.line(c, ox - 4 * k, oy - 2 * k, ox + 4 * k, oy - 2 * k, AMARELO, 1, 12)
    for x in (ox - 4 * k, ox + 4 * k):
        c.drawCircle(x, oy - 2 * k, 18, M.paint(AMARELO))
    c.drawCircle(ox, oy - 2 * k, 14, M.paint(BR))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_foco_nao_e_8", a), ("capa_B_foco_e_diretriz", b), ("capa_C_largura_4p", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
