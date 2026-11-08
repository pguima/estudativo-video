"""Capas do MAT-RAZ-023 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: o apartamento do tamanho de um tapetinho
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "apartamento de", 84, 360, 120, "i", BR)
    E.escreve(c, "0,24 m²?", 84, 600, 230, "g", BR)
    E.risco(c, 70, 640, 1000, 430, 9, 0, "#FFD500", 30)
    E.escreve(c, "a planta de 1 : 200", 84, 840, 100, "i", BR)
    E.escreve(c, "dá 48 m²", 84, 980, 130, "g", BR)
    u, x, y = 100, 1360, 440
    for i in range(4):
        for j in range(3):
            c.drawRect(skia.Rect.MakeXYWH(x + i * u + 4, y + j * u + 4, u - 8, u - 8), M.paint(BR, 0.85))
    c.drawRect(skia.Rect.MakeXYWH(x, y, 4 * u, 3 * u), M.paint(BR, stroke=8))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "escalas", "5 situações de prova")


def d(c):  # o macete
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cl = E.mix(COR, BR, 0.55)
    for i, (l1, l2) in enumerate((("comprimento", "× escala"), ("área", "× escala²"), ("volume", "× escala³"))):
        y = 400 + i * 230
        E.escreve(c, l1, 84, y, 130, "i", cl)
        E.escreve(c, l2, 900, y, 160, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_apartamento_tapetinho", a), ("capa_B_praticando_escalas", b), ("capa_C_direto_quadrado_cubo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
