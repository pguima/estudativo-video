"""Capas do MAT-EQU-001 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: x = 5, quanto vale 2x? 25 é o erro
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "se x = 5,", 84, 360, 150, "i", BR)
    E.escreve(c, "2x =", 84, 680, 300, "g", BR)
    E.escreve(c, "25", 820, 680, 300, "g", BR)
    E.risco(c, 790, 720, 1290, 420, 9, 0, AMARELO, 34)
    E.escreve(c, "10", 1380, 680, 300, "g", AMARELO)
    E.escreve(c, "a letra no lugar de um número", 84, 960, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "O que é", "o x?", "na matemática")


def d(c):  # o atalho: o teste do 10
    palco(c)
    E.escreve(c, "o atalho", 84, 340, 150, "i", BR)
    E.escreve(c, "teste do 10", 76, 580, 230, "g", BR)
    E.formula(c, "2x + 3 → 2 × 10 + 3 = 23", 84, 860, 130, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_2x_nao_e_25", a), ("capa_B_letra_no_lugar", b), ("capa_C_teste_do_10", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
