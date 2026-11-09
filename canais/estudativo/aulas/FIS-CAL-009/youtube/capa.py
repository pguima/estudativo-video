"""Capas do FIS-CAL-009 (1280x720). Uso: python capa.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E
import fisica as F
import motor as M
BR = "#FFFFFF"
AMARELO = "#FFD500"
COR = E.MATERIAS["Física"]["cor"]
CLARO = E.mix(COR, BR, 0.82)
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: o metal parece mais frio
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "por que o metal", 84, 380, 120, "i", BR)
    E.escreve(c, "parece mais", 84, 560, 170, "g", BR)
    E.escreve(c, "frio?", 84, 760, 200, "g", AMARELO)
    E.escreve(c, "os dois estão a 20 °C", 84, 960, 80, "i", BR)
    M.rrect(c, 1200, 540, 280, 300, 24, "#C9CDD2")
    M.rrect(c, 1540, 540, 280, 300, 24, "#8B5E3C")
    E.centro(c, "metal", 1340, 910, 60, "g", BR)
    E.centro(c, "madeira", 1680, 910, 60, "g", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Condução", "de calor", "lei de Fourier")


def d(c):  # o macete: calcule o fator
    palco_capa(c)
    E.escreve(c, "não calcule o fluxo:", 84, 340, 120, "i", BR)
    E.escreve(c, "calcule o fator", 84, 540, 170, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "Φ = f{k · A · ΔT}{L}", 84, 850, 150, "g", BR)
    E.formula(c, "L × 2 → Φ ÷ 2", 1000, 840, 100, "g", claro)


CAPAS = (("capa_A_metal_parece_frio", a), ("capa_B_conducao_de_calor", b), ("capa_C_calcule_o_fator", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
