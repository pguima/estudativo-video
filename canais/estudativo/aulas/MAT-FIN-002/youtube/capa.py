"""Capas do MAT-FIN-002 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a 5% ao mês, dobra em 40 meses? não, em 20
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5% ao mês", 84, 330, 150, "g", BR)
    E.escreve(c, "dobra em", 88, 470, 110, "i", BR)
    E.escreve(c, "40 meses?", 84, 760, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 790, 1160, 580, 9, 0, AMARELO, 30)
    E.escreve(c, "não!", 1330, 600, 120, "i", BR)
    E.centro(c, "20 meses", 1430, 975, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Capital, taxa", "ou tempo?", "isole a letra que falta")


def d(c):  # o atalho para dobrar
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "para dobrar", 84, 340, 140, "i", BR)
    E.escreve(c, "100 ÷ taxa", 84, 580, 220, "g", BR)
    E.escreve(c, "100 ÷ 5 =", 84, 860, 170, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "20 meses", 900, 860, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_40", a), ("capa_B_capital_taxa_tempo", b), ("capa_C_atalho_100", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
