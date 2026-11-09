"""Capas do FIS-OPT-008 (1280x720). Uso: python capa.py"""
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
    E.escreve(c, "por que o míope", 84, 400, 130, "g", BR)
    E.escreve(c, "usa grau", 84, 560, 150, "g", BR)
    E.escreve(c, "negativo?", 84, 730, 160, "g", AMARELO)
    E.escreve(c, "miopia, hipermetropia e astigmatismo", 84, 890, 64, "i", BR)
    M.rrect(c, 1360, 300, 450, 320, 24, BR)
    E.escreve(c, "receita", 1410, 380, 50, "i", "#6B6B76")
    E.escreve(c, "−2,00", 1410, 560, 130, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Olho", "humano", "e os defeitos da visão")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "Míope →", 84, 450, 200, "g", BR)
    E.escreve(c, "Menos", 84, 680, 220, "g", claro)
    E.escreve(c, "lente divergente, grau negativo", 84, 880, 76, "i", BR)
    E.orbita(c, 1640, 300, 170, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_miope_usa_menos", a), ("capa_B_olho_humano", b), ("capa_C_miope_menos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
