"""Capas do MAT-ARE-012 (1280x720). Uso: python capa.py"""
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
AZUL = "#7FB0FF"
MASSA = "#F3D9A4"


def setor(c, O, r, g0, cor):
    path = skia.Path(); path.moveTo(*O)
    path.arcTo(skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r), -g0, -90, False); path.close()
    c.drawPath(path, M.paint(cor))


def pizza(c, cx, cy, r):
    c.drawCircle(cx, cy, r, M.paint(MASSA))
    for dx, dy in ((0.35, 0.2), (-0.4, 0.3), (0.1, -0.45), (-0.2, -0.1), (0.5, -0.3), (-0.1, 0.55)):
        c.drawCircle(cx + dx * r, cy + dy * r, r * 0.09, M.paint("#C8553D", 0.85))
    c.drawCircle(cx, cy, r, M.paint("#D98A00", 1, stroke=max(8, r * 0.07)))


def a(c):  # o gancho: a pizza grande compensa?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    pizza(c, 290, 680, 170); pizza(c, 720, 640, 255)
    E.escreve(c, "30 cm", 200, 940, 64, "g", BR); E.escreve(c, "45 cm", 640, 990, 70, "g", BR)
    E.escreve(c, "o dobro do preço:", 1050, 430, 80, "i", BR)
    E.escreve(c, "compensa?", 1030, 620, 135, "g", AMARELO)
    E.escreve(c, "4 situações", 1050, 800, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Áreas", "na prática", "4 situações")


def d(c):  # o atalho: junte os pedaços em círculos inteiros
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    x, y, L = 1220, 330, 500
    c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), M.paint(BR))
    for V, g0 in (((x, y + L), 0), ((x + L, y + L), 90), ((x + L, y), 180), ((x, y), 270)):
        setor(c, V, L / 2, g0, AZUL)
    c.drawRect(skia.Rect.MakeXYWH(x, y, L, L), M.paint(BR, 1, stroke=8))
    E.escreve(c, "4 quartos", 110, 420, 150, "g", BR)
    E.escreve(c, "= 1 círculo", 110, 600, 150, "g", AMARELO)
    E.escreve(c, "a área branca sem sofrer", 110, 800, 80, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_pizza_compensa", a), ("capa_B_areas_na_pratica", b), ("capa_C_quatro_quartos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
