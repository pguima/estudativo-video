"""Capas do MAT-CON-007 (1280x720). Uso: python capa.py"""
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


def reta(c, x0, x1, y, a, b, vmin, vmax, fecha_a, fecha_b, cor=AMARELO):
    vx = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    M.line(c, x0, y, x1, y, BR, 1.0, 8)
    for v in range(vmin, vmax + 1):
        M.line(c, vx(v), y - 22, vx(v), y + 22, BR, 1.0, 6)
        E.centro(c, str(v), vx(v), y + 90, 60, "b", BR)
    M.line(c, vx(a), y, vx(b), y, cor, 1.0, 18, cap_round=False)
    for v, f in ((a, fecha_a), (b, fecha_b)):
        c.drawCircle(vx(v), y, 26, M.paint(cor if f else COR))
        c.drawCircle(vx(v), y, 26, M.paint(cor, 1.0, stroke=9))


def a(c):  # o gancho: entre 2 e 5 não são só 3 e 4
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "entre 2 e 5", 84, 380, 120, "i", BR)
    E.escreve(c, "só 3 e 4?", 84, 600, 200, "g", BR)
    E.escreve(c, "]2, 5]", 1250, 600, 220, "g", AMARELO)
    reta(c, 140, 1780, 860, 2, 5, 1, 6, False, True)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Intervalos", "na reta", "sem confundir")


def d(c):  # o atalho: o tracinho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "olhe o", 84, 380, 130, "i", BR)
    E.escreve(c, "tracinho", 76, 600, 220, "g", BR)
    E.escreve(c, "≤  →  ]", 84, 900, 200, "g", AMARELO)
    E.escreve(c, "<  →  [", 1050, 900, 200, "g", E.mix(COR, BR, 0.55))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_so_3_e_4", a), ("capa_B_intervalos_na_reta", b), ("capa_C_olhe_o_tracinho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
