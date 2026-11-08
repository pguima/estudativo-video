"""Capas do MAT-ANA-011 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a origem está dentro ou fora?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "(x − 4)^2 + (y + 3)^2 = 49", 84, 400, 110, "g", BR)
    E.escreve(c, "a origem está", 84, 620, 150, "g", BR)
    E.escreve(c, "dentro ou fora?", 84, 820, 150, "g", AMARELO)
    cx, cy, r = 1560, 700, 250
    c.drawCircle(cx, cy, r, M.paint(BR, 1, stroke=14))
    ox, oy = cx - 4 * r / 7, cy - 3 * r / 7
    c.drawCircle(ox, oy, 22, M.paint(AMARELO))
    c.drawCircle(cx, cy, 14, M.paint(BR))


def b(c):  # o modelo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    tom = M.on(COR)
    E.escreve(c, "Circunferência", 76, 440, 175, "g", tom)
    E.escreve(c, "no plano", 76, 640, 175, "g", tom)
    E.escreve(c, "praticando em 4 situações", 84, 850, 120, "i", tom)
    E.mais(c, 1700, 880, 140, E.mix(COR, "#FFFFFF", 0.82), sombra=False)


def d(c):  # o atalho: pare antes da raiz
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "pare antes", 84, 370, 140, "i", BR)
    E.escreve(c, "da raiz", 76, 570, 190, "g", BR)
    E.formula(c, "3^2 + 4^2 = 25", 84, 780, 110, "g", E.mix(COR, BR, 0.6))
    E.formula(c, "… = 25", 84, 950, 130, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_origem_dentro_ou_fora", a), ("capa_B_circunferencia_no_plano", b), ("capa_C_pare_antes_da_raiz", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
