"""Capas do MAT-POR-005 (1280x720). Uso: python capa.py"""
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


def caixa(c, s, cx, cy, size, fundo, cor):
    w, h = E.larg(s, "g", size) + size * 1.0, size * 1.6
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 26, 26), M.paint(fundo))
    E.centro(c, s, cx, cy + size * 0.36, size, "g", cor)


def a(c):  # o gancho: de 80 para 100 não é 20%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    caixa(c, "R$ 80", 330, 400, 120, BR, COR)
    M.arrow(c, 570, 400, 760, 400, BR, 1, 10, 30)
    caixa(c, "R$ 100", 1050, 400, 120, BR, COR)
    E.escreve(c, "20%?", 84, 860, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 900, 600, 660, 9, 0, AMARELO, 30)
    E.bola(c, 1480, 780, 230, AMARELO)
    E.centro(c, "25%", 1480, 835, 150, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Variação", "percentual", "subiu ou caiu?")


def d(c):  # o atalho: novo ÷ antigo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "novo ÷ antigo", 76, 540, 190, "g", BR)
    E.escreve(c, "100 ÷ 80 = 1,25", 84, 760, 130, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "+25%", 84, 950, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_20_ou_25", a), ("capa_B_variacao_percentual", b), ("capa_C_novo_sobre_antigo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
