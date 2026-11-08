"""Capas do MAT-RAZ-022 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: a sala de 0,2 m²
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "20 cm² × 100", 84, 400, 150, "g", BR)
    E.escreve(c, "= 0,2 m²?", 84, 640, 230, "g", BR)
    E.risco(c, 70, 680, 1080, 470, 9, 0, "#FFD500", 30)
    E.escreve(c, "a sala tem", 84, 900, 130, "i", BR)
    E.escreve(c, "20 m²", 84 + E.larg("a sala tem ", "i", 130), 900, 130, "g", BR)
    # a planta: 5 × 4 quadradinhos
    u, x, y = 90, 1340, 420
    for i in range(5):
        for j in range(4):
            c.drawRect(skia.Rect.MakeXYWH(x + i * u + 4, y + j * u + 4, u - 8, u - 8), M.paint(BR, 0.85))
    c.drawRect(skia.Rect.MakeXYWH(x, y, 5 * u, 4 * u), M.paint(BR, stroke=8))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Escala", "de área", "e de volume")


def d(c):  # o macete
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cl = E.mix(COR, BR, 0.55)
    E.escreve(c, "converta", 84, 380, 150, "i", BR)
    E.escreve(c, "os lados", 84, 600, 220, "g", BR)
    E.escreve(c, "não a área", 84, 820, 150, "i", cl)
    E.escreve(c, "5 cm × 4 cm", 1080, 560, 100, "g", cl)
    E.escreve(c, "5 m × 4 m", 1080, 720, 100, "g", BR)
    E.escreve(c, "= 20 m²", 1080, 880, 130, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_sala_de_02m2", a), ("capa_B_escala_area_volume", b), ("capa_C_converta_os_lados", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
