"""Capas do MAT-DIV-005 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import motor as M
BR = "#FFFFFF"
COR = E.MATERIAS["Matemática"]["cor"]


def a(c):  # o gancho: o MMC de 12, 18 e 30
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "MMC de", 116, 370, 170, "i", BR)
    E.escreve(c, "12, 18 e 30", 110, 640, 280, "g", BR)
    E.escreve(c, "em menos de", 116, 860, 130, "i", BR)
    E.escreve(c, "1 minuto", 116, 1000, 150, "g", "#FFD500")


def b(c):  # o método
    E.capa_modelo(c, "Matemática", "Calcular", "o MMC", "sem listar")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 116, 370, 150, "i", BR)
    E.escreve(c, "MMC × MDC", 110, 620, 250, "g", BR)
    E.escreve(c, "= a × b", 116, 860, 210, "g", E.mix(COR, BR, 0.5))
    E.escreve(c, "só para 2 números", 860, 850, 90, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_mmc_12_18_30", a), ("capa_B_calcular_mmc", b), ("capa_C_atalho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
