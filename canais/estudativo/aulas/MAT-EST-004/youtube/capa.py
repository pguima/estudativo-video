"""Capas do MAT-EST-004 (1280x720). Uso: python capa.py"""
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


def fatia(c, cx, cy, r, ini, varre, cor, borda=None, lw=8):
    p = skia.Path()
    p.moveTo(cx, cy)
    p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), ini, varre, False)
    p.close()
    c.drawPath(p, M.paint(cor))
    if borda:
        c.drawPath(p, M.paint(borda, 1, stroke=lw))


def pizza(c, cx, cy, r, fundo):
    """a pizza com a fatia de 25% em amarelo e o quadradinho de 90°"""
    c.drawCircle(cx, cy, r, M.paint(BR, 0.22))
    fatia(c, cx, cy, r, -90, 90, AMARELO, fundo, 10)
    s = r * 0.18
    M.line(c, cx, cy - s, cx + s, cy - s, fundo, 1, 8)
    M.line(c, cx + s, cy - s, cx + s, cy, fundo, 1, 8)


def a(c):  # o gancho: 25% não são 25°
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    pizza(c, 1380, 560, 330, COR)
    fatia(c, 1380, 560, 330, 160, 25, VERMELHO, COR, 6)
    E.escreve(c, "fatia de 25%", 84, 360, 110, "i", BR)
    E.escreve(c, "não é 25°", 84, 560, 140, "g", BR)
    E.escreve(c, "é 90°", 84, 760, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Gráfico de", "setores", "porcentagem e ângulo")


def d(c):  # o atalho: 10% = 36°
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho:", 84, 360, 110, "i", BR)
    E.escreve(c, "10% =", 84, 580, 190, "g", BR)
    E.escreve(c, "36°", 84, 800, 220, "g", AMARELO)
    cx, cy, r = 1420, 560, 330
    c.drawCircle(cx, cy, r, M.paint("#1B1B2B"))
    fatia(c, cx, cy, r, -90, 36, AMARELO)
    for i in range(10):
        g = math.radians(-90 + 36 * i)
        M.line(c, cx, cy, cx + math.cos(g) * r, cy + math.sin(g) * r, BR, 0.7, 4)
    c.drawCircle(cx, cy, r, M.paint(BR, 1, stroke=6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_25_por_cento_e_90_graus", a), ("capa_B_grafico_de_setores", b), ("capa_C_10_por_cento_36_graus", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
