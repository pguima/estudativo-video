"""Capas do MAT-ANG-002 (1280x720). Uso: python capa.py"""
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
    c.drawArc(ret, -g1, -(g2 - g1), False, M.paint(cor, 1, stroke=10, cap_round=True))


def a(c):  # o gancho: complemento de 35° não é 145°
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "complemento de 35°", 84, 380, 130, "g", BR)
    E.escreve(c, "145°", 84, 700, 270, "g", BR)
    E.risco(c, 60, 720, 760, 480, 9, 0, AMARELO, 34)
    E.escreve(c, "55°", 960, 700, 270, "g", AMARELO)
    E.escreve(c, "não troque as palavras", 84, 950, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Complemento", "e suplemento", "sem trocar")


def d(c):  # a regra da tesoura
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    V = (520, 640)
    cunha(c, V, 0, 50, 170, claro); cunha(c, V, 180, 230, 170, claro)
    for g in (0, 50):
        M.line(c, *pt(V, 420, g + 180), *pt(V, 420, g), BR, 1, 12)
    c.drawCircle(*V, 16, M.paint(BR))
    E.centro(c, "50°", *pt((V[0], V[1] + 30), 250, 25), 80, "g", BR)
    E.centro(c, "50°", *pt((V[0], V[1] + 30), 250, 205), 80, "g", BR)
    E.escreve(c, "de frente:", 1060, 470, 130, "i", BR)
    E.escreve(c, "iguais", 1040, 700, 220, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_145", a), ("capa_B_complemento_suplemento", b), ("capa_C_tesoura", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
