"""Capas do MAT-RAZ-017 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: o tronco de 300 kg boia, o clipe afunda
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "300 kg", 76, 450, 220, "g", BR)
    E.escreve(c, "boia", 900, 450, 220, "g", AMARELO)
    E.escreve(c, "um clipe", 76, 680, 170, "g", BR)
    E.escreve(c, "afunda", 860, 680, 170, "g", AMARELO)
    E.escreve(c, "por quê? não é o peso", 84, 900, 100, "i", BR)
    M.rrect(c, 1400, 760, 440, 300, 0, E.mix(COR, BR, 0.55), 1)
    M.rrect(c, 1440, 700, 300, 90, 14, "#8A5A2B", 1)
    M.rrect(c, 1750, 1010, 60, 22, 8, "#07070F", 1)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Densidade", "boia?", "ou afunda?")


def d(c):  # o atalho: compare massa e volume
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 360, 150, "i", BR)
    E.escreve(c, "massa < volume", 76, 590, 190, "g", BR)
    E.escreve(c, "= boia", 84, 830, 170, "g", E.mix(COR, BR, 0.6))
    E.escreve(c, "em g e cm³", 1100, 820, 90, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_tronco_boia", a), ("capa_B_densidade", b), ("capa_C_massa_menor_que_volume", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
