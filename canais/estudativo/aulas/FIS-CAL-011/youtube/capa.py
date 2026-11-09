"""Capas do FIS-CAL-011 (1280x720). Uso: python capa.py"""
import subprocess, sys
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


def cilindro(c, x, y, w, h, frac, cor_gas, linha):
    ye = y + h * (1 - frac)
    M.rrect(c, x + 10, ye, w - 20, y + h - ye - 10, 8, cor_gas, 1.0)
    M.rrect(c, x + 10, ye - 60, w - 20, 60, 10, linha, 1.0)
    M.rrect(c, x + w / 2 - 16, ye - 260, 32, 200, 8, linha, 1.0)
    p = skia.Path()
    p.moveTo(x, y - 40); p.lineTo(x, y + h); p.lineTo(x + w, y + h); p.lineTo(x + w, y - 40)
    c.drawPath(p, M.paint(linha, 1.0, stroke=12))


def a(c):  # o erro: pascal vezes litro
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Pa × L", 84, 420, 200, "g", BR)
    E.escreve(c, "= 300.000 J?", 84, 640, 150, "g", BR)
    E.risco(c, 70, 680, 1080, 520, 9, 0, AMARELO, 30)
    E.escreve(c, "o erro de mil vezes", 84, 880, 92, "i", BR)
    cilindro(c, 1400, 300, 360, 560, 0.55, E.mix(COR, BR, 0.75), BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Trabalho", "de um gás", "no gráfico p × V")


def d(c):  # o macete: kPa × L = J
    palco_capa(c)
    E.escreve(c, "o atalho", 84, 360, 110, "i", BR)
    E.formula(c, "kPa × L = J", 84, 620, 230, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "sem converter nada", 84, 860, 110, "i", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_pascal_vezes_litro", a), ("capa_B_trabalho_de_um_gas", b), ("capa_C_kpa_vezes_litro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
