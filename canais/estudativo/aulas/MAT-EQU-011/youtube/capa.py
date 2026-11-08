"""Capas do MAT-EQU-011 (1280x720). Uso: python capa.py"""
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


def triangulo(c, cx, topo, meia, base, cor_l, tinta, size):
    p = skia.Path()
    p.moveTo(cx, topo); p.lineTo(cx + meia, base); p.lineTo(cx - meia, base); p.close()
    pt = M.paint(tinta, 1, stroke=12); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(p, pt)
    ym = topo + (base - topo) * 0.6
    M.line(c, cx - meia * 0.6, ym, cx + meia * 0.6, ym, tinta, 1, 12)
    M.line(c, cx, ym, cx, base, tinta, 1, 12)
    E.centro(c, "d", cx, ym - 50, size, "g", cor_l)
    E.centro(c, "v", cx - meia * 0.36, base - 60, size * 0.86, "g", cor_l)
    E.centro(c, "t", cx + meia * 0.36, base - 60, size * 0.86, "g", cor_l)


def a(c):  # o gancho: a fórmula dá v, a prova pede d
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "v = f{d}{t}", 84, 520, 260, cor=BR)
    E.escreve(c, "e se pedirem", 760, 400, 120, "i", BR)
    E.escreve(c, "a distância?", 760, 540, 150, "g", AMARELO)
    E.escreve(c, "sem decorar outra fórmula", 84, 920, 120, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Isolar a letra", "na fórmula", "sem decorar")


def d(c):  # o macete: o triângulo
    palco(c)
    E.escreve(c, "o atalho do", 84, 380, 140, "i", BR)
    E.escreve(c, "triângulo", 84, 580, 210, "g", BR)
    E.formula(c, "d = v · t", 84, 900, 170, cor=AMARELO)
    triangulo(c, 1480, 230, 360, 900, AMARELO, BR, 190)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_e_a_distancia", a), ("capa_B_isolar_letra", b), ("capa_C_triangulo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
