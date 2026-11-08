"""Capas do MAT-TOP-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5 situações
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "5 questões", 84, 420, 200, "g", BR)
    E.escreve(c, "de contagem", 84, 600, 160, "g", AMARELO)
    E.escreve(c, "binômio · chance · pombos", 90, 800, 80, "i", BR)
    E.escreve(c, "conjuntos · repetição", 90, 910, 80, "i", BR)
    E.bola(c, 1580, 520, 250, AMARELO); E.centro(c, "?", 1580, 640, 340, "g", COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Praticando", "contagem", "binômio e chance")


def d(c):  # a casquinha: 15
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2 bolas, 5 sabores,", 84, 360, 120, "i", BR)
    E.escreve(c, "pode repetir:", 84, 500, 120, "i", BR)
    E.escreve(c, "15 casquinhas", 76, 720, 190, "g", AMARELO)
    xs = [200 + i * 160 for i in range(6)]
    for i, x in enumerate(xs):
        if i in (1, 4):
            c.drawCircle(x, 900, 46, M.paint(BR))
        else:
            M.line(c, x, 840, x, 960, BR, 1, 12)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_5_questoes", a), ("capa_B_praticando_contagem", b), ("capa_C_casquinhas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
