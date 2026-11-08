"""Capas do MAT-FIN-004 (1280x720). Uso: python capa.py"""
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


def a(c):  # o gancho: R$ 1.000 a 10% por 3 meses não dá R$ 1.300 nos compostos
    E.capa_base(c, COR); E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "R$ 1.000 a 10% ao mês", 84, 330, 120, "g", BR)
    E.escreve(c, "por 3 meses, em juros compostos:", 88, 470, 84, "i", BR)
    E.escreve(c, "R$ 1.300?", 84, 760, 230, "g", E.mix(COR, BR, 0.55))
    E.risco(c, 70, 790, 1160, 580, 9, 0, AMARELO, 30)
    E.escreve(c, "não!", 1260, 600, 120, "i", BR)
    E.centro(c, "R$ 1.331", 1430, 960, 190, "g", AMARELO)


def b(c):  # o modelo padrão
    E.capa_modelo(c, "Matemática", "Juros", "compostos", "mês a mês e a fórmula")


def d(c):  # o atalho para 10%: somar a décima parte
    c.drawRect(skia.Rect.MakeWH(E.W, E.H), M.paint("#07070F"))
    for cx, cy, r in ((260, 200, 900), (1700, 980, 900)):
        p = skia.Paint(AntiAlias=True)
        p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [M.hexc(COR, 0.95), M.hexc(COR, 0.0)], [0, 1]))
        c.drawCircle(cx, cy, r, p)
    E.capa_rotulo(c, "Matemática", COR)
    E.escreve(c, "× 1,1 = somar a décima parte", 84, 330, 100, "i", BR)
    E.escreve(c, "R$ 1.000 → R$ 1.100", 84, 530, 120, "g", BR)
    E.escreve(c, "→ R$ 1.210", 84, 720, 140, "g", E.mix(COR, BR, 0.55))
    E.escreve(c, "→ R$ 1.331", 84, 930, 170, "g", AMARELO)


pasta = Path(__file__).parent
s = skia.Surface(E.W, E.H)
for nome, fn in (("capa_A_nao_e_1300", a), ("capa_B_juros_compostos", b), ("capa_C_decima_parte", d)):
    fn(s.getCanvas())
    tmp = pasta / f"{nome}.png"; s.makeImageSnapshot().save(str(tmp), skia.kPNG)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-vf", "scale=1280:720", "-q:v", "2", str(pasta / f"{nome}.jpg")], check=True)
    tmp.unlink()
