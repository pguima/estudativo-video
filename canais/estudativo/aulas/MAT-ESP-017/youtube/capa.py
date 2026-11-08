"""Capas do MAT-ESP-017 (1280x720). Uso: python capa.py"""
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
SEN, COS = math.sin(math.radians(22)), math.cos(math.radians(22))


def lata(c, cx, cy, r, h, cor=None):
    """cilindro em traço branco; cor = corpo pintado"""
    ry, ct = r * SEN, cy - h * COS
    if cor:
        p = skia.Path()
        p.moveTo(cx - r, ct); p.lineTo(cx - r, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
        p.lineTo(cx + r, ct)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), 0, 180, False)
        p.close()
        c.drawPath(p, M.paint(cor, 0.9))
        c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), M.paint(E.mix(cor, BR, 0.35)))
    pt = M.paint(BR, 1, stroke=8)
    c.drawOval(skia.Rect.MakeXYWH(cx - r, ct - ry, 2 * r, 2 * ry), pt)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 0, 180, False, pt)
    M.line(c, cx - r, cy, cx - r, ct, BR, 1, 8); M.line(c, cx + r, cy, cx + r, ct, BR, 1, 8)
    return ct


def cone(c, cx, cy, r, h, cor=None):
    ry, vy = r * SEN, cy - h * COS
    p = skia.Path()
    p.moveTo(cx, vy); p.lineTo(cx - r, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - ry, 2 * r, 2 * ry), 180, -180, False)
    p.close()
    if cor:
        c.drawPath(p, M.paint(cor, 0.9))
    pt = M.paint(BR, 1, stroke=8); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def silo(c, cx, cy, r, hc, hk, sep, cor_c=None, cor_k=None):
    ct = lata(c, cx, cy, r, hc, cor_c)
    cone(c, cx, ct - sep, r, hk, cor_k)


def a(c):  # o gancho: não existe fórmula de silo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    silo(c, 330, 960, 150, 420, 230, 60, AMARELO, BR)
    E.escreve(c, "fórmula", 760, 330, 120, "i", BR)
    E.escreve(c, "de silo?", 760, 470, 120, "i", BR)
    E.escreve(c, "cilindro", 760, 680, 140, "g", AMARELO)
    E.escreve(c, "+ cone", 760, 850, 140, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Sólidos", "compostos:", "somar e subtrair")


def d(c):  # o atalho: junte as alturas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "cilindro + cone de mesmo raio", 84, 330, 84, "i", BR)
    E.escreve(c, "6 + 3 ÷ 3 = 7", 80, 560, 150, "g", AMARELO)
    E.escreve(c, "uma conta só", 84, 760, 120, "g", BR)
    silo(c, 1580, 960, 140, 420, 210, 0, COR, COR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_formula_de_silo", a), ("capa_B_solidos_compostos", b), ("capa_C_junte_as_alturas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
