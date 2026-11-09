"""Capas do FIS-OPT-009 (1280x720). Uso: python capa.py"""
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
    E.escreve(c, "microscópio", 84, 400, 150, "g", BR)
    E.escreve(c, "e luneta:", 84, 570, 150, "g", BR)
    E.escreve(c, "o mesmo truque", 84, 740, 130, "g", AMARELO)
    E.escreve(c, "duas lentes convergentes", 84, 890, 76, "i", BR)
    for x, h in ((1400, 420), (1700, 300)):
        p = skia.Path(); p.moveTo(x, 560 - h / 2); p.quadTo(x + 70, 560, x, 560 + h / 2); p.quadTo(x - 70, 560, x, 560 - h / 2); p.close()
        c.drawPath(p, M.paint("#FFFFFF", 0.35)); c.drawPath(p, M.paint(BR, 1.0, stroke=8))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lupa", "e luneta", "e o microscópio")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o macete:", 84, 330, 110, "i", BR)
    E.escreve(c, "conte as", 84, 500, 150, "g", BR)
    E.escreve(c, "imagens reais", 84, 670, 150, "g", claro)
    E.escreve(c, "cada uma vira a imagem de cabeça para baixo", 84, 860, 60, "i", BR)
    E.orbita(c, 1640, 300, 170, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_microscopio_e_luneta", a), ("capa_B_instrumentos_opticos", b), ("capa_C_conte_as_imagens_reais", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
