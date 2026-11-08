"""Capas do MAT-ESP-011 (1280x720). Uso: python capa.py"""
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
VISTA = (-24, 18)


def solido(c, cx, cy, r, h, pir, enche=None):
    """caixa (prisma de base quadrada) ou pirâmide em traço branco; enche = fração de altura pintada de amarelo na caixa"""
    R, U, v = E._vista_alta(*VISTA)
    base = E._base_regular(4, r)
    if enche:
        P = [E._proj((x, y, z), R, U, cx, cy) for x, z in base for y in (0, h * enche)]
        p = skia.Path(); p.addPoly(sorted_hull(P), True)
        c.drawPath(p, M.paint(AMARELO, 0.95))
    if pir:
        E.piramide(c, 99, 0, cx, cy, 4, r, h, vista=VISTA, escuro=True, cor=BR, preenche=0.0, largura=8)
    else:
        E.prisma(c, 99, 0, cx, cy, 4, r, h, vista=VISTA, escuro=True, cor=BR, preenche=0.0, largura=8)


def sorted_hull(pts):
    P = sorted(set(pts))
    cr = lambda o, a, b: (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, hi = [], []
    for p in P:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(P):
        while len(hi) >= 2 and cr(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]


def a(c):  # o gancho: a pirâmide enche a caixa em 3 vezes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    solido(c, 280, 940, 190, 520, True)
    solido(c, 720, 940, 190, 520, False, enche=1 / 3)
    E.escreve(c, "cabe", 1060, 420, 120, "i", BR)
    E.escreve(c, "3 vezes", 1050, 640, 210, "g", AMARELO)
    E.escreve(c, "na caixa", 1060, 800, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Pirâmide", "volume", "um terço do prisma")


def d(c):  # o atalho: divida por 3 primeiro
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 110, "i", BR)
    E.escreve(c, "divida por 3", 76, 540, 170, "g", BR)
    E.escreve(c, "primeiro", 84, 700, 130, "i", BR)
    E.formula(c, "f{36}{3} × 10 = 120", 80, 930, 120, "g", AMARELO)
    solido(c, 1600, 700, 170, 420, True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tres_vezes", a), ("capa_B_piramide_volume", b), ("capa_C_divida_primeiro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
