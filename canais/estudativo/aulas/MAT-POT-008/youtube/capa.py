"""Capas do MAT-POT-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: expoente um meio não é metade
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "9^{1/2}", 84, 590, 340, cor=BR)
    E.escreve(c, "= ?", 760, 570, 300, "g", AMARELO)
    E.escreve(c, "não é 4,5", 84, 920, 200, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Expoente", "em fração", "é raiz disfarçada")


def d(c):  # o macete: o de baixo é a raiz
    palco(c)
    E.escreve(c, "o de baixo", 84, 350, 190, "i", BR)
    E.escreve(c, "é a raiz", 84, 560, 200, "g", AMARELO)
    E.formula(c, "8^{2/3} = 4", 84, 900, 250, cor=BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_metade", a), ("capa_B_expoente_fracionario", b), ("capa_C_de_baixo_e_a_raiz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
