"""Capas do MAT-TRA-006 (1280x720). Uso: python capa.py"""
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
VERDE = "#7CF2B0"


def pt(cx, cy, r, g):
    return cx + r * math.cos(math.radians(g)), cy - r * math.sin(math.radians(g))


def ciclo(c, cx, cy, r, tinta=BR):
    M.line(c, cx - r - 60, cy, cx + r + 60, cy, tinta, 0.8, 4)
    M.line(c, cx, cy + r + 60, cx, cy - r - 60, tinta, 0.8, 4)
    c.drawCircle(cx, cy, r, M.paint(tinta, 0.9, stroke=5))


def a(c):  # o gancho: o ângulo esquecido
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "sen x = f{1}{2}", 84, 440, 170, "g", BR)
    E.escreve(c, "só 30°?", 84, 680, 170, "g", AMARELO)
    E.escreve(c, "falta um ângulo", 84, 880, 110, "i", BR)
    cx, cy, r = 1480, 620, 270
    ciclo(c, cx, cy, r)
    y = cy - r * 0.5
    M.line(c, cx - r - 50, y, cx + r + 50, y, AMARELO, 1.0, 6, dash=[20, 12])
    P1, P2 = pt(cx, cy, r, 30), pt(cx, cy, r, 150)
    c.drawCircle(*P1, 22, M.paint(BR))
    c.drawCircle(*P2, 26, M.paint(AMARELO))
    E.escreve(c, "30°", P1[0] + 20, P1[1] - 30, 60, "g", BR)
    E.escreve(c, "?", P2[0] - 70, P2[1] - 30, 90, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Equações", "no ciclo", "e inequações")


def d(c):  # o atalho: π − x
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o parceiro", 84, 360, 130, "i", BR)
    E.formula(c, "seno: π − x", 84, 600, 150, "g", AMARELO)
    E.formula(c, "cosseno: 2π − x", 84, 840, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_so_30", a), ("capa_B_equacoes_no_ciclo", b), ("capa_C_parceiro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
