"""Capas do MAT-ESP-002 (1280x720). Uso: python capa.py"""
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


def quadrado(c, x, y, s, n, fundo, tinta, borda):
    c.drawRect(skia.Rect.MakeXYWH(x, y, s, s), M.paint(fundo))
    c.drawRect(skia.Rect.MakeXYWH(x, y, s, s), M.paint(borda, 1, stroke=8))
    if n:
        E.centro(c, n, x + s / 2, y + s / 2 + s * 0.2, s * 0.55, "g", tinta)


def a(c):  # o gancho: qual face fica de frente para o 1?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    s, x0, y0 = 190, 330, 210
    for n, (i, j) in {"1": (0, 0), "2": (0, 1), "3": (0, 2), "4": (0, 3), "5": (-1, 1), "6": (1, 1)}.items():
        quadrado(c, x0 + i * s, y0 + j * s, s, n if n in "1" else "?" if n == "3" else "",
                 AMARELO if n == "1" else BR if n != "3" else E.mix(COR, BR, 0.75), COR, COR)
    E.escreve(c, "qual face", 940, 430, 150, "g", BR)
    E.escreve(c, "fica de frente", 940, 600, 120, "i", BR)
    E.escreve(c, "para o 1?", 940, 790, 170, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Moldes", "de sólidos", "montar e desmontar")


def d(c):  # o atalho: pula uma
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho do cubo", 84, 360, 110, "i", BR)
    E.escreve(c, "pula uma", 76, 590, 230, "g", BR)
    s, x0, y0 = 200, 1000, 800
    for i, n in enumerate("1234"):
        quadrado(c, x0 + i * s, y0, s, n, AMARELO if n in "13" else "#1A1840", "#07070F" if n in "13" else BR, BR)
    E.arco(c, x0 + s * 1.5, y0 - 10, s, 180, 180, AMARELO, 12)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_face", a), ("capa_B_moldes_de_solidos", b), ("capa_C_pula_uma", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
