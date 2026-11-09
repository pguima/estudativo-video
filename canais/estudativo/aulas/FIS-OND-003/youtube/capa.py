"""Capas do FIS-OND-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o som contorna o muro, a luz não
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Você ouve,", 84, 400, 150, "g", BR)
    E.escreve(c, "mas não vê", 84, 570, 150, "g", BR)
    E.escreve(c, "a onda que contorna", 84, 860, 100, "i", BR)
    yc, mx = 900, 1460
    for r in range(80, 620, 75):  # arcos do som por cima do muro
        c.drawArc(skia.Rect.MakeXYWH(1720 - r, 640 - r, 2 * r, 2 * r), 160, 120, False, M.paint(AMARELO, max(0.25, 1 - r / 700), stroke=9))
    M.rrect(c, mx - 40, yc - 470, 80, 470, 8, "#1B1B1B", 1.0)
    M.line(c, 1080, yc, 1900, yc, BR, 1.0, 8)
    for x, cor in ((1230, BR), (1720, AMARELO)):
        M.rrect(c, x - 30, yc - 170, 60, 110, 25, cor, 1.0)
        c.drawCircle(x, yc - 205, 32, M.paint(cor))
        M.line(c, x - 14, yc - 70, x - 16, yc, cor, 1.0, 18)
        M.line(c, x + 14, yc - 70, x + 16, yc, cor, 1.0, 18)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Reflexão,", "refração", "e difração")


def d(c):  # o macete: a frequência não muda
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a frequência", 84, 380, 140, "g", BR)
    E.escreve(c, "não muda", 84, 560, 170, "g", claro)
    E.pilula(c, "v ×3", 360, 820, 100, "g", fundo=COR, cor=BR)
    F.seta(c, 520, 820, 760, 820, claro, 1.0, 14)
    E.pilula(c, "λ ×3", 930, 820, 100, "g", fundo=E.CERTO, cor=BR)
    E.escreve(c, "reflexão · refração · difração", 84, 1000, 60, "b", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_ouve_mas_nao_ve", a), ("capa_B_reflexao_refracao_difracao", b), ("capa_C_a_frequencia_nao_muda", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
