"""Capas do FIS-ELE-009 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: dobrou U, dobrou R?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "dobrou U,", 84, 380, 170, "g", BR)
    E.escreve(c, "dobrou R?", 84, 580, 190, "g", BR)
    E.risco(c, 70, 600, 1000, 420, 9, 0, AMARELO, 30)
    E.escreve(c, "não: dobra a corrente", 84, 860, 110, "i", BR)
    claro = E.mix(COR, BR, 0.85)
    F.fio(c, 1, 0, [(1180, 760), (1330, 760)], cor=claro, largura=10)
    F.fio(c, 1, 0, [(1630, 760), (1780, 760)], cor=claro, largura=10)
    p = [(1330, 760)] + [(1330 + 300 * i / 8, 760 + 50 * (1 if i % 2 else -1)) for i in range(1, 8)] + [(1630, 760)]
    F.poli(c, p, 1.0, claro, 1.0, 12)
    E.centro(c, "R", 1480, 660, 120, "g", claro)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lei de Ohm", "U = R · i", "resistência do zero")


def d(c):  # o macete: triângulo do URI
    palco(c)
    E.escreve(c, "o triângulo", 84, 340, 110, "i", BR)
    E.escreve(c, "U R i", 84, 560, 190, "g", BR)
    E.escreve(c, "tampe o que quer achar", 84, 780, 90, "i", E.mix(COR, BR, 0.5))
    cx, cy, s = 1460, 600, 300
    p = skia.Path(); p.moveTo(cx, cy - s); p.lineTo(cx + s * 1.1, cy + s * 0.7); p.lineTo(cx - s * 1.1, cy + s * 0.7); p.close()
    c.drawPath(p, M.paint(BR, 1, stroke=10))
    M.line(c, cx - s * 0.7, cy + s * 0.05, cx + s * 0.7, cy + s * 0.05, BR, 1, 10)
    M.line(c, cx, cy + s * 0.05, cx, cy + s * 0.7, BR, 1, 10)
    for k, (x, y) in {"U": (cx, cy - s * 0.18), "R": (cx - s * 0.38, cy + s * 0.5), "i": (cx + s * 0.38, cy + s * 0.5)}.items():
        E.centro(c, k, x, y + s * 0.13, s * 0.4, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobrou_u_dobrou_r", a), ("capa_B_lei_de_ohm", b), ("capa_C_triangulo_uri", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
