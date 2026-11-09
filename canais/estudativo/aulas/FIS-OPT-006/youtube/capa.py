"""Capas do FIS-OPT-006 (1280x720). Uso: python capa.py"""
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


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def a(c):  # o gancho
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a mesma lupa", 84, 400, 140, "g", BR)
    E.escreve(c, "aumenta", 84, 570, 150, "g", AMARELO)
    E.escreve(c, "e inverte", 84, 730, 150, "g", AMARELO)
    E.escreve(c, "quem decide é a distância", 84, 900, 80, "i", BR)
    p = skia.Path(); p.moveTo(1560, 260); p.quadTo(1720, 560, 1560, 860); p.quadTo(1400, 560, 1560, 260); p.close()
    c.drawPath(p, M.paint("#FFFFFF", 0.35)); c.drawPath(p, M.paint(BR, 1.0, stroke=10))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lentes", "esféricas", "e a imagem")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "olhe a última palavra:", 84, 330, 96, "i", BR)
    E.escreve(c, "convexa", 84, 520, 150, "g", BR)
    E.escreve(c, "= convergente", 84, 680, 110, "g", claro)
    E.escreve(c, "côncava = divergente", 84, 880, 90, "i", BR)
    E.orbita(c, 1640, 300, 170, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_lupa_que_inverte", a), ("capa_B_lentes_do_zero", b), ("capa_C_ultima_palavra", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
