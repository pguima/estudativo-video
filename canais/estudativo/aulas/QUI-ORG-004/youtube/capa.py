"""Capas da QUI-ORG-004 (1280x720). Uso: python capa.py"""
import subprocess, sys, math
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import quimica as Q
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")
CLARO_ = E.mix(COR, BR, 0.5)


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def base_capa(c):
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)


def anel(n=6, r=1.0, rot=90, cx=0.0, cy=0.0):
    return [(cx + r * math.cos(math.radians(rot + 360 * k / n)), cy - r * math.sin(math.radians(rot + 360 * k / n))) for k in range(n)]


def ligs_anel(i0, n):
    return [(i0 + k, i0 + (k + 1) % n) for k in range(n)]


def bast(c, M_, cx, cy, esc, escuro=True, largura=14, size=None):
    Q.bastao(c, 99, 0, M_["pts"], cx, cy, esc, duplas=M_.get("duplas", ()), triplas=M_.get("triplas", ()), rotulos=M_.get("rot"),
             ligacoes=M_.get("ligs"), escuro=escuro, largura=largura, size=size)


def salvar(capas):
    pasta = Path(__file__).parent
    s = skia.Surface(E.W, E.H)
    for nome, fn in capas:
        fn(s.getCanvas())
        tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
        tmp.unlink()
Z4, Z5 = Q.zigzag(4), Q.zigzag(5)
DMB = dict(pts=Z4 + [(Z4[1][0], Z4[1][1] + 1), (Z4[2][0], Z4[2][1] - 1)], ligs=[(0, 1), (1, 2), (2, 3), (1, 4), (2, 5)])
ISO = dict(pts=Z5 + [(Z5[1][0] - 0.5, Z5[1][1] + 0.87), (Z5[1][0] + 0.5, Z5[1][1] + 0.87), (Z5[3][0], Z5[3][1] + 1)],
           ligs=[(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (1, 6), (3, 7)])


def a(c):  # o gancho: 6 carbonos, nome de 4
    base_capa(c)
    E.escreve(c, "6 carbonos", 84, 330, 130, "g", BR)
    E.escreve(c, "mas o nome diz", 84, 470, 90, "i", BR)
    E.escreve(c, "butano?", 84, 680, 200, "g", AMARELO)
    E.escreve(c, "2,3-dimetilbutano", 84, 960, 90, "g", BR)
    bast(c, DMB, 1450, 540, 210)


def b(c):
    E.capa_modelo(c, "Química", "Cadeias", "ramificadas", "do zero")


def d(c):  # o macete: numere pelo galho mais perto
    palco_capa(c)
    E.escreve(c, "numere pelo", 84, 330, 120, "i", BR)
    E.escreve(c, "galho mais perto", 84, 520, 130, "g", CLARO_)
    E.escreve(c, "2,2,4-trimetilpentano", 84, 900, 90, "g", BR)
    bast(c, ISO, 1400, 640, 150)


salvar((("capa_A_seis_carbonos_butano", a), ("capa_B_cadeias_ramificadas", b), ("capa_C_galho_mais_perto", d)))
