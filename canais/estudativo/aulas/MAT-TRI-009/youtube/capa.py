"""Capas do MAT-TRI-009 (1280x720). Uso: python capa.py"""
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


def pt(cx, cy, r, g):
    return cx + r * math.cos(math.radians(g)), cy - r * math.sin(math.radians(g))


def ciclo(c, cx, cy, r, tinta=BR):
    M.line(c, cx - r - 60, cy, cx + r + 60, cy, tinta, 0.8, 4)
    M.line(c, cx, cy + r + 60, cx, cy - r - 60, tinta, 0.8, 4)
    c.drawCircle(cx, cy, r, M.paint(tinta, 0.9, stroke=5))


def par(c, cx, cy, r, a1, a2, cor=AMARELO):
    P1, P2 = pt(cx, cy, r, a1), pt(cx, cy, r, a2)
    M.line(c, *P1, *P2, BR, 0.8, 5, dash=[18, 12])
    for P in (P1, P2):
        M.line(c, P[0], cy, *P, cor, 1.0, 14, cap_round=False)
    c.drawCircle(*P1, 20, M.paint(cor))
    c.drawCircle(*P2, 20, M.paint(COR)); c.drawCircle(*P2, 20, M.paint(cor, 1.0, stroke=6))


def a(c):  # o gancho: sen 150° = sen 30°
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "sen 150°", 84, 430, 180, "g", BR)
    E.escreve(c, "= sen 30°", 84, 630, 160, "g", AMARELO)
    E.escreve(c, "o parceiro no 1º quadrante", 84, 830, 80, "i", BR)
    cx, cy, r = 1480, 620, 270
    ciclo(c, cx, cy, r)
    par(c, cx, cy, r, 150, 30)
    E.escreve(c, "150°", cx - r - 70, cy - 170, 60, "g", BR)
    E.escreve(c, "30°", cx + r - 10, cy - 170, 60, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Redução ao", "1º quadrante", "seno e cosseno")


def d(c):  # o atalho: distância até o eixo horizontal
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 360, 130, "i", BR)
    E.escreve(c, "cos 240°", 84, 570, 170, "g", BR)
    E.formula(c, "= −cos 60° = −f{1}{2}", 84, 800, 110, "g", AMARELO)
    cx, cy, r = 1500, 620, 260
    ciclo(c, cx, cy, r)
    M.line(c, cx - r - 40, cy, cx + r + 40, cy, AMARELO, 1.0, 8)
    P1, P2 = pt(cx, cy, r, 240), pt(cx, cy, r, 60)
    M.line(c, *P1, *P2, BR, 0.8, 5, dash=[18, 12])
    c.drawCircle(*P1, 20, M.paint(BR)); c.drawCircle(*P2, 20, M.paint("#07070F")); c.drawCircle(*P2, 20, M.paint(BR, 1.0, stroke=6))
    rr = r + 30
    c.drawArc(skia.Rect.MakeXYWH(cx - rr, cy - rr, 2 * rr, 2 * rr), -180, -60, False, M.paint(E.mix(COR, BR, 0.55), 1.0, stroke=12, cap_round=True))
    E.escreve(c, "60°", cx - r - 150, cy + 190, 60, "g", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sen_150", a), ("capa_B_reducao_primeiro_quadrante", b), ("capa_C_atalho_eixo_horizontal", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
