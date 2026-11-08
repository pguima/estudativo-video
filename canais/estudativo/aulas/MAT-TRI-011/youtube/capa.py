"""Capas do MAT-TRI-011 (1280x720). Uso: python capa.py"""
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


def onda(c, x0, y0, w, amp, voltas, cor, larg=14, f=math.sin, fase=0.0):
    path = skia.Path()
    n = 400
    for i in range(n + 1):
        th = 2 * math.pi * voltas * i / n
        (path.moveTo if i == 0 else path.lineTo)(x0 + w * i / n, y0 - amp * f(th + fase))
    p = M.paint(cor, 1.0, stroke=larg, cap_round=True); p.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(path, p)


def a(c):  # o gancho: a altura do ponto vira uma onda
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a altura", 84, 380, 150, "i", BR)
    E.escreve(c, "vira onda", 84, 560, 190, "g", AMARELO)
    cx, cy, r = 300, 820, 150
    M.line(c, cx - r - 40, cy, cx + r + 40, cy, BR, 0.8, 4)
    M.line(c, cx, cy + r + 40, cx, cy - r - 40, BR, 0.8, 4)
    c.drawCircle(cx, cy, r, M.paint(BR, 0.9, stroke=6))
    ang = math.radians(60)
    X, Y = cx + r * math.cos(ang), cy - r * math.sin(ang)
    M.line(c, cx, cy, X, Y, BR, 1.0, 6)
    M.line(c, X, cy, X, Y, AMARELO, 1.0, 14)
    x0 = 560
    M.line(c, X, Y, x0 + 1240 * (ang / (4 * math.pi)), Y, BR, 0.6, 4, dash=[14, 10])
    onda(c, x0, cy, 1240, r, 2, AMARELO, 16)
    c.drawCircle(X, Y, 18, M.paint(AMARELO)); c.drawCircle(X, Y, 18, M.paint(COR, 1.0, stroke=4))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Gráficos", "sen e cos", "e a tangente")


def d(c):  # o atalho: o número da frente dá a imagem
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 330, 120, "i", BR)
    E.formula(c, "y = 5 · cos x", 84, 520, 150, "g", BR)
    E.formula(c, "imagem: de −5 a 5", 84, 700, 110, "g", AMARELO)
    x0, y0, amp = 1120, 880, 130
    M.line(c, x0 - 20, y0, x0 + 760, y0, BR, 0.5, 4)
    M.line(c, x0, y0 - amp - 40, x0, y0 + amp + 40, BR, 0.5, 4)
    onda(c, x0, y0, 740, amp, 1.5, AMARELO, 14, math.cos)
    for v, s in ((amp, "5"), (-amp, "−5")):
        E.escreve(c, s, x0 - 30 - E.larg(s, "g", 60), y0 - v + 22, 60, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_altura_vira_onda", a), ("capa_B_graficos_seno_cosseno", b), ("capa_C_imagem_direto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
