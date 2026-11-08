"""Capas do MAT-ANA-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: onde está o centro?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "x^2 + y^2 − 4x + 2y − 4 = 0", 84, 410, 112, "g", BR)
    E.escreve(c, "onde está", 84, 640, 190, "g", BR)
    E.escreve(c, "o centro?", 84, 850, 190, "g", AMARELO)
    cx, cy = 1600, 760
    c.drawCircle(cx, cy, 200, M.paint(BR, 1, stroke=14))
    E.centro(c, "?", cx, cy + 90, 260, "g", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Completar", "quadrados", "centro e raio")


def d(c):  # o atalho: centro direto da equação aberta
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o centro", 84, 370, 140, "i", BR)
    E.escreve(c, "sem conta", 76, 570, 190, "g", BR)
    E.formula(c, "−4x  →  x = 2", 84, 780, 120, "g", "#3CC7D3")
    E.formula(c, "+2y  →  y = −1", 84, 960, 120, "g", "#FFB833")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_onde_esta_o_centro", a), ("capa_B_completar_quadrados", b), ("capa_C_centro_sem_conta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
