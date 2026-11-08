"""Capas do MAT-EQU-002 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: 2x² − 3 com x = −2 não dá −11
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "2x^2 − 3", 84, 400, 210, cor=BR)
    E.escreve(c, "com x = −2", 1000, 390, 110, "i", BR)
    E.escreve(c, "−11", 84, 700, 230, "g", BR)
    E.risco(c, 70, 730, 520, 520, 9, 0, AMARELO, 30)
    E.escreve(c, "5", 640, 700, 230, "g", AMARELO)
    E.escreve(c, "faltou um parêntese", 84, 960, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Troque", "a letra", "sem errar o sinal")


def d(c):  # o atalho: expoente par apaga o sinal
    palco(c)
    E.escreve(c, "o atalho", 84, 340, 150, "i", BR)
    E.escreve(c, "expoente par", 76, 560, 190, "g", BR)
    E.escreve(c, "apaga o sinal", 84, 740, 160, "i", BR)
    E.formula(c, "(−2)^2 = 2^2 = 4", 84, 960, 140, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_da_menos_11", a), ("capa_B_troque_a_letra", b), ("capa_C_expoente_par", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
