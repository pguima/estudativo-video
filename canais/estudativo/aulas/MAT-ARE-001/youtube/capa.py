"""Capas do MAT-ARE-001 (1280x720). Uso: python capa.py"""
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


def cerca(c, pts, cor, larg=22, fecha=True):
    p = skia.Path(); p.addPoly(pts, fecha)
    pt = M.paint(cor, 1, stroke=larg, cap_round=True); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)


def tracej(c, pts, cor, larg=10):
    p = skia.Path(); p.addPoly(pts, False)
    pt = M.paint(cor, 0.8, stroke=larg, cap_round=True); pt.setPathEffect(skia.DashPathEffect.Make([30, 22], 0))
    c.drawPath(p, pt)


def a(c):  # o gancho: 20 + 35 = 55 m de cerca? a cerca parou no meio
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, y, w, h = 120, 330, 760, 440
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), M.paint(BR, 0.16))
    tracej(c, [(x + w, y + h), (x + w, y), (x, y)], BR)
    cerca(c, [(x, y), (x, y + h), (x + w, y + h)], AMARELO, fecha=False)
    E.centro(c, "35 m", x + w / 2, y + h + 130, 100, "g", BR)
    E.escreve(c, "20 m", x + 30, y + h / 2 + 40, 100, "g", BR)
    E.escreve(c, "55 m", 1040, 560, 230, "g", BR)
    E.risco(c, 1020, 600, 1640, 360, 9, 0, AMARELO, 34)
    E.escreve(c, "de cerca?", 1050, 760, 130, "i", BR)
    E.escreve(c, "a cerca não fecha", 1040, 930, 90, "i", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Perímetro", "do zero", "sem errar")


def d(c):  # o atalho do retângulo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    x, y, w, h = 110, 440, 480, 300
    cerca(c, [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], claro, 18)
    E.centro(c, "35", x + w / 2, y + h + 110, 90, "g", BR)
    E.escreve(c, "20", x + w + 40, y + h / 2 + 32, 90, "g", BR)
    E.escreve(c, "o atalho", 860, 380, 130, "i", BR)
    E.escreve(c, "some e dobre", 850, 590, 140, "g", BR)
    E.escreve(c, "(35 + 20) × 2 = 110", 860, 800, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cerca_pela_metade", a), ("capa_B_perimetro", b), ("capa_C_some_e_dobre", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
