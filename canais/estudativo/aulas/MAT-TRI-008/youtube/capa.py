"""Capas do MAT-TRI-008 (1280x720). Uso: python capa.py"""
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
AMBAR, PETROLEO = "#FFB84D", "#3CC7D3"


def ciclo(c, cx, cy, r, tinta=BR):
    M.line(c, cx - r - 60, cy, cx + r + 60, cy, tinta, 0.8, 4)
    M.line(c, cx, cy + r + 60, cx, cy - r - 60, tinta, 0.8, 4)
    c.drawCircle(cx, cy, r, M.paint(tinta, 0.9, stroke=5))


def a(c):  # o gancho: cos 180° = −1
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "cos 180°", 84, 430, 190, "g", BR)
    E.escreve(c, "= −1", 84, 640, 190, "g", AMARELO)
    E.escreve(c, "sem triângulo", 84, 850, 100, "i", BR)
    cx, cy, r = 1480, 600, 280
    ciclo(c, cx, cy, r)
    c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), 0, -180, False, M.paint(BR, 1.0, stroke=10, cap_round=True))
    M.line(c, cx, cy, cx - r, cy, AMARELO, 1.0, 16, cap_round=False)
    c.drawCircle(cx - r, cy, 22, M.paint(AMARELO))
    E.escreve(c, "−1", cx - r - 40, cy + 90, 70, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Seno e", "cosseno", "no ciclo")


def d(c):  # o macete: to, se, ta, co
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o macete dos sinais", 84, 360, 100, "i", BR)
    E.escreve(c, "to se", 84, 590, 200, "g", BR)
    E.escreve(c, "ta co", 84, 800, 200, "g", BR)
    cx, cy, r = 1460, 600, 290
    ciclo(c, cx, cy, r)
    for s, ang, cor in (("TO", 45, BR), ("SE", 135, AMBAR), ("TA", 225, BR), ("CO", 315, PETROLEO)):
        X, Y = cx + r * 0.55 * math.cos(math.radians(ang)), cy - r * 0.55 * math.sin(math.radians(ang))
        E.centro(c, s, X, Y + 34, 96, "g", cor)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cos_180", a), ("capa_B_seno_cosseno_ciclo", b), ("capa_C_to_se_ta_co", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
