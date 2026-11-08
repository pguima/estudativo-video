"""Capas do MAT-FIN-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: quanto aplicar hoje para ter R$ 1.210 em 2 anos a 10%?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "quanto aplicar hoje", 84, 330, 120, "g", BR)
    E.escreve(c, "para ter R$ 1.210 em 2 anos, a 10%?", 88, 450, 72, "i", BR)
    E.escreve(c, "R$ 1.210 ÷ 1,21", 84, 700, 150, "g", E.mix(COR, BR, 0.55))
    E.centro(c, "= R$ 1.000", 1280, 940, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Capital", "ou tempo?", "nos juros compostos")


def d(c):  # o atalho: regra do 72
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "quando o dinheiro dobra?", 84, 330, 100, "i", BR)
    E.escreve(c, "a regra do 72", 84, 560, 190, "g", BR)
    E.escreve(c, "72 ÷ 10 =", 84, 790, 150, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "7,2 anos", 84, 980, 180, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quanto_aplicar", a), ("capa_B_capital_tempo", b), ("capa_C_regra_72", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
