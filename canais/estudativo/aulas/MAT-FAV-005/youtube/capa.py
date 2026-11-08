"""Capas do MAT-FAV-005 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def curva(c, cx, cy, k, cor, lw=16):
    """y = x² de −3 a 3, com o fundo em (cx, cy); k = px por unidade de x (y em k/3)"""
    pts = [(cx + k * x / 20, cy - k / 3 * (x / 20) ** 2) for x in range(-60, 61)]
    p = skia.Path(); p.moveTo(*pts[0])
    for q in pts[1:]:
        p.lineTo(*q)
    c.drawPath(p, M.paint(cor, 1, stroke=lw, cap_round=True))


def a(c):  # o gancho: 2 ou −2?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "?² = 4", 84, 420, 200, "g", BR)
    E.escreve(c, "2 ou −2?", 84, 640, 170, "g", AMARELO)
    E.escreve(c, "sem inversa", 84, 840, 120, "i", BR)
    curva(c, 1450, 900, 150, BR)
    M.line(c, 1150, 900 - 150 / 3 * 4, 1760, 900 - 150 / 3 * 4, AMARELO, 1, 8)
    for x in (-2, 2):
        c.drawCircle(1450 + 150 * x, 900 - 150 / 3 * 4, 22, M.paint(AMARELO))


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Função", "bijetora", "e a inversa")


def d(c):  # o atalho: a reta horizontal
    palco(c)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "reta", 84, 400, 170, "g", BR)
    E.escreve(c, "horizontal", 84, 580, 170, "g", BR)
    E.escreve(c, "corta 2 vezes: sem inversa", 84, 800, 90, "i", AMARELO)
    curva(c, 1480, 920, 130, BR)
    y = 920 - 130 / 3 * 4
    M.line(c, 1150, y, 1800, y, AMARELO, 1, 8, dash=[26, 18])
    for x in (-2, 2):
        c.drawCircle(1480 + 130 * x, y, 22, M.paint(AMARELO))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_2_ou_menos_2", a), ("capa_B_funcao_bijetora", b), ("capa_C_reta_horizontal", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
