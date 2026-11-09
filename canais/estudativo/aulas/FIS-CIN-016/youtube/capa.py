"""Capas do FIS-CIN-016 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


def curva(c, x0, yb, ang, k, cor, larg=8):
    r = math.radians(ang)
    vx, vy = 20 * math.cos(r), 20 * math.sin(r)
    T = 2 * vy / 10
    pts = [(x0 + vx * T * i / 60 * k, yb - (vy * T * i / 60 - 5 * (T * i / 60) ** 2) * k) for i in range(61)]
    F.poli(c, pts, 1.0, cor, 1.0, larg)


def a(c):  # o gancho: 30° ou 60°?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "30° ou 60°:", 84, 400, 150, "g", BR)
    E.escreve(c, "qual vai", 84, 580, 130, "i", BR)
    E.escreve(c, "mais longe?", 84, 750, 150, "g", BR)
    E.escreve(c, "empatam", 84, 930, 110, "i", AMARELO)
    x0, yb, k = 1060, 900, 22.0
    M.line(c, 1000, yb, 1880, yb, BR, 1.0, 6)
    curva(c, x0, yb, 30, k, E.mix(COR, BR, 0.6))
    curva(c, x0, yb, 60, k, BR)
    c.drawCircle(x0 + 34.64 * k, yb, 44, M.paint(AMARELO, 1.0, stroke=10))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lançamento", "oblíquo", "altura e alcance")


def d(c):  # o macete: A = vx · vy ÷ 5
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o alcance", 84, 330, 120, "i", BR)
    E.escreve(c, "sem sofrer", 76, 500, 150, "g", BR)
    E.formula(c, "A = f{vx · vy}{5}", 84, 800, 150, "g", E.mix(COR, BR, 0.5))
    x0, yb, k = 1160, 760, 16.0
    M.line(c, 1120, yb, 1880, yb, BR, 1.0, 5)
    curva(c, x0, yb, 45, k, BR)
    E.escreve(c, "45°", 1180, 960, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_30_ou_60_graus", a), ("capa_B_lancamento_obliquo", b), ("capa_C_alcance_sem_sofrer", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
