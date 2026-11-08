"""Capas do MAT-TRI-001 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AM = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]
OPO, ADJ = "#FFB020", "#5FE0EA"  # âmbar e petróleo clareados para o fundo índigo


def tri(c, A, R, T, cores, rot, size=80, larg=14):
    path = skia.Path(); path.addPoly([A, R, T], True)
    c.drawPath(path, M.paint(BR, 0.12))
    for (P, Q), cor in zip(((A, R), (R, T), (A, T)), cores):
        M.line(c, *P, *Q, cor, 1.0, larg)
    q = 36
    M.line(c, R[0] - q, R[1], R[0] - q, R[1] - q, BR, 1.0, 5); M.line(c, R[0] - q, R[1] - q, R[0], R[1] - q, BR, 1.0, 5)
    for s, x, y, cor in rot:
        E.escreve(c, s, x, y, size, "g", cor)


def a(c):  # o gancho: 3/5 e 6/10 dão o mesmo 0,6
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    tri(c, (110, 860), (430, 860), (430, 620), (BR, OPO, BR), (("3", 455, 770, OPO), ("5", 220, 720, BR)), 70)
    tri(c, (560, 960), (1200, 960), (1200, 480), (BR, OPO, BR), (("6", 1230, 760, OPO), ("10", 790, 680, BR)), 80)
    E.escreve(c, "3/5 = 6/10", 84, 330, 150, "g", BR)
    E.escreve(c, "= 0,6", 1350, 760, 180, "g", AM)
    E.escreve(c, "por quê?", 1400, 940, 110, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Seno,", "cosseno", "e tangente")


def d(c):  # o macete: os três nomes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "nunca mais troque", 84, 320, 120, "i", BR)
    E.escreve(c, "sen = oposto/hip", 84, 520, 110, "g", BR)
    E.escreve(c, "cos = adjacente/hip", 84, 680, 110, "g", BR)
    E.escreve(c, "tg = oposto/adjacente", 84, 840, 110, "g", BR)
    E.escreve(c, "oposto", 84 + E.larg("sen = ", "g", 110), 520, 110, "g", OPO)
    E.escreve(c, "adjacente", 84 + E.larg("cos = ", "g", 110), 680, 110, "g", ADJ)
    E.escreve(c, "oposto", 84 + E.larg("tg = ", "g", 110), 840, 110, "g", OPO)
    E.escreve(c, "adjacente", 84 + E.larg("tg = oposto/", "g", 110), 840, 110, "g", ADJ)
    tri(c, (1380, 960), (1820, 960), (1820, 630), ((ADJ, OPO, E.mix(COR, BR, 0.5))), ())


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mesmo_0_6", a), ("capa_B_seno_cosseno_tangente", b), ("capa_C_oposto_adjacente", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
