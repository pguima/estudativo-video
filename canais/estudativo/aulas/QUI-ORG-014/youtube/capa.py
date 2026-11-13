"""Capas da QUI-ORG-014 (1280x720). Uso: python capa.py"""
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
Z3 = Q.zigzag(3)


def a(c):  # o gancho: mesma fórmula, um líquido e um gás
    base_capa(c)
    Q.formula(c, "C2H6O", 84, 400, 170, AMARELO)
    E.escreve(c, "líquido", 84, 600, 120, "g", BR)
    E.escreve(c, "ou gás?", 84, 760, 120, "g", BR)
    E.escreve(c, "mesma fórmula, outra substância", 84, 980, 66, "i", BR)
    bast(c, dict(pts=Z3, rot={2: "OH"}), 1450, 380, 170, size=110)
    bast(c, dict(pts=Z3, rot={1: "O"}), 1450, 800, 170, size=110)


def b(c):
    E.capa_modelo(c, "Química", "Isomeria", "plana", "do zero")


def d(c):  # o macete: duas perguntas
    palco_capa(c)
    E.escreve(c, "5 tipos,", 84, 340, 120, "i", BR)
    E.escreve(c, "2 perguntas", 84, 540, 170, "g", CLARO_)
    E.escreve(c, "mesma função? o que mudou?", 84, 740, 76, "g", BR)
    E.escreve(c, "cadeia · posição · função · compensação · tautomeria", 84, 920, 50, "i", BR)


salvar((("capa_A_liquido_ou_gas", a), ("capa_B_isomeria_plana", b), ("capa_C_duas_perguntas", d)))
