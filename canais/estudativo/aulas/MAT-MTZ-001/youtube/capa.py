"""Capas do MAT-MTZ-001 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a₂₁ não é 5
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    G = E.matriz(c, 9, 0, [[1, 5], [3, 2]], 1450, 560, 230, cor=BR, escuro=True)
    E.matriz_marca(c, G, 1, 0, AMARELO, 1, 1, cheia=0.0)
    E.formula(c, "a₂₁ = 5?", 84, 560, 230, "g", BR)
    E.risco(c, 560, 600, 980, 380, 9, 0, AMARELO, 34)
    E.escreve(c, "linha ou coluna primeiro?", 84, 860, 100, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Matrizes", "do zero", "sem mistério")


def d(c):  # o atalho: transposta sem montar
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "transposta", 84, 380, 150, "i", BR)
    E.escreve(c, "sem montar", 76, 590, 200, "g", BR)
    E.formula(c, "A^t = A", 84, 860, 190, "g", E.mix(COR, BR, 0.6))
    G = E.matriz(c, 9, 0, [[2, 3], [3, 4]], 1580, 800, 150, cor=BR, escuro=True)
    M.line(c, G.x[0] - 80, G.y[0] - 80, G.x[1] + 80, G.y[1] + 80, AMARELO, 1, 8, dash=[18, 12])


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_linha_ou_coluna", a), ("capa_B_matrizes_do_zero", b), ("capa_C_transposta_sem_montar", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
