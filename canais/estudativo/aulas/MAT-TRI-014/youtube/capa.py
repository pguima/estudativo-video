"""Capas do MAT-TRI-014 (1280x720). Uso: python capa.py"""
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
ROSA = "#FF7FC4"


def onda(c, x0, y0, w, f, xmax, escala, cor, larg=14, a=1.0, dash=None):
    path = skia.Path()
    n = 500
    for i in range(n + 1):
        xv = xmax * i / n
        (path.moveTo if i == 0 else path.lineTo)(x0 + w * i / n, y0 - escala * f(xv))
    p = M.paint(cor, a, stroke=larg, cap_round=True); p.setStrokeJoin(skia.Paint.kRound_Join)
    if dash:
        p.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawPath(path, p)


def partes(c, lista, x, y, size):
    for s, cor in lista:
        E.formula(c, s, x, y, size, "g", cor)
        x += E.formula(None, s, 0, 0, size, "g", a=0)


def a(c):  # o gancho: a fórmula assustadora e as três tarefas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    partes(c, [("y = ", BR), ("1", AMARELO), (" + ", BR), ("2", BR), (" · cos(", BR), ("2", ROSA), ("x)", BR)], 84, 400, 150)
    E.escreve(c, "em segundos:", 84, 600, 90, "i", BR)
    E.formula(c, "máx 3 · mín −1 · período π", 84, 760, 110, "g", AMARELO)
    x0, y0, w = 1080, 1010, 760
    M.line(c, x0, y0 - 45, x0 + w, y0 - 45, AMARELO, 0.8, 4, dash=[18, 12])
    onda(c, x0, y0, w, lambda v: 1 + 2 * math.cos(2 * v), 2 * math.pi, 45, BR, 10, 1.0)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Mexer", "na onda", "a, b e c sem decorar")


def d(c):  # o atalho: três contas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho: 3 contas", 84, 320, 110, "i", BR)
    partes(c, [("máx = ", BR), ("a", AMARELO), (" + ", BR), ("b", BR)], 84, 520, 130)
    partes(c, [("mín = ", BR), ("a", AMARELO), (" − ", BR), ("b", BR)], 84, 720, 130)
    partes(c, [("período = 2π ÷ ", BR), ("c", ROSA)], 84, 920, 130)
    x0, y0, w = 1150, 640, 680
    M.line(c, x0, y0 - 70, x0 + w, y0 - 70, AMARELO, 0.9, 5, dash=[18, 12])
    onda(c, x0, y0, w, lambda v: 1 + 2 * math.cos(2 * v), 2 * math.pi, 70, AMARELO, 12)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tarefas_em_segundos", a), ("capa_B_mexer_na_onda", b), ("capa_C_tres_contas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
