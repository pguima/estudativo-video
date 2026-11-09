"""Capas do FIS-OND-005 (1280x720). Uso: python capa.py"""
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


def onda(c, x0, x1, y, A, lam, cor, larg=10):
    pts = [(x0 + (x1 - x0) * i / 200, y - A * math.sin(2 * math.pi * (x1 - x0) * i / 200 / lam)) for i in range(201)]
    F.poli(c, pts, 1.0, cor, 1.0, larg)


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho: conta ou nome do fenômeno?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "conta ou", 84, 420, 170, "g", BR)
    E.escreve(c, "fenômeno?", 84, 610, 170, "g", BR)
    E.escreve(c, "5 questões de ondas", 84, 860, 100, "i", BR)
    onda(c, 1180, 1830, 330, 80, 260, AMARELO)
    E.formula(c, "v = λ · f", 1250, 640, 130, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "ondas", "5 questões")


def d(c):  # o macete: o que a onda fez?
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o que a onda fez?", 84, 330, 130, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (p, r) in enumerate((("voltou", "reflexão"), ("trocou de meio", "refração"), ("contornou", "difração"))):
        y = 520 + i * 170
        E.escreve(c, p, 84, y, 90, "g", claro)
        F.seta(c, 900, y - 30, 1060, y - 30, claro, 1.0, 12)
        E.escreve(c, r, 1110, y, 100, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_conta_ou_fenomeno", a), ("capa_B_praticando_ondas", b), ("capa_C_o_que_a_onda_fez", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
