"""Capas do MAT-POT-013 (1280x720). Uso: python capa.py"""
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


def escuro(c):
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)


def a(c):  # o gancho: a soma que dá quase o triplo
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.formula(c, "3 × 10^5 + 8 × 10^4", 84, 430, 170, "g", BR)
    E.formula(c, "= 11 × 10^5", 84, 690, 200, "g", AMARELO)
    E.selo(c, 1480, 610, 120, False)
    E.escreve(c, "o erro da soma", 84, 950, 170, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Contas em", "notação", "científica")


def d(c):  # o atalho: ache o expoente antes da conta
    escuro(c)
    E.escreve(c, "ache o expoente", 84, 380, 170, "i", BR)
    E.escreve(c, "antes da conta", 84, 580, 170, "g", BR)
    E.formula(c, "7 + 1 = 8", 84, 870, 240, "g", AMARELO)


NOMES = (("capa_A_erro_da_soma", a), ("capa_B_contas_em_notacao", b), ("capa_C_expoente_antes", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in NOMES:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()

