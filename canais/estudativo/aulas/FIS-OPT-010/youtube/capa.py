"""Capas do FIS-OPT-010 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho
    E.capa_base(c, COR); E.capa_rotulo(c, "Física", COR)
    E.escreve(c, "5", 84, 560, 380, "g", AMARELO)
    E.escreve(c, "questões", 330, 440, 140, "g", BR)
    E.escreve(c, "de óptica", 330, 590, 140, "g", BR)
    E.escreve(c, "do espelho aos óculos, resolvidas", 84, 820, 80, "i", BR)
    E.orbita(c, 1600, 560, 260, E.mix(COR, BR, 0.82))


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Física", "Óptica", "na prática", "5 questões")


def d(c):  # o macete
    palco(c)
    E.capa_rotulo(c, "Física", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "4 atalhos", 84, 340, 140, "g", BR)
    for i, s in enumerate(("altura ÷ 2", "p' = f · p ÷ (p − f)", "sen L = menor ÷ maior", "f (cm) = 100 ÷ grau")):
        E.escreve(c, s, 84, 500 + 130 * i, 84, "g", claro if i % 2 else BR)
    E.orbita(c, 1640, 300, 170, E.mix(COR, BR, 0.82))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_cinco_questoes", a), ("capa_B_optica_na_pratica", b), ("capa_C_quatro_atalhos", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
