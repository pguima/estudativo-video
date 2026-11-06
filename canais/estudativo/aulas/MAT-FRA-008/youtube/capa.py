"""Capas do MAT-FRA-008 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o erro: 1/2 + 1/3 não é 2/5
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.fracao(c, 1, 2, 300, 560, 290, BR)
    E.mais(c, 650, 545, 110, "#FFFFFF", sombra=False)
    E.fracao(c, 1, 3, 1000, 560, 290, BR)
    E.escreve(c, "=", 1190, 640, 240, "g", BR)
    E.fracao(c, 2, 5, 1600, 560, 290, BR)
    E.risco(c, 1400, 860, 1800, 220, 9, 0, "#FFD500", 34)
    E.escreve(c, "por que não dá isso?", 84, 1010, 120, "i", BR)


def b(c):  # o método
    E.capa_modelo(c, "Matemática", "Somar", "frações", "sem errar")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 360, 150, "i", BR)
    E.escreve(c, "borboleta", 76, 590, 240, "g", BR)
    E.fracao(c, 1, 2, 420, 800, 170, BR); E.fracao(c, 1, 3, 860, 800, 170, BR)
    M.line(c, 490, 710, 790, 890, E.mix(COR, BR, 0.5), 1, 10); M.line(c, 490, 890, 790, 710, E.mix(COR, BR, 0.5), 1, 10)
    E.escreve(c, "= 5/6", 1060, 860, 170, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_erro", a), ("capa_B_sem_errar", b), ("capa_C_borboleta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
