"""Capas do MAT-CNT-013 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def moeda(c, cx, cy, r, face, fundo=BR, tinta=None):
    c.drawCircle(cx, cy, r, M.paint(fundo))
    c.drawCircle(cx, cy, r * 0.82, M.paint(tinta or COR, 0.5, stroke=r * 0.05))
    s = r * 0.8
    E.escreve(c, face, cx - E.larg(face, "g", s) / 2, cy + s * 0.35, s, "g", tinta or COR)


def a(c):  # o gancho: pelo menos 1 cara em 3 moedas = 1 − 1/8 = 7/8
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i, f in enumerate(("Ca", "Co", "Ca")):
        moeda(c, 210 + i * 230, 390, 100, f)
    E.escreve(c, "pelo menos", 860, 360, 120, "i", BR)
    E.escreve(c, "1 cara?", 860, 500, 150, "g", AMARELO)
    y = 820
    E.escreve(c, "1 −", 120, y + 60, 170, "g", BR)
    E.fracao(c, 1, 8, 470, y, 170, BR)
    E.escreve(c, "=", 620, y + 60, 170, "g", BR)
    E.bola(c, 1000, 810, 220, "#FFFFFF")
    E.fracao(c, 7, 8, 1000, 800, 190, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "O lado", "contrário", "evento complementar")


def d(c):  # o macete: pelo menos um → 1 − P(nenhum)
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "viu “pelo menos um”?", 84, 400, 120, "i", BR)
    E.escreve(c, "1 − P(nenhum)", 84, 680, 220, "g", AMARELO)
    E.escreve(c, "e pronto", 84, 920, 120, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_pelo_menos_uma", a), ("capa_B_lado_contrario", b), ("capa_C_um_menos_nenhum", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
