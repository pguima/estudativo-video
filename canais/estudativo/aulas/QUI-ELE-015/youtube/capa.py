"""Capas da QUI-ELE-015 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


def base(c):
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)


def salvar(capas):
    pasta = Path(__file__).parent
    s = skia.Surface(E.W, E.H)
    for nome, fn in capas:
        fn(s.getCanvas())
        tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
        tmp.unlink()


def a(c):  # o gancho: parece balanceada, mas está errada
    base(c)
    Q.formula(c, "Al + Cu^2+ -> Al^3+ + Cu", 84, 380, 140, BR)
    E.escreve(c, "parece certa.", 84, 640, 150, "g", BR)
    E.escreve(c, "está errada.", 84, 820, 150, "g", AMARELO)
    E.escreve(c, "sobra elétron", 84, 980, 80, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Balancear", "com elétrons", "por oxirredução")


def d(c):  # o macete: cruze os elétrons
    palco_capa(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "cruze os elétrons", 84, 300, 120, "i", BR)
    Q.formula(c, "2 Al + 3 Cu^2+", 84, 560, 170, BR, cores={"coef": claro}, escuro=True)
    E.escreve(c, "perde 3", 84, 760, 90, "g", "#FFB347")
    E.escreve(c, "ganha 2", 600, 760, 90, "g", "#7FB2FF")
    E.escreve(c, "6 = 6", 84, 960, 130, "g", claro)


salvar((("capa_A_parece_certa_esta_errada", a), ("capa_B_balancear_por_oxirreducao", b), ("capa_C_cruze_os_eletrons", d)))
