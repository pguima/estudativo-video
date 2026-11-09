"""Capas do FIS-ELE-021 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho: o erro de esquecer a resistência interna
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "12 ÷ 5 = 2,4 A?", 84, 400, 150, "g", BR)
    E.risco(c, 70, 430, 1220, 300, 9, 0, AMARELO, 26)
    E.escreve(c, "faltou o", 84, 620, 130, "i", BR)
    M.rrect(c, 70, 680, 1000, 230, 30, BR)
    E.escreve(c, "r de dentro", 110, 850, 160, "g", COR)
    E.orbita(c, 1600, 600, 240, E.mix(COR, BR, 0.82))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lei de", "Pouillet", "circuito simples")


def d(c):  # o macete: potência máxima com R = r
    palco_capa(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "potência máxima", 84, 360, 130, "i", BR)
    E.escreve(c, "R = r", 84, 610, 260, "g", E.mix(COR, BR, 0.35))
    E.formula(c, "P = f{ε^2}{4r}", 1500, 560, 170, "g", BR, 1.0, "center")
    E.escreve(c, "rendimento: 50 %", 84, 900, 100, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_faltou_o_r_de_dentro", a), ("capa_B_lei_de_pouillet", b), ("capa_C_potencia_maxima_R_igual_r", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
