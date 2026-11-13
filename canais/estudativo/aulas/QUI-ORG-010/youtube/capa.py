"""Capas da QUI-ORG-010 (1280x720). Uso: python capa.py"""
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
CL = Q.cor_el("Cl")


def a(c):  # o gancho: um cloro, milhares de ozônios
    base_capa(c)
    E.escreve(c, "1 cloro", 84, 330, 150, "g", BR)
    E.escreve(c, "destrói", 84, 480, 110, "i", BR)
    E.escreve(c, "milhares", 84, 680, 180, "g", AMARELO)
    E.escreve(c, "de ozônios", 84, 820, 110, "g", BR)
    E.escreve(c, "o estrago do CFC", 84, 990, 76, "i", BR)
    Q.atomo(c, 1450, 520, 120, "Cl")
    for k in range(5):
        Q.molecula_desenho(c, "O3", 1200 + k * 130, 830 - (k % 2) * 60, 40, 0.9, separa=0.4)


def b(c):
    E.capa_modelo(c, "Química", "Haletos,", "CFC e DDT", "do zero")


def d(c):  # o macete: troque O por S
    palco_capa(c)
    E.escreve(c, "troque O por S", 84, 340, 120, "g", BR)
    E.escreve(c, "+ tio", 84, 560, 200, "g", CLARO_)
    E.escreve(c, "álcool vira tiol · éter vira tioéter", 84, 760, 70, "i", BR)
    Q.atomo(c, 1500, 560, 140, "S", escuro=True)


salvar((("capa_A_um_cloro_milhares", a), ("capa_B_haletos_funcoes", b), ("capa_C_troque_o_por_s", d)))
