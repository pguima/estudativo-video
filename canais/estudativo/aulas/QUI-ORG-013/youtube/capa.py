"""Capas da QUI-ORG-013 (1280x720). Uso: python capa.py"""
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
GORD = "#E8B04A"


def micela(c, cx, cy, r, n=14):
    E.bola(c, cx, cy, r - 70, GORD)
    for k in range(n):
        g = math.radians(360 * k / n)
        hx, hy = cx + r * math.cos(g), cy + r * math.sin(g)
        for i in range(5):
            d0, d1 = 24 + i * 16, 24 + (i + 1) * 16
            o0, o1 = (6 if i % 2 else -6), (-6 if i % 2 else 6)
            ux, uy = -math.cos(g), -math.sin(g)
            M.line(c, hx + ux * d0 - uy * o0, hy + uy * d0 + ux * o0, hx + ux * d1 - uy * o1, hy + uy * d1 + ux * o1, "#6B5A2A", 1, 4)
        E.bola(c, hx, hy, 18, BR)


def a(c):  # o gancho: como o sabão tira a gordura
    base_capa(c)
    E.escreve(c, "como o sabão", 84, 330, 110, "i", BR)
    E.escreve(c, "prende", 84, 530, 190, "g", AMARELO)
    E.escreve(c, "a gordura", 84, 700, 150, "g", BR)
    E.escreve(c, "polar e apolar ao mesmo tempo", 84, 980, 66, "i", BR)
    micela(c, 1480, 560, 230, 16)


def b(c):
    E.capa_modelo(c, "Química", "Solubilidade", "e sabão", "do zero")


def d(c):  # o macete do teste da gasolina
    palco_capa(c)
    E.escreve(c, "álcool na gasolina?", 84, 340, 110, "g", BR)
    E.escreve(c, "dobre", 84, 560, 200, "g", CLARO_)
    E.escreve(c, "o que a água subiu", 84, 740, 100, "g", BR)
    E.escreve(c, "subiu 15 mL: 30%", 84, 920, 76, "i", BR)


salvar((("capa_A_sabao_prende_gordura", a), ("capa_B_solubilidade_sabao", b), ("capa_C_dobre_o_aumento", d)))
