"""Capas do MAT-TRI-007 (1280x720). Uso: python capa.py"""
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


def pt(cx, cy, r, ang):
    return cx + r * math.cos(math.radians(ang)), cy - r * math.sin(math.radians(ang))


def espiral(c, cx, cy, r, total, cor, passo, larg=12):
    path = skia.Path()
    n = int(total / 2)
    for i in range(n + 1):
        ang = total * i / n
        X, Y = pt(cx, cy, r + passo * ang / 360, ang)
        (path.moveTo if i == 0 else path.lineTo)(X, Y)
    p = M.paint(cor, 1.0, stroke=larg, cap_round=True); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)


def ciclo(c, cx, cy, r, tinta=BR):
    M.line(c, cx - r - 60, cy, cx + r + 60, cy, tinta, 0.8, 4)
    M.line(c, cx, cy + r + 60, cx, cy - r - 60, tinta, 0.8, 4)
    c.drawCircle(cx, cy, r, M.paint(tinta, 0.9, stroke=5))


def a(c):  # o gancho: 390° cai no 30°
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "390°", 84, 450, 230, "g", BR)
    E.escreve(c, "= 30°?", 84, 640, 160, "g", AMARELO)
    E.escreve(c, "o ciclo explica", 84, 840, 100, "i", BR)
    cx, cy, r = 1460, 600, 280
    ciclo(c, cx, cy, r)
    espiral(c, cx, cy, r - 50, 390, AMARELO, 70)
    X, Y = pt(cx, cy, r, 30)
    c.drawCircle(X, Y, 20, M.paint(AMARELO)); c.drawCircle(X, Y, 20, M.paint(COR, 1.0, stroke=4))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Radianos", "e o ciclo", "trigonométrico")


def d(c):  # o atalho: troque π por 180°
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 130, "i", BR)
    E.formula(c, "π = 180°", 84, 580, 230, "g", BR)
    E.formula(c, "f{π}{3} = f{180°}{3} = 60°", 84, 880, 120, "g", AMARELO)
    cx, cy, r = 1480, 700, 300
    ciclo(c, cx, cy, r)
    c.drawArc(skia.Rect.MakeXYWH(cx - r - 30, cy - r - 30, 2 * r + 60, 2 * r + 60), 0, -180, False, M.paint(AMARELO, 1.0, stroke=14, cap_round=True))
    E.escreve(c, "π rad", cx - 90, cy - r - 60, 80, "g", AMARELO)
    E.escreve(c, "180°", cx - 190, cy - 90, 80, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_390_e_30", a), ("capa_B_radianos_e_ciclo", b), ("capa_C_pi_e_180", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
