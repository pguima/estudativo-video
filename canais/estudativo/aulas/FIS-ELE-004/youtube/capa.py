"""Capas do FIS-ELE-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o erro: d² no potencial
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "potencial com d²?", 84, 360, 130, "g", BR)
    E.formula(c, "V = f{k · Q}{d^2}", 84, 620, 170, "g", BR)
    E.risco(c, 70, 700, 760, 430, 9, 0, AMARELO, 30)
    E.formula(c, "V = f{k · Q}{d}", 900, 620, 170, "g", E.mix(COR, BR, 0.82))
    E.escreve(c, "sem quadrado", 900, 900, 110, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Potencial", "elétrico", "e energia")


def d(c):  # o macete: volt = joule por coulomb e τ = q·U
    palco(c)
    E.escreve(c, "volt mede o quê?", 84, 340, 110, "i", BR)
    E.escreve(c, "1 V = 1 J/C", 84, 580, 190, "g", BR)
    E.escreve(c, "τ = q · U", 84, 830, 160, "g", E.mix(COR, BR, 0.5))
    E.orbita(c, 1520, 640, 280, E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_potencial_sem_quadrado", a), ("capa_B_potencial_eletrico", b), ("capa_C_volt_joule_por_coulomb", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
