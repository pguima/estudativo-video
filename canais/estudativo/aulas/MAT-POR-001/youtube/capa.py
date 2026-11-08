"""Capas do MAT-POR-001 (1280x720). Uso: python capa.py"""
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


def pizza(c, cx, cy, r, n, pint, cor, sai=0):
    c.drawCircle(cx, cy, r, M.paint(BR, 0.16))
    for i in range(n):
        ang = math.radians(-90 + i * 360 / n)
        M.line(c, cx, cy, cx + r * math.cos(ang), cy + r * math.sin(ang), BR, 0.6, 5)
    c.drawCircle(cx, cy, r, M.paint(BR, 1, stroke=8))
    for i in range(pint):
        a0 = -90 + i * 360 / n
        m = math.radians(a0 + 180 / n)
        x, y = cx + sai * math.cos(m), cy + sai * math.sin(m)
        p = skia.Path(); p.moveTo(x, y); p.arcTo(skia.Rect.MakeXYWH(x - r, y - r, 2 * r, 2 * r), a0, 360 / n, False); p.close()
        c.drawPath(p, M.paint(cor)); c.drawPath(p, M.paint(COR, 1, stroke=6))


def a(c):  # o gancho: 12,5% é uma fatia de pizza de 8
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "12,5%", 84, 470, 270, "g", BR)
    E.escreve(c, "= 1 fatia", 90, 680, 170, "g", AMARELO)
    E.escreve(c, "de uma pizza de 8", 90, 860, 110, "i", BR)
    pizza(c, 1500, 520, 290, 8, 1, AMARELO, 50)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Porcentagem", "em fração", "e em decimal")


def d(c):  # o atalho: o caminho das metades
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o caminho das", 84, 330, 130, "i", BR)
    E.escreve(c, "metades", 76, 540, 220, "g", BR)
    for i, (pc, dd) in enumerate((("50%", 2), ("25%", 4), ("12,5%", 8))):
        x = 330 + i * 560
        E.centro(c, pc, x, 730, 110, "g", E.mix(COR, BR, 0.55))
        E.fracao(c, 1, dd, x, 900, 100, BR)
        if i:
            M.arrow(c, x - 380, 690, x - 240, 690, BR, 1, 8, 26)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_fatia_de_pizza", a), ("capa_B_porcentagem_fracao_decimal", b), ("capa_C_metades", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
