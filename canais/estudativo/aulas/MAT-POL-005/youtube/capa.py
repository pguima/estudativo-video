"""Capas do MAT-POL-005 (1280x720). Uso: python capa.py"""
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


def pt(O, r, g):
    return O[0] + r * math.cos(math.radians(g)), O[1] - r * math.sin(math.radians(g))


def arco(c, O, r, g1, g2, cor, larg):
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor, 1, stroke=larg, cap_round=True))


def a(c):  # o gancho: a borda de uma fatia
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    O, r = (480, 620), 330
    c.drawCircle(*O, r, M.paint("#F3D9A4"))
    for dx, dy in ((0.35, 0.2), (-0.4, 0.3), (0.1, -0.45), (-0.2, -0.1), (0.5, -0.3), (-0.1, 0.55)):
        c.drawCircle(O[0] + dx * r, O[1] + dy * r, r * 0.09, M.paint("#C8553D", 0.8))
    c.drawCircle(*O, r, M.paint("#D98A00", 1, stroke=22))
    for k in range(6):
        M.line(c, *O, *pt(O, r, 60 * k), "#121214", 1, 6)
    arco(c, O, r + 4, 0, 60, AMARELO, 34)
    E.escreve(c, "a borda", 940, 380, 150, "i", BR)
    E.escreve(c, "da fatia?", 930, 590, 170, "g", BR)
    E.escreve(c, "= 2π", 940, 850, 200, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Medir", "um arco", "com regra de três")


def d(c):  # o atalho: fração da volta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho", 90, 340, 130, "i", BR)
    E.escreve(c, "sem cruz", 90, 560, 190, "g", BR)
    E.formula(c, "60° = f{1}{6} da volta", 90, 820, 110, "g", claro)
    O, r = (1560, 640), 230
    c.drawCircle(*O, r, M.paint(BR, 1, stroke=10))
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    p = skia.Path(); p.moveTo(*O); p.arcTo(ret, -90, 60, False); p.close()
    c.drawPath(p, M.paint(AMARELO, 0.85))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_borda_da_fatia", a), ("capa_B_arco", b), ("capa_C_fracao_da_volta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
