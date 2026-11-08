"""Capas do MAT-FAT-007 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def fra(c, cima, baixo, cx, y, size, cor):
    w = max(E.formula(None, cima, 0, 0, size, a=0), E.formula(None, baixo, 0, 0, size, a=0)) + size * 0.3
    E.formula(c, cima, cx, y - size * 0.32, size, cor=cor, align="center")
    b = size * 0.07
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, y - b / 2, w, b), b / 2, b / 2), M.paint(cor))
    E.formula(c, baixo, cx, y + size * 0.98, size, cor=cor, align="center")
    return w

def a(c):  # o gancho: x² = 49 tem duas respostas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "x^2 = 49", 84, 470, 220, cor=BR)
    E.formula(c, "x = 7", 84, 760, 170, cor=BR)
    E.escreve(c, "e", 570, 750, 130, "i", BR)
    E.formula(c, "x = −7", 690, 760, 170, cor=AMARELO)
    E.escreve(c, "falta metade da resposta", 84, 990, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Equação", "incompleta", "sem fórmula")


def d(c):  # o atalho: sem c, uma raiz é 0 e a outra é −b/a
    palco(c)
    E.escreve(c, "o atalho do", 84, 330, 110, "i", BR)
    E.escreve(c, "c = 0", 640, 330, 120, "g", AMARELO)
    E.formula(c, "3x^2 + 12x = 0", 84, 600, 160, cor=BR)
    E.formula(c, "x = 0  e  x = −4", 84, 840, 160, cor=AMARELO)
    E.escreve(c, "uma raiz é sempre zero", 84, 1000, 80, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_metade_da_resposta", a), ("capa_B_incompleta", b), ("capa_C_atalho_c_zero", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
