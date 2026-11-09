"""Capas do FIS-OND-007 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def corda(c, x0, x1, y, A, n, cor, larg=10):
    for s in (1, -1):
        pts = [(x0 + (x1 - x0) * i / 200, y - s * A * math.sin(n * math.pi * i / 200)) for i in range(201)]
        F.poli(c, pts, 1.0, cor, 1.0 if s == 1 else 0.45, larg)
    for j in range(n + 1):
        c.drawCircle(x0 + (x1 - x0) * j / n, y, 16, M.paint(BR))


def a(c):  # o gancho: mesmo comprimento, notas diferentes
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "por que a", 84, 420, 170, "g", BR)
    E.escreve(c, "nota sobe?", 84, 610, 170, "g", AMARELO)
    E.escreve(c, "cordas e harmônicos", 84, 860, 100, "i", BR)
    for i, n in enumerate((1, 2, 3)):
        corda(c, 1280, 1830, 300 + i * 220, 70, n, AMARELO if i == 0 else BR, 8)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Cordas", "e tubos", "harmônicos")


def d(c):  # o macete: tubo fechado só tem ímpares
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "tubo fechado:", 84, 360, 130, "i", BR)
    E.escreve(c, "só ímpares", 84, 590, 200, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, s in enumerate(("×1", "×3", "×5")):
        E.pilula(c, s, 240 + i * 290, 830, 100, "g", fundo=COR, cor=BR)
    x0, x1, y, h = 1150, 1800, 820, 170
    for yy in (y - h / 2, y + h / 2):
        M.line(c, x0, yy, x1, yy, BR, 1.0, 12)
    M.line(c, x1, y - h / 2 - 6, x1, y + h / 2 + 6, BR, 1.0, 20)
    for s in (1, -1):
        pts = [(x0 + (x1 - x0) * i / 120, y - s * 60 * math.cos(math.pi / 2 * i / 120)) for i in range(121)]
        F.poli(c, pts, 1.0, claro, 1.0, 8)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_por_que_a_nota_sobe", a), ("capa_B_cordas_e_tubos", b), ("capa_C_tubo_fechado_so_impares", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
