"""Capas do MAT-FIN-001 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: R$ 1.000 a 36% ao ano por 5 meses não dá R$ 1.800 de juros
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "R$ 1.000 a 36% ao ano", 84, 330, 110, "g", BR)
    E.escreve(c, "por 5 meses: juros de", 88, 470, 100, "i", BR)
    E.escreve(c, "R$ 1.800?", 84, 760, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 790, 1130, 580, 9, 0, AMARELO, 30)
    E.escreve(c, "não!", 1220, 640, 120, "i", BR)
    E.centro(c, "R$ 150", 1500, 860, 200, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Juros", "simples", "J = C · i · t")


def d(c):  # o atalho: taxa × tempo numa porcentagem só
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "2% × 6 meses = 12%", 84, 560, 150, "g", BR)
    E.escreve(c, "12% de R$ 1.200", 84, 740, 130, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "= R$ 144", 84, 960, 200, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_1800", a), ("capa_B_juros_simples", b), ("capa_C_atalho_12", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
