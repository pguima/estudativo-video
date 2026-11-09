"""Capas do FIS-ELE-002 (1280x720). Uso: python capa.py"""
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
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o erro: dobrou a distância, a força cai pela metade?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "distância × 2", 84, 360, 150, "g", BR)
    E.escreve(c, "força ÷ 2?", 84, 580, 190, "g", BR)
    E.risco(c, 70, 600, 1000, 430, 9, 0, AMARELO, 30)
    E.escreve(c, "não: ÷ 4", 84, 860, 170, "i", BR)
    E.orbita(c, 1560, 560, 280, E.mix(COR, BR, 0.82))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lei de", "Coulomb", "por proporção")


def d(c):  # o macete: d × 2 → F ÷ 4
    palco(c)
    E.escreve(c, "o macete do quadrado", 84, 340, 110, "i", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (l, r) in enumerate((("d × 2", "F ÷ 4"), ("d × 3", "F ÷ 9"))):
        y = 560 + i * 220
        E.escreve(c, l, 90, y, 170, "g", BR)
        F.seta(c, 700, y - 60, 960, y - 60, claro, 1.0, 16)
        E.escreve(c, r, 1040, y, 170, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_forca_pela_metade", a), ("capa_B_lei_de_coulomb", b), ("capa_C_macete_do_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
