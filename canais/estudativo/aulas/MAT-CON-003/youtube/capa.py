"""Capas do MAT-CON-003 (1280x720). Uso: python capa.py"""
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


def venn(c, cx, cy, r, nums):
    """dois círculos brancos com os números das regiões (só A, meio, só B)"""
    a, b = (cx - r * 0.62, cy), (cx + r * 0.62, cy)
    pa, pb = skia.Path(), skia.Path()
    pa.addCircle(*a, r); pb.addCircle(*b, r)
    c.drawPath(skia.Op(pa, pb, skia.PathOp.kIntersect_PathOp), M.paint(AMARELO))
    for x, y in (a, b):
        c.drawCircle(x, y, r, M.paint(BR, 1.0, stroke=12))
    for (x, s, cor) in zip((cx - r * 0.95, cx, cx + r * 0.95), nums, (BR, COR, BR)):
        E.centro(c, s, x, cy + 36, 100, "g", cor)


def a(c):  # o gancho: 40 − 22 − 17 = 1? São 8
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "quantos não", 84, 360, 120, "i", BR)
    E.escreve(c, "jogam nenhum?", 84, 530, 140, "g", BR)
    venn(c, 1510, 480, 200, ("15", "7", "10"))
    E.escreve(c, "40 − 22 − 17 = 1", 84, 800, 110, "g", BR)
    E.risco(c, 70, 830, 940, 720, 9, 0, AMARELO, 26)
    E.bola(c, 1700, 900, 130, AMARELO)
    E.centro(c, "8", 1700, 970, 190, "g", COR)


def b(c):  # o modelo
    E.capa_modelo(c, "Matemática", "Problemas", "de Venn", "sem errar")


def d(c):  # o atalho
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "a fórmula", 84, 380, 130, "i", BR)
    E.escreve(c, "ao contrário", 76, 600, 200, "g", BR)
    E.formula(c, "35 + 30 − x = 50", 84, 860, 140, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "x = 15", 1300, 1000, 120, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_um", a), ("capa_B_problemas_de_venn", b), ("capa_C_formula_ao_contrario", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
