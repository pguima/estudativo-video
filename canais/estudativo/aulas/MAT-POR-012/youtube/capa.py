"""Capas do MAT-POR-012 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: de 8% para 10%, subiu 2% ou 25%?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "de 8% para 10%", 84, 400, 160, "g", BR)
    E.escreve(c, "subiu", 84, 590, 120, "i", BR)
    x = 84 + E.larg("subiu", "i", 120) + 40
    E.escreve(c, "2%", x, 600, 200, "g", E.mix(COR, BR, 0.55))
    x2 = x + E.larg("2%", "g", 200) + 40
    E.escreve(c, "ou", x2, 590, 120, "i", BR)
    E.escreve(c, "25%?", x2 + E.larg("ou", "i", 120) + 40, 600, 200, "g", AMARELO)
    E.escreve(c, "um jornal errou", 84, 900, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Ponto", "percentual", "e porcentagem de %")


def d(c):  # o atalho: 30% de 40% = 12%
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    CL = E.mix(COR, BR, 0.55)
    E.escreve(c, "% de %: o atalho", 84, 340, 130, "i", BR)
    E.escreve(c, "30% de 40%", 76, 580, 200, "g", BR)
    E.escreve(c, "30 × 40 ÷ 100 = 12%", 84, 840, 130, "g", CL)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_2_ou_25", a), ("capa_B_ponto_percentual", b), ("capa_C_porcentagem_de_porcentagem", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
