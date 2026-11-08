"""Capas do MAT-FUN-008 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
VERMELHO = "#FF4D55"


def eixos(c, x, y, w, h, x0, x1, y0, y1, tinta=BR):
    X = lambda v: x + (v - x0) / (x1 - x0) * w
    Y = lambda v: y + h - (v - y0) / (y1 - y0) * h
    M.arrow(c, x, Y(0), x + w + 30, Y(0), tinta, 1, 6, 24)
    M.arrow(c, X(0), y + h, X(0), y - 30, tinta, 1, 6, 24)
    return X, Y


def a(c):  # o gancho: a pergunta que mais derruba
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "ela pede", 84, 430, 130, "i", BR)
    E.escreve(c, "o x ou", 76, 640, 210, "g", BR)
    E.escreve(c, "o y?", 76, 850, 210, "g", AMARELO)
    pts = [(0, 4), (4, 8), (10, 2), (12, 3)]
    X, Y = eixos(c, 1120, 230, 640, 600, -0.5, 12.5, -0.5, 9)
    pa = skia.Path()
    for i, (u, v) in enumerate(pts):
        (pa.lineTo if i else pa.moveTo)(X(u), Y(v))
    p = M.paint(BR, 1, stroke=12, cap_round=True); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(pa, p)
    M.line(c, X(0), Y(6), X(12), Y(6), AMARELO, 1, 8, dash=[22, 14])
    for u in (2, 6):
        c.drawCircle(X(u), Y(6), 26, M.paint(AMARELO, 1, stroke=8))
        M.line(c, X(u), Y(6), X(u), Y(0), AMARELO, 1, 6, dash=[16, 12])
        E.pilula(c, str(u), X(u), Y(0) + 54, 50, "g", fundo=AMARELO, cor="#121214")
    E.pilula(c, "6", X(0) - 50, Y(6), 50, "g", fundo=BR, cor=COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Praticando:", "função", "4 situações")


def d(c):  # o macete: a régua em pé no V
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o V é", 84, 420, 130, "i", claro)
    E.escreve(c, "função?", 76, 640, 210, "g", BR)
    E.escreve(c, "régua em pé", 84, 840, 140, "i", BR)
    X, Y = eixos(c, 1180, 240, 600, 580, -3, 3, -1.8, 3, claro)
    pa = skia.Path()
    pa.moveTo(X(-1.8), Y(2.8)); pa.lineTo(X(1), Y(-1)); pa.lineTo(X(3), Y(1.7))
    p = M.paint(BR, 1, stroke=12, cap_round=True); p.setStrokeJoin(skia.Paint.kMiter_Join)
    c.drawPath(pa, p)
    M.line(c, X(1), 210, X(1), 860, AMARELO, 1, 8, dash=[22, 14])
    c.drawCircle(X(1), Y(-1), 28, M.paint(AMARELO, 1, stroke=8))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_x_ou_y", a), ("capa_B_praticando_funcao", b), ("capa_C_regua_no_v", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
