"""Capas da QUI-ORG-002 (1280x720). Uso: python capa.py"""
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
Z4 = Q.zigzag(4)
MBE = dict(pts=Z4 + [(Z4[2][0], Z4[2][1] - 1.0)], ligs=[(0, 1), (1, 2), (2, 3), (2, 4)], duplas={(0, 1)})


def a(c):  # o gancho: quatro palavras, quatro perguntas
    base_capa(c)
    for k, s in enumerate(("aberta?", "ramificada?", "insaturada?", "heterogênea?")):
        E.escreve(c, s, 84, 330 + k * 175, 140, "g", AMARELO if k == 1 else BR)
    bast(c, MBE, 1500, 560, 190)


def b(c):
    E.capa_modelo(c, "Química", "Cadeias", "carbônicas", "do zero")


def d(c):  # o macete: achou um terciário, é ramificada
    palco_capa(c)
    E.escreve(c, "ramificada?", 84, 330, 120, "i", BR)
    E.escreve(c, "ache o T", 84, 560, 210, "g", CLARO_)
    E.escreve(c, "o carbono com 3 vizinhos", 84, 760, 76, "i", BR)
    Z = Q.zigzag(4)
    M_ = dict(pts=Z + [(Z[1][0], Z[1][1] + 1.0)], ligs=[(0, 1), (1, 2), (2, 3), (1, 4)])
    bast(c, M_, 1480, 520, 170)
    x, y = 1480 + Z[1][0] * 170, 520 + Z[1][1] * 170
    E.bola(c, x - 70, y + 40, 52, COR); E.centro(c, "T", x - 70, y + 64, 66, "g", BR)


salvar((("capa_A_quatro_perguntas", a), ("capa_B_cadeias_carbonicas", b), ("capa_C_ache_o_terciario", d)))
