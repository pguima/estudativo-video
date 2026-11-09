"""Capas do FIS-OND-004 (1280x720). Uso: python capa.py"""
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


def onda(c, x0, x1, y, A, lam, cor, larg=12):
    n = int((x1 - x0) / 4)
    pts = [(x0 + (x1 - x0) * i / n, y - A * math.sin(2 * math.pi * ((x1 - x0) * i / n) / lam)) for i in range(n + 1)]
    F.poli(c, pts, 1.0, cor, 1.0, larg)


def a(c):  # o gancho: som + som = silêncio
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "som + som", 84, 400, 170, "g", BR)
    E.escreve(c, "= silêncio?", 84, 600, 170, "g", AMARELO)
    E.escreve(c, "o fone que cancela ruído", 84, 860, 90, "i", BR)
    onda(c, 1180, 1840, 330, 70, 220, BR)
    onda(c, 1180, 1840, 520, -70, 220, AMARELO)
    M.line(c, 1180, 740, 1840, 740, BR, 1.0, 12)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Somar e", "polarizar", "ondas, do zero")


def d(c):  # o macete: diferença ÷ meio λ
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "reforça ou cancela?", 84, 330, 110, "i", BR)
    E.formula(c, "f{diferença}{meio λ}", 84, 600, 150, "g", BR)
    E.pilula(c, "par → reforço", 1430, 470, 90, "g", fundo=E.CERTO, cor=BR)
    E.pilula(c, "ímpar → cancela", 1430, 680, 90, "g", fundo=E.ERRADO, cor=BR)
    E.escreve(c, "o macete da interferência", 84, 960, 64, "b", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_som_mais_som_silencio", a), ("capa_B_interferencia_polarizacao", b), ("capa_C_par_reforca_impar_cancela", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
