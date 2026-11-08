"""Capas do MAT-FIN-009 (1280x720). Uso: python capa.py"""
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



def a(c):  # o gancho: 5% e 4% não dão 9%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "inflação", 84, 370, 150, "i", BR)
    E.escreve(c, "5% e 4%", 84, 570, 200, "g", BR)
    E.escreve(c, "= 9%?", 84, 820, 220, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 850, 640, 640, 9, 0, AMARELO, 30)
    E.centro(c, "9,2%", 1430, 820, 240, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Inflação", "acumulada", "e poder de compra")


def d(c):  # o atalho: subiu 1/4, perde 1/5
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 290, 120, "i", BR)
    E.escreve(c, "preço subiu", 84, 460, 90, "i", BR)
    E.fracao(c, 1, 4, 260, 690, 170, BR)
    E.escreve(c, "→", 560, 730, 150, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "você perde", 900, 460, 90, "i", BR)
    E.fracao(c, 1, 5, 1080, 690, 170, AMARELO)
    E.escreve(c, "25% → 20%", 84, 990, 110, "g", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_9", a), ("capa_B_inflacao_acumulada", b), ("capa_C_um_quarto_um_quinto", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
