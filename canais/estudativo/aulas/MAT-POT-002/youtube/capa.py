"""Capas do MAT-POT-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: um par de parênteses troca o sinal
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "(−3)^2 = 9", 84, 500, 240, cor=BR)
    E.formula(c, "−3^2 = −9", 84, 780, 240, cor=AMARELO)
    E.escreve(c, "por quê?", 1060, 960, 170, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Potência de", "negativo", "fração e decimal")


def d(c):  # o macete: olhe o expoente
    escuro(c)
    E.escreve(c, "olhe", 84, 370, 170, "i", BR)
    E.escreve(c, "o expoente", 84, 560, 170, "g", BR)
    w = E.formula(c, "(−1)^{25} =", 84, 880, 230, cor=BR)
    E.formula(c, "−1", 84 + w + 36, 880, 240, cor=AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nove_ou_menos_nove", a), ("capa_B_negativo_fracao_decimal", b), ("capa_C_olhe_o_expoente", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
