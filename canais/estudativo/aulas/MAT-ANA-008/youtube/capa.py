"""Capas do MAT-ANA-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: o raio não é 9
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "(x − 2)^2 + (y + 1)^2 = 9", 84, 400, 120, "g", BR)
    E.escreve(c, "raio 9?", 84, 680, 230, "g", BR)
    E.risco(c, 70, 700, 900, 520, 1.0, 0.0, AMARELO, 30)
    E.escreve(c, "é 3", 84, 940, 220, "g", AMARELO)
    cx, cy = 1520, 760
    c.drawCircle(cx, cy, 230, M.paint(BR, 1, stroke=14))
    c.drawCircle(cx, cy, 18, M.paint(BR))
    M.line(c, cx, cy, cx + 230, cy, AMARELO, 1, 12)


def b(c):  # o modelo, com a palavra longa menor
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    tom = M.on(COR)
    E.escreve(c, "Equação da", 76, 440, 190, "g", tom)
    E.escreve(c, "circunferência", 76, 640, 175, "g", tom)
    E.escreve(c, "centro e raio de olho", 84, 850, 140, "i", tom)
    E.mais(c, 1700, 860, 150, E.mix(COR, "#FFFFFF", 0.82), sombra=False)


def d(c):  # o atalho: o que zera cada parêntese
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o centro em", 84, 370, 140, "i", BR)
    E.escreve(c, "5 segundos", 76, 570, 190, "g", BR)
    E.formula(c, "(x − 2)  →  2", 84, 780, 120, "g", "#3CC7D3")
    E.formula(c, "(y + 1)  →  −1", 84, 960, 120, "g", "#FFB833")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_raio_nao_e_9", a), ("capa_B_equacao_da_circunferencia", b), ("capa_C_centro_em_5_segundos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
