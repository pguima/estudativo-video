"""Capas da QUI-EQL-003 (1280x720). Uso: python capa.py"""
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


NOMES = ("capa_A_cem_mil_vezes", "capa_B_ph_e_poh", "capa_C_conte_as_casas")


def a(c):  # o gancho: limão pH 2, água pH 7, 100 000 vezes
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "pH 2 contra pH 7:", 84, 360, 110, "i", BR)
    E.escreve(c, "100 000", 84, 590, 230, "g", AMARELO)
    E.escreve(c, "vezes mais ácido", 84, 790, 140, "g", BR)
    E.escreve(c, "o pH sem medo de log", 84, 990, 84, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "pH e pOH", "sem medo", "do zero")


def d(c):  # o macete: conte as casas
    escuro(c)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete", 84, 320, 120, "i", BR)
    E.formula(c, "0,001 → pH 3", 84, 560, 170, "g", BR)
    E.formula(c, "2 · 10^{−3} → 2,7", 84, 780, 150, "g", claro)
    E.formula(c, "pH + pOH = 14", 84, 960, 100, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in zip(NOMES, (a, b, d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
