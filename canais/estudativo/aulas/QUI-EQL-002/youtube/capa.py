"""Capas da QUI-EQL-002 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)


NOMES = ("capa_A_para_que_lado", "capa_B_le_chatelier", "capa_C_calor_como_substancia")


def a(c):  # o gancho: para que lado vai o equilíbrio?
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    Q.formula(c, "N2 + 3 H2 <=> 2 NH3", 84, 380, 120, BR)
    E.escreve(c, "para que", 84, 600, 190, "g", BR)
    E.escreve(c, "lado vai?", 84, 800, 190, "g", AMARELO)
    E.escreve(c, "o equilíbrio foge da mudança", 84, 990, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Le", "Chatelier", "do zero")


def d(c):  # o macete: calor como substância
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete", 84, 320, 120, "i", BR)
    Q.formula(c, "N2 + 3 H2 <=> 2 NH3 + calor", 84, 540, 110, BR, escuro=True)
    E.escreve(c, "esquentou?", 84, 760, 140, "g", BR)
    E.escreve(c, "foge do calor", 84, 930, 140, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
