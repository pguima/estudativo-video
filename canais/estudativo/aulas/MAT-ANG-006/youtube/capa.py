"""Capas do MAT-ANG-006 (1280x720). Uso: python capa.py"""
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


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def palito(c, P, Q, cor, larg=26):
    s = skia.Paint(AntiAlias=True, Color=M.hexc("#000000", 0.3))
    s.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 8))
    s.setStyle(skia.Paint.kStroke_Style); s.setStrokeWidth(larg); s.setStrokeCap(skia.Paint.kRound_Cap)
    path = skia.Path(); path.moveTo(*P); path.lineTo(*Q)
    c.save(); c.translate(4, 8); c.drawPath(path, s); c.restore()
    c.drawPath(path, M.paint(cor, 1, stroke=larg, cap_round=True))


def a(c):  # o gancho: 2, 3 e 6 não fecham
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    u = 130
    L, R = (120, 900), (120 + 6 * u, 900)
    Pa, Pb = pt(L, 2 * u, 65), pt(R, 3 * u, 180 - 65)
    palito(c, L, R, BR); palito(c, L, Pa, AMARELO); palito(c, R, Pb, "#C9C9FF")
    M.line(c, *Pa, *Pb, AMARELO, 1, 8, dash=[22, 16])
    E.escreve(c, "6", 470, 1010, 80, "g", BR); E.escreve(c, "2", 90, 760, 80, "g", AMARELO); E.escreve(c, "3", 840, 700, 80, "g", "#C9C9FF")
    E.escreve(c, "2, 3 e 6", 1060, 420, 150, "g", BR)
    E.escreve(c, "não fecha", 1040, 660, 170, "g", AMARELO)
    E.escreve(c, "por quê?", 1060, 860, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Existe esse", "triângulo?", "o teste dos lados")


def d(c):  # o atalho: diferença < x < soma
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o terceiro lado", 90, 380, 120, "i", BR)
    E.escreve(c, "diferença < x < soma", 80, 600, 140, "g", BR)
    E.escreve(c, "8 − 5 < x < 8 + 5", 90, 820, 120, "g", claro)
    E.escreve(c, "→ 3 < x < 13", 1160, 820, 120, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_fecha", a), ("capa_B_existe_triangulo", b), ("capa_C_diferenca_e_soma", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
