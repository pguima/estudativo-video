"""Capas do MAT-ANA-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: duas equações, a mesma reta
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "y = 2x + 1", 84, 400, 170, "g", BR)
    E.escreve(c, "2x − y + 1 = 0", 84, 610, 170, "g", BR)
    M.line(c, 1500, 1000, 1880, 240, AMARELO, 1, 18)
    c.drawCircle(1690, 620, 30, M.paint(BR))
    E.escreve(c, "a mesma reta!", 84, 900, 140, "i", AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Equação", "da reta", "3 jeitos")


def d(c):  # o atalho: ponto e inclinação
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "a reta numa", 84, 380, 140, "i", BR)
    E.escreve(c, "linha só", 76, 580, 190, "g", BR)
    x = 84
    for s, cor in (("y − y₀ = ", BR), ("m", claro), ("(x − x₀)", BR)):
        E.formula(c, s, x, 880, 150, "g", cor)
        x += E.formula(None, s, 0, 0, 150, "g", a=0)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_a_mesma_reta", a), ("capa_B_equacao_da_reta", b), ("capa_C_numa_linha_so", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
