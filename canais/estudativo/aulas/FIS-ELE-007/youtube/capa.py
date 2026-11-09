"""Capas do FIS-ELE-007 (1280x720). Uso: python capa.py"""
import subprocess, sys
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: qual fórmula usar?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "qual fórmula", 84, 380, 170, "g", BR)
    E.escreve(c, "usar?", 84, 580, 200, "g", BR)
    E.escreve(c, "5 questões de eletrostática", 84, 840, 90, "i", BR)
    claro = E.mix(COR, BR, 0.85)
    for i, (s, x, y) in enumerate((("Q = n · e", 1520, 330), ("E = f{F}{q}", 1640, 540), ("τ = q · U", 1420, 720), ("C = f{Q}{U}", 1640, 920))):
        E.formula(c, s, x, y, 100, "g", claro, 1.0, "center")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "cargas", "em 5 questões")


def d(c):  # o macete: o que a questão pede
    palco(c)
    E.escreve(c, "o método", 84, 340, 110, "i", BR)
    E.escreve(c, "1. o que pede?", 84, 560, 140, "g", BR)
    E.escreve(c, "2. fórmula + dados", 84, 760, 140, "g", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_formula_usar", a), ("capa_B_praticando_eletrostatica", b), ("capa_C_o_metodo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
