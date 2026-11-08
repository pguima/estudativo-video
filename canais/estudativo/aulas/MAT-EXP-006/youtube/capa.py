"""Capas do MAT-EXP-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a equação de 3 termos vira 2º grau com um apelido
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "4^x − 6 · 2^x + 8 = 0", 84, 430, 150, "g", BR)
    E.escreve(c, "um apelido e vira", 84, 640, 90, "i", BR)
    E.formula(c, "y^2 − 6y + 8 = 0", 84, 880, 150, "g", AMARELO)
    E.pilula(c, "2ˣ = y", 1600, 620, 70, "g", fundo=AMARELO, cor=COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Troca de", "variável", "equação exponencial")


def d(c):  # o atalho: separe a soma do expoente
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 360, 120, "i", claro)
    E.escreve(c, "separe a soma", 76, 580, 170, "g", BR)
    E.escreve(c, "do expoente", 76, 770, 170, "g", AMARELO)
    E.formula(c, "2^{x+1} = 2 · 2^x", 1060, 980, 100, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_um_apelido", a), ("capa_B_troca_de_variavel", b), ("capa_C_separe_a_soma", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
