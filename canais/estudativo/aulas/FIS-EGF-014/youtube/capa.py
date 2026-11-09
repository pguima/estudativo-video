"""Capas do FIS-EGF-014 (1280x720). Uso: python capa.py"""
import math, subprocess, sys
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
E.usar("Física")


def palco_capa(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: 5 situações, da alavanca ao satélite
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "5 situações", 84, 400, 180, "g", BR)
    E.escreve(c, "da alavanca", 84, 570, 120, "i", BR)
    E.escreve(c, "ao satélite", 84, 720, 150, "g", AMARELO)
    claro = E.mix(COR, BR, 0.82)
    p = skia.Path(); p.moveTo(1400, 700); p.lineTo(1340, 800); p.lineTo(1460, 800); p.close()
    c.drawPath(p, M.paint(claro))
    M.rrect(c, 1120, 668, 560, 32, 10, claro)
    F.bloco(c, 1180, 610, 100, 100, "?", cor="#1B1B20", size=50)
    E.bola(c, 1640, 330, 90, "#2F6FB0")
    pt = M.paint(BR, 0.8, stroke=5); pt.setPathEffect(skia.DashPathEffect.Make([18, 14], 0))
    c.drawCircle(1640, 330, 150, pt)
    M.rrect(c, 1770, 240, 40, 40, 6, "#1B1B20")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Torque e", "gravitação", "praticando")


def d(c):  # o macete: procure o fator
    palco_capa(c)
    E.escreve(c, "antes da conta,", 84, 330, 100, "i", BR)
    E.escreve(c, "procure o fator", 84, 490, 130, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    E.formula(c, "braço × 4  →  força ÷ 4", 84, 720, 100, "g", claro)
    E.formula(c, "raio × 4  →  ano × 8", 84, 900, 100, "g", AMARELO)


CAPAS = (("capa_A_cinco_situacoes", a), ("capa_B_praticando_torque_gravitacao", b), ("capa_C_procure_o_fator", d))

pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in CAPAS:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
