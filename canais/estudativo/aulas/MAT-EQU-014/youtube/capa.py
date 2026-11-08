"""Capas do MAT-EQU-014 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: qual plano é mais barato?
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "A", 84, 420, 150, "g", AMARELO)
    E.escreve(c, "R$ 40 + 0,50/min", 250, 420, 150, "g", BR)
    E.escreve(c, "B", 84, 640, 150, "g", AMARELO)
    E.escreve(c, "R$ 20 + 1/min", 250, 640, 150, "g", BR)
    E.escreve(c, "qual sai mais barato?", 84, 900, 140, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Comparar", "dois planos", "com equação")


def d(c):  # o macete: diferença ÷ diferença
    escuro(c)
    E.escreve(c, "o atalho", 84, 330, 140, "i", BR)
    E.formula(c, "f{40 − 20}{1 − 0,5}", 84, 640, 230, "g", BR)
    E.escreve(c, "= 40 min", 830, 700, 200, "g", AMARELO)
    E.escreve(c, "e os planos empatam", 84, 960, 120, "i", BR)


NOMES = (("capa_A_qual_mais_barato", a), ("capa_B_comparar_dois_planos", b), ("capa_C_atalho_diferenca", d))


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in NOMES:
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
