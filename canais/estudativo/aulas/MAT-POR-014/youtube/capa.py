"""Capas do MAT-POR-014 (1280x720). Uso: python capa.py"""
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


def caixa(c, s, cx, cy, size, fundo, cor):
    w, h = E.larg(s, "g", size) + size * 1.0, size * 1.6
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 26, 26), M.paint(fundo))
    E.centro(c, s, cx, cy + size * 0.36, size, "g", cor)


def a(c):  # o gancho: o erro menor pesa mais
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "qual erro pesa mais?", 84, 270, 110, "i", BR)
    caixa(c, "1 cm em 2 m", 500, 470, 104, BR, COR)
    caixa(c, "1 mm em 1 cm", 1380, 470, 104, BR, COR)
    E.centro(c, "0,5%", 500, 760, 120, "g", E.mix(COR, BR, 0.55))
    E.bola(c, 1380, 780, 190, AMARELO)
    E.centro(c, "10%", 1380, 830, 140, "g", COR)
    E.centro(c, "ou", 940, 500, 90, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Erro", "relativo", "qual erro pesa mais?")


def d(c):  # o atalho: mesmo número em cima, olhe embaixo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 300, 130, "i", BR)
    E.escreve(c, "olhe só embaixo", 84, 470, 150, "g", BR)
    E.fracao(c, 1, 200, 520, 760, 170, E.mix(COR, BR, 0.55))
    E.centro(c, "<", 900, 800, 170, "g", BR)
    E.fracao(c, 1, 10, 1260, 760, 170, AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_erro_pesa_mais", a), ("capa_B_erro_relativo", b), ("capa_C_olhe_embaixo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
