"""Capas do MAT-NUM-018 (1280x720). Uso: python capa.py"""
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
CLARO = E.mix(COR, BR, 0.5)


def fundo_escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: 4 ou −11?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "−3 + 2 × (−4)", 84, 460, 240, "g", BR)
    E.escreve(c, "4", 84, 830, 320, "g", BR)
    E.escreve(c, "ou", 340, 800, 170, "i", BR)
    E.escreve(c, "−11?", 610, 830, 320, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Expressões", "com inteiros", "sem perder o sinal")


def d(c):  # o atalho: blocos, com sinal colado
    fundo_escuro(c)
    E.escreve(c, "o atalho", 84, 340, 150, "i", BR)
    E.escreve(c, "os blocos", 80, 590, 270, "g", BR)
    E.escreve(c, "sinal colado", 84, 790, 170, "i", BR)
    E.escreve(c, "não corta", 84, 970, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_4_ou_menos_11", a), ("capa_B_expressoes_inteiros", b), ("capa_C_blocos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
