"""Capas do FIS-MAG-003 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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
PELE = "#F4D3B8"


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def mao(c, cx, cy, s):
    """mão direita aberta, palma para quem olha, dedos para cima, polegar para a direita"""
    rr = lambda x, y, w, h, r: skia.Path().addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r))
    forma = rr(-0.5 * s, -0.3 * s, s, 0.85 * s, 0.22 * s)
    fw = 0.23 * s
    for dx, L in ((-0.375, 0.5), (-0.125, 0.66), (0.125, 0.72), (0.375, 0.64)):
        forma = skia.Op(forma, rr(dx * s - fw / 2, -0.3 * s - L * s, fw, L * s + 0.2 * s, fw / 2), skia.PathOp.kUnion_PathOp)
    pol = rr(0, -0.13 * s, 0.62 * s, 0.26 * s, 0.13 * s)
    m = skia.Matrix(); m.setRotate(-28); m.postTranslate(0.36 * s, 0.22 * s)
    pol.transform(m)
    forma = skia.Op(forma, pol, skia.PathOp.kUnion_PathOp)
    c.save(); c.translate(cx, cy)
    c.drawPath(forma, M.paint(PELE))
    pt = M.paint("#1B1B22", 1, stroke=8); pt.setStrokeJoin(skia.Paint.kRound_Join)
    c.drawPath(forma, pt)
    c.restore()


def a(c):  # o gancho: a aurora
    palco_capa(c)
    for lado in (-1, 1):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(1450, 540 + lado * 250), 260, [M.hexc("#3CF08A", 0.9), M.hexc("#3CF08A", 0)], [0, 1]))
        c.drawCircle(1450, 540 + lado * 250, 260, p)
    E.bola(c, 1450, 540, 260, "#2F7FC2")
    c.drawCircle(1380, 500, 90, M.paint("#3FA45B", 0.85)); c.drawCircle(1530, 620, 70, M.paint("#3FA45B", 0.85))
    E.escreve(c, "a força que", 84, 380, 130, "i", BR)
    E.escreve(c, "acende a", 84, 570, 170, "g", BR)
    E.escreve(c, "aurora", 84, 760, 190, "g", "#3CF08A")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Força", "magnética", "na carga")


def d(c):  # o macete: a mão do tapa
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "a mão do", 84, 380, 140, "i", BR)
    E.escreve(c, "tapa", 84, 620, 260, "g", BR)
    E.escreve(c, "dá o sentido", 84, 820, 120, "i", AMARELO)
    mao(c, 1430, 600, 330)
    F.seta(c, 1430, 220, 1430, 110, BR, 1, 14)
    F.seta(c, 1760, 560, 1880, 560, BR, 1, 14)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_forca_da_aurora", a), ("capa_B_forca_magnetica_na_carga", b), ("capa_C_a_mao_do_tapa", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
