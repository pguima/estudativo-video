"""Capas do MAT-POR-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5 situações de compra e venda
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5", 84, 560, 400, "g", AMARELO)
    E.escreve(c, "situações", 380, 400, 150, "g", BR)
    E.escreve(c, "de compra", 380, 560, 150, "g", BR)
    E.escreve(c, "e venda", 84, 760, 150, "g", BR)
    E.escreve(c, "você resolve antes da resposta", 84, 960, 96, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "porcentagem", "aumentos e lucro")


def d(c):  # o atalho: 10% + 5%
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    CL = E.mix(COR, BR, 0.55)
    E.escreve(c, "15% de cabeça", 84, 340, 140, "i", BR)
    E.escreve(c, "10% + 5%", 76, 600, 230, "g", BR)
    E.escreve(c, "240 + 120 = 360", 84, 860, 140, "g", CL)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_5_situacoes", a), ("capa_B_praticando", b), ("capa_C_10_mais_5", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
