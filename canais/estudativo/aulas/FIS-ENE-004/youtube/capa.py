"""Capas do FIS-ENE-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: x em centímetro dá 100.000 J
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "mola esticada 20 cm", 84, 380, 110, "i", BR)
    E.escreve(c, "100.000 J?", 84, 620, 200, "g", BR)
    E.risco(c, 70, 650, 1080, 450, 9, 0, AMARELO, 30)
    E.escreve(c, "são 10 J", 84, 860, 180, "g", AMARELO)
    claro = E.mix(COR, BR, 0.82)
    F.parede(c, 1250, 640, 860, -1, 1.0)
    F.mola(c, 1250, 760, 1600, 760, 8, 70, BR, 1.0, 10)
    M.rrect(c, 1600, 680, 170, 160, 18, claro)


def b(c):  # o modelo padrão
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "Energia", 76, 450, 210, "g", BR)
    E.escreve(c, "potencial", 76, 660, 210, "g", BR)
    E.escreve(c, "altura e mola", 84, 860, 150, "i", BR)
    E.simbolo(c, 1590, 760, 260, cor=E.mix(COR, BR, 0.82), forma="orbita")


def d(c):  # o macete: Ep = F · x / 2
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "sem o k? use a área", 84, 340, 110, "i", BR)
    E.formula(c, "Ep = f{F · x}{2}", 76, 640, 200, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    x0, y0 = 1250, 900
    M.line(c, x0, y0, x0 + 520, y0, BR, 1, 6)
    M.line(c, x0, y0, x0, y0 - 480, BR, 1, 6)
    p = skia.Path(); p.moveTo(x0, y0); p.lineTo(x0 + 420, y0 - 380); p.lineTo(x0 + 420, y0); p.close()
    c.drawPath(p, M.paint(COR, 0.6))
    M.line(c, x0, y0, x0 + 420, y0 - 380, claro, 1, 10)
    E.escreve(c, "F", x0 + 440, y0 - 380, 70, "g", BR)
    E.escreve(c, "x", x0 + 190, y0 + 80, 70, "g", F.VEL)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mola_em_centimetro", a), ("capa_B_energia_potencial", b), ("capa_C_area_do_triangulo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
