"""Capas da QUI-ATO-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: Na⁺ ganhou ou perdeu?
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "^{23}_{11}Na^+", 84, 560, 300, BR, cores={"carga": AMARELO})
    E.escreve(c, "ganhou", 1000, 420, 130, "g", BR)
    E.risco(c, 990, 440, 1460, 330, 9, 0, AMARELO, 26)
    E.escreve(c, "ou perdeu?", 1000, 600, 130, "g", AMARELO)
    E.escreve(c, "prótons, nêutrons e elétrons", 84, 880, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Z, A, íons", "e isótopos", "do zero")


def d(c):  # o macete: elétrons = Z − carga
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "elétrons =", 84, 400, 150, "g", BR)
    E.escreve(c, "Z − carga", 84, 580, 170, "g", claro)
    Q.formula(c, "Cl^-", 84, 860, 160, BR, escuro=True)
    E.formula(c, "17 − (−1) = 18", 400, 850, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_ganhou_ou_perdeu", a), ("capa_B_z_a_ions_isotopos", b), ("capa_C_eletrons_z_menos_carga", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
