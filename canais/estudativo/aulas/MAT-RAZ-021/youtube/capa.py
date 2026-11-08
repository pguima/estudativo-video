"""Capas do MAT-RAZ-021 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def barra(c, x, y, n, tr, cor, fundo, size=56, rot=("0", "5", "10 km")):
    for i in range(n):
        r = skia.Rect.MakeXYWH(x + i * tr, y, tr, 40)
        c.drawRect(r, M.paint(cor if i % 2 == 0 else fundo))
        c.drawRect(r, M.paint(cor, stroke=6))
    for i, s in enumerate(rot):
        E.centro(c, s, x + i * tr, y + 40 + size * 1.2, size, "b", cor)


def a(c):  # o gancho: a cópia reduzida deixa a escala escrita errada
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "cópia reduzida:", 84, 360, 120, "i", BR)
    E.escreve(c, "1 : 50.000", 84, 570, 190, "g", BR)
    E.risco(c, 70, 600, 1060, 430, 9, 0, "#FFD500", 30)
    E.escreve(c, "a escala que não erra:", 84, 800, 100, "i", BR)
    barra(c, 1000, 830, 2, 360, BR, COR, 70)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Descobrir", "a escala", "e a escala gráfica")


def d(c):  # o macete
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cl = E.mix(COR, BR, 0.55)
    E.escreve(c, "real ÷ desenho", 84, 400, 170, "g", BR)
    E.escreve(c, "4 cm para 10 km", 84, 620, 120, "i", cl)
    E.escreve(c, "1 : 250.000", 84, 880, 210, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_copia_reduzida", a), ("capa_B_descobrir_escala", b), ("capa_C_real_sobre_desenho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
