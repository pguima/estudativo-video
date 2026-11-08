"""Capas do MAT-POR-008 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: não é 50%
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "leve 3,", 84, 400, 190, "g", BR)
    E.escreve(c, "pague 2", 84, 590, 190, "g", BR)
    E.escreve(c, "50%", 1000, 500, 220, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 980, 540, 1440, 330, 9, 0, AMARELO, 30)
    E.escreve(c, "≈ 33%", 1000, 760, 200, "g", AMARELO)
    E.escreve(c, "de desconto de verdade", 84, 960, 100, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Leve 3,", "pague 2", "quanto é de desconto?")


def d(c):  # o atalho: três frações
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    CL = E.mix(COR, BR, 0.55)
    E.escreve(c, "guarde 3 frações", 84, 330, 120, "i", BR)
    for i, (n, dd, pct) in enumerate(((1, 3, "≈ 33%"), (1, 4, "25%"), (1, 5, "20%"))):
        x = 300 + i * 600
        E.fracao(c, n, dd, x, 560, 170, BR)
        E.centro(c, pct, x, 920, 120, "g", CL)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_50", a), ("capa_B_leve_3_pague_2", b), ("capa_C_tres_fracoes", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
