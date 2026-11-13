"""Capas da QUI-ATO-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: Fe²⁺, de onde saem os elétrons?
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "Fe^{2+}", 84, 520, 300, BR, cores={"carga": AMARELO})
    E.escreve(c, "de onde saem", 760, 380, 110, "i", BR)
    E.escreve(c, "os elétrons?", 760, 540, 150, "g", AMARELO)
    E.formula(c, "... 3p^6 4s^2 3d^6", 84, 860, 120, "g", BR)


def b(c):
    E.capa_modelo(c, "Química", "Valência", "e íons", "do zero")


def d(c):  # o macete: entra pela energia, sai pela camada
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "entra pela energia,", 84, 400, 120, "i", BR)
    E.escreve(c, "sai pela camada", 84, 590, 150, "g", BR)
    E.formula(c, "3d^6 4s^2", 84, 850, 150, "g", claro)
    M.arrow(c, 760, 800, 1000, 800, AMARELO, 1, 10, 34)
    E.escreve(c, "tire do fim", 1040, 830, 100, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_de_onde_saem_os_eletrons", a), ("capa_B_valencia_e_ions", b), ("capa_C_sai_pela_camada", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
