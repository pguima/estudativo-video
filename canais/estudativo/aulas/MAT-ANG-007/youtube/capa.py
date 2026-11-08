"""Capas do MAT-ANG-007 (1280x720). Uso: python capa.py"""
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
LILAS = "#C9C9FF"


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def tri(B, BC, gb, gc):
    ga = 180 - gb - gc
    AB = BC * math.sin(math.radians(gc)) / math.sin(math.radians(ga))
    return pt(B, AB, gb), B, (B[0] + BC, B[1])


def cunha(c, V, g1, g2, r, cor, alfa=0.55):
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    p = skia.Path(); p.moveTo(*V); p.arcTo(ret, -g1, -(g2 - g1), False); p.close()
    c.drawPath(p, M.paint(cor, alfa))
    c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor, 1, stroke=7, cap_round=True))


def triangulo(c, A, B, Cc, r, tinta=BR, larg=12):
    """triângulo de 60° em B e 70° em C (50° em A), com as cunhas das três famílias"""
    cunha(c, B, 0, 60, r, LILAS)
    cunha(c, Cc, 110, 180, r, AMARELO)
    cunha(c, A, 240, 290, r * 0.9, BR, 0.45)
    for P, Q in ((A, B), (B, Cc), (Cc, A)):
        M.line(c, *P, *Q, tinta, 1, larg)


def a(c):  # o gancho: mesmos ângulos, tamanhos diferentes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    triangulo(c, *tri((90, 960), 330, 60, 70), 85, larg=10)
    triangulo(c, *tri((470, 960), 560, 60, 70), 140)
    E.escreve(c, "mesmos", 1100, 380, 120, "i", BR)
    E.escreve(c, "ângulos", 1090, 540, 150, "g", BR)
    E.escreve(c, "iguais?", 1090, 760, 190, "g", AMARELO)
    E.escreve(c, "não!", 1100, 940, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Triângulos", "iguais?", "os 4 casos")


def d(c):  # o atalho: dois ângulos valem por três
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "2 ângulos", 90, 420, 190, "g", BR)
    E.escreve(c, "valem por 3", 90, 620, 150, "i", claro)
    E.escreve(c, "180 − 50 − 60 = 70", 90, 840, 110, "g", claro)
    E.escreve(c, "→ ALA", 1130, 840, 110, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mesmos_angulos", a), ("capa_B_triangulos_iguais", b), ("capa_C_dois_angulos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
