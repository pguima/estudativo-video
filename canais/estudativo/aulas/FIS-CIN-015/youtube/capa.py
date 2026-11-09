"""Capas do FIS-CIN-015 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: empurrada ou solta, chegam juntas
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "qual chega", 84, 380, 140, "i", BR)
    E.escreve(c, "primeiro?", 84, 570, 180, "g", BR)
    E.escreve(c, "nenhuma: juntas", 84, 770, 110, "i", AMARELO)
    x0, y0, yb = 1500, 560, 960
    M.rrect(c, 1220, y0 + 34, 300, 26, 6, "#5A3A22")
    M.rrect(c, 1240, y0 + 58, 24, yb - y0 - 58, 4, "#5A3A22")
    M.rrect(c, 1476, y0 + 58, 24, yb - y0 - 58, 4, "#5A3A22")
    M.line(c, 1180, yb, 1900, yb, BR, 1.0, 6)
    for k in range(4):
        u = k / 3
        y = y0 + u * u * (yb - 40 - y0)
        E.bola(c, x0 + 320 * u, y, 32, E.mix(COR, BR, 0.85) if k == 3 else E.mix(COR, BR, 0.5))
        E.bola(c, x0 + 30, y, 32, AMARELO if k == 3 else E.mix(AMARELO, COR, 0.5))
        if k:
            M.line(c, x0 + 66, y, x0 + 320 * u - 36, y, BR, 0.5, 3, dash=[12, 10])


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Lançamento", "horizontal", "tempo e alcance")


def d(c):  # o macete: a altura manda no tempo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a altura", 84, 330, 130, "i", BR)
    E.escreve(c, "manda", 76, 510, 180, "g", BR)
    E.escreve(c, "no tempo", 76, 700, 180, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    x0, y0, yb = 1100, 420, 900
    M.rrect(c, x0 - 220, y0 + 30, 220, yb - y0 - 30, 6, "#3A3A48")
    M.line(c, x0 - 240, yb, 1880, yb, BR, 1.0, 5)
    for vx, cor in ((1, claro), (2, BR)):
        pts = [(x0 + 360 * vx * u, y0 + (yb - y0 - 30) * u * u) for u in [i / 40 for i in range(41)]]
        F.poli(c, pts, 1.0, cor, 1.0, 8)
    E.bola(c, x0, y0, 34, COR)
    E.centro(c, "2 s", x0 + 360, yb + 100, 80, "g", claro)
    E.centro(c, "2 s", x0 + 720, yb + 100, 80, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_chega_primeiro", a), ("capa_B_lancamento_horizontal", b), ("capa_C_altura_manda_no_tempo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
