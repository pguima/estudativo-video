"""Capas do MAT-RAZ-014 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: trocar a ordem é o erro
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "faltas 2, 3 e 4", 84, 360, 120, "i", BR)
    E.escreve(c, "pesos 4, 3, 2?", 76, 610, 200, "g", BR)
    E.risco(c, 60, 660, 1400, 470, 9, 0, AMARELO, 30)
    E.escreve(c, "inverso não é trocar a ordem", 84, 860, 96, "i", BR)
    E.fracao(c, 1, 2, 1450, 300, 120, AMARELO)
    E.fracao(c, 1, 3, 1630, 300, 120, AMARELO)
    E.fracao(c, 1, 4, 1810, 300, 120, AMARELO)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Divisão", "inversa", "do jeito certo")


def d(c):  # o atalho: MMC ÷ cada número
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 360, 150, "i", BR)
    E.escreve(c, "MMC ÷ número", 76, 590, 200, "g", BR)
    E.formula(c, "12 ÷ 2 = 6   12 ÷ 3 = 4   12 ÷ 4 = 3", 84, 860, 104, "g", E.mix(COR, BR, 0.6))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_trocar_a_ordem", a), ("capa_B_divisao_inversa", b), ("capa_C_mmc_dividido", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
