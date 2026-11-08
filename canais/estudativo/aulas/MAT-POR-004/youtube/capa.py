"""Capas do MAT-POR-004 (1280x720). Uso: python capa.py"""
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


def caixa(c, s, cx, cy, size, fundo, cor):
    w, h = E.larg(s, "g", size) + size * 1.0, size * 1.6
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h), 26, 26), M.paint(fundo))
    E.centro(c, s, cx, cy + size * 0.36, size, "g", cor)


def a(c):  # o gancho: + 15% numa conta só
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "+15%", 84, 470, 260, "g", BR)
    E.escreve(c, "numa conta só", 90, 640, 120, "i", BR)
    caixa(c, "R$ 200", 330, 870, 110, BR, COR)
    M.arrow(c, 560, 870, 700, 870, BR, 1, 9, 28)
    caixa(c, "× 1,15", 960, 870, 120, AMARELO, COR)
    M.arrow(c, 1220, 870, 1360, 870, BR, 1, 9, 28)
    caixa(c, "R$ 230", 1600, 870, 110, BR, COR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Fator de", "aumento", "e de desconto")


def d(c):  # o atalho: leia o fator ao contrário
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "leia o fator", 84, 340, 140, "i", BR)
    E.escreve(c, "ao contrário", 76, 540, 190, "g", BR)
    caixa(c, "× 0,7", 330, 820, 110, E.mix(COR, BR, 0.55), "#07070F")
    M.arrow(c, 560, 820, 700, 820, BR, 1, 9, 28)
    E.escreve(c, "−30%", 760, 880, 180, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_numa_conta_so", a), ("capa_B_fator", b), ("capa_C_fator_ao_contrario", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
