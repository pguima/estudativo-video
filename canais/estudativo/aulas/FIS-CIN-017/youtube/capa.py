"""Capas do FIS-CIN-017 (1280x720). Uso: python capa.py"""
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


def a(c):  # o desafio: 125 m de queda
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "caiu de", 84, 390, 130, "i", BR)
    E.escreve(c, "125 m:", 84, 600, 220, "g", BR)
    E.escreve(c, "quantos segundos?", 84, 800, 110, "i", AMARELO)
    E.escreve(c, "resolva antes de mim", 84, 950, 70, "i", BR)
    x, y0, yb = 1560, 200, 960
    M.line(c, x + 140, y0, x + 140, yb, BR, 0.8, 6, dash=[20, 14])
    for i, h in enumerate((0, 5, 20, 45, 80, 125)):
        y = y0 + h * (yb - y0 - 40) / 125
        E.bola(c, x, y, 34, E.mix(COR, BR, 0.85) if i == 5 else E.mix(COR, BR, 0.45))
    M.line(c, 1400, yb, 1880, yb, BR, 1.0, 6)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "queda", "e lançamentos")


def d(c):  # os três macetes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "3 macetes", 84, 330, 150, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (l1, l2) in enumerate((("gráfico:", "leia o eixo"), ("queda:", "a tabela do 5"), ("lançamento:", "a altura manda"))):
        y = 540 + i * 160
        E.bola(c, 140, y - 34, 50, COR)
        E.centro(c, str(i + 1), 140, y - 10, 64, "g", BR)
        E.escreve(c, l1, 230, y, 80, "g", BR)
        E.escreve(c, l2, 230 + E.larg(l1, "g", 80) + 30, y, 84, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_caiu_de_125_m", a), ("capa_B_praticando_lancamentos", b), ("capa_C_tres_macetes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
