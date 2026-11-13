"""Capas da QUI-LIG-001 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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


CLARO = E.mix(COR, BR, 0.5)

def a(c):  # o gancho: metal violento + gás venenoso = sal
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.atomo(c, 260, 470, 130, "Na")
    E.escreve(c, "+", 440, 520, 150, "g", BR)
    Q.atomo(c, 720, 470, 150, "Cl")
    E.escreve(c, "=", 920, 520, 150, "g", BR)
    Q.formula(c, "NaCl", 1060, 545, 230, AMARELO)
    E.escreve(c, "quem entrega", 84, 830, 130, "g", BR)
    E.escreve(c, "o elétron?", 84, 980, 130, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Ligação", "iônica", "e octeto")


def d(c):  # o macete: cruzar as cargas
    palco_capa(c)
    E.escreve(c, "cruze as cargas", 84, 330, 120, "i", BR)
    Q.formula(c, "Al^{3+}  O^{2-}", 84, 580, 200, BR, cores={"carga": CLARO}, escuro=True)
    E.escreve(c, "→", 84, 880, 160, "g", CLARO)
    Q.formula(c, "Al2O3", 320, 900, 250, BR, cores={"indice": CLARO}, escuro=True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quem_entrega_o_eletron", a), ("capa_B_ligacao_ionica", b), ("capa_C_cruze_as_cargas", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
