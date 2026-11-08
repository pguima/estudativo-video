"""Capas do MAT-EST-007 (1280x720). Uso: python capa.py"""
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
VERMELHO = "#FF5A5A"


def barras(c, x, y, w, h, vals, vmax, destaque=1, grade=2, cor=BR):
    """barras brancas com a grade de 2 em 2; a do destaque em amarelo"""
    n = len(vals)
    for v in range(grade, vmax + 1, grade):
        yy = y + h - v / vmax * h
        M.line(c, x, yy, x + w, yy, cor, 0.25, 3)
    M.line(c, x, y + h, x + w, y + h, cor, 1, 6)
    for i, v in enumerate(vals):
        bw = w / n * 0.62
        cx = x + w * (i + 0.5) / n
        top = y + h - v / vmax * h
        M.rrect(c, cx - bw / 2, top, bw, y + h - top, 10, AMARELO if i == destaque else cor, 1)


def a(c):  # o gancho: 6 linhas não são 6 pessoas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    barras(c, 1060, 250, 760, 580, [20, 12, 10, 8], 20)
    E.escreve(c, "6 linhas =", 84, 360, 110, "i", BR)
    E.escreve(c, "6 pessoas?", 84, 540, 130, "g", VERMELHO)
    E.escreve(c, "são 12", 84, 740, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando:", "tabelas e", "gráficos")


def d(c):  # o ângulo: o total vira 100
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "total 50?", 84, 360, 110, "i", BR)
    E.escreve(c, "vezes 2", 84, 560, 150, "g", BR)
    E.escreve(c, "vira 100", 84, 760, 170, "g", AMARELO)
    E.centro(c, "12 · 2 = 24%", 1450, 560, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_6_linhas_12_pessoas", a), ("capa_B_praticando_tabelas_graficos", b), ("capa_C_total_vira_100", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
