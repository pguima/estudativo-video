"""Capas do FIS-CIN-020 (1280x720). Uso: python capa.py"""
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


def engrenagem(c, cx, cy, r, n, ang, cor, miolo):
    p = skia.Path()
    h = r * 0.16
    for k in range(n * 4 + 1):
        g = math.radians(ang + 360 * k / (n * 4))
        rr = r if (k % 4) in (1, 2) else r - h
        x, y = cx + math.cos(g) * rr, cy - math.sin(g) * rr
        p.moveTo(x, y) if k == 0 else p.lineTo(x, y)
    p.close()
    c.drawPath(p, M.paint(cor))
    c.drawCircle(cx, cy, r * 0.55, M.paint(miolo))
    c.drawCircle(cx, cy, r * 0.12, M.paint(cor))


def corrente(c, A, ra, B, rb, cor):
    dx, dy = B[0] - A[0], B[1] - A[1]
    d = math.hypot(dx, dy); th = math.atan2(dy, dx); phi = math.acos((ra - rb) / d)
    for s in (1, -1):
        al = th + s * phi
        P = (A[0] + ra * math.cos(al), A[1] + ra * math.sin(al)); Q = (B[0] + rb * math.cos(al), B[1] + rb * math.sin(al))
        pt = M.paint(cor, 1.0, stroke=10); pt.setPathEffect(skia.DashPathEffect.Make([30, 14], 0))
        path = skia.Path(); path.moveTo(*P); path.lineTo(*Q); c.drawPath(path, pt)


def a(c):  # o gancho: 1 pedalada, 3 voltas
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "1 pedalada", 84, 400, 150, "g", BR)
    E.escreve(c, "=", 84, 560, 130, "g", AMARELO)
    E.escreve(c, "3 voltas", 220, 560, 150, "g", AMARELO)
    E.escreve(c, "da roda. como?", 84, 740, 110, "i", BR)
    A, B = (1250, 700), (1680, 700)
    c.drawCircle(*B, 220, M.paint(BR, 0.8, stroke=14))
    corrente(c, A, 150, B, 50, "#2A1A10")
    engrenagem(c, *A, 150, 24, 0, BR, COR)
    engrenagem(c, *B, 50, 8, 0, BR, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Polias e", "correias", "engrenagens e eixos")


def d(c):  # o macete em duas linhas
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "o atalho", 84, 330, 120, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "correia:", 84, 540, 120, "g", BR)
    E.escreve(c, "v igual", 640, 540, 120, "g", claro)
    E.escreve(c, "eixo:", 84, 740, 120, "g", BR)
    E.escreve(c, "ω igual", 460, 740, 120, "g", claro)
    engrenagem(c, 1600, 640, 220, 20, 8, COR, "#07070F")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_uma_pedalada_tres_voltas", a), ("capa_B_polias_e_correias", b), ("capa_C_correia_e_eixo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
