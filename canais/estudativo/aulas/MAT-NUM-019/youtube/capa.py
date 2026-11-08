"""Capas do MAT-NUM-019 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: a pegadinha do colchete
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "−3 + 2 × [4 − (1 − 6)]", 84, 420, 150, "g", BR)
    E.escreve(c, "−5?", 84, 720, 230, "g", AMARELO)
    E.risco(c, 70, 740, 480, 560, 9, 0, BR, 30)
    E.escreve(c, "a pegadinha do sinal", 600, 690, 110, "i", BR)
    E.escreve(c, "= 15", 1340, 960, 220, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Exercícios", "negativos", "pause e resolva")


def d(c):  # o atalho: tirar dívida é ganhar
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "tirar uma dívida", 84, 380, 140, "i", BR)
    E.escreve(c, "é ganhar", 84, 600, 210, "g", AMARELO)
    E.formula(c, "4 − (−5) = 4 + 5", 84, 880, 160, "g", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_pegadinha_do_sinal", a), ("capa_B_exercicios", b), ("capa_C_tirar_divida", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
