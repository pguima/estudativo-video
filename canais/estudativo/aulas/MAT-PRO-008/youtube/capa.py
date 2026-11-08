"""Capas do MAT-PRO-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 3, 6, 12, 24 … o 8º termo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    xs = (190, 490, 790, 1090)
    for i, (x, v) in enumerate(zip(xs, (3, 6, 12, 24))):
        caixa(c, x, 450, 240, 190, str(v), f"{i + 1}º")
        if i < 3:
            E.salto(c, 9, 0, x, xs[i + 1], 340, 80, AM, "×2", size=64)
    E.escreve(c, "…", 1270, 480, 160, "g", BR)
    caixa(c, 1660, 450, 300, 190, "384", "8º", AM)
    E.escreve(c, "dobra, dobra, dobra…", 84, 920, 120, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Progressão", "geométrica", "razão e termo geral")


def d(c):  # o atalho: pule do termo mais perto
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "pule termos", 76, 540, 190, "g", BR)
    cl = E.mix(COR, BR, 0.55)
    caixa(c, 420, 790, 240, 180, "24", "4º", BR, "#1A1830", 110)
    caixa(c, 1500, 790, 260, 180, "384", "8º", AM, "#1A1830", 110)
    E.salto(c, 9, 0, 560, 1360, 760, 120, cl, "4 saltos", size=64)
    E.formula(c, "24 · 2^4", 960, 900, 84, "g", cl, align="center")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_dobra_384", a), ("capa_B_progressao_geometrica", b), ("capa_C_pule_termos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
