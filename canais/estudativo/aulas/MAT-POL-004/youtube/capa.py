"""Capas do MAT-POL-004 (1280x720). Uso: python capa.py"""
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


def roda(c, cx, cy, r, tinta=BR, raios=None):
    for k in range(8):
        g = math.radians(k * 45 + 10)
        M.line(c, cx, cy, cx + r * 0.9 * math.cos(g), cy + r * 0.9 * math.sin(g), raios or tinta, 0.8, 5)
    c.drawCircle(cx, cy, r, M.paint(tinta, 1, stroke=r * 0.1))
    c.drawCircle(cx, cy, r * 0.08, M.paint(tinta))


def a(c):  # o gancho: 100 voltas, quanto andou?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    cx, cy, r = 400, 620, 240
    roda(c, cx, cy, r)
    M.line(c, cx, cy, cx, cy - r, AMARELO, 1, 14)
    E.escreve(c, "30 cm", cx + 30, cy - r / 2, 80, "g", AMARELO)
    M.line(c, 80, cy + r + 10, 1840, cy + r + 10, BR, 1, 8)
    M.line(c, cx, cy + r + 10, 1840, cy + r + 10, AMARELO, 1, 18)
    E.escreve(c, "100 voltas", 830, 380, 150, "g", BR)
    E.escreve(c, "andou quanto?", 830, 580, 120, "i", BR)
    E.escreve(c, "180 m", 1180, 820, 150, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Raio e", "C = 2πr", "do zero")


def d(c):  # o atalho: volta = 3 × diâmetro
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho", 90, 340, 130, "i", BR)
    E.escreve(c, "volta = 3 × d", 90, 560, 180, "g", BR)
    E.escreve(c, "com", 90, 740, 110, "i", claro); E.escreve(c, "π = 3", 285, 740, 110, "g", claro)
    roda(c, 1500, 760, 200, BR, claro)
    M.line(c, 1300, 760, 1700, 760, AMARELO, 1, 14)
    E.centro(c, "d", 1580, 720, 90, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cem_voltas", a), ("capa_B_circunferencia", b), ("capa_C_triplo_do_diametro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
