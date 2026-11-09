"""Capas do FIS-OND-010 (1280x720). Uso: python capa.py"""
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
ARCO_IRIS = ["#E53935", "#FB8C00", "#FDD835", "#43A047", "#1E88E5", "#3949AB", "#8E24AA"]


def onda(c, x0, x1, y, A, lam, cor, larg=8):
    pts = [(x, y - A * math.sin(2 * math.pi * (x - x0) / lam)) for x in range(int(x0), int(x1) + 1, 2)]
    F.poli(c, pts, 1.0, cor, 1.0, larg)


def a(c):  # o erro: raio X mais rápido?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "raio X é mais", 84, 400, 150, "g", BR)
    E.escreve(c, "rápido?", 84, 570, 170, "g", BR)
    E.risco(c, 70, 600, 760, 440, 9, 0, AMARELO, 30)
    E.escreve(c, "a mesma velocidade", 84, 840, 100, "i", BR)
    E.escreve(c, "rádio", 1080, 330, 64, "b", BR)
    onda(c, 1080, 1840, 420, 60, 300, BR)
    E.escreve(c, "raio X", 1080, 640, 64, "b", BR)
    onda(c, 1080, 1840, 730, 26, 34, AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Espectro", "em ordem", "do rádio ao gama")


def d(c):  # o macete: a frase da ordem
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a ordem numa frase", 84, 330, 120, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    y = 520
    for linha in (("Rita", "Mandou", "Isabel", "Ver"), ("Uma", "Xícara", "Grande")):
        x = 84
        for p in linha:
            E.escreve(c, p[0], x, y, 150, "g", AMARELO)
            w0 = E.larg(p[0], "g", 150) + E.APERTO["g"] * 150
            E.escreve(c, p[1:], x + w0, y, 150, "g", BR)
            x += E.larg(p, "g", 150) + 50
        y += 180
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(84, 0), skia.Point(1836, 0)], [M.hexc(cc) for cc in ARCO_IRIS]))
    c.drawRect(skia.Rect.MakeXYWH(84, 900, 1752, 40), p)
    E.escreve(c, "rádio → gama", 84, 1020, 56, "b", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_raio_x_mais_rapido", a), ("capa_B_espectro_em_ordem", b), ("capa_C_a_ordem_numa_frase", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
