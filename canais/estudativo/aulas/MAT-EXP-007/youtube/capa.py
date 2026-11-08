"""Capas do MAT-EXP-007 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a conta apressada da máquina
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "R$ 80.000, perde 20% ao ano", 84, 330, 96, "i", BR)
    E.escreve(c, "em 2 anos:", 84, 500, 110, "i", BR)
    E.escreve(c, "48.000?", 84, 720, 170, "g", BR)
    E.risco(c, 70, 690, 790, 630, 1.0, 0.0, "#FF4D5E", 18)
    E.escreve(c, "51.200", 900, 720, 170, "g", AMARELO)
    E.pilula(c, "4 situações resolvidas", 1380, 900, 64, "g", fundo=AMARELO, cor=COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Praticando:", "exponencial", "4 situações resolvidas")


def d(c):  # o atalho: conte as dobras
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    claro = E.mix(COR, BR, 0.5)
    E.escreve(c, "o atalho:", 84, 300, 120, "i", claro)
    E.escreve(c, "conte as", 76, 510, 190, "g", BR)
    E.escreve(c, "dobras", 76, 710, 190, "g", AMARELO)
    E.escreve(c, "100 → 3.200 = 5 dobras", 84, 930, 90, "g", claro)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_48_mil_ou_51_mil", a), ("capa_B_praticando_exponencial", b), ("capa_C_conte_as_dobras", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
