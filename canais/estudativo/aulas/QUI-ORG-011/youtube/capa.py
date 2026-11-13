"""Capas da QUI-ORG-011 (1280x720). Uso: python capa.py"""
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
PH = anel(6, 1, 0, -4.2, 0)
RD = ligs_anel(0, 6)
DUP = {(0, 1), (2, 3), (4, 5)}
PENI = dict(pts=PH + [(-2.33, -0.5), (-1.46, 0), (-1.46, 1.0), (-0.59, -0.5), (0.28, 0), (1.28, 0), (1.28, 1.0), (0.28, 1.0), (-0.45, 1.7),
                      (2.23, -0.31), (2.82, 0.5), (2.23, 1.31), (3.8, 0.75), (3.3, -0.35), (2.6, 2.25), (3.55, 2.55), (1.95, 3.0)],
            ligs=RD + [(0, 6), (6, 7), (7, 8), (7, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 10), (13, 14), (11, 15), (15, 16), (16, 17),
                       (17, 12), (16, 18), (16, 19), (17, 20), (20, 21), (20, 22)],
            duplas=DUP | {(7, 8), (13, 14), (20, 21)}, rot={8: "O", 9: "NH", 12: "N", 14: "O", 15: "S", 21: "O", 22: "OH"})
ASPIRINA = dict(pts=HX + [(0, -2), (-0.87, -2.5), (0.87, -2.5), (-1.74, -1.0), (-2.61, -0.5), (-2.61, 0.5), (-3.48, -1.0)],
                ligs=RD + [(0, 6), (6, 7), (6, 8), (1, 9), (9, 10), (10, 11), (10, 12)], duplas=DUP | {(6, 7), (10, 11)},
                rot={7: "O", 8: "OH", 9: "O", 11: "O"})


def a(c):  # o gancho: quantas funções tem a penicilina?
    base_capa(c)
    E.escreve(c, "quantas funções", 84, 330, 110, "i", BR)
    E.escreve(c, "tem a penicilina?", 84, 490, 120, "g", AMARELO)
    bast(c, PENI, 980, 720, 105, size=62)


def b(c):
    E.capa_modelo(c, "Química", "Funções", "em remédios", "praticando")


def d(c):  # o macete: ache o que não é C nem H
    palco_capa(c)
    E.escreve(c, "ache o que", 84, 340, 120, "i", BR)
    E.escreve(c, "não é C nem H", 84, 540, 140, "g", CLARO_)
    E.escreve(c, "e olhe os vizinhos", 84, 720, 80, "i", BR)
    bast(c, ASPIRINA, 1560, 620, 110, size=76)


salvar((("capa_A_funcoes_da_penicilina", a), ("capa_B_moleculas_reais", b), ("capa_C_nao_e_c_nem_h", d)))
