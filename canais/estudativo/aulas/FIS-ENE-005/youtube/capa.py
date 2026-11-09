"""Capas do FIS-ENE-005 (1280x720). Uso: python capa.py"""
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


def trilho(c, x0, x1, y0, y1, cor):
    pts = [(lerp(x0, x1, i / 40), lerp(y0, y1, (1 - math.cos(math.pi * i / 40)) / 2)) for i in range(41)]
    F.poli(c, pts, 1.0, cor, 1.0, 14)


def lerp(a, b, k):
    return a + (b - a) * k


def a(c):  # o gancho: 20 m de altura, a que velocidade?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "desce 20 m", 84, 380, 130, "i", BR)
    E.escreve(c, "v = ?", 84, 640, 260, "g", BR)
    E.escreve(c, "a massa não importa", 84, 860, 90, "g", AMARELO)
    claro = E.mix(COR, BR, 0.85)
    trilho(c, 1150, 1800, 330, 880, claro)
    E.bola(c, 1150, 290, 44, AMARELO)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Conservação", 76, 450, 190, "g", BR)
    E.escreve(c, "da energia", 76, 660, 190, "g", BR)
    E.escreve(c, "e energia dissipada", 84, 860, 110, "i", BR)
    E.simbolo(c, 1620, 780, 230, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o atalho: v = √(2gh)
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "do repouso, sem atrito", 84, 340, 110, "i", BR)
    E.formula(c, "v = r{2 · g · h}", 84, 640, 220, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "h = 20 m  →  v = 20 m/s", 84, 900, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_desce_20_m_v_igual_a", a), ("capa_B_conservacao_da_energia", b), ("capa_C_raiz_de_2gh", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
