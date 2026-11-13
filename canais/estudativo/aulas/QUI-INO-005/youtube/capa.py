"""Capas da QUI-INO-005 (1280x720). Uso: python capa.py"""
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




def a(c):  # o gancho: o repolho que muda de cor
    E.capa_base(c, COR); E.capa_rotulo(c, "Química", COR)
    E.escreve(c, "o repolho roxo", 84, 400, 130, "g", BR)
    E.escreve(c, "diz o pH", 84, 580, 150, "g", AMARELO)
    for k, (cor, x) in enumerate((("#E0457B", 1180), ("#7A3FA0", 1420), ("#9BCB3C", 1660))):
        M.rrect(c, x - 100, 560, 200, 300, 30, cor, 1, shadow=True)
    E.escreve(c, "ácido · neutro · básico", 84, 860, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Química", "Escala", "de pH", "e indicadores")


def d(c):  # o macete: fenolftaleína rosa = base
    palco_capa(c)
    E.escreve(c, "fenolftaleína", 84, 340, 110, "i", BR)
    E.pilula(c, "rosa", 260, 520, 110, "g", fundo="#E85AA8")
    E.escreve(c, "= base", 480, 560, 130, "g", BR)
    E.pilula(c, "incolor", 300, 760, 100, "g", fundo="#3A3B42")
    E.escreve(c, "= não sei", 560, 795, 110, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "ácido ou neutro?", 84, 990, 80, "i", BR)


CAPAS = (("capa_A_repolho_roxo", a), ("capa_B_escala_de_ph", b), ("capa_C_fenolftaleina", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
