"""Capas do MAT-RAZ-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 2 km = R$ 11, 4 km = R$ 22?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "táxi", 84, 300, 120, "i", BR)
    E.escreve(c, "2 km  R$ 11", 84, 500, 150, "g", BR)
    E.escreve(c, "4 km  R$ 22?", 84, 700, 150, "g", AMARELO)
    w = E.larg("4 km  ", "g", 150)
    E.risco(c, 84 + w - 20, 730, 84 + E.larg("4 km  R$ 22?", "g", 150) + 20, 590, 9, 0, BR, 26)
    E.escreve(c, "não é proporcional", 84, 950, 120, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "O teste", "do dobro", "direta ou inversa")


def d(c):  # o atalho: o teste do zero
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    cl = E.mix(COR, BR, 0.55)
    E.escreve(c, "o atalho:", 84, 340, 140, "i", BR)
    E.escreve(c, "o teste do zero", 76, 540, 180, "g", BR)
    E.escreve(c, "0 km → R$ 5", 84, 800, 150, "g", cl)
    E.pilula(c, "não é direta", 1450, 750, 80, "g", fundo="#E5484D")


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_taxi_nao_dobra", a), ("capa_B_teste_do_dobro", b), ("capa_C_teste_do_zero", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
