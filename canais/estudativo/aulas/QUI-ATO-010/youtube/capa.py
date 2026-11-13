"""Capas da QUI-ATO-010 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
AMBAR = "#F2A33A"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def esfera(c, cx, cy, r, s, cor=None):
    E.bola(c, cx, cy, r, cor or E.mix(COR, BR, 0.6))
    Q.formula(c, s, cx, cy + r * 0.2, r * 0.55, E.TINTA, 1, "center")


def a(c):  # o gancho: mais prótons, átomo menor
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "mais prótons,", 84, 380, 140, "g", BR)
    E.escreve(c, "átomo menor?", 84, 560, 140, "g", AMARELO)
    E.escreve(c, "o raio atômico", 84, 720, 90, "i", BR)
    esfera(c, 1400, 660, 220, "Na")
    esfera(c, 1760, 700, 165, "Mg")


def b(c):
    E.capa_modelo(c, "Química", "Raio", "atômico", "do zero")


def d(c):  # o macete: a seta para baixo e para a esquerda
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "uma seta", 84, 400, 130, "i", BR)
    E.escreve(c, "resolve", 84, 580, 170, "g", BR)
    E.escreve(c, "para baixo e para a esquerda", 84, 760, 70, "g", AMBAR)
    for s, (z, per, g) in Q._posicoes().items():
        if g is None:
            continue
        M.rrect(c, 1080 + (g - 1) * 44 + 2, 300 + (per - 1) * 44 + 2, 40, 40, 6, "#4A4E5C", 1)
    M.arrow(c, 1820, 330, 1120, 590, AMBAR, 1, 18, 56)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mais_protons_atomo_menor", a), ("capa_B_raio_atomico", b), ("capa_C_uma_seta_resolve", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
