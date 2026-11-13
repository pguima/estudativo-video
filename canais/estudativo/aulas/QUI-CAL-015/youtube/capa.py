"""Capas da QUI-CAL-015 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Química", COR)
def a(c):  # o desafio: 5 questões de gases
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "gases", 84, 360, 150, "g", BR)
    E.escreve(c, "5 questões", 84, 600, 220, "g", AMARELO)
    E.escreve(c, "pneu · balão · cilindro · mergulho", 84, 790, 70, "g", BR)
    E.escreve(c, "você resolve antes de mim?", 84, 990, 90, "i", BR)


def b(c):
    E.capa_modelo(c, "Química", "Praticando", "gases", "estudo dos gases")


def d(c):  # o macete: a lista de conferência
    palco(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "antes de responder:", 84, 330, 110, "i", BR)
    for k, s in enumerate(("kelvin?", "unidades do R?", "o que fica parado?")):
        E.selo(c, 140, 520 + k * 170 - 40, 46, True)
        E.escreve(c, s, 220, 520 + k * 170, 110, "g", claro if k == 1 else BR)


CAPAS = (("capa_A_5_questoes", a), ("capa_B_praticando_gases", b), ("capa_C_lista_de_conferencia", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
