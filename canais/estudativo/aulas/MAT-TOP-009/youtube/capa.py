"""Capas do MAT-TOP-009 (1280x720). Uso: python capa.py"""
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


def circ(c, cx, cy, r, cor, w=12):
    c.drawCircle(cx, cy, r, M.paint(cor, 1, stroke=w))


def a(c):  # o gancho: 3 + 2 = 5, encostam
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    k, cx, cy = 95, 1120, 560
    circ(c, cx, cy, 3 * k, BR)
    circ(c, cx + 5 * k, cy, 2 * k, AMARELO)
    M.line(c, cx, cy, cx + 5 * k, cy, BR, 0.6, 8, dash=[24, 18])
    c.drawCircle(cx + 3 * k, cy, 26, M.paint(AMARELO))
    E.escreve(c, "3 + 2 = 5", 84, 470, 170, "g", BR)
    E.escreve(c, "se cortam", 84, 680, 110, "i", BR)
    E.escreve(c, "ou encostam?", 84, 820, 110, "i", BR)


def b(c):  # o modelo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)  # como o capa_modelo, com a palavra longa menor
    tom = M.on(COR)
    E.escreve(c, "Duas", 76, 450, 210, "g", tom)
    E.escreve(c, "circunferências", 76, 640, 170, "g", tom)
    E.escreve(c, "posição sem desenhar", 84, 860, 150, "i", tom)
    E.mais(c, 1700, 400, 170, E.mix(COR, "#FFFFFF", 0.82), 1.0)


def d(c):  # o atalho: a régua
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 360, 140, "i", BR)
    E.escreve(c, "a régua de 2 marcas", 76, 560, 150, "g", BR)
    y = 820
    M.line(c, 120, y, 1800, y, BR, 1, 10)
    for x, s in ((680, "diferença"), (1240, "soma")):
        M.line(c, x, y - 50, x, y + 50, AMARELO, 1, 14)
        E.centro(c, s, x, y - 80, 70, "g", AMARELO)
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(700, y - 22, 1220, y + 22), 14, 14), M.paint(COR))
    E.centro(c, "secantes", 960, y + 120, 80, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_encostam", a), ("capa_B_duas_circunferencias", b), ("capa_C_regua", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
