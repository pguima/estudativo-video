"""Capas do MAT-TRI-013 (1280x720). Uso: python capa.py"""
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
VERDE = "#3BE38B"


def ciclo(c, cx, cy, r, ang, cor_arco):
    M.line(c, cx - r - 50, cy, cx + r + 50, cy, BR, 0.8, 4)
    M.line(c, cx, cy + r + 50, cx, cy - r - 50, BR, 0.8, 4)
    c.drawCircle(cx, cy, r, M.paint(BR, 0.9, stroke=5))
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -ang, False, M.paint(cor_arco, 1.0, stroke=14, cap_round=True))
    X, Y = cx + r * math.cos(math.radians(ang)), cy - r * math.sin(math.radians(ang))
    c.drawCircle(X, Y, 18, M.paint(cor_arco)); c.drawCircle(X, Y, 18, M.paint(COR, 1.0, stroke=4))


def a(c):  # o gancho: 4 questões, pause e resolva
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "4", 84, 560, 380, "g", AMARELO)
    E.escreve(c, "questões", 330, 470, 130, "i", BR)
    E.escreve(c, "você resolve?", 84, 850, 120, "g", BR)
    ciclo(c, 1500, 400, 170, 135, AMARELO)
    E.formula(c, "495°", 1160, 270, 70, "g", AMARELO)
    path = skia.Path()
    for i in range(201):
        X = 1180 + 640 * i / 200
        (path.moveTo if i == 0 else path.lineTo)(X, 820 - 90 * math.sin(2 * math.pi * 1.5 * i / 200))
    p = M.paint(BR, 1.0, stroke=10, cap_round=True); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "o ciclo", "e as ondas")


def d(c):  # a pegadinha da tangente no 3º quadrante
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a pegadinha", 84, 330, 120, "i", BR)
    E.formula(c, "(−) ÷ (−) = +", 84, 560, 150, "g", VERDE)
    E.escreve(c, "tg no 3º quadrante", 84, 760, 100, "g", BR)
    E.escreve(c, "é positiva", 84, 900, 100, "g", AMARELO)
    cx, cy, r = 1500, 560, 260
    M.line(c, cx - r - 50, cy, cx + r + 50, cy, BR, 0.8, 4)
    M.line(c, cx, cy + r + 50, cx, cy - r - 50, BR, 0.8, 4)
    c.drawCircle(cx, cy, r, M.paint(BR, 0.9, stroke=5))
    path = skia.Path(); path.moveTo(cx, cy); path.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -180, -90, False); path.close()
    c.drawPath(path, M.paint(VERDE, 0.35))
    E.escreve(c, "3º", cx - 170, cy + 150, 90, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quatro_questoes", a), ("capa_B_praticando_ciclo", b), ("capa_C_tangente_no_3o", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
