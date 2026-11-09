"""Capas do FIS-ELE-019 (1280x720). Uso: python capa.py"""
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


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)


def lampada(c, cx, cy, r, b, cor_linha=BR):
    if b > 0:
        g = skia.Paint(AntiAlias=True)
        g.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r * 3, [M.hexc(AMARELO, 0.8 * b), M.hexc(AMARELO, 0)], [0, 1]))
        c.drawCircle(cx, cy, r * 3, g)
    c.drawCircle(cx, cy, r, M.paint(E.mix("#FFFFFF", AMARELO, b)))
    c.drawCircle(cx, cy, r, M.paint(cor_linha, 1, stroke=10))
    k = r * 0.68
    M.line(c, cx - k, cy - k, cx + k, cy + k, cor_linha, 1, 10)
    M.line(c, cx - k, cy + k, cx + k, cy - k, cor_linha, 1, 10)


def a(c):  # o gancho: no inverno, a resistência é MENOR
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "chuveiro no", 84, 380, 130, "i", BR)
    E.escreve(c, "inverno:", 84, 560, 190, "g", BR)
    M.rrect(c, 70, 640, 900, 230, 30, BR)
    E.escreve(c, "MENOS R", 110, 815, 170, "g", COR)
    E.orbita(c, 1560, 560, 280, E.mix(COR, BR, 0.82))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Chuveiro", "e lâmpadas", "série e paralelo")


def d(c):  # o macete: em série, brilha a de menor potência
    palco_capa(c)
    E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "em série, brilha", 84, 340, 120, "i", BR)
    E.escreve(c, "a de menor", 84, 520, 170, "g", BR)
    E.escreve(c, "potência", 84, 700, 170, "g", E.mix(COR, BR, 0.35))
    lampada(c, 1380, 820, 95, 0.9)
    lampada(c, 1700, 820, 95, 0.15)
    E.centro(c, "25 W", 1380, 1000, 64, "g", BR)
    E.centro(c, "100 W", 1700, 1000, 64, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_chuveiro_no_inverno", a), ("capa_B_chuveiro_e_lampadas", b), ("capa_C_serie_brilha_a_menor", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
