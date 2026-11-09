"""Capas do FIS-ELE-022 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def pilha(c, cx, cy, w, h, vira=False, corpo="#22222A"):
    c.save()
    if vira:
        c.translate(2 * cx, 0); c.scale(-1, 1)
    M.rrect(c, cx - w / 2, cy - h / 2, w, h, h * 0.18, corpo, 1, shadow=True)
    M.rrect(c, cx + w * 0.12, cy - h / 2, w * 0.38, h, h * 0.18, BR)
    M.rrect(c, cx + w / 2 - 6, cy - h * 0.17, h * 0.22, h * 0.34, 6, "#B9BCC4")
    c.restore()
    s = -1 if vira else 1
    E.centro(c, "1,5 V", cx - s * w * 0.15, cy + h * 0.16, h * 0.4, "g", BR)
    E.centro(c, "+", cx + s * w * 0.31, cy + h * 0.17, h * 0.45, "g", COR)


def a(c):  # o gancho: o motor travado esquenta
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "motor travado", 84, 390, 130, "i", BR)
    M.rrect(c, 70, 450, 1010, 230, 30, BR)
    E.escreve(c, "ESQUENTA", 110, 625, 170, "g", COR)
    E.escreve(c, "por quê?", 84, 880, 150, "g", BR)
    cx, cy, r = 1560, 540, 270
    c.drawCircle(cx, cy, r, M.paint(BR, 1, stroke=12))
    for k in range(3):
        import math
        g_ = math.radians(30 + 120 * k)
        p = skia.Path(); p.moveTo(cx, cy)
        p.quadTo(cx + math.cos(g_ - 0.55) * r * 0.75, cy + math.sin(g_ - 0.55) * r * 0.75, cx + math.cos(g_) * r * 0.88, cy + math.sin(g_) * r * 0.88)
        p.quadTo(cx + math.cos(g_ + 0.35) * r * 0.55, cy + math.sin(g_ + 0.35) * r * 0.55, cx, cy)
        c.drawPath(p, M.paint(E.mix(COR, BR, 0.8)))
    c.drawCircle(cx, cy, 50, M.paint(BR))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Motores", "e pilhas", "receptores")


def d(c):  # o macete: pilha invertida subtrai
    palco_capa(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "uma pilha invertida", 84, 360, 120, "i", BR)
    E.escreve(c, "SUBTRAI", 84, 560, 200, "g", E.mix(COR, BR, 0.35))
    for k in range(4):
        pilha(c, 330 + k * 420, 800, 400, 150, vira=(k == 2), corpo="#8A1F22" if k == 2 else "#22222A")
    E.escreve(c, "6 V → 3 V", 1180, 600, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_motor_travado_esquenta", a), ("capa_B_motores_e_pilhas", b), ("capa_C_pilha_invertida_subtrai", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
