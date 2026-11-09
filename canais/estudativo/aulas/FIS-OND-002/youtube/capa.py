"""Capas do FIS-OND-002 (1280x720). Uso: python capa.py"""
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


def onda(c, x0, x1, y, A, lam, cor, larg=12):
    n = int((x1 - x0) / 4)
    pts = [(x0 + (x1 - x0) * i / n, y - A * math.sin(2 * math.pi * ((x1 - x0) * i / n) / lam)) for i in range(n + 1)]
    F.poli(c, pts, 1.0, cor, 1.0, larg)


def a(c):  # o erro: amplitude de crista a vale
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Isto é a", 84, 400, 150, "g", BR)
    E.escreve(c, "amplitude?", 84, 570, 150, "g", BR)
    E.escreve(c, "o erro de crista a vale", 84, 860, 90, "i", BR)
    x0, y, A, lam = 1120, 560, 170, 520
    M.line(c, x0 - 20, y, 1860, y, BR, 0.5, 4)
    onda(c, x0, 1860, y, A, lam, BR)
    xc, xv = x0 + lam / 4, x0 + 3 * lam / 4
    M.line(c, xc - 60, y - A, xv + 60, y - A, AMARELO, 1.0, 4)
    M.line(c, xc - 60, y + A, xv + 60, y + A, AMARELO, 1.0, 4)
    F.seta(c, xv + 40, y, xv + 40, y - A, AMARELO, 1.0, 10)
    F.seta(c, xv + 40, y, xv + 40, y + A, AMARELO, 1.0, 10)
    E.risco(c, xv - 40, y + 150, xv + 130, y - 150, 9, 0, AMARELO, 26)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Ondas", "v = λ · f", "do zero")


def d(c):  # o macete: f é da fonte, v é do meio
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "f é da fonte", 84, 380, 150, "g", BR)
    E.escreve(c, "v é do meio", 84, 560, 150, "g", claro)
    onda(c, 100, 1100, 760, 60, 330, claro, 9)
    onda(c, 100, 1100, 930, 60, 165, BR, 9)
    E.pilula(c, "f", 1240, 760, 70, "g", fundo="#3A3A48", cor=BR)
    E.pilula(c, "2f → λ ÷ 2", 1480, 930, 80, "g", fundo=COR, cor=BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_isto_e_a_amplitude", a), ("capa_B_ondas_v_lambda_f", b), ("capa_C_f_da_fonte_v_do_meio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
