"""Capas do MAT-ARE-006 (1280x720). Uso: python capa.py"""
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


def ret(c, x, y, w, h, cor, alfa, borda, larg=8):
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(cor, alfa))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(borda, 1, stroke=larg))


def a(c):  # o gancho: mesma cerca, áreas diferentes
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    k, yb = 24, 860
    for x0, bb, hh, area, cor in ((100, 19, 1, "19", BR), (620, 15, 5, "75", BR), (1080, 10, 10, "?", AMARELO)):
        ret(c, x0, yb - hh * k, bb * k, hh * k, cor, 0.25, cor)
        E.centro(c, area, x0 + bb * k / 2, yb - hh * k - 30, 110, "g", cor)
    E.escreve(c, "40 m de cerca", 100, 360, 140, "g", BR)
    E.escreve(c, "qual a maior área?", 110, 500, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Maior área", "com a cerca", "sem chutar")


def d(c):  # o atalho: o quadrado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    ret(c, 1300, 360, 440, 440, claro, 0.3, BR, 10)
    E.centro(c, "10 × 10", 1520, 620, 100, "g", BR)
    E.escreve(c, "o atalho", 110, 360, 130, "i", BR)
    E.escreve(c, "a resposta", 100, 560, 140, "g", BR)
    E.escreve(c, "é o quadrado", 100, 720, 140, "g", claro)
    E.formula(c, "lado = f{40}{4} = 10", 110, 930, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mesma_cerca", a), ("capa_B_maior_area", b), ("capa_C_o_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
