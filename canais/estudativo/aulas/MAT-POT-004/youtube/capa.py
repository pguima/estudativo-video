"""Capas do MAT-POT-004 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: somar ou multiplicar os expoentes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "(2^3)^4 =", 84, 560, 300, cor=BR)
    E.formula(c, "2^7", 1090, 560, 300, cor=AMARELO)
    E.risco(c, 1070, 590, 1480, 300, 9, 0, largura=24)
    E.escreve(c, "soma ou", 84, 790, 170, "i", BR)
    E.escreve(c, "multiplica?", 84, 960, 170, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Potência", "de potência", "e de um produto")


def d(c):  # o macete: pares de 2 e 5
    escuro(c)
    E.escreve(c, "pares de", 84, 370, 170, "i", BR)
    E.escreve(c, "2 e 5", 84, 560, 170, "g", BR)
    w = E.formula(c, "2^4 · 5^3 =", 84, 880, 220, cor=BR)
    E.formula(c, "2.000", 84 + w + 36, 880, 220, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_soma_ou_multiplica", a), ("capa_B_potencia_de_potencia", b), ("capa_C_pares_de_2_e_5", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
