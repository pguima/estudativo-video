"""Capas do FIS-MAG-005 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def barra(c, cx, cy, w, h):
    for lado, cor in ((1, COR), (-1, F.NEG)):
        x0 = cx if lado > 0 else cx - w / 2
        r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0, cy - h / 2, w / 2, h), 14, 14)
        c.drawRRect(r, M.paint(cor)); c.drawRRect(r, M.paint(BR, 1, stroke=6))
    E._meio(c, "N", cx + w / 4, cy, h * 0.6, "g", BR)
    E._meio(c, "S", cx - w / 4, cy, h * 0.6, "g", BR)


def a(c):  # o gancho: corrente sem pilha
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "corrente", 84, 400, 200, "g", BR)
    E.escreve(c, "sem pilha", 84, 600, 200, "g", AMARELO)
    E.escreve(c, "só com um ímã", 84, 800, 120, "i", BR)
    x0, cy, w, ry = 1440, 520, 380, 170
    barra(c, 1320, cy, 300, 110)
    for k in range(8):
        x = x0 + w / 8 * (k + 0.5)
        p = skia.Path(); p.moveTo(x, cy - ry)
        p.cubicTo(x + 50, cy - ry * 0.6, x + 50, cy + ry * 0.6, x, cy + ry)
        c.drawPath(p, M.paint("#1B1B22", 1, stroke=10))
    F.seta(c, 1180, 760, 1380, 760, BR, 1, 14)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Fluxo e", "Faraday", "do zero")


def d(c):  # o macete: Faraday só vê mudança
    palco_capa(c)
    E.escreve(c, "Faraday só vê", 84, 330, 130, "i", BR)
    E.escreve(c, "mudança", 84, 540, 200, "g", BR)
    E.formula(c, "ε = f{ΔΦ}{Δt}", 1450, 520, 190, "g", BR, 1, "center")
    E.formula(c, "barra: ε = B·L·v", 84, 860, 110, "g", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_corrente_sem_pilha", a), ("capa_B_fluxo_e_faraday", b), ("capa_C_faraday_so_ve_mudanca", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
