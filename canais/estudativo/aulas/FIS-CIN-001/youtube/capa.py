"""Capas do FIS-CIN-001 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
E.usar("Física")


def a(c):  # o erro: misturar unidades
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "72 km/h", 84, 400, 170, "g", BR)
    E.escreve(c, "× 10 s", 84, 590, 170, "g", BR)
    E.escreve(c, "= 720 m?", 84, 800, 190, "g", BR)
    E.risco(c, 70, 840, 980, 650, 9, 0, AMARELO, 30)
    E.orbita(c, 1520, 520, 300, E.mix(COR, BR, 0.82))
    E.escreve(c, "o erro das unidades", 84, 1000, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Grandezas", "e o SI", "do zero")


def d(c):  # o macete: conferir a fórmula pela unidade
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "confira a fórmula", 84, 340, 130, "i", BR)
    E.escreve(c, "pela unidade", 76, 540, 190, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for s, x in (("d", 300), ("=", 520), ("v", 760), ("·", 960), ("t", 1140)):
        E.centro(c, s, x, 800, 170, "g", BR)
    for s, x in (("[m]", 300), ("[m/s]", 760), ("[s]", 1140)):
        E.formula(c, s, x, 960, 90, "b", claro, 1.0, "center")
    F.seta(c, 1330, 880, 1540, 880, claro, 1.0, 14)
    E.selo(c, 1690, 880, 120, True)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_erro_das_unidades", a), ("capa_B_grandezas_e_o_si", b), ("capa_C_confira_pela_unidade", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
