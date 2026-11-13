"""Capas da QUI-LIG-005 (1280x720). Uso: python capa.py"""
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

def a(c):  # o gancho: 4 questões
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.bola(c, 1460, 560, 300, BR)
    E.centro(c, "4", 1460, 700, 420, "g", COR)
    E.escreve(c, "questões de", 84, 450, 140, "g", BR)
    E.escreve(c, "ligações", 84, 620, 170, "g", AMARELO)
    Q.formula(c, "K2S   O2   MgO", 84, 880, 130, BR)


def b(c):
    E.capa_modelo(c, "Química", "Praticando", "ligações", "4 questões")


def d(c):  # o macete: a carga pela família
    palco_capa(c)
    E.escreve(c, "a carga pela família", 84, 320, 110, "i", BR)
    for k, (f, s) in enumerate((("1", "+1"), ("2", "+2"), ("13", "+3"))):
        E.centro(c, f, 300 + 360 * k, 520, 80, "b", BR); E.centro(c, s, 300 + 360 * k, 650, 130, "g", CLARO)
    for k, (f, s) in enumerate((("15", "−3"), ("16", "−2"), ("17", "−1"))):
        E.centro(c, f, 300 + 360 * k, 820, 80, "b", BR); E.centro(c, s, 300 + 360 * k, 950, 130, "g", CLARO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quatro_questoes", a), ("capa_B_praticando_ligacoes", b), ("capa_C_carga_pela_familia", d)):
    c = s.getCanvas()
    c.clear(skia.ColorWHITE)
    fn(c)
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
