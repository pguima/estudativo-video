"""Capas da QUI-ATO-012 (1280x720). Uso: python capa.py"""
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
AMBAR = "#F2A33A"
COR = E.MATERIAS["Química"]["cor"]
E.usar("Química")


def grade(c, x, y, cel, cor="#FFFFFF", a=0.85):
    for s, (z, per, g) in Q._posicoes().items():
        if g is None:
            continue
        M.rrect(c, x + (g - 1) * cel + 2, y + (per - 1) * cel + 2, cel - 4, cel - 4, cel * 0.14, cor, a)


def a(c):  # o gancho: lítio ou césio, quem reage mais?
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "lítio ou césio:", 84, 380, 130, "g", BR)
    E.escreve(c, "quem explode", 84, 560, 150, "g", AMARELO)
    E.escreve(c, "mais na água?", 84, 720, 120, "g", AMARELO)
    E.escreve(c, "4 questões de tabela periódica", 84, 880, 70, "i", BR)
    E.bola(c, 1400, 520, 100, E.mix(COR, BR, 0.6)); Q.formula(c, "Li", 1400, 550, 80, E.TINTA, 1, "center")
    E.bola(c, 1660, 640, 200, E.mix(COR, BR, 0.6)); Q.formula(c, "Cs", 1660, 690, 140, E.TINTA, 1, "center")


def b(c):
    E.capa_modelo(c, "Química", "Praticando:", "a tabela", "4 questões")


def d(c):  # o macete: duas setas resolvem
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "duas setas", 84, 420, 160, "g", BR)
    E.escreve(c, "resolvem a prova", 84, 580, 110, "i", claro)
    grade(c, 1060, 300, 44, "#4A4E5C", 1)
    M.arrow(c, 1800, 330, 1110, 580, AMBAR, 1, 16, 50)
    M.arrow(c, 1160, 600, 1790, 360, claro, 1, 16, 50)
    E.escreve(c, "raio", 1060, 720, 70, "g", AMBAR)
    E.escreve(c, "ionização e", 1330, 700, 54, "g", claro)
    E.escreve(c, "eletronegatividade", 1330, 770, 54, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_litio_ou_cesio", a), ("capa_B_praticando_a_tabela", b), ("capa_C_duas_setas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
