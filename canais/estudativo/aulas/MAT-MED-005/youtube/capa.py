"""Capas do MAT-MED-005 (1280x720). Uso: python capa.py"""
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


def cubinho(c, x, y, s, cor, borda):
    dx, dy = 0.394 * s, -0.308 * s
    for pts, tinta in (([(x, y - s), (x + s, y - s), (x + s + dx, y - s + dy), (x + dx, y - s + dy)], E.mix(cor, BR, 0.35)),
                       ([(x + s, y), (x + s + dx, y + dy), (x + s + dx, y - s + dy), (x + s, y - s)], E.mix(cor, "#000000", 0.25)),
                       ([(x, y), (x + s, y), (x + s, y - s), (x, y - s)], cor)):
        p = skia.Path(); p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        p.close()
        c.drawPath(p, M.paint(tinta)); c.drawPath(p, M.paint(borda, 1.0, stroke=3))


def a(c):  # o gancho: 2 m³ não são 2 litros
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "2 m³ =", 84, 420, 190, "g", BR)
    E.escreve(c, "2 L", 760, 420, 170, "g", BR)
    E.risco(c, 740, 460, 1100, 290, 9, 0, AMARELO, 30)
    E.escreve(c, "2.000 L", 760, 680, 190, "g", AMARELO)
    E.escreve(c, "a caixa-d'água não encolhe", 84, 960, 100, "i", BR)
    for i in range(2):
        cubinho(c, 1380 + i * 200, 1000, 200, AMARELO, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Volume", "e litros", "metro cúbico")


def d(c):  # o atalho: m³ para litro, vezes mil
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "de", 84, 340, 120, "i", BR); E.escreve(c, "m³", 210, 340, 110, "g", BR); E.escreve(c, "para litro", 400, 340, 120, "i", BR)
    E.escreve(c, "× 1.000", 84, 560, 220, "g", BR)
    E.escreve(c, "1 dm³ = 1 L", 84, 820, 150, "g", AMARELO)
    cubinho(c, 1350, 900, 330, COR, BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_caixa_dagua", a), ("capa_B_volume_e_litros", b), ("capa_C_vezes_mil", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
