"""Capas do MAT-LEI-005 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: R$ 196,80 cobra quase R$ 80 a mais
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "24 m³ de água", 84, 380, 140, "g", BR)
    E.escreve(c, "R$ 196,80", 84, 640, 200, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 660, 1060, 520, 9, 0, AMARELO, 30)
    E.escreve(c, "R$ 117,80", 1120, 640, 160, "g", AMARELO)
    E.escreve(c, "a conta por faixas, sem cair na pegadinha", 84, 900, 80, "i", BR)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Conta", "por faixas", "a conta de água")


def d(c):  # o atalho: faixa cheia vira valor fixo
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "faixa cheia vira", 84, 360, 140, "i", BR)
    E.escreve(c, "valor fixo", 76, 590, 230, "g", BR)
    E.escreve(c, "35 + 50 = 85", 84, 850, 150, "g", AMARELO)
    E.escreve(c, "+ só o que passou", 1000, 840, 90, "i", BR)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_196_ou_117", a), ("capa_B_conta_por_faixas", b), ("capa_C_valor_fixo", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
