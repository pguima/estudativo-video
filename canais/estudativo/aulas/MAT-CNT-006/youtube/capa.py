"""Capas do MAT-CNT-006 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def letra(c, cx, cy, s, ch, fundo=BR, tinta=None):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.16, s * 0.16)
    c.drawRRect(r, M.paint(fundo))
    E.centro(c, ch, cx, cy + s * 0.22, s * 0.6, "g", tinta or COR)


def a(c):  # o gancho: ARARA não tem 120 anagramas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i, ch in enumerate("ARARA"):
        letra(c, 180 + i * 210, 380, 180, ch)
    E.escreve(c, "5! = 120", 84, 720, 190, "g", BR)
    E.risco(c, 60, 660, 860, 650, 9, 0, AMARELO, 30)
    E.escreve(c, "são só", 84, 930, 130, "i", BR)
    E.bola(c, 1450, 700, 240, "#FFFFFF")
    E.centro(c, "10", 1450, 700 + 80, 220, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Letras", "repetidas", "e mesa redonda")


def d(c):  # o macete: mesa redonda, fixe uma pessoa
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cx, cy, R = 1450, 600, 300
    c.drawCircle(cx, cy, R * 0.55, M.paint(BR, 0.12)); c.drawCircle(cx, cy, R * 0.55, M.paint(BR, 1, stroke=6))
    cores = ("#E08A3C", "#8E5BD9", "#5B8DB8", "#55895A", "#C2463A")
    for k in range(5):
        ang = math.radians(-90 + k * 72)
        x, y = cx + R * math.cos(ang), cy + R * math.sin(ang)
        c.drawCircle(x, y, 62, M.paint(cores[k]))
        E.centro(c, "ABCDE"[k], x, y + 25, 70, "g", BR)
        if k == 0:
            c.drawCircle(x, y, 82, M.paint(AMARELO, 1, stroke=10))
    E.escreve(c, "mesa redonda?", 84, 380, 130, "i", BR)
    E.escreve(c, "fixe uma", 84, 580, 170, "g", BR)
    E.formula(c, "(n − 1)!", 84, 860, 220, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_arara_10", a), ("capa_B_repetidas_mesa", b), ("capa_C_fixe_uma", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
