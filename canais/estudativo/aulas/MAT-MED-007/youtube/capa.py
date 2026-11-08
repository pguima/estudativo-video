"""Capas do MAT-MED-007 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def a(c):  # o gancho: 5 h 75 min não existe
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "3 h 50 + 2 h 25", 84, 400, 150, "g", BR)
    E.escreve(c, "= 5 h 75 min?", 84, 620, 150, "g", BR)
    E.risco(c, 300, 650, 1080, 500, 9, 0, AMARELO, 30)
    E.escreve(c, "= 6 h 15 min", 84, 860, 170, "g", AMARELO)
    M.rrect(c, 1340, 640, 480, 230, 34, "#07070F")
    E.centro(c, "5:75", 1580, 810, 170, "g", "#FF5A5A")
    E.selo(c, 1810, 640, 60, False)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Somar", "horas", "e subtrair")


def d(c):  # o atalho: complete a hora cheia
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "complete a", 84, 340, 130, "i", BR)
    E.escreve(c, "hora cheia", 84, 560, 220, "g", BR)
    y = 860
    c.drawLine(120, y, 1800, y, M.paint(BR, 1, stroke=6))
    for x, s in ((200, "14:40"), (560, "15:00"), (1340, "17:00"), (1720, "17:10")):
        c.drawLine(x, y - 22, x, y + 22, M.paint(BR, 1, stroke=6))
        E.centro(c, s, x, y + 90, 60, "b", BR)
    for x0, x1, s in ((200, 560, "20 min"), (560, 1340, "2 h"), (1340, 1720, "10 min")):
        p = skia.Path(); p.moveTo(x0, y - 10); p.quadTo((x0 + x1) / 2, y - 170, x1, y - 10)
        c.drawPath(p, M.paint(AMARELO, 1, stroke=8, cap_round=True))
        E.centro(c, s, (x0 + x1) / 2, y - 110, 56, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_e_setenta_e_cinco", a), ("capa_B_somar_subtrair_horas", b), ("capa_C_hora_cheia", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
