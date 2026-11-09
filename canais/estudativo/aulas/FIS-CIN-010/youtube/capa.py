"""Capas do FIS-CIN-010 (1280x720). Uso: python capa.py"""
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
E.usar("Física")


def palco(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Física", COR)


def a(c):  # o gancho: o difícil é escolher a fórmula
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.55)
    E.escreve(c, "qual fórmula", 84, 410, 160, "g", BR)
    E.escreve(c, "usar?", 84, 600, 180, "g", AMARELO)
    E.escreve(c, "5 questões de cinemática", 84, 770, 84, "i", claro)
    for i in range(5):
        x = 1240 + (i % 3) * 210
        y = 300 + (i // 3) * 300
        M.rrect(c, x, y, 180, 230, 26, BR if i % 2 == 0 else AMARELO, 1.0)
        E.centro(c, str(i + 1), x + 90, y + 160, 140, "g", COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Praticando", "cinemática", "5 questões")


def d(c):  # o macete: a grandeza que falta
    palco(c)
    E.escreve(c, "a grandeza que falta", 84, 330, 110, "i", BR)
    E.escreve(c, "escolhe a fórmula", 76, 520, 150, "g", BR)
    claro = E.mix(COR, BR, 0.5)
    for i, (f_, sem) in enumerate((("v = v₀ + a·t", "Δs"), ("v² = v₀² + 2·a·Δs", "t"), ("Δs = (v₀ + v)/2 · t", "a"))):
        y = 700 + i * 140
        E.escreve(c, f_, 120, y, 90, "g", claro)
        M.rrect(c, 1250, y - 80, 220, 100, 50, COR, 1.0)
        E.centro(c, "sem " + sem, 1360, y - 6, 56, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_qual_formula_usar", a), ("capa_B_praticando_cinematica", b), ("capa_C_a_grandeza_que_falta", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
