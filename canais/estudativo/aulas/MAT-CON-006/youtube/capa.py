"""Capas do MAT-CON-006 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: √16 é natural, √7 não vira fração
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "r{16} = 4", 90, 470, 200, "g", BR)
    E.formula(c, "r{7} = ?", 90, 820, 200, "g", AMARELO)
    E.escreve(c, "mesma", 1250, 430, 110, "i", BR)
    E.escreve(c, "família?", 1250, 560, 120, "g", BR)
    E.escreve(c, "não vira fração", 1060, 1000, 90, "i", BR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Irracionais", "e reais", "do zero")


def d(c):  # o atalho: eleve ao quadrado
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "eleve ao", 84, 380, 130, "i", BR)
    E.escreve(c, "quadrado", 76, 600, 220, "g", BR)
    E.formula(c, "1,4 < r{2} < 1,5", 84, 900, 160, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mesma_familia", a), ("capa_B_irracionais_e_reais", b), ("capa_C_eleve_ao_quadrado", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
