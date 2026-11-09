"""Capas do FIS-OND-006 (1280x720). Uso: python capa.py"""
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


def onda(c, x0, x1, y, A, lam, cor, larg=10):
    pts = [(x0 + (x1 - x0) * i / 300, y - A * math.sin(2 * math.pi * (x1 - x0) * i / 300 / lam)) for i in range(301)]
    F.poli(c, pts, 1.0, cor, 1.0, larg)


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho: som alto é som agudo
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "som alto", 84, 420, 170, "g", BR)
    E.escreve(c, "= agudo?", 84, 610, 170, "g", AMARELO)
    E.escreve(c, "não é o volume", 84, 860, 110, "i", BR)
    E.escreve(c, "agudo", 1250, 330, 60, "g", BR)
    onda(c, 1250, 1830, 420, 60, 70, AMARELO)
    E.escreve(c, "grave", 1250, 630, 60, "g", BR)
    onda(c, 1250, 1830, 720, 60, 260, BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Som e", "decibéis", "do zero")


def d(c):  # o macete: conte as dezenas de decibéis
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o macete do decibel", 84, 330, 120, "i", BR)
    E.escreve(c, "+10 dB", 84, 600, 230, "g", BR)
    E.escreve(c, "= ×10", 84, 830, 230, "g", E.mix(COR, BR, 0.5))
    E.pilula(c, "60 → 90 dB", 1530, 520, 80, "g", fundo=COR, cor=BR)
    F.seta(c, 1530, 600, 1530, 720, E.mix(COR, BR, 0.5), 1.0, 14)
    E.pilula(c, "×1.000", 1530, 820, 90, "g", fundo=E.CERTO, cor=BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_som_alto_e_agudo", a), ("capa_B_som_e_decibeis", b), ("capa_C_mais_10_db_vezes_10", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
