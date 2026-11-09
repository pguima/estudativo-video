"""Capas do FIS-ELE-006 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o erro: esquecer o ÷ 2
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "energia =", 84, 360, 130, "g", BR)
    E.escreve(c, "Q · U ?", 84, 580, 200, "g", BR)
    E.risco(c, 70, 600, 760, 420, 9, 0, AMARELO, 30)
    E.formula(c, "f{Q · U}{2}", 900, 560, 210, "g", E.mix(COR, BR, 0.85))
    E.escreve(c, "não esqueça o ÷ 2", 84, 900, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "O que é um", "capacitor", "e o flash da câmera")


def d(c):  # o macete: a energia é o triângulo
    palco(c)
    E.escreve(c, "a energia é", 84, 340, 110, "i", BR)
    E.escreve(c, "o triângulo", 84, 540, 170, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    x0, y0 = 1150, 920
    M.line(c, x0, y0, 1800, y0, BR, 1, 8)
    M.line(c, x0, y0, x0, 300, BR, 1, 8)
    p = skia.Path(); p.moveTo(x0, y0); p.lineTo(1700, 380); p.lineTo(1700, y0); p.close()
    c.drawPath(p, M.paint(COR, 0.6))
    M.line(c, x0, y0, 1700, 380, claro, 1, 10)
    E.escreve(c, "Q · U ÷ 2", 84, 800, 130, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_esquecer_o_dividido_por_2", a), ("capa_B_capacitores", b), ("capa_C_energia_e_o_triangulo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
