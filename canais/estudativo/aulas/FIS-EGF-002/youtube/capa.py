"""Capas do FIS-EGF-002 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def orbita_capa(c, cx, cy, a, b, cor, sol=True):
    pt = M.paint(cor, 0.9, stroke=6)
    pt.setPathEffect(skia.DashPathEffect.Make([22, 16], 0))
    c.drawOval(skia.Rect.MakeXYWH(cx - a, cy - b, 2 * a, 2 * b), pt)
    f = math.sqrt(a * a - b * b)
    if sol:
        E.bola(c, cx + f, cy, 70, "#FFB020")
    return cx + f


def a(c):  # o gancho: a Terra corre mais em janeiro
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "em janeiro,", 84, 380, 120, "i", BR)
    E.escreve(c, "a Terra", 84, 560, 190, "g", BR)
    E.escreve(c, "corre mais", 84, 750, 190, "g", BR)
    claro = E.mix(COR, BR, 0.82)
    fx = orbita_capa(c, 1380, 800, 400, 240, claro)
    E.bola(c, 1380 + 400, 800, 40, "#2F6FB0")
    F.seta(c, 1800, 740, 1770, 600, AMARELO, 1.0, 14)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Leis", "de Kepler", "do zero")


def d(c):  # o macete: raio × k → período × k·√k
    palco_capa(c)
    E.escreve(c, "o ano de outro planeta", 84, 330, 96, "i", BR)
    E.escreve(c, "numa conta só", 84, 490, 130, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "raio × 4", 84, 720, 120, "g", BR)
    E.formula(c, "→ ano × 8", 600, 720, 120, "g", AMARELO)
    E.formula(c, "k · r{k}", 84, 940, 140, "g", claro)


CAPAS = (("capa_A_terra_corre_em_janeiro", a), ("capa_B_leis_de_kepler", b), ("capa_C_ano_numa_conta_so", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
