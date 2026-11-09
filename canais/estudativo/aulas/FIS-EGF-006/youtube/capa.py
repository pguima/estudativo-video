"""Capas do FIS-EGF-006 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def prensa_capa(c, x1, w1, x2, w2, yb, n1, n2, cor):
    c.drawRect(skia.Rect.MakeLTRB(x1 - w1 / 2, yb - n1, x1 + w1 / 2, yb), M.paint("#E9B44C"))
    c.drawRect(skia.Rect.MakeLTRB(x2 - w2 / 2, yb - n2, x2 + w2 / 2, yb), M.paint("#E9B44C"))
    c.drawRect(skia.Rect.MakeLTRB(x1, yb - 70, x2, yb), M.paint("#E9B44C"))
    p = skia.Path()
    top = yb - 520
    p.moveTo(x1 - w1 / 2, top); p.lineTo(x1 - w1 / 2, yb); p.lineTo(x2 + w2 / 2, yb); p.lineTo(x2 + w2 / 2, top)
    p.moveTo(x1 + w1 / 2, top); p.lineTo(x1 + w1 / 2, yb - 70); p.lineTo(x2 - w2 / 2, yb - 70); p.lineTo(x2 - w2 / 2, top)
    c.drawPath(p, M.paint(cor, 1.0, stroke=8))
    M.rrect(c, x1 - w1 / 2 + 4, yb - n1 - 24, w1 - 8, 24, 4, "#1B1B20")
    M.rrect(c, x2 - w2 / 2 + 4, yb - n2 - 28, w2 - 8, 28, 4, "#1B1B20")


def a(c):  # o gancho: levantar um carro com uma mão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "um carro", 84, 380, 150, "g", BR)
    E.escreve(c, "com a força", 84, 540, 120, "i", BR)
    E.escreve(c, "de um braço", 84, 720, 160, "g", AMARELO)
    prensa_capa(c, 1180, 80, 1600, 380, 960, 380, 260, BR)
    F.bloco(c, 1600, 610, 300, 130, "carro", cor="#1B1B20", size=46)
    F.seta(c, 1180, 330, 1180, 540, AMARELO, 1.0, 16)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Princípio", "de Pascal", "a prensa")


def d(c):  # o macete: diâmetro × 10, área × 100
    palco_capa(c)
    E.escreve(c, "deu o diâmetro?", 84, 330, 110, "i", BR)
    E.escreve(c, "eleve ao quadrado", 84, 490, 120, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "D × 10  →  A × 100", 84, 760, 140, "g", AMARELO)
    E.formula(c, "força × 100", 84, 950, 100, "g", claro)


CAPAS = (("capa_A_um_carro_com_um_braco", a), ("capa_B_principio_de_pascal", b), ("capa_C_eleve_ao_quadrado", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
