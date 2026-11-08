"""Capas do MAT-ESP-005 (1280x720). Uso: python capa.py"""
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
KX, KY = 0.394, -0.308


def agua(c, x, y, w, d, h):
    dx, dy = KX * d, KY * d
    for pts, tinta in (([(x + w, y), (x + w + dx, y + dy), (x + w + dx, y + dy - h), (x + w, y - h)], E.mix(AMARELO, "#000000", 0.2)),
                       ([(x, y - h), (x + w, y - h), (x + w + dx, y - h + dy), (x + dx, y - h + dy)], E.mix(AMARELO, BR, 0.35)),
                       ([(x, y), (x + w, y), (x + w, y - h), (x, y - h)], AMARELO)):
        p = skia.Path(); p.addPoly(pts, True)
        c.drawPath(p, M.paint(tinta))


def a(c):  # o gancho: quantos litros cabem na caixa-d'água?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    x, y, w, d, h = 120, 900, 560, 420, 280
    agua(c, x, y, w, d, h * 0.8)
    E.paralelepipedo(c, 99, 0, x, y, w, d, h, escuro=True, cor=BR, preenche=0.0, largura=8)
    E.escreve(c, "2 × 1,5 × 1", 900, 400, 130, "g", BR)
    E.escreve(c, "quantos litros?", 900, 560, 100, "i", BR)
    E.escreve(c, "3.000 L", 890, 800, 210, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Volume", "da caixa", "cubo e bloco")


def d(c):  # o atalho: medir em decímetros
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 110, "i", BR)
    E.escreve(c, "meça em dm", 76, 560, 190, "g", BR)
    E.escreve(c, "e sai em litros", 84, 720, 120, "i", BR)
    E.escreve(c, "1 dm³ = 1 L", 80, 940, 150, "g", AMARELO)
    s = 300
    x, y = 1380, 820
    dx, dy = KX * s, KY * s
    for pts, tinta in (([(x, y - s), (x + s, y - s), (x + s + dx, y - s + dy), (x + dx, y - s + dy)], E.mix(COR, BR, 0.35)),
                       ([(x + s, y), (x + s + dx, y + dy), (x + s + dx, y - s + dy), (x + s, y - s)], E.mix(COR, "#000000", 0.25)),
                       ([(x, y), (x + s, y), (x + s, y - s), (x, y - s)], COR)):
        p = skia.Path(); p.addPoly(pts, True)
        c.drawPath(p, M.paint(tinta)); c.drawPath(p, M.paint(BR, 1, stroke=5))
    E.centro(c, "1 L", x + s / 2, y - s / 2 + 40, 110, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_quantos_litros", a), ("capa_B_volume_da_caixa", b), ("capa_C_meca_em_dm", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
