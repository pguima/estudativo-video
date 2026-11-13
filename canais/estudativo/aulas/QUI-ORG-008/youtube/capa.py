"""Capas da QUI-ORG-008 (1280x720). Uso: python capa.py"""
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
Z3f = [(x, -y) for x, y in Q.zigzag(3)]
Z5f = [(x, -y) for x, y in Q.zigzag(5)]
ACETICO = dict(pts=Z3f + [(Z3f[1][0], Z3f[1][1] - 1)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 3)}, rot={2: "OH", 3: "O"})
ET_ET = dict(pts=Z5f + [(Z5f[1][0], Z5f[1][1] - 1)], ligs=[(0, 1), (1, 2), (2, 3), (3, 4), (1, 5)], duplas={(1, 5)}, rot={2: "O", 5: "O"})


def a(c):  # o gancho: vinagre e banana
    base_capa(c)
    E.escreve(c, "vinagre", 84, 330, 130, "g", BR)
    E.escreve(c, "e banana:", 84, 480, 130, "g", BR)
    E.escreve(c, "o lugar de um H", 84, 680, 110, "i", BR)
    E.escreve(c, "muda tudo", 84, 860, 170, "g", AMARELO)
    bast(c, ACETICO, 1450, 330, 140, size=90)
    bast(c, ET_ET, 1450, 800, 130, size=90)


def b(c):
    E.capa_modelo(c, "Química", "Ácido", "e éster", "do zero")


def d(c):  # o macete: o segundo oxigênio
    palco_capa(c)
    E.escreve(c, "COOH ou COO–C?", 84, 340, 110, "g", BR)
    E.escreve(c, "olhe o", 84, 520, 110, "i", BR)
    E.escreve(c, "2º oxigênio", 84, 700, 170, "g", CLARO_)
    E.escreve(c, "com H, ácido · com C, éster", 84, 900, 70, "i", BR)


salvar((("capa_A_vinagre_e_banana", a), ("capa_B_acido_ester", b), ("capa_C_segundo_oxigenio", d)))
