"""Capas do MAT-CNT-016 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 5 caras seguidas, a coroa está devendo? Não: 1/2
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i in range(5):
        moeda(c, 170 + i * 190, 340, 82, "Ca")
    c.drawCircle(1150, 340, 82, M.paint(AMARELO))
    E.escreve(c, "?", 1150 - E.larg("?", "g", 120) / 2, 382, 120, "g", COR)
    E.escreve(c, "a coroa está", 90, 600, 110, "i", BR)
    E.escreve(c, "devendo?", 90, 740, 150, "g", AMARELO)
    E.escreve(c, "não:", 90, 930, 120, "i", BR)
    E.bola(c, 1400, 760, 240, "#FFFFFF")
    E.fracao(c, 1, 2, 1400, 750, 200, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Multiplicar", "as chances", "eventos independentes")


def d(c):  # o macete: chance repetida vira potência
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 caras seguidas?", 84, 400, 120, "i", BR)
    w = E.formula(c, "(f{1}{2})^3 =", 84, 760, 200, "g", BR)
    E.fracao(c, 1, 8, 84 + w + 130, 700, 200, AMARELO)
    E.escreve(c, "chance repetida vira potência", 84, 1000, 80, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_coroa_devendo", a), ("capa_B_multiplicar_chances", b), ("capa_C_potencia", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
