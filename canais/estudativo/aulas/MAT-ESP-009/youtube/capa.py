"""Capas do MAT-ESP-009 (1280x720). Uso: python capa.py"""
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
KX, KY = 0.394, -0.308


def agua(c, x, y, w, d, h):
    dx, dy = KX * d, KY * d
    for pts, tinta in (([(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + dy - h), (x + w, y - h)], E.mix(AMARELO, "#000000", 0.2)),
                       ([(x, y - h), (x + w, y - h), (x + w + dx, y - h + dy), (x + dx, y - h + dy)], E.mix(AMARELO, BR, 0.35)),
                       ([(x, y), (x + w, y), (x + w, y - h), (x, y - h)], AMARELO)):
        p = skia.Path(); p.addPoly(pts, True)
        c.drawPath(p, M.paint(tinta))


def a(c):  # o gancho: um balde de 9 L sobe quanto?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, y, w, d, h = 110, 900, 600, 300, 400
    agua(c, x, y, w, d, 70)
    E.paralelepipedo(c, 99, 0, x, y, w, d, h, escuro=True, cor=BR, preenche=0.0, largura=8)
    E.escreve(c, "+ 9 litros", 960, 400, 130, "g", BR)
    E.escreve(c, "o nível sobe", 960, 560, 100, "i", BR)
    E.escreve(c, "5 cm", 950, 820, 250, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Encher", "a caixa", "nível, vazão e tempo")


def d(c):  # o atalho: um quarto do tempo, um quarto da altura
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho, sem converter", 84, 340, 96, "i", BR)
    E.formula(c, "f{1}{4} do tempo", 80, 600, 150, "g", BR)
    E.formula(c, "= f{1}{4} da altura", 80, 860, 150, "g", AMARELO)
    x, y, w, h = 1450, 980, 300, 640
    c.drawRect(skia.Rect.MakeXYWH(x, y - h / 4, w, h / 4), M.paint(AMARELO))
    c.drawRect(skia.Rect.MakeXYWH(x, y - h, w, h), M.paint(BR, 1, stroke=8))
    for k in range(1, 4):
        pt = M.paint(BR, 0.7, stroke=4); pt.setPathEffect(skia.DashPathEffect.Make([16, 12], 0))
        c.drawLine(x, y - h * k / 4, x + w, y - h * k / 4, pt)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nove_litros", a), ("capa_B_encher_a_caixa", b), ("capa_C_um_quarto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
