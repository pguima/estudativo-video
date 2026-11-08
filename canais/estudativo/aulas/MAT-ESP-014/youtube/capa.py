"""Capas do MAT-ESP-014 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"
SEN = math.sin(math.radians(22))


def bola(c, cx, cy, r, cor=None, equador=True):
    """esfera em traço branco; cor = corpo pintado"""
    if cor:
        c.drawCircle(cx, cy, r, M.paint(cor, 0.9))
    pt = M.paint(BR, 1, stroke=8)
    c.drawCircle(cx, cy, r, pt)
    if equador:
        c.drawArc(skia.Rect.MakeXYWH(cx - r, cy - r * SEN, 2 * r, 2 * r * SEN), 0, 180, False, M.paint(BR, 1, stroke=6))


def circulo(c, cx, cy, r, cheio):
    if cheio:
        c.drawCircle(cx, cy, r, M.paint(AMARELO, 0.95))
    c.drawCircle(cx, cy, r, M.paint(BR, 1, stroke=7))


def a(c):  # o gancho: a casca da laranja cobre 4 círculos
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    bola(c, 330, 560, 220, AMARELO)
    for k in range(4):
        circulo(c, 760 + k * 270, 470, 115, True)
    E.escreve(c, "a casca cobre", 690, 780, 100, "i", BR)
    E.escreve(c, "4 círculos", 680, 960, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Esfera", "área", "e volume")


def d(c):  # o atalho com π = 3
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "esfera com", 84, 330, 96, "i", BR)
    E.formula(c, "π = 3", 84 + E.larg("esfera com", "i", 96) + 30, 330, 96, "g", BR)
    E.formula(c, "V = 4r^3", 80, 580, 180, "g", AMARELO)
    E.formula(c, "A = 12r^2", 84, 820, 150, "g", BR)
    bola(c, 1560, 640, 260, COR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_casca_de_laranja", a), ("capa_B_esfera_area_e_volume", b), ("capa_C_quatro_r_ao_cubo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
