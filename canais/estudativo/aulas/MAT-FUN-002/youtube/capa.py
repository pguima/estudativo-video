"""Capas do MAT-FUN-002 (1280x720). Uso: python capa.py"""
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


def diagrama(c, cxa, cxb, cy, A, B, flechas, cor_ruim, ruim, tinta=BR, size=78, dy=130, rw=130):
    for cx, els in ((cxa, A), (cxb, B)):
        rh = (max(len(A), len(B)) * dy + 60) / 2
        c.drawOval(skia.Rect.MakeXYWH(cx - rw, cy - rh, 2 * rw, 2 * rh), M.paint(tinta, 1, stroke=8))
    pa = {v: (cxa, cy + (i - (len(A) - 1) / 2) * dy) for i, v in enumerate(A)}
    pb = {v: (cxb, cy + (i - (len(B) - 1) / 2) * dy) for i, v in enumerate(B)}
    for d in (pa, pb):
        for v, (x, y) in d.items():
            E.centro(c, str(v), x, y + size * 0.36, size, "g", tinta)
    for e, s in flechas:
        (x0, y0), (x1, y1) = pa[e], pb[s]
        M.arrow(c, x0 + 50, y0, x1 - 60, y1, cor_ruim if e == ruim else tinta, 1, 9, 30)


def a(c):  # o gancho: isso é função?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "isso é", 84, 470, 150, "i", BR)
    E.escreve(c, "função?", 76, 680, 210, "g", BR)
    diagrama(c, 1230, 1650, 560, [1, 2, 3], [2, 4, 6], [(1, 2), (2, 4), (2, 6), (3, 6)], AMARELO, 2)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "O que é", "função", "do zero")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "olhe só", 84, 420, 150, "i", BR)
    E.escreve(c, "as entradas", 76, 640, 190, "g", BR)
    E.escreve(c, "o atalho para saber se é função", 84, 840, 76, "i", claro)
    diagrama(c, 1340, 1700, 560, [1, 2, 3], [2, 4, 6], [(1, 2), (2, 4), (3, 6)], BR, None, size=66, dy=115, rw=105)
    c.drawOval(skia.Rect.MakeXYWH(1340 - 125, 560 - 222, 250, 444), M.paint(AMARELO, 1, stroke=8))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_isso_e_funcao", a), ("capa_B_o_que_e_funcao", b), ("capa_C_olhe_as_entradas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
