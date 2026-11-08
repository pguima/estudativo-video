"""Capas do MAT-ANA-010 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: corta, encosta ou passa longe?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "corta,", 84, 420, 170, "g", BR)
    E.escreve(c, "encosta", 84, 600, 170, "g", BR)
    E.escreve(c, "ou passa longe?", 84, 790, 140, "i", BR)
    E.escreve(c, "uma conta responde", 84, 960, 90, "i", AMARELO)
    cx, cy, r = 1560, 600, 230
    c.drawCircle(cx, cy, r, M.paint(BR, 1, stroke=14))
    M.line(c, cx - 330, cy - r, cx + 330, cy - r, AMARELO, 1, 10)
    M.line(c, cx - 330, cy + 200, cx + 300, cy - 260, AMARELO, 0.75, 8)


def b(c):  # o modelo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    tom = M.on(COR)
    E.escreve(c, "Ponto, reta e", 76, 440, 175, "g", tom)
    E.escreve(c, "circunferência", 76, 640, 175, "g", tom)
    E.escreve(c, "posições relativas", 84, 850, 140, "i", tom)
    E.mais(c, 1700, 880, 140, E.mix(COR, "#FFFFFF", 0.82), sombra=False)


def d(c):  # o atalho: a distância se lê no plano
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "tangente", 84, 370, 140, "i", BR)
    E.escreve(c, "sem conta", 76, 570, 190, "g", BR)
    E.formula(c, "x^2 + y^2 = 25  e  y = 5", 84, 780, 90, "g", E.mix(COR, BR, 0.6))
    E.formula(c, "d = 5 = raio", 84, 950, 130, "g", AMARELO)
    cx, cy, r = 1560, 640, 200
    c.drawCircle(cx, cy, r, M.paint("#3CC7D3", 1, stroke=10))
    M.line(c, cx - 300, cy - r, cx + 300, cy - r, BR, 1, 8)
    M.line(c, cx, cy, cx, cy - r, "#FFB833", 1, 10)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_corta_ou_encosta", a), ("capa_B_posicoes_relativas", b), ("capa_C_tangente_sem_conta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
