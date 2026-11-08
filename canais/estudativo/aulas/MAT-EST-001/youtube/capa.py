"""Capas do MAT-EST-001 (1280x720). Uso: python capa.py"""
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


def grade(c, x, y, cols, lins, passo, r, amostra):
    for j in range(lins):
        for i in range(cols):
            cx, cy = x + i * passo, y + j * passo
            if amostra(i, j):
                c.drawCircle(cx, cy, r, M.paint(AMARELO))
                c.drawCircle(cx, cy, r + 8, M.paint(BR, 1, stroke=5))
            else:
                c.drawCircle(cx, cy, r, M.paint(BR, 0.35))


def a(c):  # o gancho: uma colher basta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "uma colher", 84, 380, 150, "g", BR)
    E.escreve(c, "basta?", 84, 560, 170, "g", AMARELO)
    E.escreve(c, "censo ou amostra", 84, 800, 100, "i", BR)
    grade(c, 1150, 300, 7, 7, 100, 30, lambda i, j: (i * 5 + j * 3) % 7 == 0)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "População", "e amostra", "e os tipos de variável")


def d(c):  # o atalho: a mesma % de cada grupo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "amostra proporcional", 84, 340, 110, "i", BR)
    E.escreve(c, "80 de 1.000", 84, 580, 170, "g", BR)
    E.escreve(c, "= 8%", 84, 820, 220, "g", AMARELO)
    E.escreve(c, "de cada grupo", 680, 820, 110, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_uma_colher_basta", a), ("capa_B_populacao_e_amostra", b), ("capa_C_mesma_porcentagem", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
