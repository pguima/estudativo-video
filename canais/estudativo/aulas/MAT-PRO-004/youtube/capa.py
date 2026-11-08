"""Capas do MAT-PRO-004 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AM = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def caixa(c, cx, cy, w, h, s, pos, cor=BR, fundo=None, size=120):
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 26, 26)
    if fundo:
        c.drawRRect(rr, M.paint(fundo))
    c.drawRRect(rr, M.paint(cor, 1, stroke=9))
    E.centro(c, s, cx, cy + size * 0.36, size, "g", cor)
    E.centro(c, pos, cx, cy + h / 2 + 76, 64, "b", cor)


def a(c):  # o gancho: qual é o 20º termo?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    for i, v in enumerate((5, 9, 13, 17)):
        caixa(c, 190 + i * 300, 400, 240, 200, str(v), f"{i + 1}º")
    E.escreve(c, "…", 1290, 430, 160, "g", BR)
    caixa(c, 1640, 400, 260, 200, "?", "20º", AM)
    E.escreve(c, "uma conta só", 84, 880, 150, "i", BR)
    E.escreve(c, "= 81", 1140, 880, 170, "g", AM)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Termo geral", "da PA", "sem listar tudo")


def d(c):  # o atalho: pule de um termo conhecido
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "pule termos", 76, 540, 200, "g", BR)
    cl = E.mix(COR, BR, 0.55)
    caixa(c, 420, 790, 240, 180, "13", "3º", BR, "#1A1830", 110)
    caixa(c, 1500, 790, 240, 180, "81", "20º", AM, "#1A1830", 110)
    E.salto(c, 9, 0, 560, 1360, 760, 120, cl, "17 saltos", size=64)
    E.centro(c, "13 + 17 · 4", 960, 900, 80, "g", cl)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_vigesimo_termo", a), ("capa_B_termo_geral", b), ("capa_C_pule_termos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
