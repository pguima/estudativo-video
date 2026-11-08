"""Capas do MAT-CNT-012 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
VERM = "#D94B3D"
COR = E.MATERIAS["Matemática"]["cor"]
PINTAS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
          5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}


def dado(c, cx, cy, s, n, fundo=BR, pinta=None):
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - s / 2, cy - s / 2, s, s), s * 0.2, s * 0.2), M.paint(fundo))
    for dx, dy in PINTAS[n]:
        c.drawCircle(cx + dx * s * 0.27, cy + dy * s * 0.27, s * 0.09, M.paint(pinta or ("#111111" if fundo == BR else BR)))


def a(c):  # o gancho: 1/11 riscado, é 1/6
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    dado(c, 230, 380, 230, 3)
    dado(c, 500, 380, 230, 4, VERM)
    E.escreve(c, "soma 7?", 700, 440, 170, "g", BR)
    y = 820
    E.fracao(c, 1, 11, 260, y, 170, BR)
    E.risco(c, 140, 960, 400, 680, 9, 0, AMARELO, 30)
    E.escreve(c, "é", 560, y + 50, 150, "i", BR)
    E.bola(c, 1000, 800, 230, "#FFFFFF")
    E.fracao(c, 1, 6, 1000, 790, 180, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Probabilidade", "e contagem", "dois dados e sorteios")


def d(c):  # o macete: vagas sobre pessoas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "chance de ser sorteado?", 84, 370, 110, "i", BR)
    E.fracao(c, "vagas", "pessoas", 500, 640, 170, BR)
    E.escreve(c, "3 em 8:", 1000, 610, 120, "i", BR)
    E.fracao(c, 3, 8, 1480, 600, 200, AMARELO)
    E.escreve(c, "sem combinação", 84, 1000, 110, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_soma_7", a), ("capa_B_prob_contagem", b), ("capa_C_vagas_pessoas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
