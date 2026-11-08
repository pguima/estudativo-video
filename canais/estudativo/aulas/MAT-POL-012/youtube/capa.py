"""Capas do MAT-POL-012 (1280x720). Uso: python capa.py"""
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


def hora(cx, cy, rr, h):
    a = math.radians(h * 30)
    return cx + rr * math.sin(a), cy - rr * math.cos(a)


def relogio(c, cx, cy, r, h, numeros=True):
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.3))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 16))
    c.drawCircle(cx + 8, cy + 14, r, s)
    c.drawCircle(cx, cy, r, M.paint(BR))
    c.drawCircle(cx, cy, r, M.paint("#121214", 1, stroke=10))
    for k in range(12):
        M.line(c, *hora(cx, cy, r * 0.86, k), *hora(cx, cy, r * 0.95, k), "#121214", 1, 8 if k % 3 == 0 else 4)
    if numeros:
        for n in range(1, 13):
            x, y = hora(cx, cy, r * 0.68, n)
            E.centro(c, str(n), x, y + 22, 60, "g", "#121214")
    M.line(c, cx, cy, *hora(cx, cy, r * 0.62, 0), "#121214", 1, 12)
    M.line(c, cx, cy, *hora(cx, cy, r * 0.42, h), COR, 1, 20)
    c.drawCircle(cx, cy, 16, M.paint("#121214"))


def a(c):  # o gancho: o relógio no espelho
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    cx, cy, r = 480, 610, 290
    ret = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - r - 50, cy - r - 50, 2 * r + 100, 2 * r + 100), 30, 30)
    c.drawRRect(ret, M.paint("#CDE8FA"))
    c.drawRRect(ret, M.paint("#9A9AA6", 1, stroke=18))
    relogio(c, cx, cy, r, 2, numeros=False)
    E.escreve(c, "no espelho:", 1000, 360, 110, "i", BR)
    E.escreve(c, "2 h", 1000, 580, 220, "g", BR)
    E.escreve(c, "de verdade?", 1000, 800, 130, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Simetrias", "na prática", "5 situações")


def d(c):  # o atalho: 12 menos a hora do espelho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    relogio(c, 1440, 580, 290, 10)
    M.line(c, 1440, 230, 1440, 930, AMARELO, 1, 8, dash=[22, 14])
    E.escreve(c, "o atalho", 90, 360, 130, "i", BR)
    E.escreve(c, "12 − 2", 90, 580, 200, "g", BR)
    E.escreve(c, "= 10 h", 90, 790, 200, "g", AMARELO)
    E.escreve(c, "relógio no espelho", 90, 950, 80, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_relogio_no_espelho", a), ("capa_B_simetrias_na_pratica", b), ("capa_C_doze_menos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
