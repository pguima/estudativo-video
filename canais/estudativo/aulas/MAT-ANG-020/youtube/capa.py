"""Capas do MAT-ANG-020 (1280x720). Uso: python capa.py"""
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
PAPELAO = "#C9A46C"


def a(c):  # o gancho: o papelão na ponta do lápis
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    T = [(470, 300), (110, 720), (900, 720)]
    G = (sum(p[0] for p in T) / 3, sum(p[1] for p in T) / 3)
    # lápis
    x, y = G
    path = skia.Path(); path.moveTo(x, y); path.lineTo(x - 30, y + 90); path.lineTo(x + 30, y + 90); path.close()
    c.drawPath(path, M.paint("#E8C9A0"))
    M.rrect(c, x - 30, y + 90, 60, 600, 6, AMARELO, 1)
    path = skia.Path(); path.addPoly(T, True)
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.3))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
    c.save(); c.translate(8, 18); c.drawPath(path, s); c.restore()
    c.drawPath(path, M.paint(PAPELAO))
    c.drawPath(path, M.paint("#8E6A35", 1, stroke=7))
    c.drawCircle(*G, 22, M.paint(BR))
    c.drawCircle(*G, 10, M.paint(COR))
    E.escreve(c, "equilibra", 1010, 440, 150, "g", BR)
    E.escreve(c, "onde?", 1010, 660, 210, "g", AMARELO)
    E.escreve(c, "conta de cabeça", 1020, 850, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Pontos", "notáveis", "e o baricentro")


def d(c):  # o atalho: mediana ÷ 3
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "2 para 1", 90, 430, 210, "g", BR)
    E.escreve(c, "mediana ÷ 3", 90, 640, 140, "i", claro)
    E.escreve(c, "30 → 10 e 20", 90, 860, 150, "g", AMARELO)
    x, y0, y1 = 1600, 220, 960
    yg = y0 + 2 / 3 * (y1 - y0)
    M.line(c, x, y0, x, yg, AMARELO, 1, 26)
    M.line(c, x, yg, x, y1, claro, 1, 26)
    c.drawCircle(x, yg, 30, M.paint(BR))
    E.escreve(c, "20", x + 60, (y0 + yg) / 2 + 40, 110, "g", AMARELO)
    E.escreve(c, "10", x + 60, (yg + y1) / 2 + 40, 110, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_equilibra_onde", a), ("capa_B_pontos_notaveis", b), ("capa_C_dois_para_um", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
