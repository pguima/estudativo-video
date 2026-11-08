"""Capas do MAT-FIN-013 (1280x720). Uso: python capa.py"""
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



def a(c):  # o gancho: o imposto não come o capital
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "R$ 10.000 → R$ 11.000", 84, 360, 110, "g", BR)
    E.escreve(c, "imposto de 15%", 84, 500, 100, "i", BR)
    E.escreve(c, "R$ 9.350?", 84, 740, 160, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 770, 860, 600, 9, 0, AMARELO, 30)
    E.escreve(c, "você leva", 980, 700, 100, "i", BR)
    E.escreve(c, "R$ 10.850", 900, 930, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Rendimento", "líquido", "o imposto certo")


def d(c):  # o atalho: tire 10% e mais 5% da taxa
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 320, 120, "i", BR)
    E.escreve(c, "12% − 1,2 − 0,6", 84, 540, 160, "g", BR)
    E.escreve(c, "= 10,2%", 84, 760, 190, "g", AMARELO)
    E.escreve(c, "líquidos", 84, 900, 110, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_imposto_capital", a), ("capa_B_rendimento_liquido", b), ("capa_C_atalho_taxa", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
