"""Capas da QUI-ORG-012 (1280x720). Uso: python capa.py"""
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
BUTANO = dict(pts=Q.zigzag(4))
ACETICO = dict(pts=Z3f + [(Z3f[1][0], Z3f[1][1] - 1)], ligs=[(0, 1), (1, 2), (1, 3)], duplas={(1, 3)}, rot={2: "OH", 3: "O"})


def a(c):  # o gancho: mesma massa, 118 graus de diferença
    base_capa(c)
    E.escreve(c, "mesma massa,", 84, 330, 110, "i", BR)
    E.escreve(c, "0 °C × 118 °C", 84, 560, 170, "g", AMARELO)
    E.escreve(c, "quem ferve primeiro?", 84, 760, 90, "g", BR)
    bast(c, BUTANO, 1480, 330, 140)
    bast(c, ACETICO, 1480, 800, 150, size=100)


def b(c):
    E.capa_modelo(c, "Química", "Ponto de", "ebulição", "dos orgânicos")


def d(c):  # o macete: procure o H preso a O
    palco_capa(c)
    E.escreve(c, "ordene em 5 s:", 84, 330, 110, "i", BR)
    E.escreve(c, "procure o H", 84, 520, 160, "g", CLARO_)
    E.escreve(c, "preso a O", 84, 700, 160, "g", CLARO_)
    E.escreve(c, "ácido > álcool > o resto", 84, 900, 76, "i", BR)


salvar((("capa_A_mesma_massa", a), ("capa_B_ponto_ebulicao", b), ("capa_C_h_preso_a_o", d)))
