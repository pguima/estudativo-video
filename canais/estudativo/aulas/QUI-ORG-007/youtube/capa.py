"""Capas da QUI-ORG-007 (1280x720). Uso: python capa.py"""
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
Z3 = [(x, -y) for x, y in Q.zigzag(3)]
PROPANONA = dict(pts=Z3 + [(Z3[1][0], Z3[1][1] - 1.0)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 3)}, rot={3: "O"})
PROPANAL = dict(pts=Q.zigzag(4), rot={3: "O"}, duplas={(2, 3)})


def a(c):  # o gancho: formol e acetona, o mesmo C=O
    base_capa(c)
    E.escreve(c, "formol e acetona", 84, 330, 110, "g", BR)
    E.escreve(c, "o mesmo", 84, 500, 110, "i", BR)
    E.escreve(c, "C=O", 84, 720, 220, "g", AMARELO)
    E.escreve(c, "só muda o lugar", 84, 980, 80, "i", BR)
    Q.lewis(c, 99, 0, [("C", 0, 0), ("O", 1.2, 0), ("H", -0.8, -0.6), ("H", -0.8, 0.6)], [(0, 1, 2), (0, 2, 1), (0, 3, 1)], 1400, 330, escala=130, size=100, escuro=True)
    bast(c, PROPANONA, 1450, 820, 150, size=100)


def b(c):
    E.capa_modelo(c, "Química", "Aldeído", "e cetona", "do zero")


def d(c):  # o macete: 1 ou 2 carbonos = aldeído
    palco_capa(c)
    E.escreve(c, "1 ou 2 carbonos?", 84, 340, 120, "g", BR)
    E.escreve(c, "só aldeído", 84, 560, 170, "g", CLARO_)
    E.escreve(c, "a menor cetona tem 3", 84, 760, 90, "i", BR)
    bast(c, PROPANONA, 1500, 600, 170, size=110)


salvar((("capa_A_o_mesmo_CO", a), ("capa_B_aldeido_cetona", b), ("capa_C_menor_cetona", d)))
