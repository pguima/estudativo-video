"""Capas do MAT-TOP-017 (1280x720). Uso: python capa.py"""
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


def quad(c, x, y, l, n, cor, lw=8):
    for i in range(n):
        for j in range(n):
            c.drawRect(skia.Rect.MakeXYWH(x + j * l + 6, y + i * l + 6, l - 12, l - 12), M.paint(cor, 0.35))
    c.drawRect(skia.Rect.MakeXYWH(x, y, n * l, n * l), M.paint(BR, 1, stroke=lw))
    for i in range(1, n):
        M.line(c, x + i * l, y, x + i * l, y + n * l, BR, 1, 4)
        M.line(c, x, y + i * l, x + n * l, y + i * l, BR, 1, 4)


def a(c):  # o gancho: lado × 2, área × 4
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "lado × 2", 84, 420, 170, "g", BR)
    E.escreve(c, "área × 2?", 84, 640, 150, "i", BR)
    E.risco(c, 70, 660, 700, 540, 9, 0, AMARELO, 26)
    E.escreve(c, "área × 4", 84, 880, 190, "g", AMARELO)
    quad(c, 1060, 640, 170, 1, BR)
    quad(c, 1340, 470, 170, 2, BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Homotetia", "do zero", "lado e área")


def d(c):  # o macete: ache o centro
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "onde está", 84, 400, 150, "i", BR)
    E.escreve(c, "o centro?", 84, 600, 190, "g", BR)
    E.escreve(c, "ligue ponto e imagem", 84, 880, 100, "i", BR)
    O = (1200, 900)
    obj = ((1330, 820), (1460, 820), (1330, 700))
    img = tuple((O[0] + 2.2 * (x - O[0]), O[1] + 2.2 * (y - O[1])) for x, y in obj)
    for A_, B_ in zip(obj, img):
        M.line(c, *O, *B_, "#3CC7D3", 0.9, 5, dash=[16, 12])
    for pts, cor in ((obj, BR), (img, AMARELO)):
        path = skia.Path(); path.addPoly(list(pts), True)
        c.drawPath(path, M.paint(cor, 1, stroke=8))
    c.drawCircle(*O, 22, M.paint("#3CC7D3"))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_area_vezes_4", a), ("capa_B_homotetia", b), ("capa_C_ache_o_centro", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
