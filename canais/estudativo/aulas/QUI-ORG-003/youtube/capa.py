"""Capas da QUI-ORG-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: o nome é um código
    base_capa(c)
    E.escreve(c, "o nome é", 84, 330, 120, "i", BR)
    E.escreve(c, "um código", 84, 520, 170, "g", BR)
    x = 84
    for s, cor in (("pent-", AMARELO), ("2-", BR), ("en", BR), ("o", BR)):
        E.escreve(c, s, x, 800, 190, "g", cor); x += E.larg(s, "g", 190)
    E.escreve(c, "5 C · dupla no 2 · hidrocarboneto", 90, 960, 60, "i", BR)
    bast(c, dict(pts=Q.zigzag(5), duplas={(1, 2)}), 1500, 380, 120)


def b(c):
    E.capa_modelo(c, "Química", "Prefixo,", "infixo, sufixo", "do zero")


def d(c):  # o macete das vogais
    palco_capa(c)
    E.escreve(c, "an, en, in", 84, 360, 150, "g", BR)
    E.escreve(c, "a, e, i = 1, 2, 3 traços", 84, 560, 100, "g", CLARO_)
    for k in range(3):
        for j in range(k + 1):
            M.line(c, 120 + k * 380, 760 + j * 34, 380 + k * 380, 760 + j * 34, BR, 1, 12)
    E.escreve(c, "simples · dupla · tripla", 84, 990, 70, "i", BR)


salvar((("capa_A_o_nome_e_um_codigo", a), ("capa_B_prefixo_infixo_sufixo", b), ("capa_C_a_e_i", d)))
