"""Capas do MAT-ANG-003 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def pt(V, L, g):
    return V[0] + L * math.cos(math.radians(g)), V[1] - L * math.sin(math.radians(g))


def cunha(c, V, g1, g2, r, cor, alfa=0.6):
    ret = skia.Rect.MakeXYWH(V[0] - r, V[1] - r, 2 * r, 2 * r)
    p = skia.Path(); p.moveTo(*V); p.arcTo(ret, -g1, -(g2 - g1), False); p.close()
    c.drawPath(p, M.paint(cor, alfa))
    c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor, 1, stroke=8, cap_round=True))


def figura(c, cx, cy, w, gap, inc, ag, ob, tinta, letras=True):
    """paralelas com a transversal e os 8 ângulos: agudos numa cor, obtusos na outra"""
    y1, y2 = cy - gap / 2, cy + gap / 2
    k = 1 / math.tan(math.radians(inc))
    P1, P2 = (cx + gap / 2 * k, y1), (cx - gap / 2 * k, y2)
    for P in (P1, P2):
        for j, (g1, g2) in enumerate(((0, inc), (inc, 180), (180, 180 + inc), (180 + inc, 360))):
            cunha(c, P, g1, g2, 95 if j % 2 == 0 else 72, ag if j % 2 == 0 else ob, 0.55)
            if letras:
                g = (g1 + g2) / 2
                E.centro(c, "a" if j % 2 == 0 else "b", *(lambda q: (q[0], q[1] + 26))(pt(P, 150 if j % 2 == 0 else 125, g)), 72, "g", ag if j % 2 == 0 else ob)
    for yy in (y1, y2):
        M.line(c, cx - w / 2, yy, cx + w / 2, yy, tinta, 1, 12)
    ext = gap / 2 / math.sin(math.radians(inc)) + 160
    M.line(c, *pt((cx, cy), ext, inc + 180), *pt((cx, cy), ext, inc), tinta, 1, 12)


def a(c):  # o gancho: 8 ângulos, só 2 medidas
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    figura(c, 560, 640, 900, 380, 60, AMARELO, BR, BR)
    E.escreve(c, "8 ângulos", 1140, 470, 150, "g", BR)
    E.escreve(c, "só 2", 1140, 720, 230, "g", AMARELO)
    E.escreve(c, "medidas", 1150, 880, 130, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Retas", "paralelas", "e a transversal")


def d(c):  # o atalho: agudo com agudo, iguala
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    figura(c, 520, 640, 820, 360, 60, claro, "#8A8A90", BR, letras=False)
    E.escreve(c, "agudo + agudo", 1040, 430, 110, "g", claro)
    E.escreve(c, "iguala", 1040, 590, 150, "g", BR)
    E.escreve(c, "agudo + obtuso", 1040, 780, 110, "g", claro)
    E.escreve(c, "soma 180°", 1040, 940, 150, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_so_duas_medidas", a), ("capa_B_paralelas_transversal", b), ("capa_C_agudo_obtuso", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
