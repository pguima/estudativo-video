"""Capas do MAT-RAZ-007 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o erro: mais pintores e mais dias?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "4 pintores", 84, 400, 130, "g", BR)
    E.escreve(c, "9 dias", 1180, 400, 130, "g", BR)
    E.escreve(c, "6 pintores", 84, 640, 130, "g", BR)
    E.escreve(c, "13,5 dias", 1180, 640, 130, "g", BR)
    E.risco(c, 1150, 680, 1820, 520, 9, 0, "#FFD500", 30)
    E.escreve(c, "mais gente, mais dias?", 84, 950, 130, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Regra", "de três", "inversa")


def d(c):  # o atalho: multiplique na linha
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "na inversa,", 84, 350, 140, "i", BR)
    E.escreve(c, "multiplique", 76, 540, 190, "g", BR)
    E.escreve(c, "na linha", 76, 720, 190, "g", BR)
    E.formula(c, "4 · 9 = 6 · x", 84, 950, 150, "g", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mais_gente_mais_dias", a), ("capa_B_regra_de_tres_inversa", b), ("capa_C_multiplique_na_linha", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
