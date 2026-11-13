"""Capas da QUI-ORG-009 (1280x720). Uso: python capa.py"""
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
HX = anel(6)
DUP = {(0, 1), (2, 3), (4, 5)}
PARA = dict(pts=HX + [(0, -2), (0, 2), (0.87, 2.5), (0.87, 3.5), (1.74, 2.0)],
            ligs=ligs_anel(0, 6) + [(0, 6), (3, 7), (7, 8), (8, 9), (8, 10)], duplas=DUP | {(8, 9)}, rot={6: "OH", 7: "NH", 9: "O"})
TRIMETIL = dict(pts=[(0, 0), (0, -1), (-0.87, 0.5), (0.87, 0.5)], ligs=[(0, 1), (0, 2), (0, 3)], rot={0: "N"})


def a(c):  # o gancho: o cheiro de peixe
    base_capa(c)
    E.escreve(c, "o cheiro", 84, 330, 120, "i", BR)
    E.escreve(c, "de peixe", 84, 500, 170, "g", BR)
    E.escreve(c, "é uma base", 84, 700, 150, "g", AMARELO)
    E.escreve(c, "e o limão resolve", 84, 960, 80, "i", BR)
    bast(c, TRIMETIL, 1450, 560, 200, size=130)


def b(c):
    E.capa_modelo(c, "Química", "Amina, amida", "e nitrila", "do zero")


def d(c):  # o macete: ache a amida no remédio
    palco_capa(c)
    E.escreve(c, "N ao lado do C=O?", 84, 340, 110, "g", BR)
    E.escreve(c, "amida", 84, 580, 220, "g", CLARO_)
    E.escreve(c, "a do paracetamol", 84, 780, 80, "i", BR)
    bast(c, PARA, 1450, 470, 100, size=70)


salvar((("capa_A_cheiro_de_peixe", a), ("capa_B_amina_amida_nitrila", b), ("capa_C_amida_no_remedio", d)))
