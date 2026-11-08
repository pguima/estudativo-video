"""Capas do MAT-EST-005 (1280x720). Uso: python capa.py"""
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
FREQ = [2, 7, 7, 3, 1]


def hist(c, x, y, w, h, freqs, cores, fundo, rotulos=None, size=44):
    """colunas coladas, base em y + h; rotulos = limites embaixo"""
    n, vmax = len(freqs), max(freqs) * 1.1
    cw = w / n
    M.line(c, x - 10, y + h, x + w + 10, y + h, BR, 0.8, 6)
    for i, f in enumerate(freqs):
        top = y + h - f / vmax * h
        c.drawRect(skia.Rect.MakeLTRB(x + i * cw, top, x + (i + 1) * cw, y + h), M.paint(cores[i]))
        c.drawRect(skia.Rect.MakeLTRB(x + i * cw, top, x + (i + 1) * cw, y + h), M.paint(fundo, 1, stroke=6))
    if rotulos:
        for i, s in enumerate(rotulos):
            E.centro(c, s, x + i * cw, y + h + size + 14, size, "b", BR)


def a(c):  # o gancho: parece barras, mas é histograma
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    hist(c, 1040, 260, 760, 560, FREQ, [BR] * 5, COR, ["10", "20", "30", "40", "50", "60"])
    E.escreve(c, "colunas coladas?", 84, 360, 100, "i", BR)
    E.escreve(c, "não é", 84, 560, 150, "g", BR)
    E.escreve(c, "barras", 84, 740, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Histograma:", "como ler", "e não confundir")


def d(c):  # o atalho: conte o lado menor
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "conte o", 84, 360, 110, "i", BR)
    E.escreve(c, "lado menor", 84, 560, 140, "g", AMARELO)
    E.escreve(c, "20 − 9 = 11", 84, 760, 130, "g", BR)
    hist(c, 1180, 300, 640, 520, FREQ, [AMARELO, AMARELO, "#3A3A55", "#3A3A55", "#3A3A55"], "#07070F")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_barras", a), ("capa_B_histograma", b), ("capa_C_lado_menor", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
