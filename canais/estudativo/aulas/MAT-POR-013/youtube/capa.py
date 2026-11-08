"""Capas do MAT-POR-013 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: −30% e mais −20% não é 50%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "−30% e mais −20%", 84, 400, 150, "g", BR)
    E.escreve(c, "50%", 84, 690, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 720, 520, 520, 9, 0, AMARELO, 30)
    E.escreve(c, "44%", 84 + E.larg("50%", "g", 230) + 70, 690, 230, "g", AMARELO)
    E.escreve(c, "5 situações para resolver", 84, 960, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Praticando", "variações", "sucessivas")


def d(c):  # o atalho: 5% e 10% = 15,5%
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    CL = E.mix(COR, BR, 0.55)
    E.escreve(c, "+5% e +10% de cabeça", 84, 340, 120, "i", BR)
    E.escreve(c, "15,5%", 76, 620, 280, "g", BR)
    E.escreve(c, "5 + 10 + 5 × 10 ÷ 100", 84, 860, 120, "g", CL)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_50", a), ("capa_B_praticando", b), ("capa_C_atalho", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
