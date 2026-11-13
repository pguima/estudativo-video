"""Capas da QUI-ORG-005 (1280x720). Uso: python capa.py"""
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
LIM = dict(pts=HX + [(0, -2), (0, 2), (-0.87, 2.5), (0.87, 2.5)], ligs=ligs_anel(0, 6) + [(0, 6), (3, 7), (7, 8), (7, 9)], duplas={(0, 1), (7, 8)})


def a(c):  # o gancho: o limoneno da laranja
    base_capa(c)
    E.escreve(c, "a molécula", 84, 330, 110, "i", BR)
    E.escreve(c, "da laranja", 84, 500, 160, "g", BR)
    Q.formula(c, "C10H16?", 84, 760, 170, AMARELO)
    E.escreve(c, "4 questões de prova", 84, 990, 80, "i", BR)
    bast(c, LIM, 1480, 520, 125)


def b(c):
    E.capa_modelo(c, "Química", "Cadeias", "e nomes", "praticando")


def d(c):  # o ângulo do macete
    palco_capa(c)
    E.escreve(c, "4 questões", 84, 330, 130, "g", BR)
    E.escreve(c, "combustível e remédio", 84, 480, 84, "i", BR)
    E.formula(c, "H = 2C + 2", 84, 740, 170, "g", CLARO_)
    E.escreve(c, "− 2 por anel e por dupla", 84, 900, 76, "i", BR)


salvar((("capa_A_molecula_da_laranja", a), ("capa_B_praticando_cadeias", b), ("capa_C_quatro_questoes", d)))
