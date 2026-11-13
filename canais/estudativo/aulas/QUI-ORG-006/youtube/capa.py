"""Capas da QUI-ORG-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o mesmo O, três funções
    base_capa(c)
    E.escreve(c, "mesmo oxigênio,", 84, 330, 110, "i", BR)
    E.escreve(c, "3 funções", 84, 520, 170, "g", AMARELO)
    E.escreve(c, "álcool · fenol · éter", 84, 700, 90, "g", BR)
    E.escreve(c, "olhe quem está do lado", 84, 980, 76, "i", BR)
    bast(c, dict(pts=HX + [(0, -2)], ligs=ligs_anel(0, 6) + [(0, 6)], duplas=DUP, rot={6: "OH"}), 1500, 620, 150, size=110)


def b(c):
    E.capa_modelo(c, "Química", "Álcool, fenol", "e éter", "do zero")


def d(c):  # o macete: os vizinhos do O
    palco_capa(c)
    E.escreve(c, "os 2 vizinhos do O", 84, 330, 110, "g", BR)
    for k, (viz, fn) in enumerate((("H – O – C", "álcool"), ("H – O – anel", "fenol"), ("C – O – C", "éter"))):
        y = 540 + k * 170
        E.escreve(c, viz, 84, y, 100, "g", BR)
        E.pilula(c, fn, 1300, y - 34, 70, "g", fundo=COR)


salvar((("capa_A_mesmo_oxigenio", a), ("capa_B_alcool_fenol_eter", b), ("capa_C_vizinhos_do_oxigenio", d)))
