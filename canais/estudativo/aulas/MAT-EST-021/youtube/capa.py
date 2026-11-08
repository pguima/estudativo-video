"""Capas do MAT-EST-021 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF5A5A"


def pizza(c, cx, cy, r, partes, cores):
    """setores na proporção das partes (como o gráfico errado faria)"""
    tot = sum(partes)
    ang = -90.0
    for v, cor in zip(partes, cores):
        varre = 360 * v / tot
        p = skia.Path(); p.moveTo(cx, cy)
        p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ang, varre, False); p.close()
        c.drawPath(p, M.paint(cor)); c.drawPath(p, M.paint(COR, 1, stroke=6))
        m = math.radians(ang + varre / 2)
        E.centro(c, f"{v}%", cx + math.cos(m) * r * 0.6, cy + math.sin(m) * r * 0.6 + 24, 66, "g", COR if cor != COR else BR)
        ang += varre


def a(c):  # o gancho: a pizza de 135%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "essa pizza", 84, 340, 110, "i", BR)
    E.escreve(c, "soma", 84, 540, 150, "g", BR)
    E.escreve(c, "135%", 84, 760, 220, "g", AMARELO)
    pizza(c, 1450, 560, 330, [60, 45, 30], [BR, AMARELO, E.mix(BR, COR, 0.4)])


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Análise", "crítica", "de dados, praticando")


def d(c):  # o atalho: some as fatias
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 340, 110, "i", BR)
    E.escreve(c, "some as", 84, 540, 160, "g", BR)
    E.escreve(c, "fatias", 84, 720, 160, "g", AMARELO)
    E.escreve(c, "passou de 100%? contou 2 vezes", 84, 900, 70, "i", BR)
    pizza(c, 1500, 640, 250, [50, 30, 20], [BR, AMARELO, E.mix(BR, COR, 0.4)])


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_pizza_de_135", a), ("capa_B_analise_critica", b), ("capa_C_some_as_fatias", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
