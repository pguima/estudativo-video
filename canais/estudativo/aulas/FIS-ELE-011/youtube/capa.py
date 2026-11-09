"""Capas do FIS-ELE-011 (1280x720). Uso: python capa.py"""
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


def lampada(c, cx, cy, r, acesa, cor=BR):
    if acesa:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 2.4, [M.hexc(AMARELO, 0.7), M.hexc(AMARELO, 0)], [0, 1]))
        c.drawCircle(cx, cy, r * 2.4, g)
    c.drawCircle(cx, cy, r, M.paint(AMARELO if acesa else E.mix(COR, "#000000", 0.25)))
    c.drawCircle(cx, cy, r, M.paint(cor, 1.0, stroke=6))
    k = r * 0.68
    M.line(c, cx - k, cy - k, cx + k, cy + k, cor, 1.0, 6)
    M.line(c, cx - k, cy + k, cx + k, cy - k, cor, 1.0, 6)


def a(c):  # o gancho: uma queimou, a fileira toda apagou
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "uma queimou,", 84, 330, 130, "i", BR)
    E.escreve(c, "todas apagam", 84, 520, 170, "g", BR)
    y = 760
    M.line(c, 60, y, 1860, y, BR, 1.0, 8)
    for k in range(6):
        cx = 220 + k * 300
        lampada(c, cx, y, 70, False)
    cx = 220 + 3 * 300
    M.line(c, cx - 90, y - 90, cx + 90, y + 90, AMARELO, 1.0, 16)
    M.line(c, cx - 90, y + 90, cx + 90, y - 90, AMARELO, 1.0, 16)
    E.escreve(c, "por quê?", 84, 980, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Resistores", "em série", "do zero")


def d(c):  # o macete: a tensão se divide na proporção das resistências
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "tensão em cada um", 84, 330, 120, "i", BR)
    E.escreve(c, "sem conta", 84, 510, 170, "g", BR)
    E.escreve(c, "12 V", 1420, 510, 170, "g", E.mix(COR, BR, 0.4))
    x, w, y, h = 120, 1680, 640, 200
    claro = E.mix(COR, BR, 0.4)
    for x0, ww, cor, s1, s2 in ((x, w / 3, claro, "2 Ω", "4 V"), (x + w / 3, w * 2 / 3, COR, "4 Ω", "8 V")):
        M.rrect(c, x0 + 6, y, ww - 12, h, 20, cor)
        E.centro(c, s1, x0 + ww / 2, y + h / 2 + 30, 90, "g", BR)
        E.centro(c, s2, x0 + ww / 2, y + h + 130, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_uma_queimou_todas_apagam", a), ("capa_B_resistores_em_serie", b), ("capa_C_tensao_sem_conta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
