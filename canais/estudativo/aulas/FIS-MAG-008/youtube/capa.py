"""Capas do FIS-MAG-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: qual fórmula usar?
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "qual fórmula", 84, 420, 170, "g", BR)
    E.escreve(c, "usar?", 84, 620, 200, "g", AMARELO)
    E.escreve(c, "5 questões de magnetismo", 84, 820, 90, "i", BR)
    for i, s in enumerate(("q·v·B", "B·i·L", "f{ΔΦ}{Δt}", "f{N₁}{N₂}")):
        E.formula(c, s, 1500, 300 + i * 170, 100, "g", BR, 1, "center")


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "magnetismo", "e indução")


def d(c):  # o macete: três perguntas
    palco_capa(c)
    E.escreve(c, "3 perguntas", 84, 340, 150, "g", BR)
    for i, s in enumerate(("corrente cria campo?", "alguém sente força?", "o fluxo muda?")):
        E.escreve(c, f"{i + 1}. {s}", 84, 520 + i * 140, 90, "b", E.mix(COR, BR, 0.5))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_formula_usar", a), ("capa_B_praticando_magnetismo", b), ("capa_C_tres_perguntas", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
