"""Capas do MAT-POL-006 (1280x720). Uso: python capa.py"""
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


def reto(c, V, A, B, s, cor):
    u = [(P[0] - V[0], P[1] - V[1]) for P in (A, B)]
    u = [(x / math.hypot(x, y), y / math.hypot(x, y)) for x, y in u]
    q1 = (V[0] + u[0][0] * s, V[1] + u[0][1] * s)
    q2 = (V[0] + u[1][0] * s, V[1] + u[1][1] * s)
    qm = (q1[0] + u[1][0] * s, q1[1] + u[1][1] * s)
    p = skia.Path(); p.moveTo(*V); p.lineTo(*q1); p.lineTo(*qm); p.lineTo(*q2); p.close()
    c.drawPath(p, M.paint(cor, 0.85))


def a(c):  # o gancho: meia pizza, sempre 90°
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    O, r = (520, 900), 420
    ret = skia.Rect.MakeXYWH(O[0] - r, O[1] - r, 2 * r, 2 * r)
    p = skia.Path(); p.moveTo(O[0] - r, O[1]); p.arcTo(ret, 180, 180, False); p.close()
    c.drawPath(p, M.paint("#F3D9A4"))
    c.drawArc(ret, 180, 180, False, M.paint("#D98A00", 1, stroke=24))
    A, B = (O[0] - r, O[1]), (O[0] + r, O[1])
    for g in (130, 60):
        P = pt(O, r, g)
        M.line(c, *P, *A, "#121214", 1, 8); M.line(c, *P, *B, "#121214", 1, 8)
        reto(c, P, A, B, 46, COR)
        c.drawCircle(*P, 14, M.paint(COR))
    M.line(c, *A, *B, "#121214", 1, 10)
    E.escreve(c, "sempre", 1060, 400, 140, "i", BR)
    E.escreve(c, "90°", 1040, 660, 300, "g", AMARELO)
    E.escreve(c, "por quê?", 1070, 860, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Central e", "inscrito", "vale a metade")


def d(c):  # o atalho: diâmetro = reto
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho", 90, 340, 130, "i", BR)
    E.escreve(c, "diâmetro", 90, 560, 170, "g", BR)
    E.escreve(c, "= ângulo reto", 90, 760, 130, "g", claro)
    O, r = (1520, 640), 260
    c.drawCircle(*O, r, M.paint(BR, 1, stroke=9))
    A, B, P = pt(O, r, 180), pt(O, r, 0), pt(O, r, 120)
    p = skia.Path(); p.addPoly([A, B, P], True)
    pa = M.paint(BR, 1, stroke=9); pa.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pa)
    M.line(c, *A, *B, AMARELO, 1, 14)
    reto(c, P, A, B, 50, AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sempre_90", a), ("capa_B_central_e_inscrito", b), ("capa_C_diametro_reto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
