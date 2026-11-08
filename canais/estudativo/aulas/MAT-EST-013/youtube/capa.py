"""Capas do MAT-EST-013 (1280x720). Uso: python capa.py"""
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
SAL = [2.0] * 4 + [2.5] * 3 + [3.0] * 2 + [21.0]


def colunas(c, x, y, w, h, cor=BR, destaque=AMARELO):
    """os dez salários em colunas brancas; a do diretor em amarelo"""
    for i, v in enumerate(SAL):
        bw = w / 10 * 0.62
        cx = x + w * (i + 0.5) / 10
        hh = v / 22 * h
        M.rrect(c, cx - bw / 2, y + h - hh, bw, hh, 8, destaque if i == 9 else cor, 1.0)
    M.line(c, x - 10, y + h, x + w + 10, y + h, cor, 1, 6)


def a(c):  # o gancho: o salário médio engana
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "salário médio", 84, 340, 110, "i", BR)
    E.escreve(c, "R$ 4.250?", 84, 540, 170, "g", AMARELO)
    E.escreve(c, "9 de 10 ganham", 84, 760, 110, "g", BR)
    E.escreve(c, "até R$ 3.000", 84, 900, 110, "g", BR)
    colunas(c, 1150, 300, 640, 640)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Média, mediana", "ou moda?", "qual usar")


def d(c):  # o atalho: compare a média com a mediana
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "média bem acima", 84, 360, 110, "i", BR)
    E.escreve(c, "da mediana?", 84, 530, 140, "g", BR)
    E.escreve(c, "alguém está", 84, 750, 110, "g", AMARELO)
    E.escreve(c, "puxando", 84, 920, 150, "g", AMARELO)
    colunas(c, 1200, 330, 600, 600)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_salario_medio_engana", a), ("capa_B_qual_medida_usar", b), ("capa_C_media_puxada", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
