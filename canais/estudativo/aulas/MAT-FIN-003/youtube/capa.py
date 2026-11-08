"""Capas do MAT-FIN-003 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: conta de R$ 200 com 10 dias de atraso não dá R$ 242
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "conta de R$ 200", 84, 330, 130, "g", BR)
    E.escreve(c, "10 dias de atraso:", 88, 470, 100, "i", BR)
    E.escreve(c, "R$ 242?", 84, 760, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 790, 980, 580, 9, 0, AMARELO, 30)
    E.escreve(c, "não!", 1130, 600, 120, "i", BR)
    E.centro(c, "R$ 206", 1430, 920, 200, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Conta", "atrasada", "multa com juros")


def d(c):  # o atalho: some as porcentagens antes
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "o atalho: some antes", 84, 340, 130, "i", BR)
    E.escreve(c, "2% + 1% = 3%", 84, 580, 190, "g", BR)
    E.escreve(c, "3% de R$ 200", 84, 780, 130, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "= R$ 6", 84, 980, 190, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_242", a), ("capa_B_conta_atrasada", b), ("capa_C_atalho_3", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
