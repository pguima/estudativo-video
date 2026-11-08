"""Capas do MAT-MTZ-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: elemento com elemento
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    s = 130
    E.matriz(c, 9, 0, [[1, 2], [0, 1]], 330, 470, s, cor=BR, escuro=True)
    E.escreve(c, "·", 545, 500, 160, "g", BR)
    E.matriz(c, 9, 0, [[1, 0], [3, 1]], 800, 470, s, cor=BR, escuro=True)
    E.escreve(c, "=", 1010, 515, 160, "g", BR)
    E.matriz(c, 9, 0, [[1, 0], [0, 1]], 1330, 470, s, cor=BR, escuro=True)
    E.risco(c, 1150, 650, 1500, 290, 9, 0, AMARELO, 34)
    E.escreve(c, "não é casa com casa", 84, 900, 120, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Multiplicar", "matrizes", "linha por coluna")


def d(c):  # o atalho do tamanho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o produto existe?", 84, 380, 140, "i", BR)
    E.escreve(c, "olhe o meio", 76, 590, 210, "g", BR)
    x, y, s = 120, 880, 170
    for txt, cor in (("2×", BR), ("3", AMARELO), ("  ·  ", BR), ("3", AMARELO), ("×4", BR)):
        E.escreve(c, txt, x, y, s, "g", cor)
        x += E.larg(txt, "g", s) + 16
    E.escreve(c, "= 2×4", 1260, y, s, "g", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_casa_com_casa", a), ("capa_B_linha_por_coluna", b), ("capa_C_olhe_o_meio", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
