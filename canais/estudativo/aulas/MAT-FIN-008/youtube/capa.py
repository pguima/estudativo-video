"""Capas do MAT-FIN-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: 1% ao mês não é 12% ao ano
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "1% ao mês", 84, 400, 190, "g", BR)
    E.escreve(c, "em 1 ano dá", 88, 540, 110, "i", BR)
    E.escreve(c, "12%?", 84, 800, 240, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 830, 640, 620, 9, 0, AMARELO, 30)
    E.escreve(c, "não!", 1000, 560, 120, "i", BR)
    E.centro(c, "12,68%", 1420, 820, 200, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Taxa", "equivalente", "e taxa efetiva")


def d(c):  # o atalho para dois períodos
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho", 84, 340, 140, "i", BR)
    E.escreve(c, "10% + 10%", 84, 560, 190, "g", BR)
    E.escreve(c, "+ 10 × 10 ÷ 100", 84, 740, 130, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "= 21%", 84, 960, 200, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_12", a), ("capa_B_taxa_efetiva", b), ("capa_C_atalho_21", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
