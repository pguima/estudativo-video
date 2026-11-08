"""Capas do MAT-CNT-011 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]
PINTAS = {2: [(-1, -1), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)],
          1: [(0, 0)], 3: [(-1, -1), (0, 0), (1, 1)], 5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)]}


def dado(c, cx, cy, s, n, pinta=COR):
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.2, s * 0.2), M.paint(BR))
    for dx, dy in PINTAS[n]:
        c.drawCircle(cx + dx * s * 0.27, cy + dy * s * 0.27, s * 0.09, M.paint(pinta))


def fr(c, n, d, cx, cy, size, cor):
    E.fracao(c, n, d, cx, cy, size, cor)


def a(c):  # o gancho: 3/6 = 1/2 = 50%, as três certas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i, n in enumerate((2, 4, 6)):
        dado(c, 180 + i * 230, 360, 190, n)
    E.escreve(c, "chance de par?", 840, 400, 120, "i", BR)
    y = 820
    fr(c, 3, 6, 220, y, 170, BR)
    E.escreve(c, "=", 380, y + 60, 170, "g", BR)
    fr(c, 1, 2, 620, y, 170, BR)
    E.escreve(c, "=", 780, y + 60, 170, "g", BR)
    E.escreve(c, "50%", 960, y + 80, 230, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Probabilidade", "do zero", "a chance em fração")


def d(c):  # o macete: leve o de baixo até 100
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "virar porcentagem?", 84, 370, 120, "i", BR)
    y = 680
    fr(c, 3, 10, 250, y, 190, BR)
    E.escreve(c, "× 10", 430, y + 50, 110, "g", AMARELO)
    fr(c, 30, 100, 880, y, 190, BR)
    E.escreve(c, "= 30%", 1170, y + 70, 200, "g", AMARELO)
    E.escreve(c, "leve o de baixo até 100", 84, 1010, 96, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tres_respostas", a), ("capa_B_probabilidade", b), ("capa_C_ate_100", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
