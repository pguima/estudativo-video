"""Capas do FIS-EGF-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: distância dobrada, força pela metade?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "distância × 2", 84, 380, 150, "g", BR)
    E.escreve(c, "força ÷ 2?", 84, 580, 190, "g", BR)
    M.line(c, 70, 600, 1000, 440, AMARELO, 1.0, 26)
    E.escreve(c, "é ÷ 4", 84, 820, 190, "g", AMARELO)
    claro = E.mix(COR, BR, 0.82)
    E.bola(c, 1420, 760, 150, "#2F6FB0")
    E.bola(c, 1780, 760, 60, "#A9A9B4")
    F.seta(c, 1580, 760, 1660, 760, BR, 1.0, 14)
    F.seta(c, 1710, 760, 1640, 760, BR, 1.0, 14)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Gravitação", "universal", "do zero")


def d(c):  # o macete: monte o fator
    palco_capa(c)
    E.escreve(c, "gravidade de Marte", 84, 330, 100, "i", BR)
    E.escreve(c, "sem calcular G", 84, 490, 130, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "g × f{1/10}{(1/2)^2} = 4 m/s^2", 84, 800, 130, "g", BR)
    E.bola(c, 1650, 760, 150, "#C4512A")


CAPAS = (("capa_A_distancia_dobrada", a), ("capa_B_gravitacao_universal", b), ("capa_C_sem_calcular_g", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
