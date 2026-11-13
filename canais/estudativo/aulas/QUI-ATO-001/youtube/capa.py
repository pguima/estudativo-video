"""Capas da QUI-ATO-001 (1280x720). Uso: python capa.py"""
import subprocess, sys
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


def eletron(c, x, y, r):
    E.bola(c, x, y, r, Q.ELETRON)
    M.line(c, x - r * 0.45, y, x + r * 0.45, y, BR, 1, max(3, r * 0.16))


def pudim(c, cx, cy, r):
    E.bola(c, cx, cy, r, E.mix(COR, BR, 0.55))
    for ux, uy in ((-0.45, -0.35), (0.38, -0.5), (0.05, 0.05), (-0.5, 0.35), (0.48, 0.3), (0.0, 0.62), (-0.1, -0.72)):
        eletron(c, cx + ux * r, cy + uy * r, r * 0.12)


def a(c):  # o gancho: a bola de bilhar não explica o elétron
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "o átomo", 84, 380, 150, "i", BR)
    E.escreve(c, "se divide?", 84, 560, 190, "g", BR)
    E.bola(c, 1480, 600, 230, "#7A7D86")
    E.risco(c, 1260, 840, 1700, 360, 9, 0, AMARELO, 30)
    eletron(c, 1760, 300, 70)
    E.escreve(c, "Dalton × Thomson", 84, 900, 96, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Dalton e", "Thomson", "do zero")


def d(c):  # o macete: a palavra-chave decide
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "bola de bilhar", 84, 360, 120, "i", BR)
    E.escreve(c, "ou pudim?", 84, 560, 190, "g", BR)
    E.bola(c, 560, 820, 150, "#7A7D86")
    pudim(c, 1060, 820, 150)
    E.escreve(c, "a palavra-chave", 1300, 800, 84, "i", claro)
    E.escreve(c, "decide", 1300, 900, 100, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_o_atomo_se_divide", a), ("capa_B_dalton_e_thomson", b), ("capa_C_bilhar_ou_pudim", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
