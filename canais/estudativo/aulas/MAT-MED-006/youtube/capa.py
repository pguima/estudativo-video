"""Capas do MAT-MED-006 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]
AMARELO = "#FFD500"


def relogio(c, cx, cy, r, frac, cor, decimos=False, fundo=BR, tinta="#111111"):
    c.drawCircle(cx, cy, r, M.paint(fundo))
    p = skia.Path(); p.moveTo(cx, cy); p.arcTo(skia.Rect.MakeXYWH(cx - r, cy - r, 2 * r, 2 * r), -90, 360 * frac, False); p.close()
    c.drawPath(p, M.paint(cor))
    for k in range(12):
        ang = math.radians(-90 + k * 30)
        c.drawLine(cx + math.cos(ang) * r * 0.82, cy + math.sin(ang) * r * 0.82, cx + math.cos(ang) * r * 0.97, cy + math.sin(ang) * r * 0.97, M.paint(tinta, 1, stroke=6))
    if decimos:
        for k in range(10):
            ang = math.radians(-90 + k * 36)
            c.drawLine(cx, cy, cx + math.cos(ang) * r, cy + math.sin(ang) * r, M.paint(tinta, 0.5, stroke=3))
    c.drawCircle(cx, cy, r, M.paint(tinta, 1, stroke=8))


def a(c):  # o gancho: 2,2 h não é 2 h 20 min
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2,2 h =", 84, 420, 190, "g", BR)
    E.escreve(c, "2 h 20 min", 84, 650, 150, "g", BR)
    E.risco(c, 70, 680, 900, 540, 9, 0, AMARELO, 30)
    E.escreve(c, "2 h 12 min", 84, 880, 170, "g", AMARELO)
    relogio(c, 1500, 640, 300, 0.2, AMARELO, decimos=True)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Hora com", "vírgula", "sem errar")


def d(c):  # o atalho: cada décimo de hora são 6 minutos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "cada décimo de hora", 84, 340, 110, "i", BR)
    E.escreve(c, "= 6 min", 84, 560, 220, "g", BR)
    E.escreve(c, "0,2 h = 12 min", 84, 820, 130, "g", AMARELO)
    relogio(c, 1500, 640, 300, 0.2, COR, decimos=True, fundo="#1B1840", tinta=BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_doze_minutos", a), ("capa_B_hora_com_virgula", b), ("capa_C_seis_minutos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
