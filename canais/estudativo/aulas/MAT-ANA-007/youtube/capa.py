"""Capas do MAT-ANA-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: as duas retas da situação 3 se cruzam?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    k, x0, y0 = 70, 1390, 860  # px por unidade; (0, 0) do plano
    P = lambda x, y: (x0 + x * k, y0 - y * k)
    M.arrow(c, 1250, y0, 1840, y0, BR, 0.7, 6, 22, 1.0)
    M.arrow(c, x0, 1060, x0, 160, BR, 0.7, 6, 22, 1.0)
    M.line(c, *P(-0.2, -2.6), *P(3.1, 7.3), BR, 1, 12)
    M.line(c, *P(-1.6, -2.3), *P(1.6, 7.3), AMARELO, 1, 12)
    E.escreve(c, "y = 3x − 2", 84, 380, 110, "g", BR)
    E.escreve(c, "6x − 2y + 5 = 0", 84, 520, 110, "g", AMARELO)
    E.escreve(c, "se cruzam?", 76, 790, 200, "g", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Pontos", "e retas", "em 4 situações")


def d(c):  # o atalho: m da equação geral sem isolar o y
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o m sem", 84, 370, 140, "i", BR)
    E.escreve(c, "isolar o y", 76, 570, 190, "g", BR)
    E.formula(c, "6x − 2y + 5 = 0", 84, 760, 110, "g", E.mix(COR, BR, 0.6))
    E.formula(c, "m = −f{6}{−2} = 3", 84, 960, 130, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_se_cruzam", a), ("capa_B_pontos_e_retas", b), ("capa_C_m_sem_isolar", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
