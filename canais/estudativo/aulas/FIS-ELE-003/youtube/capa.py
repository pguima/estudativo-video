"""Capas do FIS-ELE-003 (1280x720). Uso: python capa.py"""
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
    E.capa_rotulo(c, "Física", COR)


def carga_radial(c, cx, cy, r, cor, sinal_cor):
    for i in range(12):
        g = 2 * math.pi * i / 12
        F.seta(c, cx + math.cos(g) * r * 1.3, cy + math.sin(g) * r * 1.3, cx + math.cos(g) * r * 3.1, cy + math.sin(g) * r * 3.1, cor, 1.0, 10)
    c.drawCircle(cx, cy, r, M.paint(BR))
    k = r * 0.5
    M.line(c, cx - k, cy, cx + k, cy, sinal_cor, 1, r * 0.22)
    M.line(c, cx, cy - k, cx, cy + k, sinal_cor, 1, r * 0.22)


def a(c):  # o erro: o campo depende da carga de teste?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o campo depende", 84, 360, 120, "i", BR)
    E.escreve(c, "do q?", 84, 590, 220, "g", BR)
    E.risco(c, 70, 610, 640, 430, 9, 0, AMARELO, 30)
    E.escreve(c, "não: E = kQ/d²", 84, 860, 120, "g", BR)
    carga_radial(c, 1460, 520, 90, E.mix(COR, BR, 0.75), COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Campo", "elétrico", "e linhas de força")


def d(c):  # o macete: linhas juntas, campo forte
    palco(c)
    E.escreve(c, "leia as linhas", 84, 340, 120, "i", BR)
    E.escreve(c, "juntas = forte", 84, 560, 160, "g", BR)
    E.escreve(c, "da + para a −", 84, 760, 130, "g", E.mix(COR, BR, 0.5))
    claro = E.mix(COR, BR, 0.5)
    for i in range(6):
        y = 300 + i * 110
        F.seta(c, 1380, y, 1800, y, claro, 1.0, 8)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_campo_depende_do_q", a), ("capa_B_campo_eletrico", b), ("capa_C_leia_as_linhas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
